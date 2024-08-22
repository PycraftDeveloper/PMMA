#version 330

in vec2 v_uv;
uniform sampler2D texture2d;
uniform sampler2D texture3d;
uniform sampler2D pygame_texture;
uniform vec3 color_key;
out vec4 frag_color;

vec4 layer(vec4 foreground, vec4 background) {
    return foreground * foreground.a + background * (1.0 - foreground.a);
}

void main() {
    vec4 color2d = texture(texture2d, v_uv);
    if (color2d.rgb == color_key) {
        color2d = vec4(0, 0, 0, 0);
    }
    vec4 color3d = texture(texture3d, v_uv);
    if (color3d.rgb == color_key) {
        color3d = vec4(0, 0, 0, 0);
    }
    vec4 pygame_color = texture(pygame_texture, v_uv);
    if (pygame_color.rgb == color_key) {
        pygame_color = vec4(0, 0, 0, 0);
    }

    vec4 primary_layer = layer(color3d, color2d);
    vec4 blended_color = layer(pygame_color, primary_layer);

    frag_color = blended_color;  // Final color output
}