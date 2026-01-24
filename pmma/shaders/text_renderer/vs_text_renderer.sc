$input a_position, a_texcoord0, a_texcoord1
$output v_ForegroundColorIndex, v_BackgroundColorIndex, v_texture_uv

#include "common.sh"

uniform mat4 OrthDisplayProj;

void main() {
    v_ForegroundColorIndex = a_texcoord0.x;
    v_BackgroundColorIndex = a_texcoord0.y;
    v_texture_uv = a_texcoord1;

    gl_Position = mul(OrthDisplayProj, vec4(a_position.xy, 0.0, 1.0));
}