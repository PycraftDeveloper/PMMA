#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <vector>

#include "Internal/Management/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance::CPP_RenderPipelineInstance() {
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .end();

    instanceLayout.begin()
        .add(bgfx::Attrib::TexCoord7, 4, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord6, 4, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord5, 4, bgfx::AttribType::Float)
        .end();

    s_colorTex = bgfx::createUniform(
        "s_colorTex",
        bgfx::UniformType::Sampler);

    u_colorInfo = bgfx::createUniform(
        "u_colorInfo",
        bgfx::UniformType::Vec4);

    OrthDisplayProj = bgfx::createUniform(
        "OrthDisplayProj",
        bgfx::UniformType::Mat4);

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
        bgfx::makeRef(
            VertexData,
            sizeof(Vertex) * 4),
        m_layout);

    ibh = bgfx::createIndexBuffer(
        bgfx::makeRef(
            IndexData,
            sizeof(uint16_t) * 6));

    instanceVbh = bgfx::createDynamicVertexBuffer(
        instanceCount,
        instanceLayout);

    const bgfx::Caps *caps = bgfx::getCaps();

    ColorTexture.MaxTextureDimension =
        std::min(
            (uint32_t)caps->limits.maxTextureSize,
            (uint32_t)std::numeric_limits<uint16_t>::max());
}

void PMMA::Internal::Rendering::Core2D::CPP_RenderPipelineInstance::Render() {
    if (ColorChanged || !ColorTexture.UsingCache) {
        PMMA_Core::DisplayInstance->TriggerEventRefresh();

        ColorTexture.Assemble();
    }

    if (ShapePropertyChanged || instanceCount != PreviousBufferSize || !bgfx::isValid(instanceVbh)) {
        CurrentInstanceData.resize(instanceCount); // Free memory if instanceCount decreased
        CurrentInstanceData.shrink_to_fit();       // Free memory if instanceCount decreased

        CurrentShapeIDs.resize(instanceCount);
        CurrentShapeIDs.shrink_to_fit();

        PreviousShapeIDs[BufferID] = CurrentShapeIDs;
        PreviousInstanceData[BufferID] = CurrentInstanceData;

        PMMA_Core::DisplayInstance->TriggerEventRefresh();

        uint32_t CurrentBufferSize = PreviousInstanceData[BufferID].size();

        const bgfx::Memory *instanceDataMem = bgfx::makeRef(
            PreviousInstanceData[BufferID].data(),
            CurrentBufferSize * sizeof(InstanceData));

        if (bgfx::isValid(instanceVbh)) {
            if (CurrentBufferSize != PreviousBufferSize) {
                bgfx::destroy(instanceVbh);
                instanceVbh = bgfx::createDynamicVertexBuffer(
                    instanceDataMem,
                    instanceLayout);
            } else {
                bgfx::update(
                    instanceVbh,
                    0,
                    instanceDataMem);
            }
        } else {
            instanceVbh = bgfx::createDynamicVertexBuffer(
                instanceDataMem,
                instanceLayout);
        }

        PreviousBufferSize = CurrentBufferSize;

        PreviousBufferID = BufferID;
        BufferID = (BufferID + 1) % 4;
    }

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
        PreviousBufferSize);

    bgfx::setTexture(0, s_colorTex, ColorTexture.ColorTexture, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);

    bgfx::setState(
        BGFX_STATE_WRITE_RGB |
        BGFX_STATE_WRITE_A |
        BGFX_STATE_BLEND_ALPHA);

    bgfx::submit(
        0,
        ShapeDefinitionsShaderProgram->Use());
}