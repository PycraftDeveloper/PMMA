#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

class CPP_Core2D_RenderPipelineInstance;

class CPP_LineShape;
class CPP_RadialPolygonShape;
class CPP_ArcShape;

struct Vertex {
    float x, y, u, v;
};

struct InstanceData {
    float position, size;
    float point_count_gradient_type, rotation_shape_property_one;
    float color_index, shape_type_width;
    float texture_position, texture_size;
    float shape_property_two = 0, shape_property_three = 0;
    float shape_property_four, shape_property_five = 0;
};

class CPP_Core2D_ColorTexture {
private:
    std::vector<uint8_t> ShapeColors;
    std::vector<uintptr_t> PreviousShapeIDs;
    std::vector<uintptr_t> CurrentShapeIDs;
    uint32_t ColorCount = 0;

public:
    bool UsingCache = false;

    bgfx::TextureHandle ColorTexture;

    uint32_t m_colorTextureWidth = 0;
    uint32_t m_colorTextureHeight = 0;
    uint32_t MaxTextureDimension;

    CPP_Core2D_ColorTexture() {
        ColorTexture = BGFX_INVALID_HANDLE;
    }

    ~CPP_Core2D_ColorTexture() {
        if (bgfx::isValid(ColorTexture)) {
            bgfx::destroy(ColorTexture);
        }
    }

    inline uint32_t AddColor(CPP_Color *Color, uintptr_t ShapeID, bool ColorDataChanged) {
        size_t currentShapeIndex = ColorCount / 4;
        size_t targetIndex = ColorCount;

        if (currentShapeIndex >= PreviousShapeIDs.size()) {
            UsingCache = false;
        }

        if (UsingCache && currentShapeIndex < PreviousShapeIDs.size() && PreviousShapeIDs[currentShapeIndex] == ShapeID) {
            if (ColorDataChanged) {
                size_t requiredSize = targetIndex + 4;
                if (ShapeColors.size() < requiredSize) {
                    ShapeColors.resize(requiredSize);
                }
                Color->Get_RGBA(&ShapeColors[targetIndex]);
            }

            if (CurrentShapeIDs.empty() || CurrentShapeIDs.back() != ShapeID) {
                if (currentShapeIndex < CurrentShapeIDs.size()) {
                    CurrentShapeIDs.resize(currentShapeIndex);
                }
                CurrentShapeIDs.push_back(ShapeID);
            }

            ColorCount += 4;
            return (uint32_t)currentShapeIndex;
        }

        UsingCache = false;

        if (CurrentShapeIDs.empty() || CurrentShapeIDs.back() != ShapeID) {
            if (currentShapeIndex < CurrentShapeIDs.size()) {
                CurrentShapeIDs.resize(currentShapeIndex);
            }
            CurrentShapeIDs.push_back(ShapeID);
        }

        size_t needBytes = targetIndex + 4;
        if (ShapeColors.size() < needBytes) {
            ShapeColors.resize(needBytes);
        }

        Color->Get_RGBA(&ShapeColors[targetIndex]);
        ColorCount += 4;

        return (uint32_t)currentShapeIndex;
    }

    inline void Reset() {
        ColorCount = 0;
        PreviousShapeIDs = CurrentShapeIDs;
        CurrentShapeIDs.clear();
        UsingCache = true;
    }

    inline void Assemble() {
        ShapeColors.resize(ColorCount);

        uint32_t numColors = (uint32_t)ShapeColors.size() / 4;
        uint32_t width = std::min(MaxTextureDimension, numColors);
        uint32_t height = (numColors + width - 1) / width;

        size_t expectedSize = width * height * 4;
        if (ShapeColors.size() < expectedSize) {
            ShapeColors.resize(expectedSize, 0); // Pad with transparent black
        }

        const bgfx::Memory *texMem = bgfx::copy(
            ShapeColors.data(),
            static_cast<uint32_t>(ShapeColors.size() * sizeof(uint8_t)));

        // If texture exists but size changed, destroy and recreate it
        if (bgfx::isValid(ColorTexture)) {
            if (m_colorTextureWidth != width || m_colorTextureHeight != height) {
                bgfx::destroy(ColorTexture);
                ColorTexture = BGFX_INVALID_HANDLE;
            }
        }

        // create texture if missing
        if (!bgfx::isValid(ColorTexture)) {
            ColorTexture = bgfx::createTexture2D(
                (uint16_t)width, (uint16_t)height,
                false, // hasMips
                1,     // num layers
                bgfx::TextureFormat::RGBA8,
                BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
        }

        bgfx::updateTexture2D(ColorTexture, 0, 0, 0, 0, width, height, texMem);

        // store width/height for shader normalization
        m_colorTextureWidth = width;
        m_colorTextureHeight = height;
    }
};

class CPP_Core2D_RenderPipelineManager {
private:
    std::vector<CPP_Core2D_RenderPipelineInstance *> RenderPipelineInstances;
    std::vector<CPP_Core2D_RenderPipelineInstance *> CachedRenderPipelineInstances;

public:
    ~CPP_Core2D_RenderPipelineManager();

    void Add(CPP_LineShape *lineShape);
    void Add(CPP_RadialPolygonShape *radialPolygonShape);
    void Add(CPP_ArcShape *arcShape);

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

    void Reset();

    void Render();
};