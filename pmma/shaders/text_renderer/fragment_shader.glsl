#version 330 core
in vec2 TexCoords;
in vec3 FragColor;
uniform sampler2D textTexture;
out vec4 color;

void main() {
    float alpha = texture(textTexture, TexCoords).r;
    color = vec4(FragColor, alpha);
}