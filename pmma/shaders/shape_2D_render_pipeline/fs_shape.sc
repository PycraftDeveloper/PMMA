$input v_shapeIndex

#include "common.sh"

SAMPLER2D(s_colorTex, 0);

uniform vec4 u_colorInfo;

void main()
{
    int idx = int(floor(v_shapeIndex.x + 0.5));
    float u = (float(idx) + 0.5) / u_colorInfo.x;
    vec4 color = texture2D(s_colorTex, vec2(u, 0.5));
    gl_FragColor = color;
}
