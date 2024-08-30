#version 330

in vec2 in_position;
in vec2 in_texcoord_0;

out vec2 v_uv;

uniform float aspect_ratio;

void main() {
    // Correct the x-coordinate by dividing by the aspect ratio
    vec2 corrected_position = in_position;
    corrected_position.x /= aspect_ratio;

    // Set the gl_Position using the corrected position
    gl_Position = vec4(corrected_position, 0.0, 1.0);

    // Pass through the texture coordinates
    v_uv = in_texcoord_0;
}
