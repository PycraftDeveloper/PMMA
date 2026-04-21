$input a_position, a_texcoord0
$output v_uv

#include "common.sh"

void main() {
    v_uv = a_texcoord0;

    gl_Position = vec4(a_position.x, a_position.y, 0.0, 1.0);
}