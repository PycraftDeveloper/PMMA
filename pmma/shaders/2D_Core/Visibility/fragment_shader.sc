$input v_instanceID, v_depthKey

#include "common.sh"

IMAGE2D_WR(u_visibilityBuffer, r32ui, 0);
IMAGE2D_WR(u_depthBuffer, r32f, 1);

void main()
{
    ivec2 pixel = ivec2(gl_FragCoord.xy);

    float newDepth = v_depthKey;
    float oldDepth = imageLoad(u_depthBuffer, pixel).r;

    // highest instance wins (newest on top)
    if (newDepth > oldDepth)
    {
        imageStore(u_depthBuffer, pixel, vec4(newDepth));
        imageStore(u_visibilityBuffer, pixel, uvec4(v_instanceID));
    }
}