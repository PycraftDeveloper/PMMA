#version 330
in vec2 in_position;
uniform float aspect_ratio;
void main() {
    gl_Position = vec4(in_position.x, in_position.y / aspect_ratio, 0.0, 1.0);
}