$input v_uv

#include "common.sh"

SAMPLER2D(s_colorTex, 0);

void main()
{
    gl_FragColor = texture2D(s_colorTex, v_uv);
}