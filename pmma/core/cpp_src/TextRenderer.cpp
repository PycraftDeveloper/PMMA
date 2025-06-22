#include "TextRenderer.hpp"

#pragma once
#include "PMMA_Exports.hpp"

#include <ft2build.h>
#include FT_FREETYPE_H

#include <glad/gl.h>
#include <GLFW/glfw3.h>

#include <iostream>
#include <map>
#include <vector>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include "OpenGL.hpp"
#include "PMMA_Core.hpp"

FontAtlas::FontAtlas(const string& path, int pixelHeight) {
    FT_Library ft;
    if (FT_Init_FreeType(&ft)) {
        cerr << "Could not init FreeType\n";
        exit(EXIT_FAILURE);
    }

    FT_Face face;
    if (FT_New_Face(ft, path.c_str(), 0, &face)) {
        cerr << "Failed to load font\n";
        exit(EXIT_FAILURE);
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

CPP_TextRenderer::CPP_TextRenderer(const string& path, int pixelHeight) {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not initialized!");
    }

    atlas = new FontAtlas(path, pixelHeight);

    string vertex_shader_path[] = {"shaders", "text_renderer", "vertex_shader.glsl"};
    string fragment_shader_path[] = {"shaders", "text_renderer", "fragment_shader.glsl"};

    string vertex_shader = PMMA::PMMA_Location;
    for (const auto& part : vertex_shader_path) {
        vertex_shader += PMMA::PathSeparator + part;
    }

    string fragment_shader = PMMA::PMMA_Location;
    for (const auto& part : fragment_shader_path) {
        fragment_shader += PMMA::PathSeparator + part;
    }

    CPP_Shader Shader;
    shaderProgram = Shader.CreateShaderProgram(vertex_shader, fragment_shader);

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

void CPP_TextRenderer::begin() {
    glyphs.clear();
}

void CPP_TextRenderer::drawText(const string& text, float* raw_pos, float scale, float* raw_color) {
    glm::vec2 pos = glm::vec2(raw_pos[0], raw_pos[1]);
    glm::vec3 color = glm::vec3(raw_color[0], raw_color[1], raw_color[2]);

    float x = pos.x;
    for (char c : text) {
        if (atlas->characters.count(c) == 0) continue;
        const Character& ch = atlas->characters[c];
        float xpos = x + ch.bearing.x * scale;
        float ypos = pos.y + (atlas->BaseLine - ch.bearing.y) * scale;

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

void CPP_TextRenderer::end() {

    glUseProgram(shaderProgram);
    glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(PMMA::DisplayInstance->GetDisplayProjection()));

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
    glBufferSubData(GL_ARRAY_BUFFER, 0, glyphs.size() * sizeof(GlyphInstance), glyphs.data());

    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, atlas->textureID);

    glBindVertexArray(quadVAO);
    glDrawArraysInstanced(GL_TRIANGLES, 0, 6, glyphs.size());
    glBindVertexArray(0);

    glDisable(GL_BLEND);
}