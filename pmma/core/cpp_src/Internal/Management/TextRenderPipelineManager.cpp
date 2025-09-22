// CPP_TextRendererPipelineManager_BGFX.cpp
// BGFX rewrite of your OpenGL text renderer pipeline.
// Requires: bgfx, bimg, glm, FreeType (your FontAtlas BGFX version from earlier)

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>
#include <bx/math.h>

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <ft2build.h>
#include FT_FREETYPE_H

#include "PMMA_Core.hpp"

using namespace std;

CPP_TextRendererPipelineManager::CPP_TextRendererPipelineManager() {
    if (FT_Init_FreeType(&m_ft))
        throw std::runtime_error("Failed to init FreeType");
    ResetAtlas();
    // Setup BGFX vertex layout (see shaders below)
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::Color0, 4, bgfx::AttribType::Uint8, true)
        .end();
    m_texUniform = bgfx::createUniform("u_fontAtlas", bgfx::UniformType::Sampler);

    string TextRendererShaderPath = PMMA_Registry::PMMA_Location
        + PMMA_Registry::PathSeparator + "shaders"
        + PMMA_Registry::PathSeparator + "text_renderer";

    ShaderProgram = new CPP_Shader();
    ShaderProgram->LoadShaderFromFolder(TextRendererShaderPath, true);
}

CPP_TextRendererPipelineManager::~CPP_TextRendererPipelineManager() {
    if (m_face) {
        FT_Done_Face(m_face);
    }

    if (m_ft) {
        FT_Done_FreeType(m_ft);
    }

    if (bgfx::isValid(m_atlasTex)) {
        bgfx::destroy(m_atlasTex);
    }

    if (bgfx::isValid(m_texUniform)) {
        bgfx::destroy(m_texUniform);
    }

    delete ShaderProgram;
    ShaderProgram = nullptr;
}

void CPP_TextRendererPipelineManager::DelayedSetup(string NewFontPath, unsigned int NewPixelHeight) {
    FontPath = NewFontPath;
    PixelHeight = NewPixelHeight;

    if (m_face) {
        FT_Done_Face(m_face); m_face = nullptr;
    }

    if (FT_New_Face(m_ft, FontPath.c_str(), 0, &m_face)) {
        return;
    }

    FT_Set_Pixel_Sizes(m_face, 0, PixelHeight);
    m_fontSize = PixelHeight;
    ResetAtlas();
    m_glyphs.clear();
}

void CPP_TextRendererPipelineManager::ResetAtlas() {
    m_atlasW = 512; m_atlasH = 512; m_nextX = 0; m_nextY = 0; m_rowH = 0;
    m_atlasData.assign(m_atlasW * m_atlasH, 0);
    m_dirtyRects.clear();
    if (bgfx::isValid(m_atlasTex)) {
        bgfx::destroy(m_atlasTex);
    }
    m_atlasTex = bgfx::createTexture2D(m_atlasW, m_atlasH, false, 1, bgfx::TextureFormat::R8, 0, nullptr);
}

void CPP_TextRendererPipelineManager::EnsureGlyph(char32_t codepoint) {
    if (m_glyphs.count(codepoint)) {
        return;
    }

    if (FT_Load_Char(m_face, codepoint, FT_LOAD_RENDER)) {
        return;
    }

    FT_GlyphSlot slot = m_face->glyph;

    // Will it fit?
    uint16_t spaceX = m_nextX + slot->bitmap.width;
    uint16_t spaceY = m_nextY + slot->bitmap.rows;
    if (spaceX > m_atlasW || spaceY > m_atlasH) {
        // Try to grow the atlas (minimum required size for new glyph)
        GrowAtlasAndRepack(slot->bitmap.width, slot->bitmap.rows, codepoint, slot);
        return;
    }
    AddGlyphToAtlas(codepoint, slot);
}

void CPP_TextRendererPipelineManager::GrowAtlasAndRepack(uint16_t requiredW, uint16_t requiredH, char32_t newCodepoint, FT_GlyphSlot slot) {
    // Estimate new atlas size (double current size, clamp to maximum, and ensure it fits the new glyph)
    uint16_t newW = m_atlasW, newH = m_atlasH;
    do {
        if (newW < newH) {
            newW *= 2;
        } else {
            newH *= 2;
        }

        newW = std::min(newW, m_maxAtlasDim);
        newH = std::min(newH, m_maxAtlasDim);
    } while ((newW < m_nextX + requiredW) || (newH < m_nextY + requiredH));

    std::vector<uint8_t> newAtlasData(newW * newH, 0);

    // Reset packing
    uint16_t penX = 0, penY = 0, rowH = 0;
    std::unordered_map<char32_t, GlyphInfo> newGlyphs;

    // Re-pack all glyphs
    for (const auto& pair : m_glyphs) {
        char32_t cp = pair.first;
        const GlyphInfo& oldG = pair.second;
        // Load glyph again from font
        if (FT_Load_Char(m_face, cp, FT_LOAD_RENDER)) {
            continue;
        }

        FT_GlyphSlot s = m_face->glyph;
        if (penX + s->bitmap.width > newW) {
            penX = 0;
            penY += rowH;
            rowH = 0;
        }

        if (penY + s->bitmap.rows > newH) {
            continue; // Out of space (shouldn't happen)
        }

        for (uint16_t row = 0; row < s->bitmap.rows; ++row) {
            memcpy(&newAtlasData[(penY + row)*newW + penX], &s->bitmap.buffer[row * s->bitmap.width], s->bitmap.width);
        }

        newGlyphs[cp] = {
            penX,
            penY,
            static_cast<uint16_t>(s->bitmap.width),
            static_cast<uint16_t>(s->bitmap.rows),
            static_cast<int16_t>(s->bitmap_left),
            static_cast<int16_t>(s->bitmap_top),
            static_cast<uint16_t>(s->advance.x >> 6)};

        penX += s->bitmap.width + 1;

        if (s->bitmap.rows > rowH) {
            rowH = s->bitmap.rows;
        }
    }

    // Add the new glyph
    if (FT_Load_Char(m_face, newCodepoint, FT_LOAD_RENDER) == 0) {
        FT_GlyphSlot s = m_face->glyph;
        if (penX + s->bitmap.width > newW) {
            penX = 0;
            penY += rowH;
            rowH = 0;
        }

        if (penY + s->bitmap.rows > newH) {
            throw std::runtime_error("Atlas still too small after growth!");
        }

        for (uint16_t row = 0; row < s->bitmap.rows; ++row) {
            memcpy(&newAtlasData[(penY + row)*newW + penX], &s->bitmap.buffer[row * s->bitmap.width], s->bitmap.width);
        }

        newGlyphs[newCodepoint] = {
            penX,
            penY,
            static_cast<uint16_t>(s->bitmap.width),
            static_cast<uint16_t>(s->bitmap.rows),
            static_cast<int16_t>(s->bitmap_left),
            static_cast<int16_t>(s->bitmap_top),
            static_cast<uint16_t>(s->advance.x >> 6)};

        penX += s->bitmap.width + 1;
        if (s->bitmap.rows > rowH) {
            rowH = s->bitmap.rows;
        }
    }

    // Replace atlas
    m_atlasW = newW; m_atlasH = newH;
    m_nextX = penX; m_nextY = penY; m_rowH = rowH;
    m_glyphs = std::move(newGlyphs);
    m_atlasData = std::move(newAtlasData);

    // Replace BGFX texture
    if (bgfx::isValid(m_atlasTex)) {
        bgfx::destroy(m_atlasTex);
    }

    m_atlasTex = bgfx::createTexture2D(m_atlasW, m_atlasH, false, 1, bgfx::TextureFormat::R8, 0, nullptr);
    m_dirtyRects.clear();
    m_dirtyRects.push_back({0, 0, m_atlasW, m_atlasH}); // Whole atlas needs upload
}

void CPP_TextRendererPipelineManager::AddGlyphToAtlas(char32_t codepoint, FT_GlyphSlot slot) {
    uint16_t x = m_nextX, y = m_nextY, w = slot->bitmap.width, h = slot->bitmap.rows;
    for (uint16_t row = 0; row < h; ++row) {
        memcpy(&m_atlasData[(y + row)*m_atlasW + x], &slot->bitmap.buffer[row * w], w);
    }

    m_glyphs[codepoint] = {
        x,
        y,
        w,
        h,
        static_cast<int16_t>(slot->bitmap_left),
        static_cast<int16_t>(slot->bitmap_top),
        static_cast<uint16_t>(slot->advance.x >> 6)};

    m_dirtyRects.push_back({x, y, w, h});
    m_nextX += w + 1;

    if (h > m_rowH) {
        m_rowH = h;
    }
}

void CPP_TextRendererPipelineManager::FlushDirtyRects() {
    for (const auto& rect : m_dirtyRects) {
        bgfx::updateTexture2D(m_atlasTex, 0, 0, rect.x, rect.y, rect.w, rect.h,
            bgfx::copy(&m_atlasData[rect.y*m_atlasW+rect.x], rect.w*rect.h));
    }
    m_dirtyRects.clear();
}

TextInstance CPP_TextRendererPipelineManager::CreateText(const std::string& text, float x, float y, uint32_t color) {
    // Decode UTF-8 (simplified, assumes ASCII for brevity)
    for (char c : text) {
        EnsureGlyph(c);
    }

    return TextInstance(text, x, y, color);
}

void CPP_TextRendererPipelineManager::AddRenderTarget(CPP_TextRenderer* NewObject) {
}

void CPP_TextRendererPipelineManager::Reset() {

}

void CPP_TextRendererPipelineManager::InternalRender(const std::vector<TextInstance>& texts) {
    FlushDirtyRects();
    struct Vertex { float x, y, u, v; uint32_t color; };
    std::vector<Vertex> vertices;

    for (const auto& inst : texts) {
        float penX = inst.x, penY = inst.y;
        char32_t prevChar = 0;
        for (size_t i = 0; i < inst.text.size(); ++i) {
            char c = inst.text[i];
            if (c == '\n') { penX = inst.x; penY += m_fontSize; prevChar = 0; continue; }
            if (!m_glyphs.count(c)) continue;
            // Kerning
            int kern = 0;
            if (prevChar && FT_HAS_KERNING(m_face)) {
                FT_Vector delta;
                FT_Get_Kerning(m_face, FT_Get_Char_Index(m_face, prevChar), FT_Get_Char_Index(m_face, c), FT_KERNING_DEFAULT, &delta);
                kern = delta.x >> 6;
            }
            penX += kern;
            const GlyphInfo& g = m_glyphs[c];
            float x0 = penX + g.bearingX, y0 = penY - g.bearingY;
            float x1 = x0 + g.width, y1 = y0 + g.height;
            float u0 = float(g.atlasX) / m_atlasW, v0 = float(g.atlasY) / m_atlasH;
            float u1 = float(g.atlasX + g.width) / m_atlasW, v1 = float(g.atlasY + g.height) / m_atlasH;
            vertices.push_back({x0, y0, u0, v0, inst.color});
            vertices.push_back({x1, y0, u1, v0, inst.color});
            vertices.push_back({x1, y1, u1, v1, inst.color});
            vertices.push_back({x0, y0, u0, v0, inst.color});
            vertices.push_back({x1, y1, u1, v1, inst.color});
            vertices.push_back({x0, y1, u0, v1, inst.color});
            penX += g.advance;
            prevChar = c;
        }
    }
    if (vertices.empty()) return;
    bgfx::VertexBufferHandle vbh = bgfx::createVertexBuffer(
        bgfx::copy(vertices.data(), uint32_t(vertices.size()*sizeof(Vertex))), m_layout
    );
    bgfx::setVertexBuffer(0, vbh);
    bgfx::setTexture(0, m_texUniform, m_atlasTex);
    bgfx::setState(BGFX_STATE_BLEND_ALPHA | BGFX_STATE_WRITE_RGB | BGFX_STATE_WRITE_A);
    bgfx::submit(0, ShaderProgram->Use());
    bgfx::destroy(vbh);
}
