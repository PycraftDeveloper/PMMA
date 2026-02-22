$input a_position, a_texcoord0
$output v_color

#include "common.sh"

SAMPLER2D(s_colorTex, 0);

uniform vec4 u_colorInfo;
uniform mat4 OrthDisplayProj;

void main()
{
    float idxF = floor(a_texcoord0 + 0.5);

    float w = u_colorInfo.x;
    float h = u_colorInfo.y;

    float x = mod(idxF, w);
    float y = floor(idxF / w);

    vec2 uv = vec2((x + 0.5) / w,
                   (y + 0.5) / h);

    v_color = texture2D(s_colorTex, uv);

    gl_Position = mul(OrthDisplayProj,
                      vec4(a_position.xy, 0.0, 1.0));
}