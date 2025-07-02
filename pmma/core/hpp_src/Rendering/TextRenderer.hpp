#pragma once
#include "PMMA_Exports.hpp"

#include <iostream>
#include <map>
#include <vector>
#include <glm/glm.hpp>

typedef struct FT_LibraryRec_ *FT_Library;
typedef struct FT_FaceRec_ *FT_Face;
typedef unsigned int GLuint;

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
    int BaseLine;

    FontAtlas(const std::string& path, int pixelHeight);
};

struct GlyphInstance {
    glm::vec2 pos;
    glm::vec2 scale;
    glm::vec2 uvOrigin;
    glm::vec2 uvSize;
    glm::vec3 color;
};

class EXPORT CPP_TextRenderer {
private:
    GLuint quadVAO, quadVBO, instanceVBO;
    GLuint shaderProgram;
    std::vector<GlyphInstance> glyphs;
    FontAtlas* atlas = nullptr;

public:
    CPP_TextRenderer(const std::string& path, int pixelHeight);

    void begin();

    void drawText(const std::string& text, float* raw_pos, float scale, float* raw_color);

    void end();
};