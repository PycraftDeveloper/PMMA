#version 330
in vec3 v_color;
in vec2 v_pos;
out vec4 fragColor;
uniform vec2 circle_center;
uniform float circle_radius;
void main() {
    float dist = length(v_pos - circle_center);
    if (dist > circle_radius) {
        discard;
    }
    fragColor = vec4(v_color, 1.0);
}