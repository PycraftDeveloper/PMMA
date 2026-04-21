$input a_position, a_uv0, a_instancePos, a_size

$output v_uv
$output v_instanceID
$output v_depthKey

#include "common.sh"

uniform mat4 u_mvp;

void main()
{
    vec2 pos = a_position.xy;

    vec2 world = a_instancePos + pos * a_size;

    gl_Position = u_mvp * vec4(world, 0.0, 1.0);

    v_uv = a_uv0;

    v_instanceID = gl_InstanceID;
    v_depthKey = float(gl_InstanceID);
}