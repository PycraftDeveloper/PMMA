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
    uint32_t ColorCount = 0;

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

    uint32_t AddColor(uint8_t *Color) {
        size_t needBytes = (size_t)ColorCount + 4;

        if (ShapeColors.size() < needBytes) {
            ShapeColors.resize(needBytes);
        }

        ShapeColors[ColorCount] = Color[0];
        ShapeColors[ColorCount + 1] = Color[1];
        ShapeColors[ColorCount + 2] = Color[2];
        ShapeColors[ColorCount + 3] = Color[3];

        ColorCount += 4;
        return ColorCount - 4;
    }

    void Reset() {
        ShapeColors.clear();
        ColorCount = 0;
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

    void Reset();

    void Render();
};