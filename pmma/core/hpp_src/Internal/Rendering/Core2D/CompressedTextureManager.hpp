#pragma once

#include <algorithm>
#include <cstdint>
#include <limits>
#include <string>
#include <unordered_map>
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
     * Indexed by stable texture ID.
     *
     * This is current-frame state only.
     */
    std::vector<bool> TextureIsTransparent;

    /*
     * Previous-frame lookup data.
     *
     * This is retained specifically so cached textures do not need
     * to call RegisterTexture() again.
     *
     * RegisterTexture() is expensive because it dirties the atlas.
     * A cached texture therefore reuses the lookup coordinates from
     * the previous frame.
     */
    std::vector<float> PreviousLookUpTextureData;

    /*
     * Transparency information belonging to the previous frame.
     *
     * This is useful for cached entries because their atlas type must
     * be known without registering the texture again.
     */
    std::vector<bool> PreviousTextureIsTransparent;

    bgfx::TextureHandle LookUpTextureHandle =
        BGFX_INVALID_HANDLE;

    uintptr_t RenderPipelineInstanceID = 0;
    uint32_t RenderPipelineInstanceMaxTextureDimension = 0;

    /*
     * Current-frame lookup data.
     *
     * Layout:
     *
     *   texture 0 / mip 0 = XYWH
     *   texture 0 / mip 1 = XYWH
     *   ...
     *   texture 1 / mip 0 = XYWH
     *   ...
     */
    std::vector<float> LookUpTextureData;

    /*
     * Number of rows required by the CURRENT frame's lookup texture.
     *
     * This is a row count, not simply the number of new textures.
     *
     * Cached IDs can be sparse:
     *
     *     0, 4, 17
     *
     * In that case TextureID must become 18.
     */
    uint32_t TextureID = 0;

    /*
     * Stable texture ID cache.
     *
     * PreviousRegisteredTextures:
     *     texture pointer/ID -> stable lookup texture row
     *
     * CurrentRegisteredTextures:
     *     only textures actually present in the current frame
     */
    std::unordered_map<uintptr_t, uint32_t>
        PreviousRegisteredTextures;

    std::unordered_map<uintptr_t, uint32_t>
        CurrentRegisteredTextures;

private:
    inline bool IncludeTextureID(uint32_t ID) {
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

    inline void EnsureCurrentLookupDataSize(uint32_t ID) {
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

    inline void EnsureCurrentTransparencySize(uint32_t ID) {
        if (TextureIsTransparent.size() <= ID) {
            TextureIsTransparent.resize(
                static_cast<size_t>(ID) + 1,
                false);
        }
    }

    /*
     * Copy the complete lookup row belonging to a cached texture from
     * the previous frame into the current frame.
     *
     * Crucially, this does NOT call RegisterTexture().
     */
    inline bool RestoreCachedLookupData(
        uint32_t ID,
        bool Transparent) {

        if (!IncludeTextureID(ID)) {
            return false;
        }

        EnsureCurrentLookupDataSize(ID);
        EnsureCurrentTransparencySize(ID);

        TextureIsTransparent[ID] = Transparent;

        const size_t Width =
            static_cast<size_t>(
                PMMA::Constants::MAX_TEXTURE_MIPS);

        const size_t RowSize =
            Width * 4;

        const size_t Offset =
            static_cast<size_t>(ID) * RowSize;

        /*
         * The previous frame may not contain lookup data for this ID.
         *
         * This should not normally happen, but leaving the current row
         * zeroed is safer than copying out of bounds.
         */
        if (Offset + RowSize >
            PreviousLookUpTextureData.size()) {

            return false;
        }

        std::copy_n(
            PreviousLookUpTextureData.begin() + Offset,
            RowSize,
            LookUpTextureData.begin() + Offset);

        return true;
    }

    /*
     * Allocate a brand-new stable texture ID.
     *
     * This is the ONLY path which causes RegisterTexture() to be
     * called.
     */
    inline uint32_t AllocateTextureID(
        uintptr_t InternalTextureID,
        bool Transparent) {

        const uint32_t ID = TextureID;

        if (ID == std::numeric_limits<uint32_t>::max()) {
            return ID;
        }

        ++TextureID;

        CurrentRegisteredTextures[InternalTextureID] = ID;

        EnsureCurrentLookupDataSize(ID);
        EnsureCurrentTransparencySize(ID);

        TextureIsTransparent[ID] = Transparent;

        return ID;
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

        PMMA::Internal::Rendering::Core2D::
            CompressedTextureInstance *Texture =
                OpaqueCompressedTextureInstance[0];

        if (Texture == nullptr) {
            return;
        }

        in_data[2] = Texture->m_TextureWidth;
        in_data[3] = Texture->m_TextureHeight;
    }

    inline void WriteTransparentData(float *in_data) {
        in_data[1] = TextureID;

        PMMA::Internal::Rendering::Core2D::
            CompressedTextureInstance *Texture =
                TransparentCompressedTextureInstance[0];

        if (Texture == nullptr) {
            return;
        }

        in_data[2] = Texture->m_TextureWidth;
        in_data[3] = Texture->m_TextureHeight;
    }

    inline void DestroyLookupTexture() {
        if (bgfx::isValid(LookUpTextureHandle)) {
            bgfx::destroy(LookUpTextureHandle);
            LookUpTextureHandle =
                BGFX_INVALID_HANDLE;
        }
    }

    inline void Reset() {
        /*
         * Preserve the lookup information generated for this frame.
         *
         * Cached textures in the next frame can copy their rows from
         * here without calling RegisterTexture().
         */
        PreviousLookUpTextureData.swap(
            LookUpTextureData);

        PreviousTextureIsTransparent.swap(
            TextureIsTransparent);

        /*
         * The current lookup data must now be completely empty.
         *
         * This prevents stale entries from surviving into the next
         * frame.
         */
        LookUpTextureData.clear();
        TextureIsTransparent.clear();

        /*
         * The current texture map becomes the previous-frame cache.
         *
         * swap() avoids copying the entire map.
         */
        PreviousRegisteredTextures.swap(
            CurrentRegisteredTextures);

        CurrentRegisteredTextures.clear();

        /*
         * TextureID describes the current lookup texture, so it is
         * always reset.
         *
         * Cached IDs will expand it again as they are encountered.
         */
        TextureID = 0;

        /*
         * Reset the atlas instances' per-frame state.
         *
         * Importantly, cached textures are NOT re-registered below.
         * Their existing atlas placement is reused.
         */
        for (int i = 0;
             i < std::size(TransparentCompressedTextureInstance);
             ++i) {

            PMMA::Internal::Rendering::Core2D::
                CompressedTextureInstance *Texture =
                    TransparentCompressedTextureInstance[i];

            if (Texture == nullptr) {
                break;
            }

            Texture->Reset();
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
        PMMA::Internal::Rendering::Core2D::
            CompressedTextureProperty *Texture,
        uint32_t Width,
        uint32_t Height) {

        const uintptr_t InternalTextureID =
            Texture->ID;

        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        if (it != PreviousRegisteredTextures.end()) {
            const uint32_t CachedID =
                it->second;

            /*
             * A cached texture already exists in the atlas.
             *
             * Do not call RegisterTexture().
             *
             * Restore its current-frame lookup information instead.
             */
            const bool Restored =
                RestoreCachedLookupData(
                    CachedID,
                    false);

            if (!Restored) {
                /*
                 * The cache is inconsistent with the previous lookup
                 * data. Treat it as a cache miss.
                 */
                PreviousRegisteredTextures.erase(it);
            } else {
                CurrentRegisteredTextures[InternalTextureID] = CachedID;

                return true;
            }
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
        PMMA::Internal::Rendering::Core2D::
            CompressedTextureProperty *Texture,
        uint32_t Width,
        uint32_t Height) {

        const uintptr_t InternalTextureID =
            Texture->ID;

        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        if (it != PreviousRegisteredTextures.end()) {
            const uint32_t CachedID =
                it->second;

            /*
             * Reuse the existing atlas placement and lookup data.
             *
             * RegisterTexture() is deliberately NOT called.
             */
            const bool Restored =
                RestoreCachedLookupData(
                    CachedID,
                    true);

            if (!Restored) {
                PreviousRegisteredTextures.erase(it);
            } else {
                CurrentRegisteredTextures[InternalTextureID] = CachedID;

                return true;
            }
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

        auto it =
            PreviousRegisteredTextures.find(
                InternalTextureID);

        if (it != PreviousRegisteredTextures.end()) {
            const uint32_t CachedID =
                it->second;

            /*
             * Cached texture:
             *
             * - reuse stable ID
             * - reuse previous lookup coordinates
             * - DO NOT call RegisterTexture()
             */
            if (RestoreCachedLookupData(
                    CachedID,
                    false)) {

                CurrentRegisteredTextures[InternalTextureID] = CachedID;

                return static_cast<float>(CachedID);
            }

            /*
             * If the previous cache entry is invalid, fall through
             * and treat the texture as new.
             */
            PreviousRegisteredTextures.erase(it);
        }

        /*
         * This is genuinely a new texture.
         *
         * This is the only path that calls RegisterTexture().
         */
        const uint32_t ID =
            AllocateTextureID(
                InternalTextureID,
                false);

        if (ID ==
            std::numeric_limits<uint32_t>::max()) {

            return static_cast<float>(ID);
        }

        for (uint32_t i = 0;
             i < TextureProperties->MipChain.size() &&
             i < PMMA::Constants::MAX_TEXTURE_MIPS;
             ++i) {

            if (OpaqueCompressedTextureInstance[i] == nullptr) {
                OpaqueCompressedTextureInstance[i] =
                    new CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        i);
            }

            OpaqueCompressedTextureInstance[i]->RegisterTexture(
                TextureProperties,
                LookUpTextureData,
                ID);
        }

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

        if (it != PreviousRegisteredTextures.end()) {
            const uint32_t CachedID =
                it->second;

            /*
             * Cached texture:
             *
             * Reuse both the stable ID and the atlas coordinates.
             *
             * RegisterTexture() is deliberately NOT called.
             */
            if (RestoreCachedLookupData(
                    CachedID,
                    true)) {

                CurrentRegisteredTextures[InternalTextureID] = CachedID;

                return static_cast<float>(CachedID);
            }

            PreviousRegisteredTextures.erase(it);
        }

        /*
         * New texture.
         *
         * RegisterTexture() is required because the texture has never
         * been placed in the atlas.
         */
        const uint32_t ID =
            AllocateTextureID(
                InternalTextureID,
                true);

        if (ID ==
            std::numeric_limits<uint32_t>::max()) {

            return static_cast<float>(ID);
        }

        for (uint32_t i = 0;
             i < TextureProperties->MipChain.size() &&
             i < PMMA::Constants::MAX_TEXTURE_MIPS;
             ++i) {

            if (TransparentCompressedTextureInstance[i] == nullptr) {
                TransparentCompressedTextureInstance[i] =
                    new CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        i);
            }

            TransparentCompressedTextureInstance[i]->RegisterTexture(
                TextureProperties,
                LookUpTextureData,
                ID);
        }

        return static_cast<float>(ID);
    }

    inline void AssembleLookupTexture() {
        DestroyLookupTexture();

        const uint32_t Width =
            static_cast<uint32_t>(
                PMMA::Constants::MAX_TEXTURE_MIPS);

        /*
         * This is now the highest cached/new ID + 1 that occurs in
         * the current frame.
         */
        const uint32_t Height =
            TextureID;

        /*
         * This can legitimately be zero if the current frame contains
         * no textures.
         */
        if (Width == 0 || Height == 0) {
            return;
        }

        const size_t ExpectedFloatCount =
            static_cast<size_t>(Width) *
            static_cast<size_t>(Height) *
            4;

        /*
         * PaddedData starts completely zeroed.
         *
         * Therefore an ID which existed last frame but does not exist
         * this frame cannot leak into this frame's lookup texture.
         */
        std::vector<float> PaddedData(
            ExpectedFloatCount,
            0.0f);

        for (uint32_t TextureIndex = 0;
             TextureIndex < Height;
             ++TextureIndex) {

            /*
             * If this ID wasn't encountered this frame, its entire row
             * remains zero.
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
                 * A zero-sized atlas cannot be used for normalization.
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
                 * No current-frame registration for this mip.
                 *
                 * Because LookUpTextureData is rebuilt each frame,
                 * this cannot be stale data from the previous frame.
                 */
                if (TextureWidth <= 0.0f ||
                    TextureHeight <= 0.0f) {

                    continue;
                }

                PaddedData[Offset + 0] =
                    X / AtlasWidth;

                PaddedData[Offset + 1] =
                    Y / AtlasHeight;

                PaddedData[Offset + 2] =
                    TextureWidth / AtlasWidth;

                PaddedData[Offset + 3] =
                    TextureHeight / AtlasHeight;
            }
        }

        const uint32_t DataSize =
            static_cast<uint32_t>(
                PaddedData.size() *
                sizeof(float));

        const bgfx::Memory *Memory =
            bgfx::copy(
                PaddedData.data(),
                DataSize);

        LookUpTextureHandle =
            bgfx::createTexture2D(
                static_cast<uint16_t>(Width),
                static_cast<uint16_t>(Height),
                false,
                1,
                bgfx::TextureFormat::RGBA32F,
                BGFX_TEXTURE_NONE,
                Memory);
    }

    inline void Assemble() {
        /*
         * Only new textures should have dirtied an atlas.
         *
         * Cached textures do not call RegisterTexture(), so their
         * atlas should remain clean unless something else has marked
         * it dirty.
         */

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

        if (Dirty) {
            /*
             * The lookup texture itself is still rebuilt every frame, but
             * the expensive atlas rebuild only happens when an atlas has
             * actually become dirty.
             */
            std::cout << "Look up texture assemble" << std::endl;
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