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

// Fixed quadrant selection for 4 unique corners
float sdRoundRectPermutated(vec2 p, vec2 b, vec4 r)
{
    // Explicitly identify which corner the pixel belongs to
    float rad = 0.0;
    if (p.x >= 0.0) {
        if (p.y >= 0.0) rad = r.x; // Top Right (p1)
        else rad = r.w; // Bottom Right (p4)
    } else {
        if (p.y >= 0.0) rad = r.y; // Top Left (p2)
        else rad = r.z; // Bottom Left (p3)
    }

    // Ensure the radius never exceeds the local side boundaries
    rad = min(rad, min(b.x, b.y));

    vec2 q = abs(p) - b + vec2(rad, rad);
    return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - rad;
}

// ------------------------------------------------------------
// Main
// ------------------------------------------------------------

void main()
{
    // Global screen-space coordinate evaluation
    vec2 dx_uv = dFdx(v_uv);
    vec2 dy_uv = dFdy(v_uv);

    // Total absolute size of the rendering canvas in screenspace pixels
    vec2 quad_pixel_size = vec2(1.0 / length(vec2(dx_uv.x, dy_uv.x)), 1.0 / length(vec2(dx_uv.y, dy_uv.y)));

    // Transform coordinates into pixel displacements relative to center
    vec2 p_pixel = (v_uv - vec2(0.5, 0.5)) * quad_pixel_size;
    vec2 half_size = quad_pixel_size * 0.5;

    // Discard any fragments escaping the primary boundary
    if (abs(p_pixel.x) > half_size.x || abs(p_pixel.y) > half_size.y)
        discard;

    float aa = 1.0;

    // ------------------------------------------------------------
    // Instance data
    // ------------------------------------------------------------

    float pointCount = v_data0.x;
    float shapeType = v_data0.w;

    float width = v_data1.x;
    float border = width;

    float p1 = v_data2.y;
    float p2 = v_data2.z;
    float p3 = v_data2.w;
    float p4 = v_data3.x;

    float alpha = 0.0;

    // ============================================================
    // MODE 0: ELLIPSE / POLYGON
    // ============================================================

    if (shapeType < 0.5)
    {
        // Compute an ellipse by normalizing coordinates to a uniform radius unit
        float max_dim = max(half_size.x, half_size.y);
        vec2 ellipse_scale = half_size / max_dim;

        // Scale coordinate space to transform perfect circles into true ellipses
        vec2 p_ellipse = p_pixel / ellipse_scale;
        float r_ellipse = length(p_ellipse);

        float outerRadius = max_dim - aa;
        float outerDist = r_ellipse - outerRadius;

        // Re-scale distance field back to screenspace pixels for uniform AA border stroke
        outerDist *= min(ellipse_scale.x, ellipse_scale.y);

        float circleFill = aaMask(outerDist, aa);
        float innerRadius = max(outerRadius - border, 0.0);
        float innerDist = innerRadius - r_ellipse;
        innerDist *= min(ellipse_scale.x, ellipse_scale.y);

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
            float proj = (length(p_pixel) * cos(sectorAngle)) / edge;

            float min_radius = min(half_size.x, half_size.y) - aa;
            float polyOuter = proj - min_radius;
            float polyInner = (min_radius - border) - proj;

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
        float max_possible_rad = min(half_size.x, half_size.y);

        vec4 corners = vec4(p1, p1, p1, p1);

        // safety clamp
        corners = clamp(
                corners,
                vec4(0.0, 0.0, 0.0, 0.0),
                vec4(max_possible_rad, max_possible_rad, max_possible_rad, max_possible_rad)
            );

        float outerRR = sdRoundRectPermutated(p_pixel, half_size, corners);

        float innerRR = sdRoundRectPermutated(
                p_pixel,
                half_size - vec2(border, border),
                max(corners - vec4(border, border, border, border), vec4(0.0, 0.0, 0.0, 0.0))
            );

        float rrFill = aaMask(outerRR, aa);
        float rrInner = aaMask(innerRR, aa);

        alpha = (width < 0.5) ? rrFill : rrFill * (1.0 - rrInner);
    }

    // ============================================================
    // MODE 2: ARC
    // ============================================================

    else if (shapeType < 2.5)
    {
        float r_pixel = length(p_pixel);
        float outerRadius = min(half_size.x, half_size.y) - aa;
        float outerD = r_pixel - outerRadius;

        float innerR = max(outerRadius - border, 0.0);
        float innerD = innerR - r_pixel;

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
        vec2 a = v_data2.yz * quad_pixel_size;
        vec2 b = v_data2.wz * quad_pixel_size;

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

    alpha *= step(0.0039, alpha);

    gl_FragColor = vec4(v_col0.rgb, v_col0.a * alpha);
}
