#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

class CPP_Core2D_RenderPipelineInstance;

class CPP_LineShape;
class CPP_RadialPolygonShape;

struct Vertex {
    float x, y, u, v;
};

struct InstanceData {
    float position, size;
    float point_count_gradient_type, rotation_shape_property;
    float color_index, shape_type_width;
    float texture_position, texture_size;
    float line_start = 0, line_end = 0;
    float pack3, pack4 = 0;
};

class CPP_Core2D_ColorTexture {
private:
    std::vector<uint8_t> ShapeColors;
    std::vector<uintptr_t> PreviousShapeIDs;
    std::vector<uintptr_t> CurrentShapeIDs;
    uint32_t ColorCount = 0;

    bool UsingCache = false;

public:
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

    uint32_t AddColor(CPP_Color *Color, uintptr_t ShapeID, bool ColorDataChanged) {
        if (UsingCache && PreviousShapeIDs.size() > ColorCount / 4 && PreviousShapeIDs[ColorCount / 4] == ShapeID) {
            // If the shape already has a color and it's just changed, update it in place
            if (ColorDataChanged) {
                size_t index = ColorCount - 4;

                Color->Get_RGBA(&ShapeColors[index]);
            }
            if (CurrentShapeIDs.empty() || CurrentShapeIDs.back() != ShapeID) {
                size_t currentShapeIndex = ColorCount / 4;

                if (currentShapeIndex < CurrentShapeIDs.size()) {
                    CurrentShapeIDs.resize(currentShapeIndex);
                }

                CurrentShapeIDs.push_back(ShapeID);
            }
            ColorCount += 4;
            return (ColorCount - 4) / 4; // Return existing color index
        }

        UsingCache = false;

        if (CurrentShapeIDs.empty() || CurrentShapeIDs.back() != ShapeID) {
            size_t currentShapeIndex = ColorCount / 4;

            if (currentShapeIndex < CurrentShapeIDs.size()) {
                CurrentShapeIDs.resize(currentShapeIndex);
            }

            CurrentShapeIDs.push_back(ShapeID);
        }

        size_t needBytes = (size_t)ColorCount + 4;

        if (ShapeColors.size() < needBytes) {
            ShapeColors.resize(needBytes);
        }

        Color->Get_RGBA(&ShapeColors[ColorCount]);

        ColorCount += 4;
        return ColorCount - 4;
    }

    void Reset() {
        ShapeColors.clear();
        ColorCount = 0;
        PreviousShapeIDs = CurrentShapeIDs;
        UsingCache = true;
    }

    void Assemble() {
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