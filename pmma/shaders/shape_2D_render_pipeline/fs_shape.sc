$input v_shapeIndex

#include "common.sh"

SAMPLER2D(s_colorTex, 0);

uniform vec4 u_colorInfo;

void main()
{
    float idxF = floor(v_shapeIndex.x + 0.5);
    int idx = int(idxF);

    float w = u_colorInfo.x;
    float h = u_colorInfo.y;

    float x = mod(idxF, w);
    float y = floor(idxF / w);

    vec2 uv = vec2((x + 0.5) / w, (y + 0.5) / h);

    vec4 color = texture2D(s_colorTex, uv);

    gl_FragColor = color;
}
