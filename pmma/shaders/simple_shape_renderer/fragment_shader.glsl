#version 330

in vec3 v_color;
in vec2 v_pos;
out vec4 fragColor;

void main() {
    fragColor = vec4(v_color, 1.0);
}