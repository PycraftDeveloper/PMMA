#version 330

uniform sampler2D Texture;

in vec2 v_text;

out vec4 f_color;

void main() {
    f_color = texture(Texture, v_text);
}