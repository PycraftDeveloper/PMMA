$input a_position, a_texcoord0, i_data0, i_data1
$output v_uv, v_col

#include "common.sh"

uniform mat4 OrthDisplayProj;

void main()
{
    uint packedPosition = floatBitsToUint(i_data0.x);
    uint packedSize = floatBitsToUint(i_data0.y);

    vec2 Offset = vec2(float(packedPosition & 0xFFFFu), float(packedPosition >> 16u));
    vec2 Size = vec2(float(packedSize & 0xFFFFu), float(packedSize >> 16u));

    vec2 world = Offset + a_position.xy * Size;

    gl_Position = mul(OrthDisplayProj, vec4(world, 0.0, 1.0));

    v_uv = a_texcoord0;
    v_col = i_data1;
}