#pragma once

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

#include <bgfx/bgfx.h>

#include "Constants.hpp"
#include "Internal/Rendering/Core2D/CompressedTextureInstance.hpp"

namespace PMMA::Internal::Rendering::Core2D {

class CompressedTextureManager {
private:
    PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
        TransparentCompressedTextureInstance[PMMA::Constants::MAX_TEXTURE_MIPS]{};

    PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
        OpaqueCompressedTextureInstance[PMMA::Constants::MAX_TEXTURE_MIPS]{};

    bgfx::UniformHandle s_Tex[PMMA::Constants::MAX_TEXTURE_MIPS];
    bgfx::UniformHandle s_LookUpTexture;

    /*
     * Indexed by the stable texture ID.
     *
     * This is rebuilt every frame.  It must therefore only contain
     * entries for textures that actually occur in the current frame.
     */
    std::vector<bool> TextureIsTransparent;

    bgfx::TextureHandle LookUpTextureHandle = BGFX_INVALID_HANDLE;

    uintptr_t RenderPipelineInstanceID = 0;
    uint32_t RenderPipelineInstanceMaxTextureDimension = 0;

    /*
     * One XYWH entry for every:
     *
     *     texture ID * MAX_TEXTURE_MIPS + mip
     *
     * This is rebuilt every frame.
     */
    std::vector<float> LookUpTextureData;

    /*
     * Number of texture IDs required by the current frame.
     *
     * This is deliberately NOT simply incremented when a new texture
     * is registered.  Cached IDs may be sparse, e.g.:
     *
     *     0, 1, 17, 42
     *
     * In that case the lookup texture must still have 43 rows.
     */
    uint32_t TextureID = 0;

    /*
     * Stable texture ID cache.
     *
     * PreviousRegisteredTextures contains the IDs from the previous
     * frame.
     *
     * CurrentRegisteredTextures contains ONLY IDs used by the current
     * frame.
     */
    std::unordered_map<uintptr_t, uint32_t> PreviousRegisteredTextures;
    std::unordered_map<uintptr_t, uint32_t> CurrentRegisteredTextures;

    std::array<std::vector<float>, 4> PaddedData;
    char PaddedDataBufferID = 0;
    char PaddedDataPreviousBufferID = 0;

private:
    inline bool IsValidTextureID(uint32_t ID) const {
        return ID != std::numeric_limits<uint32_t>::max();
    }

    /*
     * Make sure TextureID represents the number of rows required by
     * the lookup texture.
     *
     * This is particularly important when a cached ID is reused.
     *
     * Example:
     *
     *     cached ID = 25
     *     TextureID = 0
     *
     * We must end up with:
     *
     *     TextureID = 26
     */
    inline bool IncludeTextureID(uint32_t ID) {
        if (!IsValidTextureID(ID)) {
            return false;
        }

        if (ID == std::numeric_limits<uint32_t>::max()) {
            return false;
        }

        const uint64_t RequiredHeight =
            static_cast<uint64_t>(ID) + 1u;

        if (RequiredHeight >
            static_cast<uint64_t>(
                std::numeric_limits<uint32_t>::max())) {

            return false;
        }

        TextureID =
            std::max(
                TextureID,
                static_cast<uint32_t>(RequiredHeight));

        return true;
    }

    /*
     * Register the current frame's use of a cached texture.
     *
     * The stable ID comes from the previous frame, but all current
     * frame state is still explicitly rebuilt.
     */
    inline bool RegisterCachedTexture(
        uintptr_t InternalTextureID,
        uint32_t CachedID,
        bool Transparent) {

        if (!IncludeTextureID(CachedID)) {
            return false;
        }

        CurrentRegisteredTextures[InternalTextureID] = CachedID;

        if (TextureIsTransparent.size() <= CachedID) {
            TextureIsTransparent.resize(
                static_cast<size_t>(CachedID) + 1,
                false);
        }

        TextureIsTransparent[CachedID] = Transparent;

        return true;
    }

    /*
     * Ensure the lookup data vector is large enough for a texture ID.
     *
     * Each texture occupies MAX_TEXTURE_MIPS texels and every texel
     * contains four floats.
     */
    inline void EnsureLookupDataSize(uint32_t ID) {
        const size_t Width =
            static_cast<size_t>(
                PMMA::Constants::MAX_TEXTURE_MIPS);

        const size_t RequiredSize =
            (static_cast<size_t>(ID) + 1) *
            Width *
            4;

        if (LookUpTextureData.size() < RequiredSize) {
            LookUpTextureData.resize(
                RequiredSize,
                0.0f);
        }
    }

    /*
     * Register the texture with its atlas even when the texture ID
     * came from the previous-frame cache.
     *
     * The cache only caches the stable lookup ID.  Atlas placement
     * and lookup data are current-frame state and therefore must be
     * rebuilt.
     */
    inline void RegisterTextureIntoAtlases(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *
            TextureProperties,
        uint32_t ID,
        bool Transparent) {

        EnsureLookupDataSize(ID);

        auto **Instances =
            Transparent
                ? TransparentCompressedTextureInstance
                : OpaqueCompressedTextureInstance;

        for (uint32_t i = 0;
             i < TextureProperties->MipChain.size() &&
             i < PMMA::Constants::MAX_TEXTURE_MIPS;
             ++i) {

            if (Instances[i] == nullptr) {
                Instances[i] =
                    new CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        i);
            }

            Instances[i]->RegisterTexture(
                TextureProperties,
                LookUpTextureData,
                ID);
        }
    }

public:
    CompressedTextureManager() {
        for (int i = 0; i < std::size(s_Tex); ++i) {
            std::string uniformName =
                "s_Tex_" + std::to_string(i);

            s_Tex[i] =
                bgfx::createUniform(
                    uniformName.c_str(),
                    bgfx::UniformType::Sampler);
        }

        s_LookUpTexture =
            bgfx::createUniform(
                "s_LookUpTexture",
                bgfx::UniformType::Sampler);
    }

    ~CompressedTextureManager() {
        DestroyLookupTexture();

        for (int i = 0; i < std::size(s_Tex); ++i) {
            if (bgfx::isValid(s_Tex[i])) {
                bgfx::destroy(s_Tex[i]);
            }
        }

        if (bgfx::isValid(s_LookUpTexture)) {
            bgfx::destroy(s_LookUpTexture);
        }

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureInstance);
             ++i) {

            delete OpaqueCompressedTextureInstance[i];
            OpaqueCompressedTextureInstance[i] = nullptr;
        }

        for (int i = 0;
             i < std::size(TransparentCompressedTextureInstance);
             ++i) {

            delete TransparentCompressedTextureInstance[i];
            TransparentCompressedTextureInstance[i] = nullptr;
        }
    }

    inline void WriteOpaqueData(float *in_data) {
        in_data[1] = TextureID;

        PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
            Texture = OpaqueCompressedTextureInstance[0];

        if (Texture == nullptr) {
            return;
        }

        in_data[2] = Texture->m_TextureWidth;
        in_data[3] = Texture->m_TextureHeight;
    }

    inline void WriteTransparentData(float *in_data) {
        in_data[1] = TextureID;

        PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
            Texture = TransparentCompressedTextureInstance[0];

        if (Texture == nullptr) {
            return;
        }

        in_data[2] = Texture->m_TextureWidth;
        in_data[3] = Texture->m_TextureHeight;
    }

    inline void DestroyLookupTexture() {
        if (bgfx::isValid(LookUpTextureHandle)) {
            bgfx::destroy(LookUpTextureHandle);
            LookUpTextureHandle = BGFX_INVALID_HANDLE;
        }
    }

    inline void Reset() {
        /*
         * TextureID describes the CURRENT frame, so it is always reset.
         *
         * Stable IDs themselves are retained in
         * PreviousRegisteredTextures.
         */
        TextureID = 0;

        LookUpTextureData.clear();
        TextureIsTransparent.clear();

        /*
         * Move the current frame's registrations into the previous
         * frame cache.
         *
         * Using swap avoids copying the entire unordered_map and,
         * importantly, leaves CurrentRegisteredTextures empty.
         */
        PreviousRegisteredTextures.swap(
            CurrentRegisteredTextures);

        CurrentRegisteredTextures.clear();

        for (int i = 0;
             i < std::size(TransparentCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = TransparentCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            Texture->Reset();
        }

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = OpaqueCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            Texture->Reset();
        }
    }

    inline void Initialize(
        uintptr_t NewRenderPipelineInstanceID,
        uint32_t NewRenderPipelineInstanceMaxTextureDimension) {

        RenderPipelineInstanceID =
            NewRenderPipelineInstanceID;

        RenderPipelineInstanceMaxTextureDimension =
            NewRenderPipelineInstanceMaxTextureDimension;
    }

    inline bool CanFitTextureOpaque(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *
            Texture,
        uint32_t Width,
        uint32_t Height) {

        const uintptr_t InternalTextureID =
            Texture->ID;

        /*
         * A cached texture has already been assigned a stable ID.
         *
         * Do NOT let this path leave TextureID at zero.  The ID must
         * contribute to the current lookup texture's height.
         */
        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        if (it != PreviousRegisteredTextures.end()) {
            const uint32_t CachedID = it->second;

            if (!RegisterCachedTexture(
                    InternalTextureID,
                    CachedID,
                    false)) {

                return false;
            }

            return true;
        }

        if (OpaqueCompressedTextureInstance[0] == nullptr) {
            OpaqueCompressedTextureInstance[0] =
                new PMMA::Internal::Rendering::Core2D::
                    CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        0);
        }

        return OpaqueCompressedTextureInstance[0]->CanFitTexture(
            Texture,
            Width,
            Height);
    }

    inline bool CanFitTextureTransparent(
        PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *
            Texture,
        uint32_t Width,
        uint32_t Height) {

        const uintptr_t InternalTextureID =
            Texture->ID;

        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        if (it != PreviousRegisteredTextures.end()) {
            const uint32_t CachedID = it->second;

            if (!RegisterCachedTexture(
                    InternalTextureID,
                    CachedID,
                    true)) {

                return false;
            }

            return true;
        }

        if (TransparentCompressedTextureInstance[0] == nullptr) {
            TransparentCompressedTextureInstance[0] =
                new PMMA::Internal::Rendering::Core2D::
                    CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        0);
        }

        return TransparentCompressedTextureInstance[0]->CanFitTexture(
            Texture,
            Width,
            Height);
    }

    inline float RegisterOpaque(
        PMMA::Internal::Rendering::Core2D::
            CompressedTextureProperty *TextureProperties) {

        const uintptr_t InternalTextureID =
            TextureProperties->ID;

        /*
         * First check whether this texture has a stable ID from the
         * previous frame.
         */
        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        uint32_t ID = 0;

        if (it != PreviousRegisteredTextures.end()) {
            /*
             * Reuse the stable ID, but DO NOT skip registration.
             *
             * The atlas and lookup data belong to the current frame.
             */
            ID = it->second;

            if (!RegisterCachedTexture(
                    InternalTextureID,
                    ID,
                    false)) {

                return static_cast<float>(
                    std::numeric_limits<uint32_t>::max());
            }
        } else {
            /*
             * Allocate a new stable ID.
             *
             * TextureID is the number of rows required by the current
             * frame, so incrementing it here is correct for a newly
             * allocated sequential ID.
             */
            ID = TextureID;

            if (ID == std::numeric_limits<uint32_t>::max()) {
                return static_cast<float>(
                    std::numeric_limits<uint32_t>::max());
            }

            ++TextureID;

            CurrentRegisteredTextures[InternalTextureID] = ID;

            if (TextureIsTransparent.size() <= ID) {
                TextureIsTransparent.resize(
                    static_cast<size_t>(ID) + 1,
                    false);
            }

            TextureIsTransparent[ID] = false;
        }

        RegisterTextureIntoAtlases(
            TextureProperties,
            ID,
            false);

        return static_cast<float>(ID);
    }

    inline float RegisterTransparent(
        PMMA::Internal::Rendering::Core2D::
            CompressedTextureProperty *TextureProperties) {

        const uintptr_t InternalTextureID =
            TextureProperties->ID;

        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        uint32_t ID = 0;

        if (it != PreviousRegisteredTextures.end()) {
            /*
             * Reuse the stable ID, but rebuild the current frame's
             * atlas/lookup state.
             */
            ID = it->second;

            if (!RegisterCachedTexture(
                    InternalTextureID,
                    ID,
                    true)) {

                return static_cast<float>(
                    std::numeric_limits<uint32_t>::max());
            }
        } else {
            ID = TextureID;

            if (ID == std::numeric_limits<uint32_t>::max()) {
                return static_cast<float>(
                    std::numeric_limits<uint32_t>::max());
            }

            ++TextureID;

            CurrentRegisteredTextures[InternalTextureID] = ID;

            if (TextureIsTransparent.size() <= ID) {
                TextureIsTransparent.resize(
                    static_cast<size_t>(ID) + 1,
                    false);
            }

            TextureIsTransparent[ID] = true;
        }

        RegisterTextureIntoAtlases(
            TextureProperties,
            ID,
            true);

        return static_cast<float>(ID);
    }

    inline void AssembleLookupTexture() {
        DestroyLookupTexture();

        const uint32_t Width =
            static_cast<uint32_t>(
                PMMA::Constants::MAX_TEXTURE_MIPS);

        /*
         * TextureID is now the required number of rows, rather than
         * merely the number of newly-created IDs this frame.
         *
         * Therefore a frame containing cached IDs such as 12 and 25
         * correctly produces a height of 26.
         */
        const uint32_t Height = TextureID;

        if (Width == 0 || Height == 0) {
            return;
        }

        const size_t ExpectedFloatCount =
            static_cast<size_t>(Width) *
            static_cast<size_t>(Height) *
            4;

        /*
         * Start with a completely zeroed lookup texture.
         *
         * This is important: anything that existed in the previous
         * frame must NOT survive into this frame.
         */
        PaddedData[PaddedDataBufferID].resize(ExpectedFloatCount, 0.0f);

        for (uint32_t TextureIndex = 0;
             TextureIndex < Height;
             ++TextureIndex) {

            /*
             * An ID can be sparse because stable IDs survive between
             * frames.  A row without a current-frame registration
             * remains completely zero.
             */
            if (TextureIndex >=
                TextureIsTransparent.size()) {

                continue;
            }

            const bool Transparent =
                TextureIsTransparent[TextureIndex];

            for (uint32_t Mip = 0;
                 Mip < Width;
                 ++Mip) {

                const size_t Offset =
                    (static_cast<size_t>(TextureIndex) *
                         Width +
                     Mip) *
                    4;

                if (Offset + 4 >
                    LookUpTextureData.size()) {

                    continue;
                }

                PMMA::Internal::Rendering::Core2D::
                    CompressedTextureInstance *Atlas =
                        Transparent
                            ? TransparentCompressedTextureInstance[Mip]
                            : OpaqueCompressedTextureInstance[Mip];

                if (Atlas == nullptr) {
                    continue;
                }

                const float AtlasWidth =
                    static_cast<float>(
                        Atlas->m_TextureWidth);

                const float AtlasHeight =
                    static_cast<float>(
                        Atlas->m_TextureHeight);

                /*
                 * An atlas can legitimately not exist for a mip, or
                 * may not have been assembled yet.  Do not divide by
                 * zero.
                 */
                if (AtlasWidth <= 0.0f ||
                    AtlasHeight <= 0.0f) {

                    continue;
                }

                const float X =
                    LookUpTextureData[Offset + 0];

                const float Y =
                    LookUpTextureData[Offset + 1];

                const float TextureWidth =
                    LookUpTextureData[Offset + 2];

                const float TextureHeight =
                    LookUpTextureData[Offset + 3];

                /*
                 * Zero means this texture does not have a registered
                 * entry for this mip in the current frame.
                 */
                if (TextureWidth <= 0.0f ||
                    TextureHeight <= 0.0f) {

                    continue;
                }

                PaddedData[PaddedDataBufferID][Offset + 0] =
                    X / AtlasWidth;

                PaddedData[PaddedDataBufferID][Offset + 1] =
                    Y / AtlasHeight;

                PaddedData[PaddedDataBufferID][Offset + 2] =
                    TextureWidth / AtlasWidth;

                PaddedData[PaddedDataBufferID][Offset + 3] =
                    TextureHeight / AtlasHeight;
            }
        }

        const uint32_t DataSize =
            static_cast<uint32_t>(
                PaddedData[PaddedDataBufferID].size() *
                sizeof(float));

        const bgfx::Memory *Memory =
            bgfx::makeRef(
                PaddedData[PaddedDataBufferID].data(),
                DataSize);

        std::cout << "MakeLookUpTexture" << std::endl;
        LookUpTextureHandle =
            bgfx::createTexture2D(
                static_cast<uint16_t>(Width),
                static_cast<uint16_t>(Height),
                false,
                1,
                bgfx::TextureFormat::RGBA32F,
                BGFX_TEXTURE_NONE,
                Memory);

        PaddedDataPreviousBufferID = PaddedDataBufferID;
        PaddedDataBufferID = (PaddedDataBufferID + 1) % 4;
    }

    inline void Assemble() {
        bool Dirty = false;

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::
                CompressedTextureInstance *Texture =
                    OpaqueCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            if (Texture->Dirty ||
                !bgfx::isValid(Texture->TextureHandle)) {

                Texture->Assemble();

                Dirty = true;
            }
        }

        for (int i = 0;
             i < std::size(TransparentCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::
                CompressedTextureInstance *Texture =
                    TransparentCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            if (Texture->Dirty ||
                !bgfx::isValid(Texture->TextureHandle)) {

                Texture->Assemble();

                Dirty = true;
            }
        }

        if (Dirty || !bgfx::isValid(LookUpTextureHandle)) {
            /*
             * Build this after the atlas instances have been assembled.
             */
            AssembleLookupTexture();
        }
    }

    inline void SetLookupTexture() {
        if (!bgfx::isValid(LookUpTextureHandle)) {
            return;
        }

        bgfx::setTexture(
            2,
            s_LookUpTexture,
            LookUpTextureHandle,
            BGFX_SAMPLER_U_CLAMP |
                BGFX_SAMPLER_V_CLAMP |
                BGFX_SAMPLER_MIN_POINT |
                BGFX_SAMPLER_MAG_POINT |
                BGFX_SAMPLER_MIP_POINT);
    }

    inline void OpaquePass(float *out) {
        if (OpaqueCompressedTextureInstance[0] != nullptr) {
            out[2] =
                float(
                    OpaqueCompressedTextureInstance[0]
                        ->m_TextureWidth);

            out[3] =
                float(
                    OpaqueCompressedTextureInstance[0]
                        ->m_TextureHeight);
        }

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::
                CompressedTextureInstance *Texture =
                    OpaqueCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            bgfx::setTexture(
                3 + i,
                s_Tex[i],
                Texture->TextureHandle,
                BGFX_SAMPLER_U_CLAMP |
                    BGFX_SAMPLER_V_CLAMP);
        }

        SetLookupTexture();
    }

    inline void TransparentPass(float *out) {
        if (TransparentCompressedTextureInstance[0] != nullptr) {
            out[2] =
                float(
                    TransparentCompressedTextureInstance[0]
                        ->m_TextureWidth);

            out[3] =
                float(
                    TransparentCompressedTextureInstance[0]
                        ->m_TextureHeight);
        }

        for (int i = 0;
             i < std::size(TransparentCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::
                CompressedTextureInstance *Texture =
                    TransparentCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            bgfx::setTexture(
                3 + i,
                s_Tex[i],
                Texture->TextureHandle,
                BGFX_SAMPLER_U_CLAMP |
                    BGFX_SAMPLER_V_CLAMP);
        }

        SetLookupTexture();
    }
};

} // namespace PMMA::Internal::Rendering::Core2D