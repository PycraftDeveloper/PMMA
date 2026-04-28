$input v_uv, v_col

#include "common.sh"

void main()
{
    // Circle center in UV space (0.5, 0.5)
    vec2 center = vec2(0.5, 0.5);

    // Radius of the circle (0–0.5)
    float radius = 0.4;

    // Distance from this pixel to the center
    float d = distance(v_uv, center);

    // Smooth edge (optional)
    float edge = smoothstep(radius, radius - 0.01, d);

    // Apply alpha mask
    gl_FragColor = vec4(v_col.rgb, v_col.a * edge);
}
