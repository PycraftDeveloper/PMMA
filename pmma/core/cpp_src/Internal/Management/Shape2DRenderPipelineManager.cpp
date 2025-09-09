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
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
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
    // If the shape color array changed, upload a new 1D texture containing
    // the color palette. We'll use RGBA8 (unsigned bytes) format.
    if (Changed) {
        // detect alpha presence (for potential blend state later)
        HasAlpha = false;
        for (const auto &c : shape_colors) {
            if (c.a < 1.0f) { HasAlpha = true; break; }
        }

        // --- Build or update vertex buffer data ---
        // Convert your Vertex -> BgfxVertex
        std::vector<BgfxVertex> bgfxVerts;
        bgfxVerts.reserve(combined_vertexes.size());
        for (const auto &v : combined_vertexes) {
            BgfxVertex bv;
            bv.x = v.position.x;
            bv.y = v.position.y;
            // Pack shape_id into texcoord.x as a float. Shader will interpret it
            // as an integer index (via floor() / int()) when sampling.
            bv.s = static_cast<float>(v.shape_id);
            bv.t = 0.0f;
            bgfxVerts.push_back(bv);
        }

        // Create or update vertex buffer.
        // We use a static vertex buffer that we update with bgfx::update.
        // For larger/streaming workloads you can switch to transient or dynamic
        // strategies later.

        const bgfx::Memory* mem = bgfx::copy(bgfxVerts.data(), (uint32_t)(bgfxVerts.size()*sizeof(BgfxVertex)));

        if (bgfx::isValid(m_vbh)) {
            if (m_vertexCount != bgfxVerts.size()) {
                bgfx::destroy(m_vbh);
                m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
            } else {
                bgfx::update(m_vbh, 0, mem);
            }
        } else {
            m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
        }
        m_vertexCount = bgfxVerts.size();

        // --- Create / update color texture ---
        // We create a 1 x N texture (height 1, width = number of colors) in RGBA8.
        uint32_t numColors = (uint32_t)shape_colors.size();
        uint32_t width  = std::min(PMMA_Core::RenderPipelineCore->MaxWidth, numColors);
        uint32_t height = (numColors + width - 1) / width;

        std::vector<uint8_t> colData((size_t)width * (size_t)height * 4, 0);

        // fill the texture row-major
        for (uint32_t i = 0; i < (uint32_t)numColors; ++i) {
            glm::vec4 c = shape_colors[i];
            uint32_t x = i % width;
            uint32_t y = i / width;
            uint32_t idx = (y * width + x) * 4;

            colData[idx + 0] = static_cast<uint8_t>(glm::clamp(c.r, 0.0f, 1.0f) * 255.0f);
            colData[idx + 1] = static_cast<uint8_t>(glm::clamp(c.g, 0.0f, 1.0f) * 255.0f);
            colData[idx + 2] = static_cast<uint8_t>(glm::clamp(c.b, 0.0f, 1.0f) * 255.0f);
            colData[idx + 3] = static_cast<uint8_t>(glm::clamp(c.a, 0.0f, 1.0f) * 255.0f);
        }

        const bgfx::Memory* texMem = bgfx::copy(colData.data(), (uint32_t)colData.size());

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

        // reset changed flag
        Changed = false;
    }

    if (!bgfx::isValid(m_vbh) || combined_vertexes.empty()) {
        InsertionIndex = 0;
        return;
    }

    // Setup rendering state
    uint64_t state = BGFX_STATE_WRITE_RGB | BGFX_STATE_WRITE_A | BGFX_STATE_PT_TRISTRIP;
    if (HasAlpha) {
        // enable alpha blending (src * src_alpha + dst * (1 - src_alpha))
        state |= BGFX_STATE_BLEND_FUNC(BGFX_STATE_BLEND_SRC_ALPHA, BGFX_STATE_BLEND_INV_SRC_ALPHA);
    }

    float info[4] = { float(m_colorTextureWidth), float(m_colorTextureHeight), 0.0f, 0.0f };
    bgfx::setUniform(u_colorInfo, info);

    // Set vertex buffer
    bgfx::setVertexBuffer(0, m_vbh);

    // Bind the color texture sampler to the fragment shader.
    // Use BGFX_SAMPLER_POINT when setting the texture to ensure exact nearest sampling.
    if (bgfx::isValid(m_tex)) {
        bgfx::setTexture(0, s_colorTex, m_tex, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
    }

    // Submit the draw call to the provided viewId
    bgfx::setState(state);
    bgfx::submit(0, PMMA_Core::RenderPipelineCore->Shape2D_RenderPipelineShader->Use());

    InsertionIndex = 0;
}