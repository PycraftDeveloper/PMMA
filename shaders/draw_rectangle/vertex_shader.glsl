#version 330

in vec2 in_position;

uniform float aspect_ratio;
uniform vec2 offset;

void main() {
    gl_Position = vec4(offset.x + (in_position.x / aspect_ratio), in_position.y+offset.y, 0.0, 1.0);
}