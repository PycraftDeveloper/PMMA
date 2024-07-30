#version 330

in vec2 v_uv;
uniform sampler2D texture2d;
uniform sampler2D texture3d;
uniform sampler2D pygame_texture;
out vec4 frag_color;

void main() {
    vec4 color2d = texture(texture2d, v_uv);
    vec4 color3d = texture(texture3d, v_uv);
    vec4 pygame_color = texture(pygame_texture, v_uv);
    frag_color = mix(mix(color2d, color3d, 0.5), pygame_color, 0.5);  // Simple blending
}