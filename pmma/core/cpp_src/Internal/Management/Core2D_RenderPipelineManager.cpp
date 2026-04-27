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

    OrthDisplayProj = bgfx::createUniform("OrthDisplayProj", bgfx::UniformType::Mat4);
};

void CPP_Core2D_RenderPipeline::Render() {
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);
    bgfx::setInstanceDataBuffer(&idb, 0, instanceCount);

    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_WRITE_Z |
        BGFX_STATE_DEPTH_TEST_LESS);

    float proj[16];
    PMMA_Core::DisplayInstance->GetOrthographicProjection(proj);
    bgfx::setUniform(OrthDisplayProj, proj);

    bgfx::submit(0, ShapeDefinitionsShaderProgram->Use());
}