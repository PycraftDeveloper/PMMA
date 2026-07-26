#pragma once

#include <map>
#include <string>

#include "Internal/Internal.hpp"

/*
struct TextureProperty {
    uintptr_t ID;
    uint16_t TextureSize[2];
    unsigned char Channels;
    uint32_t References = 0;
    std::vector<unsigned char> PixelData;
    std::map<uintptr_t, uint16_t[2]> RegisteredRenderPipelineInstances;

    TextureProperty() {
        ID = reinterpret_cast<uintptr_t>(this);
    }
};
*/

namespace PMMA::Internal::Rendering::Core2D {
class TextureManager { // makes texture atlas for a RenderPipelineInstance
private:
    std::map<uintptr_t, PMMA::Internal::TextureProperty *> RegisteredTextures;

public:
    bool Dirty = false;

    bgfx::TextureHandle TextureHandle = BGFX_INVALID_HANDLE;

    uint32_t m_TextureWidth = 0;
    uint32_t m_TextureHeight = 0;
    uint32_t MaxTextureDimension = 1024;
    uintptr_t RenderPipelineInstanceID;

    ~TextureManager() {
        if (bgfx::isValid(TextureHandle)) {
            bgfx::destroy(TextureHandle);
        }
    }

    // This function takes a TextureProperty struct instance by ref and adds it as a registered texture to this atlas.
    // This function should identify where in the texture atlas the texture shall be placed using properties from TextureProperty.
    // This data must be written to RegisteredTextures[Texture->ID]->RegisteredRenderPipelineInstances[RenderPipelineInstanceID] as (x, y).
    // Textures must be padded with consideration for the following MipMap generation:
    /*
    Mip LevelScaleRequired Padding Left to Avoid BleedingMip 0 (Base)100%1 pixel (Minimum required for bilinear filtering)Mip 150%2 pixelsMip 225%4 pixelsMip 312.5%8 pixelsMip 46.25%16 pixels
    */
    // Note, if an item is untextured, it's texture position and size is (1, 1) by default, so that position in the texture must be solid white.
    void RegisterTexture(PMMA::Internal::TextureProperty *Texture) {
        auto it = RegisteredTextures.find(Texture->ID);
        if (it == RegisteredTextures.end()) {          // Add texture to atlas
            RegisteredTextures[Texture->ID] = Texture; // store reference to texture
            Dirty = true;
        }
    }

    // Here, if the texture atlas is dirty, the texture atlas should be generated using the properties from 'RegisteredTextures' and written to a BGFX texture.
    void Assemble() {
    }
};
} // namespace PMMA::Internal::Rendering::Core2D