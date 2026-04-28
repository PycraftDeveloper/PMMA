$input v_uv
#include <bgfx_shader.sh>

uniform vec2 u_params;
// x = radius, y = mode encoded as 0/1/2 via pre-baked weights

void main()
{
    vec2 p = v_uv - vec2(0.5, 0.5);

    // -----------------------------------
    // 1. ULTRA CHEAP AABB REJECT
    // -----------------------------------
    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    float r = u_params.x;
    float r2 = r * r;

    // -----------------------------------
    // 2. BRANCHLESS SHAPE REJECT
    // -----------------------------------

    // Circle SDF
    float circle = dot(p, p) - r2;

    // Box SDF (cheaper form)
    float box = max(abs(p.x), abs(p.y)) - r;

    // Blend via mode weight (NO BRANCH)
    // u_params.y = 0 => circle
    // u_params.y = 1 => box
    float isBox = step(0.5, u_params.y);

    float reject = mix(circle, box, isBox);

    if (reject > 0.0)
        discard;
}