$input a_position, a_texcoord0
$output v_shapeIndex

#include "common.sh"

uniform mat4 OrthDisplayProj;

void main()
{
    v_shapeIndex = a_texcoord0;

    gl_Position = mul(OrthDisplayProj, vec4(a_position.xy, 0.0, 1.0));
}
