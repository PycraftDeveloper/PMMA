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

// Fixed Signed Distance Function for a Rectangle with per-corner radii
float sdRoundRectPermutated(vec2 p, vec2 b, vec4 r)
{
    // Select the correct radius based on which quadrant the pixel lies in
    vec2 r_sel = (p.x > 0.0) ? ((p.y > 0.0) ? r.xy : r.zw) : ((p.y > 0.0) ? r.xx : r.yy);
    // Fallback simplified logic for 4 unique corners:
    float rad = (p.x > 0.0 && p.y > 0.0) ? r.x : // Top Right
        (p.x < 0.0 && p.y > 0.0) ? r.y : // Top Left
        (p.x < 0.0 && p.y < 0.0) ? r.z : // Bottom Left
        r.w; // Bottom Right

    vec2 q = abs(p) - b + vec2(rad, rad);
    return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - rad;
}

// ------------------------------------------------------------
// Main
// ------------------------------------------------------------

void main()
{
    // 1. GLOBAL ASPECT RATIO & SCALE CORRECTION
    // Calculate the screen-space size of the UV quad to find true pixel metrics
    vec2 dx_uv = dFdx(v_uv);
    vec2 dy_uv = dFdy(v_uv);

    // Determine the absolute pixel dimensions of the rendering quad
    vec2 quad_pixel_size = vec2(1.0 / length(vec2(dx_uv.x, dy_uv.x)), 1.0 / length(vec2(dx_uv.y, dy_uv.y)));

    // Convert 0->1 UV space to absolute pixel space centered at (0,0)
    vec2 p_pixel = (v_uv - vec2(0.5, 0.5)) * quad_pixel_size;
    vec2 half_size = quad_pixel_size * 0.5;

    // Boundary discard check using absolute pixels
    if (abs(p_pixel.x) > half_size.x || abs(p_pixel.y) > half_size.y)
        discard;

    // Global Anti-Aliasing factor is exactly 1 screen pixel wide now
    float aa = 1.0;

    float r = length(p_pixel);

    // ------------------------------------------------------------
    // Instance data
    // ------------------------------------------------------------

    float pointCount = v_data0.x;
    float shapeType = v_data0.w;

    // Width is now processed directly as a uniform pixel thickness
    float width = v_data1.x;
    float border = width;

    // Raw input radii from vertex data
    float p1 = v_data2.y;
    float p2 = v_data2.z;
    float p3 = v_data2.w;
    float p4 = v_data3.x;

    float alpha = 0.0;

    // ============================================================
    // MODE 0: CIRCLE / POLYGON
    // ============================================================

    if (shapeType < 0.5)
    {
        float outerRadius = min(half_size.x, half_size.y) - aa;
        float outerDist = r - outerRadius;
        float circleFill = aaMask(outerDist, aa);

        float innerRadius = max(outerRadius - border, 0.0);
        float innerDist = innerRadius - r;
        float circleRing = aaMask(max(outerDist, innerDist), aa);

        float circleAlpha = (width < 0.5) ? circleFill : circleRing;
        float polyAlpha = circleAlpha;

        if (pointCount >= 3.0)
        {
            float N = max(pointCount, 3.0);
            float sector = 6.28318530718 / N;

            float angle = atan2(p_pixel.y, p_pixel.x);
            angle += (angle < 0.0) * 6.28318530718;

            float sectorAngle = mod(angle + sector * 0.5, sector) - sector * 0.5;
            float edge = cos(sector * 0.5);
            float proj = (r * cos(sectorAngle)) / edge;

            float polyOuter = proj - outerRadius;
            float polyInner = (outerRadius - border) - proj;

            float polyDist = (width < 0.5) ? polyOuter : max(polyOuter, polyInner);
            polyAlpha = aaMask(polyDist, aa);
        }

        alpha = polyAlpha;
    }

    // ============================================================
    // MODE 1: ROUND RECT
    // ============================================================

    else if (shapeType < 1.5)
    {
        // 2. POINT COUNT & CORNER LOGIC
        // If pointCount < 3, override individual inputs to force a smooth/max rounded corner
        float max_possible_rad = min(half_size.x, half_size.y);

        vec4 corners = vec4(p1, p2, p3, p4);
        if (pointCount < 3.0) {
            corners = vec4(max_possible_rad, max_possible_rad, max_possible_rad, max_possible_rad); // Overrides corners to completely smooth rounded caps
        }

        // Clamp radii safely to half-extents using real pixels
        corners = clamp(corners, vec4(0.0, 0.0, 0.0, 0.0), vec4(max_possible_rad, max_possible_rad, max_possible_rad, max_possible_rad));

        float outerRR = sdRoundRectPermutated(p_pixel, half_size, corners);
        float innerRR = sdRoundRectPermutated(p_pixel, half_size - vec2(border, border), max(corners - vec4(border, border, border, border), vec4(0.0, 0.0, 0.0, 0.0)));

        float rrFill = aaMask(outerRR, aa);
        float rrInner = aaMask(innerRR, aa);

        alpha = (width < 0.5) ? rrFill : rrFill * (1.0 - rrInner);
    }

    // ============================================================
    // MODE 2: ARC
    // ============================================================

    else if (shapeType < 2.5)
    {
        float outerRadius = min(half_size.x, half_size.y) - aa;
        float outerD = r - outerRadius;

        float innerR = max(outerRadius - border, 0.0);
        float innerD = innerR - r;

        float ringDist = (width < 0.5) ? outerD : max(outerD, innerD);
        float arcBase = aaMask(ringDist, aa);

        float angle = atan2(p_pixel.y, p_pixel.x);
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
        // Re-scale line anchors from UV ratios into real working pixel positions
        vec2 a = v_data2.yz * quad_pixel_size;
        vec2 b = v_data2.wz * quad_pixel_size; // Map p3, p4 safely

        vec2 ba = b - a;
        float lenBA = max(length(ba), 1e-6);
        vec2 dir = ba / lenBA;

        vec2 pa = (v_uv * quad_pixel_size) - a;

        float x = dot(pa, dir);
        float y = dot(pa, vec2(-dir.y, dir.x));

        float halfLen = lenBA * 0.5;
        float rad = 0.5;

        float dx = abs(x - halfLen);
        float dy = abs(y);

        float square = length(max(vec2(dx, dy) - vec2(halfLen, rad), 0.0)) + min(max(x - halfLen, y - rad), 0.0);

        float t = clamp(x / lenBA, 0.0, 1.0);
        float roundLine = length(pa - ba * t) - rad;

        float lineDist = (pointCount < 3.0) ? square : roundLine;
        alpha = aaMask(lineDist, aa);
    }

    // final cutoff (branchless)
    alpha *= step(0.0039, alpha);

    gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}
