#pragma once
#include <cstdint>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

struct Vertex {
    float x, y, u, v;
};

struct InstanceData {
    float position, size;
    float point_count_width_gradient_type, rotation;
    float color_index, shape_type;
    float texture_position, texture_size;
};

class CPP_Shader;

class CPP_Core2D_RenderPipeline_ColorTexture {
private:
    std::vector<uint8_t> ShapeColors;
    uint32_t ColorCount = 0;

public:
    bgfx::TextureHandle ColorTexture;

    uint32_t m_colorTextureWidth = 0;
    uint32_t m_colorTextureHeight = 0;
    uint32_t MaxTextureDimension;

    CPP_Core2D_RenderPipeline_ColorTexture() {
        ColorTexture = BGFX_INVALID_HANDLE;
    }

    ~CPP_Core2D_RenderPipeline_ColorTexture() {
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
        // ShapeColors.clear();
        // ColorCount = 0;
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

class CPP_Core2D_RenderPipeline {
private:
    CPP_Shader *ShapeDefinitionsShaderProgram = nullptr;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;
    uint32_t instanceCount = 100'000;
    std::vector<InstanceData> instanceDataArray;

    bgfx::DynamicVertexBufferHandle instanceVbh;
    bgfx::VertexLayout instanceLayout;

    Vertex VertexData[4];
    uint16_t IndexData[6];
    uint32_t numTiles;

    bgfx::UniformHandle u_colorInfo;
    bgfx::UniformHandle s_colorTex;

    CPP_Core2D_RenderPipeline_ColorTexture ColorTexture;

public:
    CPP_Core2D_RenderPipeline();

    ~CPP_Core2D_RenderPipeline() {
        if (bgfx::isValid(u_colorInfo)) {
            bgfx::destroy(u_colorInfo);
        }

        if (bgfx::isValid(s_colorTex)) {
            bgfx::destroy(s_colorTex);
        }
    };

    inline void Reset() {
        ColorTexture.Reset();
    }

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

    void Render();
};