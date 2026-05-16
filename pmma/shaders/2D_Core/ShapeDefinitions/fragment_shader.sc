$input v_uv, v_data0, v_data1, v_data2, v_col0
#include "common.sh"

SAMPLER2D(s_colorTex, 0);

vec4 ExtractColor(float ColorIndex, vec2 colorInfo) {
    float idxF = floor(ColorIndex + 0.5);

    float w = colorInfo.x;
    float h = colorInfo.y;

    float x = mod(idxF, w);
    float y = floor(idxF / w);

    vec2 color_uv = vec2((x + 0.5) / w,
                (y + 0.5) / h);

    return texture2DLod(s_colorTex, color_uv, 0.0);
}

void main()
{
    // Early exit
    vec2 p = v_uv - vec2(0.5, 0.5);

    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    float alpha = 1.0;

    // Instance Data Extraction
    uint PointCount = uint(v_data0.x);
    uint GradientType = uint(v_data0.y);
    uint ColorIndex = uint(v_data0.z);
    uint ShapeType = uint(v_data0.w);
    uint Width = uint(v_data1.x);
    vec2 TextureStart = vec2(v_data1.yz);
    vec2 TextureEnd = vec2(v_data1.w, v_data2.x);

    // ============================================================
    // MODE 0 : SDF CIRCLE OUTLINE
    // ============================================================
    if (ShapeType == 0u)
    {
        float pixel = fwidth(v_uv.x);

        float halfWidth = float(Width) * pixel * 0.5;

        // Pull radius inward so outer edge stays fixed
        float radius = 0.5 - halfWidth;

        // Signed distance from circle edge
        float dist = length(p) - radius;

        // Ring mask
        //
        // abs(dist) gives distance from the circumference itself
        //
        alpha = 1.0 - smoothstep(
            halfWidth - pixel,
            halfWidth + pixel,
            abs(dist)
        );

        if (alpha <= 0.0)
            discard;
    }

    // ============================================================
    // MODE 1 : SOLID COLOR
    // ============================================================
    else if (ShapeType == 1u)
    {
        float pixel = fwidth(v_uv.x);

        float width = float(Width) * pixel;

        // Distance to outer box edge
        float outer = max(abs(p.x), abs(p.y)) - 0.5;

        // Inner box shrinks inward
        float inner = max(abs(p.x), abs(p.y)) - (0.5 - width);

        // Border mask
        alpha =
            (1.0 - smoothstep(0.0, pixel, outer)) *
            smoothstep(0.0, pixel, inner);

        if (alpha <= 0.0)
            discard;
    }

    gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}