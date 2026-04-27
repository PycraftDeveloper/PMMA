#pragma once
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

struct Vertex {
    float x, y, u, v;
};

struct InstanceData {
    float x, y;       // position
    float w, h;       // size
    float r, g, b, a; // color
};

class CPP_Shader;

class CPP_Core2D_RenderPipeline {
private:
    CPP_Shader *ShapeDefinitionsShaderProgram = nullptr;
    CPP_Shader *ShapeVisibilityShaderProgram = nullptr;
    CPP_Shader *TileBinningShaderProgram = nullptr;
    CPP_Shader *ClearProgram = nullptr;

    bgfx::VertexLayout m_layout;
    bgfx::VertexLayout instanceLayout;
    bgfx::VertexBufferHandle vbh;
    bgfx::DynamicVertexBufferHandle instanceBuffer;
    bgfx::IndexBufferHandle ibh;
    bgfx::InstanceDataBuffer idb;
    bgfx::UniformHandle OrthDisplayProj;
    bgfx::UniformHandle u_screenSize_tileSize_instanceCount;
    uint32_t instanceCount = 2;

    bgfx::DynamicVertexBufferHandle quadBuffer;      // instance data
    bgfx::DynamicVertexBufferHandle tileWriteOffset; // per-tile counters
    bgfx::DynamicVertexBufferHandle tileData;        // tile → quad list

    Vertex VertexData[4];
    uint16_t IndexData[6];
    uint32_t numTiles;

public:
    CPP_Core2D_RenderPipeline();

    inline void Reset() {
    }

    void Render();
};