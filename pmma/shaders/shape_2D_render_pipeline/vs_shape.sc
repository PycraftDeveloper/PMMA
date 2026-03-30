$input a_position, a_texcoord0
$output v_uv

#include "common.sh"

uniform vec4 u_colorInfo;
uniform mat4 OrthDisplayProj;

void main()
{
    float idxF = floor(a_texcoord0 + 0.5);

    float w = u_colorInfo.x;
    float h = u_colorInfo.y;

    float x = mod(idxF, w);
    float y = floor(idxF / w);

    v_uv = vec2((x + 0.5) / w,
                (y + 0.5) / h);

    gl_Position = mul(OrthDisplayProj,
                      vec4(a_position.xyz, 1.0));
}