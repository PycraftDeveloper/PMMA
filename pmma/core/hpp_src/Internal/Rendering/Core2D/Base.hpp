#pragma once

#include <cstdint>
#include <future>
#include <map>
#include <vector>

namespace PMMA::Internal::Rendering::Core2D {
inline float PackValues(uint16_t value_one, uint16_t value_two) {
    uint32_t bits = (uint32_t(value_two) << 16) | uint32_t(value_one);
    float packed;
    std::memcpy(&packed, &bits, sizeof(float));
    return packed;
}

inline float PackSignedValues(int16_t value_one, int16_t value_two) {
    uint32_t bits = (static_cast<uint32_t>(static_cast<uint16_t>(value_two)) << 16) |
                    static_cast<uint32_t>(static_cast<uint16_t>(value_one));

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

struct CompressedTextureProperty {
    uintptr_t ID;
    uint32_t References = 0;
    uint8_t MipLevels;
    bool Transparent = false;

    std::vector<MipData> MipChain;

    std::future<void> LoadFuture;

    CompressedTextureProperty() {
        ID = reinterpret_cast<uintptr_t>(this);
    }
};

struct GeneratedTextureProperty {
    uintptr_t ID;
    uint16_t TextureSize[2];
    uint32_t References = 0;
    uint8_t MipLevels;
    bool Transparent = false;

    std::vector<unsigned char> PixelData;

    std::map<uintptr_t, uint16_t[2]> RegisteredRenderPipelineInstances;

    GeneratedTextureProperty() {
        ID = reinterpret_cast<uintptr_t>(this);
    }
};

struct TextureCacheHeader {
    char Magic[4];
    uint32_t Version = 1;

    uint8_t Channels;
    uint8_t MipCount;
};

struct InstanceData {
    float position, size;
    float point_count_gradient_type, rotation_shape_property_one;
    float color_index, shape_type_width;
    float texture_position = 0, texture_size = 0;
    float shape_property_two = 0, shape_property_three = 0;
    float depth = 0, texture_id = 0;
};

struct SkylineNode {
    uint32_t x;
    uint32_t y;
    uint32_t width;
};

struct AtlasAllocation {
    uint32_t X;
    uint32_t Y;
    uint32_t Width;
    uint32_t Height;
};
} // namespace PMMA::Internal::Rendering::Core2D