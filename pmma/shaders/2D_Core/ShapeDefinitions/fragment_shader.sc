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

    float pixel = length(vec2(dFdx(p.x), dFdx(p.y)));

    // Instance Data Extraction
    uint PointCount = uint(v_data0.x);
    uint GradientType = uint(v_data0.y);
    uint ColorIndex = uint(v_data0.z);
    uint ShapeType = uint(v_data0.w);
    uint Width = uint(v_data1.x);
    vec2 TextureStart = vec2(v_data1.yz);
    vec2 TextureEnd = vec2(v_data1.w, v_data2.x);
    uint ShapePropertyOne = uint(v_data2.y);
    uint ShapePropertyTwo = uint(v_data2.z);
    uint ShapePropertyThree = uint(v_data2.w);
    uint ShapePropertyFour = uint(v_data3.x);
    uint ShapePropertyFive = uint(v_data3.y);

    // ============================================================
    // MODE 0 : SDF CIRCLE / POLYGON OUTLINE
    // ============================================================
    if (ShapeType == 0u)
    {
        float r = length(p);

        // Outer radius stays strictly bounded at the UV edge
        float outerRadius = 0.5 - pixel;

        if (PointCount < 3u)
        {
            // --- CIRCLE RENDERING ---
            float outerDist = r - outerRadius;

            if (Width == 0u)
            {
                // Solid Filled Circle
                alpha = 1.0 - smoothstep(0.0, pixel, outerDist);
            }
            else
            {
                // Uniform Ring (Width extends strictly inward)
                float borderWidth = float(Width) * pixel;
                float innerRadius = max(outerRadius - borderWidth, 0.0);
                float innerDist = innerRadius - r;

                float ringDist = max(outerDist, innerDist);
                alpha = 1.0 - smoothstep(0.0, pixel, ringDist);
            }
        }
        else
        {
            // --- POLYGON RENDERING ---
            float N = float(PointCount);
            float sector = 6.28318530718 / N;
            float angle = atan2(p.y, p.x); // Apply rotation from instance data

            // Wrap geometry into a single symmetric sector
            float a = mod(angle + sector * 0.5, sector) - sector * 0.5;
            float edge = cos(sector * 0.5);

            // True planar distance to the polygon edge boundary
            float outerDist = (r * cos(a) / edge) - outerRadius;

            if (Width == 0u)
            {
                // Solid Filled Polygon
                alpha = 1.0 - smoothstep(0.0, pixel, outerDist);
            }
            else
            {
                // Uniform Polygon Border (Extends strictly inward)
                float borderWidth = float(Width) * pixel;

                // Project border thickness cleanly along the normal axis
                float innerDist = (outerRadius - borderWidth) - (r * cos(a) / edge);

                float polyBorderDist = max(outerDist, innerDist);
                alpha = 1.0 - smoothstep(0.0, pixel, polyBorderDist);
            }
        }
    }

    // ============================================================
    // MODE 1 : SOLID COLOR / ROUNDED RECTANGLE
    // ============================================================
    else if (ShapeType == 1u)
    {
        float borderWidth = float(Width) * pixel;

        // Corner radius from instance data
        float radius = float(ShapePropertyOne) * pixel;

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

        // Anti-aliasing using the stable screen pixel factor
        float aa = pixel;

        float outerRadius = 0.5 - pixel; // Keep edge crisp within UV bounds

        // ------------------------------------------------------------
        // Proper annulus/disc SDF (Filled by default when Width == 0)
        // ------------------------------------------------------------
        float ringDist;

        if (Width == 0u)
        {
            // Solid Filled Arc
            ringDist = r - outerRadius;
        }
        else
        {
            // Uniform Ring Arc (Width extends strictly inward)
            float borderWidth = float(Width) * pixel;
            float innerRadius = max(outerRadius - borderWidth, 0.0);

            float outerDist = r - outerRadius;
            float innerDist = innerRadius - r;
            ringDist = max(outerDist, innerDist);
        }

        // ------------------------------------------------------------
        // Arc angles
        // ------------------------------------------------------------

        float StartAngle = (ShapePropertyOne / 182.0) * (3.14159265359 / 180.0); // Start angle in degrees from instance data

        float EndAngle = (ShapePropertyTwo / 182.0) * (3.14159265359 / 180.0);

        float angle = atan2(p.y, p.x);

        angle = mod(angle + 6.28318530718,
                6.28318530718);

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
        // Anti-aliased ring or solid fill
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
        vec2 a = vec2(ShapePropertyOne, ShapePropertyTwo);
        vec2 b = vec2(ShapePropertyThree, ShapePropertyFour);

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
    if (alpha <= 0.00392156862) { // If less than 1/255, discard to avoid unnecessary blending
        discard;
    }

    gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}
