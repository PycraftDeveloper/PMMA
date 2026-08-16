#pragma once

#include <iostream>

#include "Constants.hpp"
#include "Internal/Rendering/Core2D/CompressedTextureInstance.hpp"

namespace PMMA::Internal::Rendering::Core2D {
class CompressedTextureManager {
public:
    PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *TransparentCompressedTextureManager[PMMA::Constants::MAX_TEXTURE_MIPS]{};
    PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *OpaqueCompressedTextureManager[PMMA::Constants::MAX_TEXTURE_MIPS]{};

    bgfx::UniformHandle s_Tex[PMMA::Constants::MAX_TEXTURE_MIPS];

    uintptr_t RenderPipelineInstanceID;
    uint32_t RenderPipelineInstanceMaxTextureDimension;

    CompressedTextureManager() {
        for (int i = 0; i < std::size(s_Tex); i++) {
            std::string uniformName = "s_Tex_" + std::to_string(i);

            s_Tex[i] = bgfx::createUniform(
                uniformName.c_str(),
                bgfx::UniformType::Sampler);
        }
    }

    void Initialize(uintptr_t NewRenderPipelineInstanceID, uint32_t NewRenderPipelineInstanceMaxTextureDimension) {
        RenderPipelineInstanceID = NewRenderPipelineInstanceID;
        RenderPipelineInstanceMaxTextureDimension = NewRenderPipelineInstanceMaxTextureDimension;
    }

    bool CanFitTextureOpaque(PMMA::Internal::TextureProperty *Texture, uint32_t Width, uint32_t Height) {
        if (OpaqueCompressedTextureManager[0] == nullptr) {
            OpaqueCompressedTextureManager[0] = new PMMA::Internal::Rendering::Core2D::CompressedTextureInstance(RenderPipelineInstanceID, RenderPipelineInstanceMaxTextureDimension, 0);
        }
        return OpaqueCompressedTextureManager[0]->CanFitTexture(Texture, Width, Height);
    }

    bool CanFitTextureTransparent(PMMA::Internal::TextureProperty *Texture, uint32_t Width, uint32_t Height) {
        if (TransparentCompressedTextureManager[0] == nullptr) {
            TransparentCompressedTextureManager[0] = new PMMA::Internal::Rendering::Core2D::CompressedTextureInstance(RenderPipelineInstanceID, RenderPipelineInstanceMaxTextureDimension, 0);
        }
        return TransparentCompressedTextureManager[0]->CanFitTexture(Texture, Width, Height);
    }

    void RegisterOpaque(PMMA::Internal::TextureProperty *TextureProperties) {
        for (int i = 0; i < TextureProperties->MipChain.size(); i++) {
            if (OpaqueCompressedTextureManager[i] == nullptr) {
                OpaqueCompressedTextureManager[i] = new PMMA::Internal::Rendering::Core2D::CompressedTextureInstance(RenderPipelineInstanceID, RenderPipelineInstanceMaxTextureDimension, i);
            }
            OpaqueCompressedTextureManager[i]->RegisterTexture(TextureProperties);
        }
    }

    void RegisterTransparent(PMMA::Internal::TextureProperty *TextureProperties) {
        for (int i = 0; i < TextureProperties->MipChain.size(); i++) {
            if (TransparentCompressedTextureManager[i] == nullptr) {
                TransparentCompressedTextureManager[i] = new PMMA::Internal::Rendering::Core2D::CompressedTextureInstance(RenderPipelineInstanceID, RenderPipelineInstanceMaxTextureDimension, i);
            }
            TransparentCompressedTextureManager[i]->RegisterTexture(TextureProperties);
        }
    }

    void Assemble() {
        for (int i = 0; i < std::size(TransparentCompressedTextureManager); i++) {
            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *Texture = TransparentCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            if (Texture->Dirty) {
                Texture->Assemble();

                std::cout << "Assembled Transparent Texture: " << i << std::endl;
            }
        }

        for (int i = 0; i < std::size(OpaqueCompressedTextureManager); i++) {
            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *Texture = OpaqueCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            if (Texture->Dirty) {
                Texture->Assemble();

                std::cout << "Assembled Opaque Texture: " << i << std::endl;
            }
        }
    }

    void OpaquePass(float *out) {
        if (OpaqueCompressedTextureManager[0] != nullptr) {
            out[2] = float(OpaqueCompressedTextureManager[0]->m_TextureWidth);
            out[3] = float(OpaqueCompressedTextureManager[0]->m_TextureHeight);
        }

        for (int i = 0; i < std::size(OpaqueCompressedTextureManager); i++) {
            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *Texture = OpaqueCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            bgfx::setTexture(2 + i, s_Tex[i], Texture->TextureHandle, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP);
        }
    }

    void TransparentPass(float *out) {
        if (TransparentCompressedTextureManager[0] != nullptr) {
            out[2] = float(TransparentCompressedTextureManager[0]->m_TextureWidth);
            out[3] = float(TransparentCompressedTextureManager[0]->m_TextureHeight);
        }

        for (int i = 0; i < std::size(TransparentCompressedTextureManager); i++) {
            PMMA::Internal::Rendering::Core2D::CompressedTextureInstance *Texture = TransparentCompressedTextureManager[i];

            if (Texture == nullptr) {
                break;
            }

            bgfx::setTexture(2 + i, s_Tex[i], Texture->TextureHandle, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP);
        }
    }
};
} // namespace PMMA::Internal::Rendering::Core2D