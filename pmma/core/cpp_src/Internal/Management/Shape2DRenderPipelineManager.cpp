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

    // create a uniform for the color texture (sampler)
    s_colorTex = bgfx::createUniform("s_colorTex", bgfx::UniformType::Sampler);

    // initial handles are BGFX_INVALID_HANDLE
    m_vbh = BGFX_INVALID_HANDLE;
    m_tex = BGFX_INVALID_HANDLE;
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
            // Replace contents of existing buffer
            bgfx::update(m_vbh, 0, mem);
        } else {
            m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
        }

        // --- Create / update color texture ---
        // We create a 1 x N texture (height 1, width = number of colors) in RGBA8.
        const uint32_t width = (uint32_t)shape_colors.size() > 0 ? (uint32_t)shape_colors.size() : 1u;
        std::vector<uint8_t> colData(width * 4);
        for (uint32_t i = 0; i < width; ++i) {
            glm::vec4 c(0.0f);
            if (i < shape_colors.size()) c = shape_colors[i];
            // clamp and convert to 0..255
            colData[i*4 + 0] = static_cast<uint8_t>(glm::clamp(c.r, 0.0f, 1.0f) * 255.0f);
            colData[i*4 + 1] = static_cast<uint8_t>(glm::clamp(c.g, 0.0f, 1.0f) * 255.0f);
            colData[i*4 + 2] = static_cast<uint8_t>(glm::clamp(c.b, 0.0f, 1.0f) * 255.0f);
            colData[i*4 + 3] = static_cast<uint8_t>(glm::clamp(c.a, 0.0f, 1.0f) * 255.0f);
        }

        const bgfx::Memory* texMem = bgfx::copy(colData.data(), (uint32_t)colData.size());

        if (bgfx::isValid(m_tex)) {
            // update existing texture
            bgfx::updateTexture2D(m_tex, 0, 0, 0, 0, width, 1, texMem, (uint16_t)(4));
        } else {
            // create texture: 1 x width (height=1) with RGBA8 format
            m_tex = bgfx::createTexture2D((uint16_t)width, 1, false, 1, bgfx::TextureFormat::RGBA8, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP);
            bgfx::updateTexture2D(m_tex, 0, 0, 0, 0, width, 1, texMem, (uint16_t)(4));
        }

        // store width for shader normalization
        m_colorTextureWidth = width;

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

    // Set vertex buffer
    bgfx::setVertexBuffer(0, m_vbh);

    // Bind the color texture sampler to the fragment shader.
    // Use BGFX_SAMPLER_POINT when setting the texture to ensure exact nearest sampling.
    if (bgfx::isValid(m_tex)) {
        bgfx::setTexture(0, s_colorTex, m_tex, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
    }

    // Set transform (identity). If you have a projection/view matrix, set them via uniforms or setTransform.
    float mtx[16];
    bx::mtxIdentity(mtx);
    bgfx::setTransform(mtx);

    // Submit the draw call to the provided viewId
    bgfx::setState(state);
    bgfx::submit(0, PMMA_Core::RenderPipelineCore->Shape2D_RenderPipelineShader->Use());

    InsertionIndex = 0;
}