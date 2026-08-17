$input v_uv , v_data0 , v_data1 , v_data2 , v_data3 , v_col0
#include "common.sh"

#define MAX_TEXTURE_MIPS 13

// SAMPLER2D(Color, 0);
// SAMPLER2D(Generated, 1);
SAMPLER2D(s_LookUpTexture, 2);
SAMPLER2D(s_Tex_0, 3);
SAMPLER2D(s_Tex_1, 4);
SAMPLER2D(s_Tex_2, 5);
SAMPLER2D(s_Tex_3, 6);
SAMPLER2D(s_Tex_4, 7);
SAMPLER2D(s_Tex_5, 8);
SAMPLER2D(s_Tex_6, 9);
SAMPLER2D(s_Tex_7, 10);
SAMPLER2D(s_Tex_8, 11);
SAMPLER2D(s_Tex_9, 12);
SAMPLER2D(s_Tex_10, 13);
SAMPLER2D(s_Tex_11, 14);
SAMPLER2D(s_Tex_12, 15);

uniform vec4 FragmentData;

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
    // MODE 0: SOLID AND SIMPLE
    // ============================================================
    if (shapeType < 0.5) {
        alpha = 1.0;
    }

    // ============================================================
    // MODE 1: ELLIPSE / POLYGON
    // ============================================================

    else if (shapeType < 1.5)
    {
        vec2 normalized_p = p_pixel / half_size;
        float ellipse_eq = dot(normalized_p, normalized_p) - 1.0;

        float screen_gradient = length(vec2(dFdx(ellipse_eq), dFdy(ellipse_eq)));
        screen_gradient = max(screen_gradient, 0.0001);

        float outerDist = ellipse_eq / screen_gradient;
        float circleFill = aaMask(outerDist, aa);
        float innerDist = -outerDist - border;

        float circleRing = aaMask(max(outerDist, innerDist), aa);
        float circleAlpha = (width < 0.5) ? circleFill : circleRing;
        float polyAlpha = circleAlpha;

        if (pointCount >= 3.0)
        {
            float N = max(pointCount, 3.0);
            float sector = 6.28318530718 / N;

            // To make the polygon scale with the ellipse axes,
            // we calculate the angles and projections using normalized coordinates
            float angle = atan2(normalized_p.y, normalized_p.x);
            angle += (angle < 0.0) * 6.28318530718;

            float sectorAngle = mod(angle + sector * 0.5, sector) - sector * 0.5;
            float edge = cos(sector * 0.5);

            // Calculate the raw, unscaled implicit distance for the polygon
            float raw_poly_proj = (length(normalized_p) * cos(sectorAngle)) / edge - 1.0;

            // Correct the polygon distance using hardware derivatives to match the screen grid
            float poly_gradient = length(vec2(dFdx(raw_poly_proj), dFdy(raw_poly_proj)));
            poly_gradient = max(poly_gradient, 0.0001);

            float polyOuter = raw_poly_proj / poly_gradient;
            float polyInner = -polyOuter - border;

            float polyDist = (width < 0.5) ? polyOuter : max(polyOuter, polyInner);
            polyAlpha = aaMask(polyDist, aa);
        }

        alpha = polyAlpha;
    }

    // ============================================================
    // MODE 2: ROUND RECT
    // ============================================================

    else if (shapeType < 2.5)
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
    // MODE 3: ARC
    // ============================================================

    else if (shapeType < 3.5)
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
    // MODE 4: LINE
    // ============================================================

    else
    {
        // 1. Reconstruct absolute pixel positions from the biased data
        vec2 a = vec2(v_data2.y, v_data2.z) - vec2(32768.0, 32768.0); // Start center point
        vec2 b = vec2(v_data2.w, v_data3.x) - vec2(32768.0, 32768.0); // End center point

        // 2. Vector math to project current pixel onto line segment AB
        vec2 pa = p_pixel - a;
        vec2 ba = b - a;

        // Project and clamp to keep the point bound strictly between the endpoints
        float h = clamp(dot(pa, ba) / max(dot(ba, ba), 1e-6), 0.0, 1.0);

        // 3. Distance from current pixel to the closest point on the segment
        float dist_line = length(pa - ba * h) - width;

        // 4. Apply your anti-aliasing mask directly to the capsule distance field
        alpha = aaMask(dist_line, aa);
    }

    alpha *= step(0.0039, alpha);

    if (alpha < FragmentData.x) {
        discard;
    }

    float textureID = v_data3.z;

    if (textureID >= 0.0)
    {
        // --------------------------------------------------------
        // Get mip-0 rectangle.
        // This is needed only to determine the source texture size.
        // --------------------------------------------------------

        vec2 lookupUV0 = vec2(
                0.5 / float(MAX_TEXTURE_MIPS),
                (textureID + 0.5) / FragmentData.y
            );

        vec4 lookup0 = texture2D(
                s_LookUpTexture,
                lookupUV0
            );

        if (lookup0.z <= 0.0 || lookup0.w <= 0.0)
        {
            gl_FragColor = vec4(
                    v_col0.rgb,
                    v_col0.a * alpha
                );
            return;
        }

        // Base-level source texture dimensions in texels.
        vec2 sourceSize =
            lookup0.zw * FragmentData.zw;

        // --------------------------------------------------------
        // Calculate LOD from v_uv.
        // --------------------------------------------------------

        vec2 ddxUV = dFdx(v_uv);
        vec2 ddyUV = dFdy(v_uv);

        vec2 dxTexels = ddxUV * sourceSize;
        vec2 dyTexels = ddyUV * sourceSize;

        float footprint = max(
                length(dxTexels),
                length(dyTexels)
            );

        float mip = log2(max(footprint, 1.0));

        float mipLevel = clamp(
                floor(mip + 0.5),
                0.0,
                float(MAX_TEXTURE_MIPS - 1)
            );

        // --------------------------------------------------------
        // Now get the independently-packed rectangle for this mip.
        // --------------------------------------------------------

        vec2 lookupUV = vec2(
                (mipLevel + 0.5) / float(MAX_TEXTURE_MIPS),
                (textureID + 0.5) / FragmentData.y
            );

        vec4 lookup = texture2D(
                s_LookUpTexture,
                lookupUV
            );

        if (lookup.z <= 0.0 || lookup.w <= 0.0)
        {
            gl_FragColor = vec4(
                    v_col0.rgb,
                    v_col0.a * alpha
                );
            return;
        }

        vec2 atlasUV =
            lookup.xy +
                v_uv * lookup.zw;

        vec4 TexColor;

        if (mip < 0.5)
        {
            TexColor = texture2D(s_Tex_0, atlasUV);
        }
        else if (mip < 1.5)
        {
            TexColor = texture2D(s_Tex_1, atlasUV);
        }
        else if (mip < 2.5)
        {
            TexColor = texture2D(s_Tex_2, atlasUV);
        }
        else if (mip < 3.5)
        {
            TexColor = texture2D(s_Tex_3, atlasUV);
        }
        else if (mip < 4.5)
        {
            TexColor = texture2D(s_Tex_4, atlasUV);
        }
        else if (mip < 5.5)
        {
            TexColor = texture2D(s_Tex_5, atlasUV);
        }
        else if (mip < 6.5)
        {
            TexColor = texture2D(s_Tex_6, atlasUV);
        }
        else if (mip < 7.5)
        {
            TexColor = texture2D(s_Tex_7, atlasUV);
        }
        else if (mip < 8.5)
        {
            TexColor = texture2D(s_Tex_8, atlasUV);
        }
        else if (mip < 9.5)
        {
            TexColor = texture2D(s_Tex_9, atlasUV);
        }
        else if (mip < 10.5)
        {
            TexColor = texture2D(s_Tex_10, atlasUV);
        }
        else if (mip < 11.5)
        {
            TexColor = texture2D(s_Tex_11, atlasUV);
        }
        else
        {
            TexColor = texture2D(s_Tex_12, atlasUV);
        }

        gl_FragColor = vec4(
                v_col0.rgb * TexColor.rgb,
                v_col0.a * alpha * TexColor.a
            );
    }
    else
    {
        gl_FragColor = vec4(
                v_col0.rgb,
                v_col0.a * alpha
            );
    }
}
