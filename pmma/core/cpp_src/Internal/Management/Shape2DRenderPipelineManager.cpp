#include <vector>
#include <cstdint>
#include <cstring>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>
#include <bx/math.h>
#include <glm/glm.hpp>

#include "PMMA_Core.hpp"

CPP_Shape2D_RenderPipelineManager::CPP_Shape2D_RenderPipelineManager() {
    // create vertex layout
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 1, bgfx::AttribType::Float)
        .end();

    // initial handles are BGFX_INVALID_HANDLE
    m_vbh = BGFX_INVALID_HANDLE;
    m_tex = BGFX_INVALID_HANDLE;

    s_colorTex   = bgfx::createUniform("s_colorTex", bgfx::UniformType::Sampler);
    u_colorInfo  = bgfx::createUniform("u_colorInfo", bgfx::UniformType::Vec4);
}

CPP_Shape2D_RenderPipelineManager::~CPP_Shape2D_RenderPipelineManager() {
    if (bgfx::isValid(m_vbh)) {
        bgfx::destroy(m_vbh);
    }

    if (bgfx::isValid(m_tex)) {
        bgfx::destroy(m_tex);
    }

    if (bgfx::isValid(s_colorTex)) {
        bgfx::destroy(s_colorTex);
    }

    if (bgfx::isValid(u_colorInfo)) {
        bgfx::destroy(u_colorInfo);
    }
}

void CPP_Shape2D_RenderPipelineManager::InternalRender() {
    if (VertexDataChanged) {
        combined_vertexes.resize(LiveVertexCount);
        PreviousRenderContent.resize(InsertionIndex);

        const bgfx::Memory* mem = bgfx::copy( // Need to use copy here due to large sizes.
            combined_vertexes.data(),
            (uint32_t)(combined_vertexes.size()*sizeof(Vertex)));

        if (bgfx::isValid(m_vbh)) {
            if (m_vertexCount != combined_vertexes.size()) {
                bgfx::destroy(m_vbh);
                m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
            } else {
                bgfx::update(m_vbh, 0, mem);
            }
        } else {
            m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
        }
        m_vertexCount = combined_vertexes.size();
    }

    if (ColorDataChanged) {
        shape_colors.resize(LiveColorCount);

        uint32_t numColors = (uint32_t)shape_colors.size() / 4;
        uint32_t width  = std::min(PMMA_Core::RenderPipelineCore->MaxWidth, numColors);
        uint32_t height = (numColors + width - 1) / width;

        size_t expectedSize = width * height * 4;
        if (shape_colors.size() < expectedSize) {
            shape_colors.resize(expectedSize, 0); // Pad with transparent black
        }

        const bgfx::Memory* texMem = bgfx::copy(
            shape_colors.data(),
            static_cast<uint32_t>(shape_colors.size() * sizeof(uint8_t))
        );

        // If texture exists but size changed, destroy and recreate it
        if (bgfx::isValid(m_tex)) {
            if (m_colorTextureWidth != width || m_colorTextureHeight != height) {
                bgfx::destroy(m_tex);
                m_tex = BGFX_INVALID_HANDLE;
            }
        }

        // create texture if missing
        if (!bgfx::isValid(m_tex)) {
            m_tex = bgfx::createTexture2D(
                (uint16_t)width, (uint16_t)height,
                false,   // hasMips
                1,       // num layers
                bgfx::TextureFormat::RGBA8,
                BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
        }

        bgfx::updateTexture2D(m_tex, 0, 0, 0, 0, width, height, texMem);

        // store width/height for shader normalization
        m_colorTextureWidth  = width;
        m_colorTextureHeight = height;
    }

    // Setup rendering state
    uint64_t state = BGFX_STATE_WRITE_RGB | BGFX_STATE_WRITE_A | BGFX_STATE_PT_TRISTRIP;

    // enable alpha blending (src * src_alpha + dst * (1 - src_alpha))
    state |= BGFX_STATE_BLEND_FUNC(BGFX_STATE_BLEND_SRC_ALPHA, BGFX_STATE_BLEND_INV_SRC_ALPHA);

    float info[4] = { float(m_colorTextureWidth), float(m_colorTextureHeight), 0.0f, 0.0f };
    bgfx::setUniform(u_colorInfo, info);

    // Set vertex buffer
    bgfx::setVertexBuffer(0, m_vbh);

    // Bind the color texture sampler to the fragment shader.
    // Use BGFX_SAMPLER_POINT when setting the texture to ensure exact nearest sampling.
    bgfx::setTexture(0, s_colorTex, m_tex, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);

    // Submit the draw call to the provided viewId
    bgfx::setState(state);
    bgfx::submit(0, PMMA_Core::RenderPipelineCore->Shape2D_RenderPipelineShader->Use());
}