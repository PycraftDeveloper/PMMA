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

    ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "Visibility";
    ShapeVisibilityShaderProgram = new CPP_Shader();
    ShapeVisibilityShaderProgram->LoadShaderFromFolder(ShaderPath, true);

    ShaderPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "shaders" + PMMA_Registry::PathSeparator + "2D_Core" + PMMA_Registry::PathSeparator + "TileBinning";
    TileBinningShaderProgram = new CPP_Shader();
    TileBinningShaderProgram->LoadShaderFromFolder(ShaderPath, true);

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
};

void CPP_Core2D_RenderPipeline::Render() {
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setIndexBuffer(ibh);

    bgfx::submit(0, ShapeDefinitionsShaderProgram->Use());
}