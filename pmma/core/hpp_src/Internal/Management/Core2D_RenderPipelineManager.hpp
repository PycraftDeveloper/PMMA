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
    CPP_Shader *TileBinningShaderProgram = nullptr;
    CPP_Shader *TileClearShaderProgram = nullptr;

    bgfx::VertexLayout m_layout;
    bgfx::VertexBufferHandle vbh;
    bgfx::IndexBufferHandle ibh;
    bgfx::UniformHandle OrthDisplayProj;
    uint32_t instanceCount = 1'000'000;
    std::vector<InstanceData> instanceDataArray;

    bgfx::DynamicVertexBufferHandle instanceVbh;
    bgfx::VertexLayout instanceLayout;

    bgfx::DynamicIndexBufferHandle tileCountBuffer;
    bgfx::DynamicIndexBufferHandle tileIndexBuffer;

    uint32_t TILE_SIZE = 16;
    uint32_t MAX_PER_TILE = 256;
    uint32_t tilesX;
    uint32_t tilesY;
    uint32_t numTiles;
    bgfx::UniformHandle u_screenInfo;

    std::vector<uint32_t> tileCounts;
    std::vector<uint32_t> tileIndices;

    std::vector<uint32_t> zeroCounts;

    bgfx::VertexLayout computeInstanceLayout;

    bgfx::VertexBufferHandle instanceBuffers[2];
    bgfx::DynamicVertexBufferHandle cpuInstanceBuffer;

    uint8_t currentBuffer = 0;

    Vertex VertexData[4];
    uint16_t IndexData[6];

public:
    CPP_Core2D_RenderPipeline();

    inline void Reset() {
    }

    void Render();
};