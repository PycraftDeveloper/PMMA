#version 330

in vec2 in_position;

uniform mat4 projection;
uniform vec2 offset;

void main() {
    gl_Position = projection * vec4(in_position + offset, 0.0, 1.0);
}