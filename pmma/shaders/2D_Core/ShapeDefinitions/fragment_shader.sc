$input v_uv, v_col
#include "common.sh"

uniform int u_mode;

void main()
{
    vec2 p = v_uv - vec2(0.5, 0.5);

    // -----------------------------------
    // FAST AABB REJECT (shared)
    // -----------------------------------
    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    float r = 0.5;

    // -----------------------------------
    // PRECOMPUTE SHAPES (NO BRANCHING)
    // -----------------------------------

    float circleDist = dot(p, p);
    float circle = smoothstep(r, r - 0.01, sqrt(circleDist));

    float boxMask = step(max(abs(p.x), abs(p.y)), r);

    vec2 q = abs(p) - vec2(r, r);
    float rectMask = step(max(q.x, q.y), 0.0);

    // -----------------------------------
    // MODE SELECTION (BRANCHLESS)
    // -----------------------------------

    float m0 = step(-0.5, float(u_mode)) * step(float(u_mode), 0.5);
    float m1 = step(0.5, float(u_mode)) * step(float(u_mode), 1.5);
    float m2 = step(1.5, float(u_mode)) * step(float(u_mode), 2.5);

    float alpha =
        circle * m0 +
        boxMask * m1 +
        rectMask * m2;

    if (alpha <= 0.0)
        discard;

    gl_FragColor = vec4(v_col.rgb, v_col.a * alpha);
}