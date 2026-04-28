$input v_uv, v_col

#include "common.sh"

void main()
{
    int u_mode = 0; // will adapt later

    // -----------------------------------
    // NORMALIZED LOCAL SPACE
    // -----------------------------------
    vec2 center = vec2(0.5, 0.5);
    vec2 p = v_uv - center;

    // -----------------------------------
    // 1. GLOBAL AABB REJECT (FASTEST KILL)
    // works for ALL modes
    // -----------------------------------
    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    // -----------------------------------
    // SHAPE PARAMETERS
    // -----------------------------------
    float radius = 0.4;
    float radiusSq = radius * radius;

    // -----------------------------------
    // 2. MODE-SPECIFIC TIGHT REJECT
    // -----------------------------------

    if (u_mode == 0)
    {
        // CIRCLE MODE (your current case)
        float distSq = dot(p, p);

        if (distSq > radiusSq)
            discard;

        float dist = sqrt(distSq);
        float edge = smoothstep(radius, radius - 0.01, dist);

        gl_FragColor = vec4(v_col.rgb, v_col.a * edge);
        return;
    }

    else if (u_mode == 1)
    {
        // BOX MODE (cheaper than circle)
        if (abs(p.x) > radius || abs(p.y) > radius)
            discard;

        gl_FragColor = vec4(v_col);
        return;
    }

    else if (u_mode == 2)
    {
        // ROUNDED RECT MODE (cheap SDF-ish)
        vec2 q = abs(p) - vec2(radius, radius);

        float outside = max(q.x, q.y);
        if (outside > 0.0)
            discard;

        gl_FragColor = vec4(v_col);
        return;
    }

    // -----------------------------------
    // FALLBACK (SAFE DEFAULT)
    // -----------------------------------
    gl_FragColor = vec4(v_col);
}