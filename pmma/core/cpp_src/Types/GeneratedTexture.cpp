#include <filesystem>

#include <STB/stb_image.h>

#include "Internal/Core/PMMA_Core.hpp"
#include "Internal/Core/PMMA_Registry.hpp"

#include "Internal/LoggingManager.hpp"
#include "Internal/ParallelWorker.hpp"

#include "Types/GeneratedTexture.hpp"

#include "Constants.hpp"
#include "Passport.hpp"

inline void GeneratedTextureSetCheck(PMMA::Internal::Rendering::Core2D::GeneratedTextureProperty *TextureProperties) {
    if (TextureProperties == nullptr) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            70,
            "Unable to get texture properties. You need to load a texture \
before calling this function!");

        throw std::runtime_error("Failed to query texture information.");
    }
}

void PMMA::Types::GeneratedTexture::InternalLoad() {
}

void PMMA::Types::GeneratedTexture::Load(std::string TexturePath) {
}

void PMMA::Types::GeneratedTexture::Load() {
}

void PMMA::Types::GeneratedTexture::Unload() {
}

PMMA::Types::GeneratedTexture::~GeneratedTexture() {
    PMMA::Types::GeneratedTexture::Unload();
}

void PMMA::Types::GeneratedTexture::Enable() {
    IsTextureEnabled = true;
}

void PMMA::Types::GeneratedTexture::GetSize(uint16_t *size) {
    GeneratedTextureSetCheck(TextureProperties);

    size[0] = TextureProperties->TextureSize[0];
    size[1] = TextureProperties->TextureSize[1];
}

uint16_t PMMA::Types::GeneratedTexture::GetWidth() {
    GeneratedTextureSetCheck(TextureProperties);

    return TextureProperties->TextureSize[0];
}

uint16_t PMMA::Types::GeneratedTexture::GetHeight() {
    GeneratedTextureSetCheck(TextureProperties);

    return TextureProperties->TextureSize[1];
}

std::string PMMA::Types::GeneratedTexture::GetPath() {
    GeneratedTextureSetCheck(TextureProperties);

    return Path;
}

unsigned char PMMA::Types::GeneratedTexture::GetChannels() {
    GeneratedTextureSetCheck(TextureProperties);

    if (TextureProperties->Transparent) {
        return 4;
    }

    return 3;
}

uint32_t PMMA::Types::GeneratedTexture::GetReferences() {
    GeneratedTextureSetCheck(TextureProperties);

    return TextureProperties->References;
}