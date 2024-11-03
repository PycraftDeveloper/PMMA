#version 330

in vec2 v_uv;

uniform sampler2D texture2d;
uniform sampler2D texture3d;

uniform sampler2DMS texture2d_ms;
uniform sampler2DMS texture3d_ms;

uniform int texture2d_samples;
uniform int texture3d_samples;

uniform vec2 texture2d_resolution;
uniform vec2 texture3d_resolution;

uniform vec3 color_key;
out vec4 frag_color;

vec4 layer(vec4 foreground, vec4 background) {
    return foreground * foreground.a + background * (1.0 - foreground.a);
}

vec4 multi_sample(sampler2DMS multi_sample_texture, int samples, vec2 v_uv, vec2 resolution) {
    // Average the samples for anti-aliasing
    ivec2 tex_coord = ivec2(v_uv * resolution);
    vec4 color = vec4(0.0);
    for (int i = 0; i < samples; i++) {
        color += texelFetch(multi_sample_texture, tex_coord, i);
    }
    color /= float(samples);
    return color;
}

void main() {
    vec4 color2d = vec4(0.0);
    vec4 color3d = vec4(0.0);

    if (texture2d_samples == 0) {
        color2d = texture(texture2d, v_uv);
    } else {
        color2d = multi_sample(texture2d_ms, texture2d_samples, v_uv, texture2d_resolution);
    }
    if (color2d.rgb == color_key) {
        color2d = vec4(0, 0, 0, 0);
    }

    if (texture3d_samples == 0) {
        color3d = texture(texture3d, v_uv);
    } else {
        color3d = multi_sample(texture3d_ms, texture3d_samples, v_uv, texture3d_resolution);
    }
    if (color3d.rgb == color_key) {
        color3d = vec4(0, 0, 0, 0);
    }

    vec4 primary_layer = layer(color3d, color2d);

    frag_color = primary_layer;  // Final color output
}