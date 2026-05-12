$input a_position, a_texcoord0, i_data0, i_data1
$output v_uv, v_col

#include "common.sh"

uniform mat4 OrthDisplayProj;

void main()
{
    float p = i_data0.x;

    uint packedBits = floatBitsToUint(p);
    float x = float(packedBits & 0xFFFFu);
    float y = float(packedBits >> 16u);
    vec2 Offset = vec2(x, y);

    vec2 world = Offset + a_position.xy * i_data0.zw;

    gl_Position = mul(OrthDisplayProj, vec4(world, 0.0, 1.0));

    v_uv = a_texcoord0;
    v_col = i_data1;
}