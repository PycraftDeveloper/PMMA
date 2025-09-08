#pragma once

#include <map>
#include <string>

#include <bgfx/bgfx.h>
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
        bgfx::TextureHandle texture;
        int atlasWidth = 0, atlasHeight = 0;
        int BaseLine;

        FontAtlas(const std::string& path, int pixelHeight);

        ~FontAtlas();
};

/*struct GlyphInstance {
    glm::vec2 pos;
    glm::vec2 scale;
    glm::vec2 uvOrigin;
    glm::vec2 uvSize;
    glm::vec4 foreground_color;
    glm::vec4 background_color;
};*/

struct GlyphInstance {
    float pos[2];         // instance: glyph position in pixels
    float scale[2];       // instance: glyph size in pixels
    float uvOrigin[2];    // instance: uv origin in atlas (0..1)
    float uvSize[2];      // instance: uv size in atlas (0..1)
    float fgColor[4];     // instance: foreground RGBA
    float bgColor[4];     // instance: background RGBA
};