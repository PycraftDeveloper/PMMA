$input v_ForegroundColorIndex, v_BackgroundColorIndex, v_texture_uv

#include "common.sh"

SAMPLER2D(s_ForegroundColorTex, 0);
SAMPLER2D(s_BackgroundColorTex, 1);
SAMPLER2D(s_fontAtlas, 2);

// u_colorInfo = (fg_width, fg_height, bg_width, bg_height)
uniform vec4 u_colorInfo;

void main()
{
    float alpha = texture2D(s_fontAtlas, v_texture_uv).r;

    // Color index (shared between fg/bg)
    float FG_idxF = floor(v_ForegroundColorIndex + 0.5);

    //
    // --- Foreground UV ---
    //
    float fgW = u_colorInfo.x;
    float fgH = u_colorInfo.y;

    float fgX = mod(FG_idxF, fgW);
    float fgY = floor(FG_idxF / fgW);

    vec2 fg_uv = vec2((fgX + 0.5) / fgW,
                      (fgY + 0.5) / fgH);

    //
    // --- Background UV ---
    //
    float BG_idxF = floor(v_BackgroundColorIndex + 0.5);
    float bgW = u_colorInfo.z;
    float bgH = u_colorInfo.w;

    float bgX = mod(BG_idxF, bgW);
    float bgY = floor(BG_idxF / bgW);

    vec2 bg_uv = vec2((bgX + 0.5) / bgW,
                      (bgY + 0.5) / bgH);

    //
    // Sample both textures independently
    //
    vec4 fgColor = texture2D(s_ForegroundColorTex, fg_uv);
    vec4 bgColor = texture2D(s_BackgroundColorTex, bg_uv);

    //
    // Blend using glyph alpha
    //
    gl_FragColor = mix(bgColor, fgColor, alpha);
}
