#pragma once
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

struct Vertex {
    float x, y, u, v;
};

class CPP_Shader;

class CPP_Core2D_RenderPipeline {
private:
    CPP_Shader *ShapeDefinitionsShaderProgram = nullptr;
    CPP_Shader *ShapeVisibilityShaderProgram = nullptr;
    CPP_Shader *TileBinningShaderProgram = nullptr;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;

    Vertex VertexData[4];
    uint16_t IndexData[6];

public:
    CPP_Core2D_RenderPipeline();

    inline void Reset() {
    }

    void Render();
};