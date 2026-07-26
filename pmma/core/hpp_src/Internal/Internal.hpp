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

inline float PackValues(uint16_t value_one, uint16_t value_two) {
    uint32_t bits = (uint32_t(value_two) << 16) | uint32_t(value_one);
    float packed;
    std::memcpy(&packed, &bits, sizeof(float));
    return packed;
}

inline float PackValues(uint8_t value_one, uint8_t value_two, uint8_t value_three) {
    uint32_t bits = (static_cast<uint32_t>(value_three) << 24) |
                    (static_cast<uint32_t>(value_two) << 16) |
                    (static_cast<uint32_t>(value_one) << 8); // Leaving lowest 8 bits empty/0

    float packed;
    std::memcpy(&packed, &bits, sizeof(float));
    return packed;
}

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
} // namespace PMMA::Internal