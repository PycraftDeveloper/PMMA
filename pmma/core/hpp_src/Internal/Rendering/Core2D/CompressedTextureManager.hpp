#pragma once

#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>

#include "Constants.hpp"
#include "Internal/Rendering/Core2D/CompressedTextureInstance.hpp"

namespace PMMA::Internal::Rendering::Core2D {

class CompressedTextureManager {
public:
    PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
        TransparentCompressedTextureManager[PMMA::Constants::MAX_TEXTURE_MIPS]{};

    PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
        OpaqueCompressedTextureManager[PMMA::Constants::MAX_TEXTURE_MIPS]{};

    bgfx::UniformHandle s_Tex[PMMA::Constants::MAX_TEXTURE_MIPS];
    bgfx::UniformHandle s_LookUpTexture;
    std::vector<bool> TextureIsTransparent;

    bgfx::TextureHandle LookUpTextureHandle = BGFX_INVALID_HANDLE;

    uintptr_t RenderPipelineInstanceID = 0;
    uint32_t RenderPipelineInstanceMaxTextureDimension = 0;

    /*
     * Four floats per mip:
     *
     *   R = X
     *   G = Y
     *   B = Width
     *   A = Height
     *
     * Data is stored texture-by-texture:
     *
     *   Texture 0:
     *       mip 0 = RGBA
     *       mip 1 = RGBA
     *       mip 2 = RGBA
     *       ...
     *
     *   Texture 1:
     *       mip 0 = RGBA
     *       mip 1 = RGBA
     *       ...
     *
     * The final BGFX texture is laid out as:
     *
     *        X/mip
     *        0       1       2       3
     *      +-------+-------+-------+-------+
     * Y 0  | mip 0 | mip 1 | mip 2 | ...   |
     *      +-------+-------+-------+-------+
     *   1  | mip 0 | mip 1 | mip 2 | ...   |
     *      +-------+-------+-------+-------+
     *   2  | mip 0 | mip 1 | mip 2 | ...   |
     *      +-------+-------+-------+-------+
     */
    std::vector<float> LookUpTextureData;

    float TextureID = 0;

    CompressedTextureManager() {
        for (int i = 0; i < std::size(s_Tex); i++) {
            std::string uniformName = "s_Tex_" + std::to_string(i);

            s_Tex[i] = bgfx::createUniform(
                uniformName.c_str(),
                bgfx::UniformType::Sampler);
        }

        s_LookUpTexture = bgfx::createUniform(
            "s_LookUpTexture",
            bgfx::UniformType::Sampler);
    }

    ~CompressedTextureManager() {
        DestroyLookupTexture();

        for (int i = 0; i < std::size(s_Tex); i++) {
            if (bgfx::isValid(s_Tex[i])) {
                bgfx::destroy(s_Tex[i]);
            }
        }

        if (bgfx::isValid(s_LookUpTexture)) {
            bgfx::destroy(s_LookUpTexture);
        }

        for (int i = 0; i < std::size(OpaqueCompressedTextureManager); i++) {
            delete OpaqueCompressedTextureManager[i];
            OpaqueCompressedTextureManager[i] = nullptr;
        }

        for (int i = 0; i < std::size(TransparentCompressedTextureManager); i++) {
            delete TransparentCompressedTextureManager[i];
            TransparentCompressedTextureManager[i] = nullptr;
        }
    }

    void WriteOpaqueData(float *in_data) {
        in_data[1] = TextureID;

        PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *Texture = OpaqueCompressedTextureManager[0];

        if (Texture == nullptr) {
            return;
        }

        in_data[2] = Texture->m_TextureWidth;
        in_data[3] = Texture->m_TextureHeight;
    }

    void WriteTransparentData(float *in_data) {
        in_data[1] = TextureID;

        PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *Texture = TransparentCompressedTextureManager[0];

        if (Texture == nullptr) {
            return;
        }

        in_data[2] = Texture->m_TextureWidth;
        in_data[3] = Texture->m_TextureHeight;
    }

    void DestroyLookupTexture() {
        if (bgfx::isValid(LookUpTextureHandle)) {
            bgfx::destroy(LookUpTextureHandle);
            LookUpTextureHandle = BGFX_INVALID_HANDLE;
        }
    }

    void Reset() {
        TextureID = 0;

        LookUpTextureData.clear();
        TextureIsTransparent.clear();

        DestroyLookupTexture();

        for (int i = 0;
             i < std::size(TransparentCompressedTextureManager);
             i++) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = TransparentCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            Texture->Reset();
        }

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureManager);
             i++) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = OpaqueCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            Texture->Reset();
        }
    }

    void Initialize(
        uintptr_t NewRenderPipelineInstanceID,
        uint32_t NewRenderPipelineInstanceMaxTextureDimension) {

        RenderPipelineInstanceID = NewRenderPipelineInstanceID;
        RenderPipelineInstanceMaxTextureDimension =
            NewRenderPipelineInstanceMaxTextureDimension;
    }

    bool CanFitTextureOpaque(
        PMMA::Internal::TextureProperty *Texture,
        uint32_t Width,
        uint32_t Height) {

        if (OpaqueCompressedTextureManager[0] == nullptr) {
            OpaqueCompressedTextureManager[0] =
                new PMMA::Internal::Rendering::Core2D::CompressedTextureInstance(
                    RenderPipelineInstanceID,
                    RenderPipelineInstanceMaxTextureDimension,
                    0);
        }

        return OpaqueCompressedTextureManager[0]->CanFitTexture(
            Texture,
            Width,
            Height);
    }

    bool CanFitTextureTransparent(
        PMMA::Internal::TextureProperty *Texture,
        uint32_t Width,
        uint32_t Height) {

        if (TransparentCompressedTextureManager[0] == nullptr) {
            TransparentCompressedTextureManager[0] =
                new PMMA::Internal::Rendering::Core2D::CompressedTextureInstance(
                    RenderPipelineInstanceID,
                    RenderPipelineInstanceMaxTextureDimension,
                    0);
        }

        return TransparentCompressedTextureManager[0]->CanFitTexture(
            Texture,
            Width,
            Height);
    }

    float RegisterOpaque(TextureProperty *TextureProperties) {
        const uint32_t ID = static_cast<uint32_t>(TextureID++);

        TextureIsTransparent.push_back(false);

        for (uint32_t i = 0;
             i < TextureProperties->MipChain.size() &&
             i < PMMA::Constants::MAX_TEXTURE_MIPS;
             ++i) {

            if (OpaqueCompressedTextureManager[i] == nullptr) {
                OpaqueCompressedTextureManager[i] =
                    new CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        i);
            }

            OpaqueCompressedTextureManager[i]->RegisterTexture(
                TextureProperties,
                LookUpTextureData,
                ID);
        }

        return static_cast<float>(ID);
    }

    float RegisterTransparent(TextureProperty *TextureProperties) {
        const uint32_t ID = static_cast<uint32_t>(TextureID++);

        TextureIsTransparent.push_back(true);

        for (uint32_t i = 0;
             i < TextureProperties->MipChain.size() &&
             i < PMMA::Constants::MAX_TEXTURE_MIPS;
             ++i) {

            if (TransparentCompressedTextureManager[i] == nullptr) {
                TransparentCompressedTextureManager[i] =
                    new CompressedTextureInstance(
                        RenderPipelineInstanceID,
                        RenderPipelineInstanceMaxTextureDimension,
                        i);
            }

            TransparentCompressedTextureManager[i]->RegisterTexture(
                TextureProperties,
                LookUpTextureData,
                ID);
        }

        return static_cast<float>(ID);
    }

    void AssembleLookupTexture() {
        DestroyLookupTexture();

        const uint32_t Width =
            static_cast<uint32_t>(
                PMMA::Constants::MAX_TEXTURE_MIPS);

        const uint32_t Height =
            static_cast<uint32_t>(TextureID);

        if (Width == 0 || Height == 0) {
            std::cout << Width << " " << Height << std::endl;
            return;
        }

        const size_t ExpectedFloatCount =
            static_cast<size_t>(Width) *
            static_cast<size_t>(Height) *
            4;

        /*
         * LookUpTextureData is already arranged as:
         *
         *   Texture 0:
         *       mip 0 = XYWH
         *       mip 1 = XYWH
         *       ...
         *
         *   Texture 1:
         *       mip 0 = XYWH
         *       ...
         *
         * Convert each entry from:
         *
         *   X Y Width Height
         *
         * into:
         *
         *   normalized X
         *   normalized Y
         *   normalized Width
         *   normalized Height
         */

        std::vector<float> PaddedData(
            ExpectedFloatCount,
            0.0f);

        for (uint32_t TextureIndex = 0;
             TextureIndex < Height;
             ++TextureIndex) {

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

                /*
                 * No registration for this mip.
                 * Leave the lookup texel as zero.
                 */
                if (Offset + 4 > LookUpTextureData.size()) {
                    continue;
                }

                CompressedTextureInstance *Atlas =
                    Transparent
                        ? TransparentCompressedTextureManager[Mip]
                        : OpaqueCompressedTextureManager[Mip];

                if (Atlas == nullptr) {
                    continue;
                }

                const float AtlasWidth =
                    static_cast<float>(
                        Atlas->m_TextureWidth);

                const float AtlasHeight =
                    static_cast<float>(
                        Atlas->m_TextureHeight);

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
                 * A zero entry means this mip wasn't registered.
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
                PaddedData.size() * sizeof(float));

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

    void Assemble() {
        for (int i = 0;
             i < std::size(TransparentCompressedTextureManager);
             i++) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = TransparentCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            if (Texture->Dirty) {
                Texture->Assemble();

                std::cout
                    << "Assembled Transparent Texture: "
                    << i << " With textures: " << Texture->RegisteredTextures.size()
                    << std::endl;
            }
        }

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureManager);
             i++) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = OpaqueCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            if (Texture->Dirty) {
                Texture->Assemble();

                std::cout
                    << "Assembled Opaque Texture: "
                    << i << " With textures: " << Texture->RegisteredTextures.size()
                    << std::endl;
            }
        }

        /*
         * Build this after the atlas instances have been assembled.
         */
        AssembleLookupTexture();
    }

    void SetLookupTexture() {
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

    void OpaquePass(float *out) {
        if (OpaqueCompressedTextureManager[0] != nullptr) {
            out[2] =
                float(OpaqueCompressedTextureManager[0]->m_TextureWidth);

            out[3] =
                float(OpaqueCompressedTextureManager[0]->m_TextureHeight);
        }

        for (int i = 0;
             i < std::size(OpaqueCompressedTextureManager);
             i++) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = OpaqueCompressedTextureManager[i];

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

    void TransparentPass(float *out) {
        if (TransparentCompressedTextureManager[0] != nullptr) {
            out[2] =
                float(TransparentCompressedTextureManager[0]->m_TextureWidth);

            out[3] =
                float(TransparentCompressedTextureManager[0]->m_TextureHeight);
        }

        for (int i = 0;
             i < std::size(TransparentCompressedTextureManager);
             i++) {

            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *
                Texture = TransparentCompressedTextureManager[i];

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