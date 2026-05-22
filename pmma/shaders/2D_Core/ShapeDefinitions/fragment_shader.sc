$input v_uv , v_data0 , v_data1 , v_data2 , v_data3 , v_col0
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

float sdRoundRect(vec2 p, vec2 b, float r)
{
    vec2 q = abs(p) - (b - vec2(r, r));
    return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
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
    uint ShapeProperty = uint(v_data2.y); // corner radius for ShapeType 1

    // ============================================================
    // MODE 0 : SDF CIRCLE / POLYGON OUTLINE
    // ============================================================
    if (ShapeType == 0u)
    {
        float r = length(p);

        float pixel = fwidth(r);
        float halfWidth = float(Width) * pixel * 0.5;

        float radius = 0.5 - halfWidth;

        if (PointCount < 3u)
        {
            float dist = r - radius;

            alpha = 1.0 - smoothstep(
                        halfWidth - pixel,
                        halfWidth + pixel,
                        abs(dist)
                    );
        }
        else
        {
            float N = float(PointCount);
            float sector = 6.28318530718 / N;

            float angle = atan2(p.y, p.x);

            // wrap into sector
            float a = mod(angle + sector * 0.5, sector) - sector * 0.5;

            // direction vector in sector space
            vec2 dir = vec2(cos(a), sin(a));

            // key trick: project onto edge normal axis
            float edge = cos(sector * 0.5);

            // stable polygon SDF approximation
            float dist = r * cos(a) / edge - radius;

            alpha = 1.0 - smoothstep(
                        halfWidth - pixel,
                        halfWidth + pixel,
                        abs(dist)
                    );
        }
    }

    // ============================================================
    // MODE 1 : SOLID COLOR / ROUNDED RECTANGLE
    // ============================================================
    else if (ShapeType == 1u)
    {
        float pixel = max(fwidth(p.x), fwidth(p.y));

        float borderWidth = float(Width) * pixel;

        // Corner radius from instance data
        float radius = float(ShapeProperty) * pixel;

        // Clamp radius so it never exceeds box size
        radius = clamp(radius, 0.0, 0.5);

        // ------------------------------------------------------------
        // Outer rounded rect
        // ------------------------------------------------------------

        float outerDist = sdRoundRect(
                p,
                vec2(0.5, 0.5),
                radius
            );

        // ------------------------------------------------------------
        // Inner rounded rect
        // ------------------------------------------------------------

        float innerRadius = max(radius - borderWidth, 0.0);

        float innerDist = sdRoundRect(
                p,
                vec2(0.5 - borderWidth, 0.5 - borderWidth),
                innerRadius
            );

        // ------------------------------------------------------------
        // Border mask
        // ------------------------------------------------------------

        float outerAlpha =
            1.0 - smoothstep(0.0, pixel, outerDist);

        float innerAlpha =
            1.0 - smoothstep(0.0, pixel, innerDist);

        alpha = outerAlpha * (1.0 - innerAlpha);
    }
    // ============================================================
    // MODE 2 : ARC
    // ============================================================
    else if (ShapeType == 2u)
    {
        float r = length(p);

        // AA only
        float aa = fwidth(r);

        // ------------------------------------------------------------
        // Stable geometric width
        // ------------------------------------------------------------

        float width = float(Width) / 100.0;

        float outerRadius = 0.5;

        float innerRadius =
            max(outerRadius - width, 0.0);

        // ------------------------------------------------------------
        // Arc angles
        // ------------------------------------------------------------

        float StartAngle = 0.0;

        float EndAngle = (ShapeProperty / 182.0) * (3.14159265359 / 180.0);

        float angle = atan2(p.y, p.x);

        angle = mod(angle + 6.28318530718,
                6.28318530718);

        // ------------------------------------------------------------
        // Proper annulus SDF
        // ------------------------------------------------------------

        float outerDist =
            r - outerRadius;

        float innerDist =
            innerRadius - r;

        float ringDist =
            max(outerDist, innerDist);

        // ------------------------------------------------------------
        // Angular mask
        // ------------------------------------------------------------

        float arcMask;

        if (EndAngle >= 6.28318530718)
        {
            arcMask = 1.0;
        }
        else
        {
            arcMask =
                step(StartAngle, angle) *
                    step(angle, EndAngle);
        }

        // ------------------------------------------------------------
        // Anti-aliased ring
        // ------------------------------------------------------------

        float ringAlpha =
            1.0 - smoothstep(-aa, aa, ringDist);

        alpha = ringAlpha * arcMask;
    }

    // ============================================================
    // MODE 3 : LINE
    // ============================================================
    else if (ShapeType == 3u)
    {
        vec2 uv = v_uv;

        // endpoints in UV space
        vec2 a = v_data2.zw;
        vec2 b = v_data3.xy;

        float uvPerPixel =
            max(fwidth(uv.x), fwidth(uv.y));

        float radius =
            max(float(Width) * uvPerPixel * 0.5,
                uvPerPixel * 0.5);

        float aa = uvPerPixel;

        vec2 ba = b - a;
        float len = max(length(ba), 1e-6);

        vec2 dir = ba / len;

        // local coordinates
        vec2 pa = uv - a;

        float x = dot(pa, dir);
        float y = dot(pa, vec2(-dir.y, dir.x));

        float dist;

        // ------------------------------------------------------------
        // Square caps
        // ------------------------------------------------------------
        if (PointCount < 3u)
        {
            vec2 d =
                abs(vec2(x - len * 0.5, y)) -
                    vec2(len * 0.5, radius);

            dist =
                length(max(d, 0.0)) +
                    min(max(d.x, d.y), 0.0);
        }
        // ------------------------------------------------------------
        // Rounded caps
        // ------------------------------------------------------------
        else
        {
            float h =
                clamp(x / len, 0.0, 1.0);

            dist =
                length(pa - ba * h) - radius;
        }

        alpha =
            1.0 - smoothstep(0.0, aa, dist);
    }
    if (alpha <= 0.0)
        discard;

    gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}
