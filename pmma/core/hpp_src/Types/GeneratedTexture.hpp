#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <fstream>
#include <iostream>
#include <string>

#include <zstd.h>

#include "Internal/Rendering/Core2D/Base.hpp"

namespace PMMA::Types {
class EXPORT GeneratedTexture {
private:
    std::string Path = "";

public:
    PMMA::Internal::Rendering::Core2D::GeneratedTextureProperty *TextureProperties;
    bool IsTextureEnabled = false;

    ~GeneratedTexture();

    void Load(std::string TexturePath);
    void Load();

    void InternalLoad();

    inline bool LoadCached() {
        return false;
    }

    inline void SaveTextureCache() {
    }

    void Unload();

    void Enable();

    inline void Disable() {
        IsTextureEnabled = false;
    }

    inline bool IsEnabled() {
        return IsTextureEnabled;
    }

    void GetSize(uint16_t *size);

    unsigned char GetChannels();

    uint32_t GetReferences();

    inline bool IsLoaded() {
        return TextureProperties != nullptr;
    }

    uint16_t GetWidth();
    uint16_t GetHeight();

    std::string GetPath();
};
} // namespace PMMA::Types