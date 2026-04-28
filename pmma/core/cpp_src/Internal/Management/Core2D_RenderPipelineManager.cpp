#include <cmath>
#include <string>

#include "Internal/Management/Core2D_RenderPipelineManager.hpp"
#include "PMMA_Core.hpp"

CPP_Core2D_RenderPipeline::CPP_Core2D_RenderPipeline() {
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .end();

    std::string ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "ShapeDefinitions";
    ShapeDefinitionsShaderProgram = new CPP_Shader();
    ShapeDefinitionsShaderProgram->LoadShaderFromFolder(ShaderPath, true);

    ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "ShapeVisibility";
    ShapeVisibilityShaderProgram = new CPP_Shader();
    ShapeVisibilityShaderProgram->LoadShaderFromFolder(ShaderPath, true);

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

    // Write instance data
    bgfx::allocInstanceDataBuffer(&idb, instanceCount, sizeof(InstanceData));
    InstanceData *data = (InstanceData *)idb.data;

    for (uint32_t i = 0; i < instanceCount - 1; i++) {
        data[i].x = rand() % 1280;
        data[i].y = rand() % 720;
        data[i].w = 50.0f;
        data[i].h = 50.0f;
        data[i].r = rand() % 256 / 255.0f;
        data[i].g = rand() % 256 / 255.0f;
        data[i].b = rand() % 256 / 255.0f;
        data[i].a = 1.0f;
    }

    data[instanceCount - 1].x = 0.0f;
    data[instanceCount - 1].y = 0.0f;
    data[instanceCount - 1].w = 50.0f;
    data[instanceCount - 1].h = 50.0f;
    data[instanceCount - 1].r = 1.0f;
    data[instanceCount - 1].g = 0.0f;
    data[instanceCount - 1].b = 0.0f;
    data[instanceCount - 1].a = 1.0f;

    OrthDisplayProj = bgfx::createUniform("OrthDisplayProj", bgfx::UniformType::Mat4);
};

void CPP_Core2D_RenderPipeline::Render() {
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);
    bgfx::setInstanceDataBuffer(&idb, 0, instanceCount);

    float proj[16];
    PMMA_Core::DisplayInstance->GetOrthographicProjection(proj);
    bgfx::setUniform(OrthDisplayProj, proj);

    // -----------------------------------------
    // PASS 1: VISIBILITY (cheap)
    // -----------------------------------------
    bgfx::setState(
        BGFX_STATE_WRITE_Z |       // only write depth
        BGFX_STATE_DEPTH_TEST_LESS // normal depth test
    );

    bgfx::submit(0, ShapeVisibilityShaderProgram->Use());

    // -----------------------------------------
    // PASS 2: SHADING (expensive)
    // -----------------------------------------
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);
    bgfx::setInstanceDataBuffer(&idb, 0, instanceCount);

    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_DEPTH_TEST_EQUAL | // only draw visible pixels
        BGFX_STATE_BLEND_ALPHA        // keep your blending
        // NOTE: NO WRITE_Z here
    );

    bgfx::submit(0, ShapeDefinitionsShaderProgram->Use());
}