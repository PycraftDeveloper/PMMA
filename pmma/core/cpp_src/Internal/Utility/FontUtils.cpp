#include <bgfx/bgfx.h>
#include <ft2build.h>
#include FT_FREETYPE_H

#include "PMMA_Core.hpp"

FontAtlas::FontAtlas(const std::string& path, int pixelHeight) {
    FT_Library ft;
    if (FT_Init_FreeType(&ft)) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            31,
            "PMMA could not initialize the FreeType module. If you have "
            "compiled PMMA from source yourself, please ensure you followed the build "
            "guides correctly. They can be found here: "
            "'https://github.com/PycraftDeveloper/PMMA/blob/main/repo/BuildGuides/intro.md' "
            "If you did not compile PMMA from source, or do not know what this means please "
            "feel free to report this as a bug so we can fix this here: "
            "'https://github.com/PycraftDeveloper/PMMA/issues'"
        );
        throw std::runtime_error("Could not init FreeType\n");
    }

    FT_Face face;
    if (FT_New_Face(ft, path.c_str(), 0, &face)) {
        PMMA_Core::LoggingManagerInstance->InternalLogWarn(
            32,
            "PMMA was unable to load the font file: '" + path + "'. Please "
            "ensure that the specified path is correct."
        );
        throw std::runtime_error("Failed to load font\n");
    }

    FT_Set_Pixel_Sizes(face, 0, pixelHeight);
    BaseLine = face->size->metrics.ascender >> 6; // Convert 26.6 fixed-point → pixels

    // Preload ASCII 32-126
    int maxWidth = 0, maxHeight = 0;
    for (char c = 32; c < 127; c++) {
        if (FT_Load_Char(face, c, FT_LOAD_RENDER)) continue;
        maxWidth += face->glyph->bitmap.width;
        maxHeight = std::max(maxHeight, (int)face->glyph->bitmap.rows);
    }
    atlasWidth = maxWidth;
    atlasHeight = maxHeight;

    // Create empty texture (1-channel grayscale → use R8 format)
    texture = bgfx::createTexture2D(
        (uint16_t)atlasWidth,
        (uint16_t)atlasHeight,
        false, // no mipmaps
        1,     // number of layers
        bgfx::TextureFormat::R8,
        BGFX_TEXTURE_NONE | BGFX_SAMPLER_MIN_POINT | BGFX_SAMPLER_MAG_POINT
    );

    if (!bgfx::isValid(texture)) {
        FT_Done_Face(face);
        FT_Done_FreeType(ft);
        throw std::runtime_error("Failed to create BGFX texture for font atlas.");
    }

    int xOffset = 0;
    for (char c = 32; c < 127; c++) {
        if (FT_Load_Char(face, c, FT_LOAD_RENDER)) continue;

        FT_Bitmap& bmp = face->glyph->bitmap;
        if (bmp.width > 0 && bmp.rows > 0) {
            std::vector<uint8_t> buffer(bmp.width * bmp.rows);
            for (int row = 0; row < bmp.rows; ++row) {
                memcpy(
                    buffer.data() + row * bmp.width,
                    bmp.buffer + row * bmp.pitch,
                    bmp.width
                );
            }
            const bgfx::Memory* mem = bgfx::copy(buffer.data(), buffer.size());
            bgfx::updateTexture2D(texture, 0, 0,
                (uint16_t)xOffset, 0,
                (uint16_t)bmp.width, (uint16_t)bmp.rows,
                mem
            );
        }

        Character ch = {
            glm::vec2((float)xOffset / atlasWidth, 0.0f),
            glm::vec2((float)bmp.width / atlasWidth, (float)bmp.rows / atlasHeight),
            glm::ivec2(bmp.width, bmp.rows),
            glm::ivec2(face->glyph->bitmap_left, face->glyph->bitmap_top),
            (unsigned int)face->glyph->advance.x
        };

        characters[c] = ch;
        xOffset += bmp.width;
    }

    FT_Done_Face(face);
    FT_Done_FreeType(ft);
}

FontAtlas::~FontAtlas() {
    if (bgfx::isValid(texture)) {
        bgfx::destroy(texture);
    }
}