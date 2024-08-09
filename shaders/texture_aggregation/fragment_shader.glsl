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

    // Alpha blending for layering textures
    vec4 blended_color = mix(color3d, color2d, color2d.a);   // Layer 2D over 3D using 2D texture's alpha
    blended_color = mix(blended_color, pygame_color, pygame_color.a); // Layer Pygame texture over the previous result

    frag_color = blended_color;  // Final color output
}