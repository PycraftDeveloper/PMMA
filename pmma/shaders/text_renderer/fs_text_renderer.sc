$input v_ColorIndex, v_texture_uv

#include "common.sh"

SAMPLER2D(s_ForegroundColorTex, 0);
SAMPLER2D(s_BackgroundColorTex, 1);
SAMPLER2D(s_fontAtlas, 2);

uniform vec4 u_colorInfo;

void main() {
    float alpha = texture2D(s_fontAtlas, v_texture_uv).r;

    float idxF = floor(v_ColorIndex + 0.5);
    int idx = int(idxF);

    float w = u_colorInfo.x;
    float h = u_colorInfo.y;

    float x = mod(idxF, w);
    float y = floor(idxF / w);

    vec2 color_uv = vec2((x + 0.5) / w, (y + 0.5) / h);

    vec4 ForegroundColor = texture2D(s_ForegroundColorTex, color_uv);
    vec4 BackgroundColor = texture2D(s_BackgroundColorTex, color_uv);

    gl_FragColor = mix(ForegroundColor, BackgroundColor, 1-alpha);
}