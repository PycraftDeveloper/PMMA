#pragma once

#include <array>
#include <cstdint>
#include <future>
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

struct MipData {
    std::vector<uint8_t> PixelData;

    uint16_t Size[2]; // logical texture size

    uint8_t Padding;
};

struct TextureProperty {
    uintptr_t ID;
    uint32_t References = 0;
    unsigned char Channels;
    uint8_t MipLevels;

    std::vector<MipData> MipChain;

    std::future<void> LoadFuture;

    TextureProperty() {
        ID = reinterpret_cast<uintptr_t>(this);
    }
};

struct TextureCacheHeader {
    char Magic[4];
    uint32_t Version = 1;

    uint8_t Channels;
    uint8_t MipCount;
};
} // namespace PMMA::Internal