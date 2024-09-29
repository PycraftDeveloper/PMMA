#version 330

in vec2 in_position;

uniform mat4 projection;

void main() {
    gl_Position = projection * vec4(in_position, 0.0, 1.0);
}