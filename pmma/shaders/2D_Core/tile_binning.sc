$compute

    struct InstanceData {
    float4 rect;
    float4 color;
};

StructuredBuffer<InstanceData> s_instances : register(t0);

RWStructuredBuffer<uint> s_tileCounts : register(u1);
RWStructuredBuffer<uint> s_tileIndices : register(u2);

cbuffer Uniforms : register(b0) {
    float4 u_screenInfo;
};

#define TILE_SIZE 16
#define MAX_PER_TILE 256

[numthreads(64, 1, 1)] void main() {
    uint instanceId = gl_GlobalInvocationID.x;

    InstanceData inst = s_instances[instanceId];

    float x = inst.rect.x;
    float y = inst.rect.y;
    float w = inst.rect.z;
    float h = inst.rect.w;

    uint minTileX = (uint)max(0.0, floor(x / TILE_SIZE));
    uint minTileY = (uint)max(0.0, floor(y / TILE_SIZE));

    uint maxTileX = (uint)min(
        u_screenInfo.z - 1.0,
        floor((x + w) / TILE_SIZE));

    uint maxTileY = (uint)min(
        u_screenInfo.w - 1.0,
        floor((y + h) / TILE_SIZE));

    for (uint ty = minTileY; ty <= maxTileY; ++ty) {
        for (uint tx = minTileX; tx <= maxTileX; ++tx) {
            uint tileId =
                ty * (uint)u_screenInfo.z + tx;

            uint index;

            InterlockedAdd(
                s_tileCounts[tileId],
                1,
                index);

            if (index < MAX_PER_TILE) {
                s_tileIndices[tileId * MAX_PER_TILE + index] = instanceId;
            }
        }
    }
}