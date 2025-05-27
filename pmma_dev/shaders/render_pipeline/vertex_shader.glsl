#version 330

in vec2 in_position;
in vec4 in_color;
in vec2 in_offset;

uniform float aspect_ratio;

out vec4 frag_color;

void main() {
    gl_Position = vec4(in_offset.x + (in_position.x / aspect_ratio), in_offset.y + in_position.y, 0.0, 1.0);
    frag_color = in_color;
}