#include "common.sh"

// -----------------------------------------------------
// Buffers (HLSL-style for BGFX D3D backend)
// -----------------------------------------------------

StructuredBuffer<float4> u_quadsPosSize : register(t0);
StructuredBuffer<float4> u_quadsExtra   : register(t1);

RWStructuredBuffer<uint> u_tileWriteOffset : register(u2);
RWStructuredBuffer<uint> u_tileData        : register(u3);

// -----------------------------------------------------

cbuffer Uniforms : register(b0)
{
    float4 u_screenSize_tileSize_instanceCount;
};

// -----------------------------------------------------

[numthreads(64, 1, 1)]
void main()
{
    uint id = gl_GlobalInvocationID.x;

    uint instanceCount = (uint)u_screenSize_tileSize_instanceCount.w;
    if (id >= instanceCount)
        return;

    float4 posSize = u_quadsPosSize[id];
    float2 pos  = posSize.xy;
    float2 size = posSize.zw;

    float2 minP = pos;
    float2 maxP = pos + size;

    float tileSize = u_screenSize_tileSize_instanceCount.z;

    int2 screenSize = int2(
        u_screenSize_tileSize_instanceCount.x,
        u_screenSize_tileSize_instanceCount.y
    );

    int2 tileCount = screenSize / (int)tileSize;

    int2 minTile = (int2)(minP / tileSize);
    int2 maxTile = (int2)(maxP / tileSize);

    minTile = clamp(minTile, int2(0,0), tileCount - 1);
    maxTile = clamp(maxTile, int2(0,0), tileCount - 1);

    for (int y = minTile.y; y <= maxTile.y; y++)
    for (int x = minTile.x; x <= maxTile.x; x++)
    {
        uint tileID = (uint)(y * tileCount.x + x);

        uint offset;
        InterlockedAdd(u_tileWriteOffset[tileID], 1, offset);

        u_tileData[offset] = id;
    }
}