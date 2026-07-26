#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <vector>

#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

PMMA::Internal::Rendering::Core2D::RenderPipelineInstance::RenderPipelineInstance() {
    ID = reinterpret_cast<uintptr_t>(this);

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

    s_Tex = bgfx::createUniform(
        "s_Tex",
        bgfx::UniformType::Sampler);

    u_textureInfo = bgfx::createUniform(
        "u_textureInfo",
        bgfx::UniformType::Vec4);

    OrthDisplayProj = bgfx::createUniform(
        "OrthDisplayProj",
        bgfx::UniformType::Mat4);

    u_transparency = bgfx::createUniform(
        "HasTransparency",
        bgfx::UniformType::Vec4);

    std::string ShaderPath =
        PMMA::Registry::PMMA_Location +
        PMMA::Registry::PathSeparator +
        "shaders" +
        PMMA::Registry::PathSeparator +
        "2D_Core" +
        PMMA::Registry::PathSeparator +
        "ShapeDefinitions";

    ShapeDefinitionsShaderProgram = new PMMA::Graphics::Shader();
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

    OpaqueInstanceVbh = bgfx::createDynamicVertexBuffer(
        OpaqueInstanceCount,
        instanceLayout);

    TransparentInstanceVbh = bgfx::createDynamicVertexBuffer(
        TransparentInstanceCount,
        instanceLayout);

    const bgfx::Caps *caps = bgfx::getCaps();

    uint32_t MaxTextureDimension = std::min(
        (uint32_t)caps->limits.maxTextureSize,
        (uint32_t)std::numeric_limits<uint16_t>::max());

    ColorTexture.MaxTextureDimension = MaxTextureDimension;

    TextureManager.MaxTextureDimension = MaxTextureDimension;
    TextureManager.RenderPipelineInstanceID = ID;
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineInstance::AdvanceView() {
    PMMA::Registry::RollingViewID++;
    if (PMMA::Registry::RollingViewID >= PMMA::Registry::MaxViewID) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            64,
            "The maximum number of internal views has been exceeded. \
Please consider reducing the number of windows or quantity of 2D shapes \
rendered if rendering more than 16,777,216 shapes to a single window.");

        throw std::runtime_error("The maximum number of internal views has been exceeded.");
    }

    bgfx::setViewRect(
        PMMA::Registry::RollingViewID,
        0,
        0,
        PMMA::Core::ActiveDisplayInstance->GetWidth(),
        PMMA::Core::ActiveDisplayInstance->GetHeight());

    bgfx::setViewFrameBuffer(
        PMMA::Registry::RollingViewID,
        PMMA::Core::ActiveDisplayInstance->DisplayFrameBufferHandle);

    bgfx::setViewClear(
        PMMA::Registry::RollingViewID,
        BGFX_CLEAR_DEPTH,
        0,
        1.0f,
        0);

    bgfx::touch(PMMA::Registry::RollingViewID);
}

void PMMA::Internal::Rendering::Core2D::RenderPipelineInstance::Render() {
    if (ColorChanged || !ColorTexture.UsingCache) {
        PMMA::Core::ActiveDisplayInstance->TriggerEventRefresh();

        ColorTexture.Assemble();
    }

    if (TextureManager.Dirty) {
        TextureManager.Assemble();
    }

    if (ShapePropertyChanged || OpaqueInstanceCount != OpaquePreviousBufferSize || TransparentInstanceCount != TransparentPreviousBufferSize || !bgfx::isValid(OpaqueInstanceVbh) || !bgfx::isValid(TransparentInstanceVbh)) {
        PMMA::Core::ActiveDisplayInstance->TriggerEventRefresh();

        CurrentInstanceData[0].resize(OpaqueInstanceCount); // Free memory if instanceCount decreased
        CurrentInstanceData[0].shrink_to_fit();             // Free memory if instanceCount decreased

        CurrentInstanceData[1].resize(TransparentInstanceCount); // Free memory if instanceCount decreased
        CurrentInstanceData[1].shrink_to_fit();                  // Free memory if instanceCount decreased

        CurrentShapeIDs[0].resize(OpaqueInstanceCount);
        CurrentShapeIDs[0].shrink_to_fit();

        CurrentShapeIDs[1].resize(TransparentInstanceCount);
        CurrentShapeIDs[1].shrink_to_fit();

        PreviousShapeIDs[BufferID] = CurrentShapeIDs;

        {
            // opaque first
            // Ensure destination has the exact required memory allocated
            PreviousInstanceData[BufferID][0].resize(CurrentInstanceData[0].size());

            // 1. Extract raw pointers to bypass all vector indexing and bounds-checking overhead
            uint32_t ArrayLength = CurrentInstanceData[0].size();

            if (ArrayLength > 0) {
                const auto *__restrict src = CurrentInstanceData[0].data() + ArrayLength - 1;
                auto *__restrict dest = PreviousInstanceData[BufferID][0].data();
                const auto *const end = dest + ArrayLength;

                // 2. Blazing fast single-pass copy and reverse loop
                while (dest < end) {
                    *dest++ = *src--;
                }
            }

            if (ArrayLength > 0) {

                const bgfx::Memory *OpaqueInstanceDataMem = bgfx::makeRef(
                    PreviousInstanceData[BufferID][0].data(),
                    ArrayLength * sizeof(InstanceData));

                if (bgfx::isValid(OpaqueInstanceVbh)) {
                    if (ArrayLength != OpaquePreviousBufferSize) {
                        bgfx::destroy(OpaqueInstanceVbh);
                        OpaqueInstanceVbh = bgfx::createDynamicVertexBuffer(
                            OpaqueInstanceDataMem,
                            instanceLayout);
                    } else {
                        bgfx::update(
                            OpaqueInstanceVbh,
                            0,
                            OpaqueInstanceDataMem);
                    }
                } else {
                    OpaqueInstanceVbh = bgfx::createDynamicVertexBuffer(
                        OpaqueInstanceDataMem,
                        instanceLayout);
                }
            }

            OpaquePreviousBufferSize = ArrayLength;
        }
        {
            // then transparent

            // Ensure destination has the exact required memory allocated
            PreviousInstanceData[BufferID][1] = CurrentInstanceData[1];

            uint32_t CurrentBufferSize = PreviousInstanceData[BufferID][1].size();

            if (CurrentBufferSize > 0) {

                const bgfx::Memory *TransparentInstanceDataMem = bgfx::makeRef(
                    PreviousInstanceData[BufferID][1].data(),
                    CurrentBufferSize * sizeof(InstanceData));

                if (bgfx::isValid(TransparentInstanceVbh)) {
                    if (CurrentBufferSize != TransparentPreviousBufferSize) {
                        bgfx::destroy(TransparentInstanceVbh);
                        TransparentInstanceVbh = bgfx::createDynamicVertexBuffer(
                            TransparentInstanceDataMem,
                            instanceLayout);
                    } else {
                        bgfx::update(
                            TransparentInstanceVbh,
                            0,
                            TransparentInstanceDataMem);
                    }
                } else {
                    TransparentInstanceVbh = bgfx::createDynamicVertexBuffer(
                        TransparentInstanceDataMem,
                        instanceLayout);
                }
            }

            TransparentPreviousBufferSize = CurrentBufferSize;
        }
        // end

        PreviousBufferID = BufferID;
        BufferID = (BufferID + 1) % 4;
    }

    // opaque
    if (OpaquePreviousBufferSize > 0) {
        float proj[16];
        PMMA::Core::ActiveDisplayInstance->GetOrthographicProjection(proj);
        bgfx::setUniform(OrthDisplayProj, proj);

        float textureInfo[4] = {float(ColorTexture.m_colorTextureWidth), float(ColorTexture.m_colorTextureHeight), float(TextureManager.m_TextureWidth), float(TextureManager.m_TextureHeight)};
        bgfx::setUniform(u_textureInfo, textureInfo);

        bgfx::setVertexBuffer(0, vbh);
        bgfx::setIndexBuffer(ibh);

        bgfx::setTexture(0, s_colorTex, ColorTexture.ColorTextureHandle, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
        bgfx::setTexture(1, s_Tex, TextureManager.TextureHandle, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP);

        float transparencyInfo[4] = {1.0f, 0.0f, 0.0f, 0.0f};
        bgfx::setUniform(u_transparency, transparencyInfo);

        bgfx::setInstanceDataBuffer(
            OpaqueInstanceVbh,
            0,
            OpaquePreviousBufferSize);

        bgfx::setState(
            BGFX_STATE_WRITE_RGB |
            BGFX_STATE_WRITE_A |
            BGFX_STATE_DEPTH_TEST_LEQUAL |
            BGFX_STATE_WRITE_Z);

        bgfx::submit(
            PMMA::Registry::RollingViewID,
            ShapeDefinitionsShaderProgram->Use());
    }

    // transparent
    if (TransparentPreviousBufferSize > 0) {
        float proj[16];
        PMMA::Core::ActiveDisplayInstance->GetOrthographicProjection(proj);
        bgfx::setUniform(OrthDisplayProj, proj);

        float textureInfo[4] = {float(ColorTexture.m_colorTextureWidth), float(ColorTexture.m_colorTextureHeight), float(TextureManager.m_TextureWidth), float(TextureManager.m_TextureHeight)};
        bgfx::setUniform(u_textureInfo, textureInfo);

        bgfx::setVertexBuffer(0, vbh);
        bgfx::setIndexBuffer(ibh);

        bgfx::setTexture(0, s_colorTex, ColorTexture.ColorTextureHandle, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
        bgfx::setTexture(1, s_Tex, TextureManager.TextureHandle, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP);

        float transparencyInfo[4] = {0.0f, 0.0f, 0.0f, 0.0f};
        bgfx::setUniform(u_transparency, transparencyInfo);

        bgfx::setInstanceDataBuffer(
            TransparentInstanceVbh,
            0,
            TransparentPreviousBufferSize);

        bgfx::setState(
            BGFX_STATE_WRITE_RGB |
            BGFX_STATE_WRITE_A |
            BGFX_STATE_BLEND_ALPHA |
            BGFX_STATE_DEPTH_TEST_LEQUAL);

        bgfx::submit(
            PMMA::Registry::RollingViewID,
            ShapeDefinitionsShaderProgram->Use());
    }

    AdvanceView();
}