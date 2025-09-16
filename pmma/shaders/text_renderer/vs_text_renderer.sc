$input a_position, a_texcoord0, a_texcoord1, a_texcoord2, a_texcoord3, a_texcoord4, a_color0, a_color1
$output v_texcoord, v_fg, v_bg

#include "common.sh"

uniform mat4 OrthDisplayProj;

void main()
{
    vec2 localPos = a_position.xy;
    vec2 pos = a_texcoord1.xy + localPos * a_texcoord2.xy; // inst.pos + local * scale

    gl_Position = mul(OrthDisplayProj, vec4(pos, 0.0, 1.0));

    v_texcoord = a_texcoord3.xy + a_texcoord0.xy * a_texcoord4.xy;
    v_fg = a_color0;
    v_bg = a_color1;
}
