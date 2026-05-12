#pragma once
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

struct Vertex
{
    float x, y, u, v;
};

struct InstanceData
{
    float x, y;       // position
    float w, h;       // size
    float r, g, b, a; // color
};

class CPP_Shader;

class CPP_Core2D_RenderPipeline
{
private:
    CPP_Shader *ShapeDefinitionsShaderProgram = nullptr;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;
    uint32_t instanceCount = 250'000'000;
    std::vector<InstanceData> instanceDataArray;

    bgfx::DynamicVertexBufferHandle instanceVbh;
    bgfx::VertexLayout instanceLayout;

    Vertex VertexData[4];
    uint16_t IndexData[6];
    uint32_t numTiles;

public:
    CPP_Core2D_RenderPipeline();

    inline void Reset()
    {
    }

    void Render();
};