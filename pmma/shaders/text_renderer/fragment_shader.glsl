#version 330 core

in vec2 TexCoords;
in vec4 ForegroundColor;
in vec4 BackgroundColor;

uniform sampler2D textTexture;

out vec4 color;

void main() {
    float TextAlpha = texture(textTexture, TexCoords).r;
    color = mix(vec4(ForegroundColor.rgb, TextAlpha * ForegroundColor.a), BackgroundColor, 1-TextAlpha);
}