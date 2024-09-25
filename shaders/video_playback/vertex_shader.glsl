#version 330

in vec2 in_vert;
in vec2 in_text;

out vec2 v_text;

uniform vec2 scale;
uniform vec2 offset;

void main() {
    gl_Position = vec4(in_vert * scale + offset, 0.0, 1.0);
    v_text = vec2(in_text.x, 1.0 - in_text.y);  // Flip the y-coordinate
}