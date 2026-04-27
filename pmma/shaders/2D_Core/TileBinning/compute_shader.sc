#include "bgfx_compute.sh"

BUFFER_RO(u_quadsPosSize, float4, 0);
BUFFER_RW(u_tileWriteOffset, uint, 1);
BUFFER_RW(u_tileData, uint, 2);

uniform float4 u_screenSize_tileSize_instanceCount;

NUM_THREADS(64, 1, 1)

void main()
{
    uint id = gl_GlobalInvocationID.x;

    uint instanceCount = (uint)u_screenSize_tileSize_instanceCount.w;
    if (id >= instanceCount)
        return;

    float screenW = u_screenSize_tileSize_instanceCount.x;
    float screenH = u_screenSize_tileSize_instanceCount.y;
    float tileSize = u_screenSize_tileSize_instanceCount.z;

    float2 pos  = u_quadsPosSize[id].xy;
    float2 size = u_quadsPosSize[id].zw;

    float2 minP = pos;
    float2 maxP = pos + size;

    int2 screenSize = int2(screenW, screenH);
    int2 tileCount = max(int2(screenSize / tileSize), int2(1));

    int2 minTile = clamp(int2(minP / tileSize), int2(0), tileCount - 1);
    int2 maxTile = clamp(int2(maxP / tileSize), int2(0), tileCount - 1);

    for (int y = minTile.y; y <= maxTile.y; y++)
    for (int x = minTile.x; x <= maxTile.x; x++)
    {
        uint tileID = uint(y * tileCount.x + x);

        uint offset = atomicAdd(u_tileWriteOffset[tileID], 1);

        if (offset < 256)
        {
            uint index = tileID * 256 + offset;
            u_tileData[index] = id;
        }
    }
}