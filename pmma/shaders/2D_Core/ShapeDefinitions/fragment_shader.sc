$input v_uv , v_data0 , v_data1 , v_data2 , v_data3 , v_col0
#include "common.sh"

SAMPLER2D(s_colorTex, 0);

// ------------------------------------------------------------
// Utility
// ------------------------------------------------------------

float aaMask(float d, float aa)
{
    return clamp(0.5 - d / aa, 0.0, 1.0);
}

float sdRoundRect(vec2 p, vec2 b, float r)
{
    vec2 q = abs(p) - (b - vec2(r, r));
    return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
}

// ------------------------------------------------------------
// Main
// ------------------------------------------------------------

void main()
{
    vec2 p = v_uv - vec2(0.5, 0.5);

    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    float dx = dFdx(p.x);
    float dy = dFdx(p.y);

    float pixel = length(vec2(dx, dy));
    float aa = pixel;

    float r2 = dot(p, p);
    float r = sqrt(r2);

    // ------------------------------------------------------------
    // Instance data
    // ------------------------------------------------------------

    float pointCount = v_data0.x;
    float shapeType = v_data0.w;

    float width = v_data1.x;

    float p1 = v_data2.y;
    float p2 = v_data2.z;
    float p3 = v_data2.w;
    float p4 = v_data3.x;

    float outerRadius = 0.5 - pixel;
    float border = width * pixel;

    float alpha = 0.0;

    // ============================================================
    // MODE 0: CIRCLE / POLYGON
    // ============================================================

    if (shapeType < 0.5)
    {
        float outerDist = r - outerRadius;

        float circleFill = aaMask(outerDist, aa);

        float innerRadius = outerRadius - border;
        innerRadius = max(innerRadius, 0.0);

        float innerDist = innerRadius - r;
        float circleRing = aaMask(max(outerDist, innerDist), aa);

        float circleAlpha = (width < 0.5) ? circleFill : circleRing;

        // ---------------- POLYGON ----------------

        float polyAlpha = circleAlpha;

        if (pointCount >= 3.0)
        {
            float N = max(pointCount, 3.0);
            float sector = 6.28318530718 / N;

            float angle = atan2(p.y, p.x);
            angle += (angle < 0.0) * 6.28318530718;

            float sectorAngle =
                mod(angle + sector * 0.5, sector) - sector * 0.5;

            float edge = cos(sector * 0.5);

            float proj = (r * cos(sectorAngle)) / edge;

            float polyOuter = proj - outerRadius;
            float polyInner = (outerRadius - border) - proj;

            float polyDist = (width < 0.5)
                ? polyOuter : max(polyOuter, polyInner);

            polyAlpha = aaMask(polyDist, aa);
        }

        alpha = polyAlpha;
    }

    // ============================================================
    // MODE 1: ROUND RECT
    // ============================================================

    else if (shapeType < 1.5)
    {
        float radius = clamp(p1 * pixel, 0.0, 0.5);

        float outerRR = sdRoundRect(p, vec2(0.5, 0.5), radius);

        float innerRR = sdRoundRect(
                p,
                vec2(0.5 - border, 0.5 - border),
                max(radius - border, 0.0)
            );

        float rrFill = aaMask(outerRR, aa);
        float rrInner = aaMask(innerRR, aa);

        alpha = (width < 0.5)
            ? rrFill : rrFill * (1.0 - rrInner);
    }

    // ============================================================
    // MODE 2: ARC
    // ============================================================

    else if (shapeType < 2.5)
    {
        float outerD = r - outerRadius;

        float innerR = max(outerRadius - border, 0.0);
        float innerD = innerR - r;

        float ringDist = (width < 0.5)
            ? outerD : max(outerD, innerD);

        float arcBase = aaMask(ringDist, aa);

        float angle = atan2(p.y, p.x);
        angle += (angle < 0.0) * 6.28318530718;

        float startA = (p1 / 182.0) * 0.01745329251;
        float endA = (p2 / 182.0) * 0.01745329251;

        float arcMask;

        if (endA >= 6.28318530718)
            arcMask = 1.0;
        else
            arcMask = step(startA, angle) * step(angle, endA);

        alpha = arcBase * arcMask;
    }

    // ============================================================
    // MODE 3: LINE
    // ============================================================

    else
    {
        vec2 a = vec2(p1, p2);
        vec2 b = vec2(p3, p4);

        vec2 ba = b - a;
        float lenBA = max(length(ba), 1e-6);
        vec2 dir = ba / lenBA;

        vec2 pa = v_uv - a;

        float x = dot(pa, dir);
        float y = dot(pa, vec2(-dir.y, dir.x));

        float halfLen = lenBA * 0.5;
        float rad = pixel * 0.5;

        float dx = abs(x - halfLen);
        float dy = abs(y);

        float square =
            length(max(vec2(dx, dy) - vec2(halfLen, rad), 0.0))
                + min(max(x - halfLen, y - rad), 0.0);

        float t = clamp(x / lenBA, 0.0, 1.0);
        float roundLine = length(pa - ba * t) - rad;

        float lineDist = (pointCount < 3.0)
            ? square : roundLine;

        alpha = aaMask(lineDist, aa);
    }

    // final cutoff (branchless)
    alpha *= step(0.0039, alpha);

    gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}
