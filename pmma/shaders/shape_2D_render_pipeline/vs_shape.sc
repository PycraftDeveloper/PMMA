$input a_position, a_texcoord0
$output v_shapeIndex

#include <bgfx_shader.sh>
#include "shaderlib.sh"

uniform mat4 screenspace;

void main()
{
    v_shapeIndex = a_texcoord0.x;

    gl_Position = mul(screenspace, vec4(a_position.xy, 0.0, 1.0));
}
