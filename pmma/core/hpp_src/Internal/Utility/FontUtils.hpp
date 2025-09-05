#pragma once

#include <map>
#include <string>

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

        ~FontAtlas();
};

struct GlyphInstance {
    glm::vec2 pos;
    glm::vec2 scale;
    glm::vec2 uvOrigin;
    glm::vec2 uvSize;
    glm::vec4 foreground_color;
    glm::vec4 background_color;
};