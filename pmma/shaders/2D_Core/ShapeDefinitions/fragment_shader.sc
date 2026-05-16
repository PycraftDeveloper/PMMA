$input v_uv, v_data0, v_data1, v_col0
#include "common.sh"

SAMPLER2D(s_colorTex, 0);

vec2 Unpack2Values(float data) {
    uint PackedData = floatBitsToUint(data);

    return vec2(float(PackedData & 0xFFFFu), float(PackedData >> 16u));
}

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
    vec2 colorInfo = vec2(v_data1.yz);

    vec2 PointCountGradientType = Unpack2Values(v_data0.x);
    float ColorIndex = v_data0.y;
    vec2 ShapeTypeWidth = Unpack2Values(v_data0.z);
    vec2 TexturePosition = Unpack2Values(v_data0.w) / colorInfo.xy;
    vec2 TextureSize = Unpack2Values(v_data1.x) / colorInfo.xy;
    uint ShapeType = uint(ShapeTypeWidth.x);
    uint debugShape = ShapeType;

    // ============================================================
    // MODE 0 : SDF CIRCLE OUTLINE
    // ============================================================
    if (ShapeType == 0)
    {
        float pixel = fwidth(v_uv.x);

        float halfWidth = float(ShapeTypeWidth.y) * pixel * 0.5;

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
    else if (ShapeType == 1)
    {
        float pixel = fwidth(v_uv.x);

        float width = float(ShapeTypeWidth.y) * pixel;

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

    float dummy = colorInfo.x + PointCountGradientType.x + ColorIndex + TexturePosition.x + TextureSize.x;
    gl_FragColor = vec4(debugShape == 0u, debugShape == 1u, debugShape > 1u, 1.0);
    //gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}