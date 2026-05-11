#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>

#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

CPP_Core2D_RenderPipeline::CPP_Core2D_RenderPipeline()
{
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
        .add(bgfx::Attrib::TexCoord7, 4, bgfx::AttribType::Float) // x, y, w, h
        .add(bgfx::Attrib::TexCoord6, 4, bgfx::AttribType::Float) // r, g, b, a
        .end();

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
    ShapeDefinitionsShaderProgram->LoadShaderFromFolder(ShaderPath, true);

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
        bgfx::makeRef(VertexData, sizeof(Vertex) * 4),
        m_layout);

    ibh = bgfx::createIndexBuffer(
        bgfx::makeRef(IndexData, sizeof(uint16_t) * 6));

    //
    // Create CPU-side instance storage
    //
    instanceDataArray.resize(instanceCount);

    for (uint32_t i = 0; i < instanceCount; ++i)
    {
        instanceDataArray[i].x = static_cast<float>(rand() % 1280);
        instanceDataArray[i].y = static_cast<float>(rand() % 720);

        instanceDataArray[i].w = 2.0f;
        instanceDataArray[i].h = 2.0f;

        instanceDataArray[i].r = (rand() % 256) / 255.0f;
        instanceDataArray[i].g = (rand() % 256) / 255.0f;
        instanceDataArray[i].b = (rand() % 256) / 255.0f;
        instanceDataArray[i].a = 1.0f;
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
    // Projection uniform
    //
    OrthDisplayProj = bgfx::createUniform(
        "OrthDisplayProj",
        bgfx::UniformType::Mat4);
}

void CPP_Core2D_RenderPipeline::Render()
{
    //
    // Projection matrix
    //
    float proj[16];
    PMMA_Core::DisplayInstance->GetOrthographicProjection(proj);

    bgfx::setUniform(OrthDisplayProj, proj);

    //
    // Bind quad geometry
    //
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);

    //
    // Bind instance buffer PROPERLY
    //
    bgfx::setInstanceDataBuffer(
        instanceVbh,
        0,
        instanceCount);

    //
    // Render state
    //
    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_BLEND_ALPHA);

    //
    // Submit draw
    //
    bgfx::submit(
        0,
        ShapeDefinitionsShaderProgram->Use());
}