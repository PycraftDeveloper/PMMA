#include <glad/gl.h>
#include <ft2build.h>
#include FT_FREETYPE_H

#include "PMMA_Core.hpp"

FontAtlas::FontAtlas(const string& path, int pixelHeight) {
    FT_Library ft;
    if (FT_Init_FreeType(&ft)) {
        PMMA_Core::InternalLoggerInstance->InternalLogError(
            31,
            "PMMA could not initialize the FreeType module. If you have \
compiled PMMA from source yourself, please ensure you followed the build \
guides correctly. They can be found here: \
'https://github.com/PycraftDeveloper/PMMA/blob/main/repo/BuildGuides/intro.md' \
If you did not compile PMMA from source, or do not know what this means please \
feel free to report this as a bug so we can fix this here: \
'https://github.com/PycraftDeveloper/PMMA/issues'"
        );
        throw runtime_error("Could not init FreeType\n");
    }

    FT_Face face;
    if (FT_New_Face(ft, path.c_str(), 0, &face)) {
        PMMA_Core::InternalLoggerInstance->InternalLogWarn(
            32,
            "PMMA was unable to load the font file: '" + path + "'. Please \
ensure that the specified path is correct."
        );
        throw runtime_error("Failed to load font\n");
    }

    FT_Set_Pixel_Sizes(face, 0, pixelHeight);
    BaseLine = face->size->metrics.ascender >> 6; // Convert from 26.6 fixed-point format to pixels

    // Preload ASCII 32-126
    int maxWidth = 0, maxHeight = 0;
    for (char c = 32; c < 127; c++) {
        if (FT_Load_Char(face, c, FT_LOAD_RENDER)) continue;
        maxWidth += face->glyph->bitmap.width;
        maxHeight = max(maxHeight, (int)face->glyph->bitmap.rows);
    }
    atlasWidth = maxWidth;
    atlasHeight = maxHeight;

    glGenTextures(1, &textureID);
    glBindTexture(GL_TEXTURE_2D, textureID);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RED, atlasWidth, atlasHeight, 0, GL_RED, GL_UNSIGNED_BYTE, nullptr);

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);


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

FontAtlas::~FontAtlas() {
    glDeleteTextures(1, &textureID);
}