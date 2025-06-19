#version 330 core
layout (location = 0) in vec2 vertPos;
layout (location = 1) in vec2 vertUV;
layout (location = 2) in vec2 glyphPos;
layout (location = 3) in vec2 glyphSize;
layout (location = 4) in vec2 uvOrigin;
layout (location = 5) in vec2 uvSize;
layout (location = 6) in vec3 glyphColor;

uniform mat4 projection;

out vec2 TexCoords;
out vec3 FragColor;

void main() {
    vec2 scaledPos = vertPos * glyphSize + glyphPos;
    gl_Position = projection * vec4(scaledPos, 0.0, 1.0);
    TexCoords = uvOrigin + vertUV * uvSize;
    FragColor = glyphColor;
}