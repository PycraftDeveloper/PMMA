// Requirements: FreeType, GLFW, GLAD, glm

#include <ft2build.h> // freetype
#include FT_FREETYPE_H

#include <glad/gl.h>
#include <GLFW/glfw3.h>

#include <iostream>
#include <map>
#include <vector>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <fstream>
#include <sstream>

// Reads a file's content into a std::string
std::string loadShaderSource(const std::string& filePath) {
    std::ifstream file(filePath);
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

// Compiles a shader and returns its ID
GLuint compileShader(GLenum type, const std::string& source) {
    GLuint shader = glCreateShader(type);
    const char* src = source.c_str();
    glShaderSource(shader, 1, &src, nullptr);
    glCompileShader(shader);

    // Check for compile errors
    GLint success;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char log[512];
        glGetShaderInfoLog(shader, 512, nullptr, log);
        std::cerr << "Shader Compilation Failed:\n" << log << std::endl;
    }

    return shader;
}

// Creates a shader program from vertex and fragment shader file paths
GLuint createShaderProgram(const std::string& vertexPath, const std::string& fragmentPath) {
    std::string vertexCode = loadShaderSource(vertexPath);
    std::string fragmentCode = loadShaderSource(fragmentPath);

    GLuint vertexShader = compileShader(GL_VERTEX_SHADER, vertexCode);
    GLuint fragmentShader = compileShader(GL_FRAGMENT_SHADER, fragmentCode);

    GLuint program = glCreateProgram();
    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);

    // Check linking errors
    GLint success;
    glGetProgramiv(program, GL_LINK_STATUS, &success);
    if (!success) {
        char log[512];
        glGetProgramInfoLog(program, 512, nullptr, log);
        std::cerr << "Program Linking Failed:\n" << log << std::endl;
    }

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    return program;
}

struct Character {
    glm::vec2 uvOrigin;
    glm::vec2 uvSize;
    glm::ivec2 size;
    glm::ivec2 bearing;
    unsigned int advance;
};

class FontAtlas {
public:
    std::map<char, Character> characters;
    GLuint textureID;
    int atlasWidth = 0, atlasHeight = 0;

    FontAtlas(const std::string& path, int pixelHeight) {
        FT_Library ft;
        if (FT_Init_FreeType(&ft)) {
            std::cerr << "Could not init FreeType\n";
            exit(EXIT_FAILURE);
        }

        FT_Face face;
        if (FT_New_Face(ft, path.c_str(), 0, &face)) {
            std::cerr << "Failed to load font\n";
            exit(EXIT_FAILURE);
        }

        FT_Set_Pixel_Sizes(face, 0, pixelHeight);

        // Preload ASCII 32-126
        int maxWidth = 0, maxHeight = 0;
        for (char c = 32; c < 127; c++) {
            if (FT_Load_Char(face, c, FT_LOAD_RENDER)) continue;
            maxWidth += face->glyph->bitmap.width;
            maxHeight = std::max(maxHeight, (int)face->glyph->bitmap.rows);
        }
        atlasWidth = maxWidth;
        atlasHeight = maxHeight;

        glGenTextures(1, &textureID);
        glBindTexture(GL_TEXTURE_2D, textureID);
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RED, atlasWidth, atlasHeight, 0, GL_RED, GL_UNSIGNED_BYTE, nullptr);

        int xOffset = 0;
        for (char c = 32; c < 127; c++) {
            if (FT_Load_Char(face, c, FT_LOAD_RENDER)) continue;

            glTexSubImage2D(GL_TEXTURE_2D, 0, xOffset, 0, face->glyph->bitmap.width, face->glyph->bitmap.rows,
                            GL_RED, GL_UNSIGNED_BYTE, face->glyph->bitmap.buffer);

            Character ch = {
                glm::vec2((float)xOffset / atlasWidth, 0.0f),
                glm::vec2((float)face->glyph->bitmap.width / atlasWidth, (float)face->glyph->bitmap.rows / atlasHeight),
                glm::ivec2(face->glyph->bitmap.width, face->glyph->bitmap.rows),
                glm::ivec2(face->glyph->bitmap_left, face->glyph->bitmap_top),
                (unsigned int)face->glyph->advance.x
            };

            characters[c] = ch;
            xOffset += face->glyph->bitmap.width;
        }

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

        FT_Done_Face(face);
        FT_Done_FreeType(ft);
    }
};

struct GlyphInstance {
    glm::vec2 pos;
    glm::vec2 scale;
    glm::vec2 uvOrigin;
    glm::vec2 uvSize;
    glm::vec3 color;
};

class TextRenderer {
    GLuint quadVAO, quadVBO, instanceVBO;
    GLuint shaderProgram = createShaderProgram("W:\\Documents\\GitHub\\PMMA\\pmma\\shaders\\text_renderer\\vertex_shader.glsl", "W:\\Documents\\GitHub\\PMMA\\pmma\\shaders\\text_renderer\\fragment_shader.glsl");
    glm::mat4 projection;
    std::vector<GlyphInstance> glyphs;
    FontAtlas& atlas;

public:
    TextRenderer(FontAtlas& fontAtlas, glm::mat4 proj, GLuint shader)
        : atlas(fontAtlas), projection(proj) {

        float quadVertices[] = {
            // positions   // texcoords
            0.0f, 1.0f,    0.0f, 1.0f,
            1.0f, 0.0f,    1.0f, 0.0f,
            0.0f, 0.0f,    0.0f, 0.0f,

            0.0f, 1.0f,    0.0f, 1.0f,
            1.0f, 1.0f,    1.0f, 1.0f,
            1.0f, 0.0f,    1.0f, 0.0f
        };

        glGenVertexArrays(1, &quadVAO);
        glGenBuffers(1, &quadVBO);
        glBindVertexArray(quadVAO);

        glBindBuffer(GL_ARRAY_BUFFER, quadVBO);
        glBufferData(GL_ARRAY_BUFFER, sizeof(quadVertices), quadVertices, GL_STATIC_DRAW);

        glEnableVertexAttribArray(0); // pos
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
        glEnableVertexAttribArray(1); // uv
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));

        glGenBuffers(1, &instanceVBO);
        glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
        glBufferData(GL_ARRAY_BUFFER, sizeof(GlyphInstance) * 1000, nullptr, GL_DYNAMIC_DRAW);

        int attrIndex = 2;
        for (int i = 0; i < 5; ++i) {
            glEnableVertexAttribArray(attrIndex);
            glVertexAttribPointer(attrIndex, i == 4 ? 3 : 2, GL_FLOAT, GL_FALSE, sizeof(GlyphInstance), (void*)(i * sizeof(glm::vec2)));
            glVertexAttribDivisor(attrIndex, 1);
            ++attrIndex;
        }

        glBindVertexArray(0);
    }

    void begin() { glyphs.clear(); }

    void drawText(const std::string& text, glm::vec2 pos, float scale, glm::vec3 color) {
        float x = pos.x;
        for (char c : text) {
            if (atlas.characters.count(c) == 0) continue;
            const Character& ch = atlas.characters[c];
            float xpos = x + ch.bearing.x * scale;
            float ypos = pos.y - (ch.size.y - ch.bearing.y) * scale;

            glyphs.push_back({
                glm::vec2(xpos, ypos),
                glm::vec2(ch.size) * scale,
                ch.uvOrigin,
                ch.uvSize,
                color
            });

            x += (ch.advance >> 6) * scale;
        }
    }

    void end() {
        glUseProgram(shaderProgram);
        glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(projection));

        glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
        glBufferSubData(GL_ARRAY_BUFFER, 0, glyphs.size() * sizeof(GlyphInstance), glyphs.data());

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, atlas.textureID);

        glBindVertexArray(quadVAO);
        glDrawArraysInstanced(GL_TRIANGLES, 0, 6, glyphs.size());
        glBindVertexArray(0);
    }
};