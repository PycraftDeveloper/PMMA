$compute

RWStructuredBuffer<uint> s_tileCounts : register(u1);

cbuffer Uniforms : register(b0)
{
    float4 u_screenInfo;
};

[numthreads(64, 1, 1)]
void main()
{
    uint tileId = gl_GlobalInvocationID.x;

    uint numTiles = (uint)(u_screenInfo.z * u_screenInfo.w);

    if (tileId >= numTiles)
        return;

    s_tileCounts[tileId] = 0;
}