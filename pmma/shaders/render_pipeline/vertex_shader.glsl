#version 330

in vec2 in_position;
in vec4 in_color;

out vec4 frag_color;

void main() {
    gl_Position = vec4(in_position, 0.0, 1.0);
    frag_color = in_color;
}