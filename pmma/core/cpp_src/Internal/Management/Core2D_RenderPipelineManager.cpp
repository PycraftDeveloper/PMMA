#include <cmath>
#include <string>

#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

CPP_Core2D_RenderPipeline::CPP_Core2D_RenderPipeline() {
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .end();

    instanceLayout.begin()
        .add(bgfx::Attrib::TexCoord1, 4, bgfx::AttribType::Float) // xy = pos, zw = size
        .end();

    std::string ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "ShapeDefinitions";
    ShapeDefinitionsShaderProgram = new CPP_Shader();
    ShapeDefinitionsShaderProgram->LoadShaderFromFolder(ShaderPath, true);

    ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "Visibility";
    ShapeVisibilityShaderProgram = new CPP_Shader();
    ShapeVisibilityShaderProgram->LoadShaderFromFolder(ShaderPath, true);

    ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "TileBinning";
    TileBinningShaderProgram = new CPP_Shader();
    TileBinningShaderProgram->LoadShaderFromFolder(ShaderPath, true);

    ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "ClearBinning";
    ClearProgram = new CPP_Shader();
    ClearProgram->LoadShaderFromFolder(ShaderPath, true);

    VertexData[0] = {-1.0f, -1.0f, 0.0f, 0.0f};
    VertexData[1] = {1.0f, -1.0f, 1.0f, 0.0f};
    VertexData[2] = {1.0f, 1.0f, 1.0f, 1.0f};
    VertexData[3] = {-1.0f, 1.0f, 0.0f, 1.0f};

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

    const uint32_t MaxInstances = 1000000; // scale later

    instanceBuffer = bgfx::createDynamicVertexBuffer(
        MaxInstances,
        instanceLayout,
        BGFX_BUFFER_ALLOW_RESIZE);

    // Write instance data
    bgfx::allocInstanceDataBuffer(&idb, instanceCount, sizeof(InstanceData));
    InstanceData *data = (InstanceData *)idb.data;

    data[0].x = 100; // rand() % 1280;
    data[0].y = 100; // rand() % 720;
    data[0].w = 10.0f;
    data[0].h = 10.0f;
    data[0].r = 1.0f;
    data[0].g = 0.0f;
    data[0].b = 0.0f;
    data[0].a = 1.0f;

    data[1].x = 100; // rand() % 1280;
    data[1].y = 100; // rand() % 720;
    data[1].w = 10.0f;
    data[1].h = 10.0f;
    data[1].r = 0.0f;
    data[1].g = 1.0f;
    data[1].b = 0.0f;
    data[1].a = 1.0f;

    /*for (uint32_t i = 0; i < instanceCount; i++) {
        data[i]
            .x = 100; // rand() % 1280;
    data[i].y = 100;  // rand() % 720;
    data[i].w = 10.0f;
    data[i].h = 10.0f;
    data[i].r = 1.0f;
    data[i].g = 0.0f;
    data[i].b = 0.0f;
    data[i].a = 1.0f;
}*/

    bgfx::setInstanceDataBuffer(&idb, 0, instanceCount);

    OrthDisplayProj = bgfx::createUniform("OrthDisplayProj", bgfx::UniformType::Mat4);
    u_screenSize_tileSize_instanceCount =
        bgfx::createUniform("u_screenSize_tileSize_instanceCount", bgfx::UniformType::Vec4);

    quadBuffer =
        bgfx::createDynamicVertexBuffer(
            instanceCount,
            instanceLayout,
            BGFX_BUFFER_COMPUTE_READ);

    float TileSize = 32.0f;
    float tilesX = std::ceil(1920.0f / TileSize);
    float tilesY = std::ceil(1080.0f / TileSize);

    numTiles = static_cast<uint32_t>(tilesX * tilesY);

    uint32_t maxQuadsPerTile = 128;
    uint32_t tileDataSize = numTiles * maxQuadsPerTile;

    tileWriteOffset =
        bgfx::createDynamicVertexBuffer(
            numTiles,
            bgfx::VertexLayout()
                .begin()
                .add(bgfx::Attrib::TexCoord0, 1, bgfx::AttribType::Uint32) // No Uint32
                .end(),
            BGFX_BUFFER_COMPUTE_READ_WRITE);

    tileData =
        bgfx::createDynamicVertexBuffer(
            tileDataSize,
            instanceLayout,
            BGFX_BUFFER_COMPUTE_READ_WRITE | BGFX_BUFFER_ALLOW_RESIZE);
};

void CPP_Core2D_RenderPipeline::Render() {
    // =====================================================
    // 0. FRAME CONSTANTS
    // =====================================================

    float screenW = 1280.0f;
    float screenH = 720.0f;
    float tileSize = 32.0f;

    float computeData[4] =
        {
            screenW,
            screenH,
            tileSize,
            (float)instanceCount};

    bgfx::setUniform(u_screenSize_tileSize_instanceCount, computeData);

    // =====================================================
    // 1. CLEAR PHASE (ONLY COUNTERS - NOT DATA)
    // =====================================================
    // We only reset tileWriteOffset (critical buffer)

    bgfx::setBuffer(0, tileWriteOffset, bgfx::Access::Write);
    bgfx::dispatch(0, ClearProgram->Use(), (numTiles + 63) / 64, 1, 1);

    // =====================================================
    // 2. BINNING COMPUTE PASS
    // =====================================================

    bgfx::setBuffer(0, quadBuffer, bgfx::Access::Read);
    bgfx::setBuffer(1, tileWriteOffset, bgfx::Access::ReadWrite);
    bgfx::setBuffer(2, tileData, bgfx::Access::ReadWrite);

    uint32_t groups = (instanceCount + 63) / 64;

    bgfx::dispatch(0, TileBinningShaderProgram->Use(), groups, 1, 1);

    // =====================================================
    // 3. RENDER PASS
    // =====================================================

    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);

    // IMPORTANT:
    // We are NOT using CPU instance buffer anymore for final scaling path
    // (eventually replace with indirect draw or GPU-driven fetch)

    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_WRITE_Z |
        BGFX_STATE_DEPTH_TEST_LESS);

    float proj[16];
    PMMA_Core::DisplayInstance->GetOrthographicProjection(proj);
    bgfx::setUniform(OrthDisplayProj, proj);

    bgfx::submit(1, ShapeDefinitionsShaderProgram->Use());
}