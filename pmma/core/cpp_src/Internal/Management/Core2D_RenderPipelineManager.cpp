#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>

#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

//
// NOTE:
// This version uses correct bgfx rules:
// - CPU data -> GPU via dynamic buffer update
// - Compute reads from GPU vertex buffers
// - Double-buffered GPU compute input
//

CPP_Core2D_RenderPipeline::CPP_Core2D_RenderPipeline() {
    //
    // Quad layout
    //
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .end();

    //
    // Instance layout (shared for compute + render)
    //
    computeInstanceLayout.begin()
        .add(bgfx::Attrib::TexCoord0, 4, bgfx::AttribType::Float) // x y w h
        .add(bgfx::Attrib::TexCoord1, 4, bgfx::AttribType::Float) // r g b a
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

    ShaderPath =
        PMMA_Registry::PMMA_Location +
        PMMA_Registry::PathSeparator +
        "shaders" +
        PMMA_Registry::PathSeparator +
        "2D_Core" +
        PMMA_Registry::PathSeparator +
        "tile_binning.sc";

    TileBinningShaderProgram = new CPP_Shader();
    TileBinningShaderProgram->LoadComputeShader(ShaderPath, true);

    ShaderPath =
        PMMA_Registry::PMMA_Location +
        PMMA_Registry::PathSeparator +
        "shaders" +
        PMMA_Registry::PathSeparator +
        "2D_Core" +
        PMMA_Registry::PathSeparator +
        "tile_clear.sc";

    TileClearShaderProgram = new CPP_Shader();
    TileClearShaderProgram->LoadComputeShader(ShaderPath, true);

    //
    // Quad geometry
    //
    VertexData[0] = {-0.5f, -0.5f, 0.0f, 0.0f};
    VertexData[1] = {0.5f, -0.5f, 1.0f, 0.0f};
    VertexData[2] = {0.5f, 0.5f, 1.0f, 1.0f};
    VertexData[3] = {-0.5f, 0.5f, 0.0f, 1.0f};

    IndexData[0] = 0;
    IndexData[1] = 1;
    IndexData[2] = 2;
    IndexData[3] = 0;
    IndexData[4] = 2;
    IndexData[5] = 3;

    vbh = bgfx::createVertexBuffer(
        bgfx::makeRef(VertexData, sizeof(Vertex) * 4),
        m_layout);

    ibh = bgfx::createIndexBuffer(
        bgfx::makeRef(IndexData, sizeof(uint16_t) * 6));

    //
    // Instance data (CPU)
    //
    instanceDataArray.resize(instanceCount);

    for (uint32_t i = 0; i < instanceCount; i++) {
        instanceDataArray[i].x = float(rand() % 1280);
        instanceDataArray[i].y = float(rand() % 720);

        instanceDataArray[i].w = 50.0f;
        instanceDataArray[i].h = 50.0f;

        instanceDataArray[i].r = (rand() % 256) / 255.0f;
        instanceDataArray[i].g = (rand() % 256) / 255.0f;
        instanceDataArray[i].b = (rand() % 256) / 255.0f;
        instanceDataArray[i].a = 1.0f;
    }

    //
    // CPU staging buffer (dynamic update source)
    //
    cpuInstanceBuffer =
        bgfx::createDynamicVertexBuffer(
            instanceCount,
            computeInstanceLayout);

    //
    // Tile buffers
    //
    tilesX = (1280 + TILE_SIZE - 1) / TILE_SIZE;
    tilesY = (720 + TILE_SIZE - 1) / TILE_SIZE;
    numTiles = tilesX * tilesY;

    tileCountBuffer =
        bgfx::createDynamicIndexBuffer(
            numTiles,
            BGFX_BUFFER_COMPUTE_READ_WRITE);

    tileIndexBuffer =
        bgfx::createDynamicIndexBuffer(
            numTiles * MAX_PER_TILE,
            BGFX_BUFFER_COMPUTE_READ_WRITE);

    zeroCounts.resize(numTiles, 0);

    //
    // Uniforms
    //
    OrthDisplayProj =
        bgfx::createUniform(
            "OrthDisplayProj",
            bgfx::UniformType::Mat4);

    u_screenInfo =
        bgfx::createUniform(
            "u_screenInfo",
            bgfx::UniformType::Vec4);
}

//
// RENDER
//
void CPP_Core2D_RenderPipeline::Render() {
    //
    // Update CPU buffer (optional staging/debug use)
    //
    bgfx::update(
        cpuInstanceBuffer,
        0,
        bgfx::copy(
            instanceDataArray.data(),
            instanceCount * sizeof(InstanceData)));

    //
    // Clear tile counts
    //
    bgfx::setBuffer(
        0,
        cpuInstanceBuffer,
        bgfx::Access::Read);

    bgfx::setBuffer(
        1,
        tileCountBuffer,
        bgfx::Access::ReadWrite);

    bgfx::setBuffer(
        2,
        tileIndexBuffer,
        bgfx::Access::ReadWrite);

    //
    // Screen uniform
    //
    float screenInfo[4] =
        {
            1280.0f,
            720.0f,
            float(tilesX),
            float(tilesY)};

    bgfx::setUniform(u_screenInfo, screenInfo);

    //
    // Compute dispatch
    //
    uint32_t groups = (instanceCount + 63) / 64;

    bgfx::dispatch(0, TileClearShaderProgram->Use(), groups, 1, 1);

    bgfx::dispatch(
        0,
        TileBinningShaderProgram->Use(),
        groups,
        1,
        1);

    //
    // Projection
    //
    float proj[16];
    PMMA_Core::DisplayInstance->GetOrthographicProjection(proj);

    bgfx::setUniform(OrthDisplayProj, proj);

    //
    // Draw quad
    //
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);

    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_BLEND_ALPHA);

    bgfx::submit(
        1,
        ShapeDefinitionsShaderProgram->Use());

    //
    // Swap buffers
    //
    currentBuffer ^= 1;
}