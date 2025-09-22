$input a_position, a_texcoord0, a_texcoord1
$output v_ColorIndex, v_texture_uv

#include "common.sh"

uniform mat4 OrthDisplayProj;

void main() {
    v_ColorIndex = a_texcoord0.x;
    v_texture_uv = a_texcoord1;

    gl_Position = mul(OrthDisplayProj, vec4(a_position.xy, 0.0, 1.0));
}