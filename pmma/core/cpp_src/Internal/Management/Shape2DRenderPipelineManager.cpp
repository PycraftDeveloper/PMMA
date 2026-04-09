#include <cstdint>
#include <cstring>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>
#include <bx/math.h>
#include <glm/glm.hpp>

#include "PMMA_Core.hpp"

CPP_Shape2D_RenderPipelineManager::CPP_Shape2D_RenderPipelineManager() {
    // create vertex layout
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::Color0, 4, bgfx::AttribType::Uint8, true)
        .end();

    m_vbh = BGFX_INVALID_HANDLE;
}

CPP_Shape2D_RenderPipelineManager::~CPP_Shape2D_RenderPipelineManager() {
    if (bgfx::isValid(m_vbh)) {
        bgfx::destroy(m_vbh);
    }
}

void CPP_Shape2D_RenderPipelineManager::InternalRender() {
    if (VertexDataChanged || ColorDataChanged) {
        glfwPostEmptyEvent();

        combined_vertexes[LiveBufferCount].resize(LiveVertexCount);
        PreviousRenderContent[LivePreviousRenderContent].resize(InsertionIndex);

        const bgfx::Memory *mem = bgfx::makeRef(
            combined_vertexes[LiveBufferCount].data(),
            (uint32_t)(combined_vertexes[LiveBufferCount].size() * sizeof(Vertex)));

        if (bgfx::isValid(m_vbh)) {
            if (m_vertexCount != combined_vertexes[LiveBufferCount].size()) {
                bgfx::destroy(m_vbh);
                m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
            } else {
                bgfx::update(m_vbh, 0, mem);
            }
        } else {
            m_vbh = bgfx::createDynamicVertexBuffer(mem, m_layout);
        }
        m_vertexCount = combined_vertexes[LiveBufferCount].size();

        LiveBufferCount++;
        if (LiveBufferCount > 3) {
            LiveBufferCount = 0;
        }
    }

    // Setup rendering state
    uint64_t state = BGFX_STATE_WRITE_RGB | BGFX_STATE_WRITE_A | BGFX_STATE_PT_TRISTRIP;

    // enable alpha blending (src * src_alpha + dst * (1 - src_alpha))
    state |= BGFX_STATE_BLEND_FUNC(BGFX_STATE_BLEND_SRC_ALPHA, BGFX_STATE_BLEND_INV_SRC_ALPHA);

    // Set vertex buffer
    bgfx::setVertexBuffer(0, m_vbh);

    // Submit the draw call to the provided viewId
    bgfx::setState(state);
    bgfx::submit(0, PMMA_Core::RenderPipelineCore->Shape2D_RenderPipelineShader->Use());

    LivePreviousRenderContent++;
    if (LivePreviousRenderContent > 3) {
        LivePreviousRenderContent = 0;
    }
}