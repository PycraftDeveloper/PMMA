#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <vector>

#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

CPP_Core2D_RenderPipeline::CPP_Core2D_RenderPipeline() {
    //
    // Quad vertex layout
    //
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .end();

    //
    // Instance layout
    //
    instanceLayout.begin()
        .add(bgfx::Attrib::TexCoord7, 4, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord6, 4, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord5, 4, bgfx::AttribType::Float)
        .end();

    //
    // Uniforms
    //
    s_colorTex = bgfx::createUniform(
        "s_colorTex",
        bgfx::UniformType::Sampler);

    u_colorInfo = bgfx::createUniform(
        "u_colorInfo",
        bgfx::UniformType::Vec4);

    OrthDisplayProj = bgfx::createUniform(
        "OrthDisplayProj",
        bgfx::UniformType::Mat4);

    //
    // Shader
    //
    std::string ShaderPath =
        PMMA_Registry::PMMA_Location +
        PMMA_Registry::PathSeparator +
        "shaders" +
        PMMA_Registry::PathSeparator +
        "2D_Core" +
        PMMA_Registry::PathSeparator +
        "ShapeDefinitions";

    ShapeDefinitionsShaderProgram = new CPP_Shader();
    ShapeDefinitionsShaderProgram->LoadShaderFromFolder(
        ShaderPath,
        true);

    //
    // Quad vertices
    //
    VertexData[0] = {-0.5f, -0.5f, 0.0f, 0.0f};
    VertexData[1] = {0.5f, -0.5f, 1.0f, 0.0f};
    VertexData[2] = {0.5f, 0.5f, 1.0f, 1.0f};
    VertexData[3] = {-0.5f, 0.5f, 0.0f, 1.0f};

    //
    // Quad indices
    //
    IndexData[0] = 0;
    IndexData[1] = 1;
    IndexData[2] = 2;
    IndexData[3] = 0;
    IndexData[4] = 2;
    IndexData[5] = 3;

    //
    // Static quad buffers
    //
    vbh = bgfx::createVertexBuffer(
        bgfx::makeRef(
            VertexData,
            sizeof(Vertex) * 4),
        m_layout);

    ibh = bgfx::createIndexBuffer(
        bgfx::makeRef(
            IndexData,
            sizeof(uint16_t) * 6));

    //
    // CPU-side instance storage
    //
    instanceDataArray.resize(instanceCount);

    srand((unsigned int)time(nullptr));

    for (uint32_t i = 0; i < instanceCount; ++i) {
        uint16_t x = static_cast<uint16_t>(rand() % 1280);
        uint16_t y = static_cast<uint16_t>(rand() % 720);

        uint8_t Color[4] =
            {
                static_cast<uint8_t>(rand() % 256),
                static_cast<uint8_t>(rand() % 256),
                static_cast<uint8_t>(rand() % 256),
                static_cast<uint8_t>(rand() % 256)};

        InstanceData &instance = instanceDataArray[i];

        // i_data0
        instance.position = PackValues(x, y);
        instance.size = PackValues(100, 100);
        instance.point_count_gradient_type = PackValues(0, 0);
        instance.rotation_shape_property = PackValues((rand() % 360) * 182, 300 * 182);
        // i_data1
        instance.color_index = ColorTexture.AddColor(Color);
        instance.shape_type_width = PackValues(3, 20);
        instance.texture_position = PackValues(730, 169);
        instance.texture_size = PackValues(480, 690);
        // i_data2
        instance.line_start = PackValues(0, 0);
        instance.line_end = PackValues(1, 1);
    }

    //
    // Create LARGE persistent dynamic instance buffer
    //
    instanceVbh = bgfx::createDynamicVertexBuffer(
        instanceCount,
        instanceLayout);

    //
    // Upload initial instance data
    //
    bgfx::update(
        instanceVbh,
        0,
        bgfx::copy(
            instanceDataArray.data(),
            instanceCount * sizeof(InstanceData)));

    //
    // Texture limits
    //
    const bgfx::Caps *caps = bgfx::getCaps();

    ColorTexture.MaxTextureDimension =
        std::min(
            (uint32_t)caps->limits.maxTextureSize,
            (uint32_t)std::numeric_limits<uint16_t>::max());
}

void CPP_Core2D_RenderPipeline::Render() {
    ColorTexture.Assemble();

    float proj[16];
    PMMA_Core::DisplayInstance->GetOrthographicProjection(proj);
    bgfx::setUniform(OrthDisplayProj, proj);

    float info[4] = {float(ColorTexture.m_colorTextureWidth), float(ColorTexture.m_colorTextureHeight), 0.0f, 0.0f};
    bgfx::setUniform(u_colorInfo, info);

    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);

    bgfx::setInstanceDataBuffer(
        instanceVbh,
        0,
        instanceCount);

    bgfx::setTexture(0, s_colorTex, ColorTexture.ColorTexture, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);

    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_BLEND_ALPHA);

    bgfx::submit(
        0,
        ShapeDefinitionsShaderProgram->Use());
}