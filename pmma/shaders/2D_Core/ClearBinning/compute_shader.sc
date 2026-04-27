#version 430

layout(local_size_x = 64) in;

layout(std430, binding = 0) buffer TileWriteOffset
{
    uint data[];
};

uniform uint u_numTiles;

void main()
{
    uint id = gl_GlobalInvocationID.x;

    if (id >= u_numTiles)
        return;

    data[id] = 0u;
}