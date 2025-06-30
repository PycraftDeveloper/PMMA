#version 330 core
flat in uint shape_id;

layout(std140) uniform ShapeColors {
    vec4 shape_colors[16];
};

out vec4 frag_color;

void main() {
    frag_color = shape_colors[shape_id];
}