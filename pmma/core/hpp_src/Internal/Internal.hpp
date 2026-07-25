#pragma once

#include <array>
#include <cstdint>
#include <string>

namespace PMMA::Internal {
struct ColorEntry {
    std::string_view name;
    std::array<uint8_t, 3> value;
};

uint32_t GetRandomSeed();

std::optional<std::array<uint8_t, 3>> FindColor(std::string_view key);

struct TextureProperty {
    uint16_t TextureSize[2];
    unsigned char Channels;
    uint32_t References = 0;
    std::vector<unsigned char> PixelData;
};
} // namespace PMMA::Internal