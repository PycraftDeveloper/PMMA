$input v_uv, v_col
#include "common.sh"

// ------------------------------------------------------------
// u_mode
// 0 = Circle Outline (SDF)
// 1 = Solid Quad
//
// u_width
// Outline thickness in pixels
// ------------------------------------------------------------

void main()
{
    int u_mode = 1;
    int u_width = 5;

    vec2 p = v_uv - vec2(0.5);

    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    float alpha = 1.0;

    // ============================================================
    // MODE 0 : SDF CIRCLE OUTLINE
    // ============================================================
    if (u_mode == 0)
    {
        float pixel = fwidth(v_uv.x);

        float halfWidth = float(u_width) * pixel * 0.5;

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
    else if (u_mode == 1)
    {
        float pixel = fwidth(v_uv.x);

        float width = float(u_width) * pixel;

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

    gl_FragColor = vec4(v_col.rgb, v_col.a * alpha);
}