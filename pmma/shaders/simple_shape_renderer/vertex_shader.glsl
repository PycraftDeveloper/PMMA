#version 330

in vec2 in_vert;
in vec3 in_color;
out vec3 v_color;
out vec2 v_pos;

uniform float aspect_ratio; // Aspect ratio of the framebuffer

void main() {
    vec2 final_position = in_vert;
    final_position.x /= aspect_ratio;

    gl_Position = vec4(final_position, 0.0, 1.0);

    v_color = in_color;
    v_pos = in_vert;
}