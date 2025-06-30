#version 330 core
layout(location = 0) in vec2 in_position;
layout(location = 1) in uint in_shape_id;

flat out uint shape_id;

void main() {
    gl_Position = vec4(in_position, 0.0, 1.0);
    shape_id = in_shape_id;
}