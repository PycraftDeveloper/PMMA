$input v_uv

#include "common.sh"

void main()
{
    gl_FragColor = vec4(v_uv.x, v_uv.y, 1.0f, 1.0f);
}
