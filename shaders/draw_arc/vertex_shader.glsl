#version 330

in vec2 in_position;

uniform float aspect_ratio;

void main() {
    gl_Position = vec4(in_position.x / aspect_ratio, in_position.y, 0.0, 1.0);
}