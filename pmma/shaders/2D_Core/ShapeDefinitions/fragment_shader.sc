$input v_uv, v_col0, v_col1, v_col2, v_col3, v_data2, v_data3
#include "common.sh"

// ------------------------------------------------------------
// u_mode
// 0 = Circle Outline (SDF)
// 1 = Solid Quad
//
// u_width
// Outline thickness in pixels
// ------------------------------------------------------------

vec2 Unpack2Values(float data) {
    uint PackedData = floatBitsToUint(data);

    return vec2(float(PackedData & 0xFFFFu), float(PackedData >> 16u));
}

vec3 Unpack3Values(float data) {
    uint PackedData = floatBitsToUint(data);

    uint val_three = (PackedData >> 24u) & 0xFFu;
    uint val_two   = (PackedData >> 16u) & 0xFFu;
    uint val_one   = (PackedData >> 8u)  & 0xFFu;
    return vec3(float(val_one), float(val_two), float(val_three));
}

void main()
{
    // Early exit
    vec2 p = v_uv - vec2(0.5);

    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    float alpha = 1.0;

    // Instance Data Extraction
    vec2 colorInfo = vec2(v_data3.xy);
    vec3 PointCountWidthGradientType = Unpack3Values(v_data2.x);
    vec2 TexturePosition = Unpack2Values(v_data2.z) / vec2(colorInfo.xy);
    vec2 TextureSize = Unpack2Values(v_data2.w) / vec2(colorInfo.xy);

    // ============================================================
    // MODE 0 : SDF CIRCLE OUTLINE
    // ============================================================
    if (v_data2.y == 0.0)
    {
        float pixel = fwidth(v_uv.x);

        float halfWidth = float(PointCountWidthGradientType.y) * pixel * 0.5;

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
    else if (v_data2.y == 1.0)
    {
        float pixel = fwidth(v_uv.x);

        float width = float(PointCountWidthGradientType.y) * pixel;

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