$input v_uv
#include <bgfx_shader.sh>

void main()
{
    int u_mode = 0;
    // -----------------------------------
    // LOCAL SPACE (match main shader)
    // -----------------------------------
    vec2 center = vec2(0.5, 0.5);
    vec2 p = v_uv - center;

    // -----------------------------------
    // 1. GLOBAL AABB REJECT (FASTEST)
    // -----------------------------------
    if (abs(p.x) > 0.5 || abs(p.y) > 0.5)
        discard;

    // -----------------------------------
    // 2. MODE-AWARE CONSERVATIVE REJECT
    // (IMPORTANT: must be "safe", not perfect)
    // -----------------------------------

    if (u_mode == 0)
    {
        // circle mode → cheap bounding circle
        float radius = 0.4;
        if (dot(p, p) > radius * radius)
            discard;
    }
    else if (u_mode == 1)
    {
        // box mode
        float r = 0.4;
        if (abs(p.x) > r || abs(p.y) > r)
            discard;
    }
    else if (u_mode == 2)
    {
        // rounded rect mode → conservative AABB already sufficient
        float r = 0.4;
        if (abs(p.x) > r || abs(p.y) > r)
            discard;
    }

    // -----------------------------------
    // no output (depth-only pass)
    // -----------------------------------
}