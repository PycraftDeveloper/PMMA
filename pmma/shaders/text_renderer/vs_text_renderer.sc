$input a_position, a_texcoord0, a_color0
$output v_uv, v_color0

void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
    v_uv = a_texcoord0;
    v_color0 = a_color0;
}