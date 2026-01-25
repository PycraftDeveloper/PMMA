// CPP_TextRenderPipelineManager_BGFX.cpp
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

CPP_TextRenderPipelineManager::CPP_TextRenderPipelineManager() {
    if (FT_Init_FreeType(&m_ft))
        throw std::runtime_error("Failed to init FreeType");

    ResetAtlas();

    // Setup BGFX vertex layout (see shaders below)
    m_layout.begin()
        .add(bgfx::Attrib::Position, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
        .add(bgfx::Attrib::TexCoord1, 2, bgfx::AttribType::Float)
        .end();

    m_fgColUniform = bgfx::createUniform("s_ForegroundColorTex", bgfx::UniformType::Sampler);
    m_bgColUniform = bgfx::createUniform("s_BackgroundColorTex", bgfx::UniformType::Sampler);
    m_texUniform = bgfx::createUniform("s_fontAtlas", bgfx::UniformType::Sampler);

    u_colorInfo  = bgfx::createUniform("u_colorInfo", bgfx::UniformType::Vec4);

    string TextRendererShaderPath = PMMA_Registry::PMMA_Location
        + PMMA_Registry::PathSeparator + "shaders"
        + PMMA_Registry::PathSeparator + "text_renderer";

    ShaderProgram = new CPP_Shader();
    ShaderProgram->LoadShaderFromFolder(TextRendererShaderPath, true);
}

CPP_TextRenderPipelineManager::~CPP_TextRenderPipelineManager() {
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

    if (bgfx::isValid(u_colorInfo)) {
        bgfx::destroy(u_colorInfo);
    }

    delete ShaderProgram;
    ShaderProgram = nullptr;
}

void CPP_TextRenderPipelineManager::DelayedSetup(string NewFontPath, unsigned int NewPixelHeight) {
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

void CPP_TextRenderPipelineManager::ResetAtlas() {
    m_atlasW = 512; m_atlasH = 512; m_nextX = 0; m_nextY = 0; m_rowH = 0;
    m_atlasData.assign(m_atlasW * m_atlasH, 0);
    m_dirtyRects.clear();
    if (bgfx::isValid(m_atlasTex)) {
        bgfx::destroy(m_atlasTex);
    }
    m_atlasTex = bgfx::createTexture2D(m_atlasW, m_atlasH, false, 1, bgfx::TextureFormat::R8, 0, nullptr);
}

void CPP_TextRenderPipelineManager::EnsureGlyph(char32_t codepoint) {
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

void CPP_TextRenderPipelineManager::GrowAtlasAndRepack(uint16_t requiredW, uint16_t requiredH, char32_t newCodepoint, FT_GlyphSlot slot) {
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
        // Load glyph again from font
        if (FT_Load_Char(m_face, cp, FT_LOAD_RENDER)) {
            continue;
        }

        FT_GlyphSlot s = m_face->glyph;
        uint16_t w = s->bitmap.width, h = s->bitmap.rows;
        if (penX + w > newW) {
            penX = 0;
            penY += rowH;
            rowH = 0;
        }

        if (penY + h > newH) {
            continue; // Out of space (shouldn't happen)
        }

        for (uint16_t row = 0; row < h; ++row) {
            const uint8_t* src;
            if (s->bitmap.pitch >= 0)
                src = s->bitmap.buffer + row * s->bitmap.pitch;
            else
                src = s->bitmap.buffer + (h - 1 - row) * (-s->bitmap.pitch);

            uint8_t* dst = &newAtlasData[(penY + row) * newW + penX];
            memcpy(dst, src, w);
        }

        newGlyphs[cp] = {
            penX,
            penY,
            static_cast<uint16_t>(w),
            static_cast<uint16_t>(h),
            static_cast<int16_t>(s->bitmap_left),
            static_cast<int16_t>(s->bitmap_top),
            static_cast<uint16_t>(s->advance.x >> 6)};

        penX += w + 1;

        if (h > rowH) {
            rowH = h;
        }
    }

    // Add the new glyph
    if (FT_Load_Char(m_face, newCodepoint, FT_LOAD_RENDER) == 0) {
        FT_GlyphSlot s = m_face->glyph;
        uint16_t w = s->bitmap.width, h = s->bitmap.rows;
        if (penX + w > newW) {
            penX = 0;
            penY += rowH;
            rowH = 0;
        }

        if (penY + h > newH) {
            throw std::runtime_error("Atlas still too small after growth!");
        }

        for (uint16_t row = 0; row < h; ++row) {
            const uint8_t* src;
            if (s->bitmap.pitch >= 0)
                src = s->bitmap.buffer + row * s->bitmap.pitch;
            else
                src = s->bitmap.buffer + (h - 1 - row) * (-s->bitmap.pitch);

            uint8_t* dst = &newAtlasData[(penY + row)*newW + penX];
            memcpy(dst, src, w);
        }

        newGlyphs[newCodepoint] = {
            penX,
            penY,
            static_cast<uint16_t>(w),
            static_cast<uint16_t>(h),
            static_cast<int16_t>(s->bitmap_left),
            static_cast<int16_t>(s->bitmap_top),
            static_cast<uint16_t>(s->advance.x >> 6)};

        penX += w + 1;
        if (h > rowH) {
            rowH = h;
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

void CPP_TextRenderPipelineManager::AddGlyphToAtlas(char32_t codepoint, FT_GlyphSlot slot) {
    uint16_t x = m_nextX, y = m_nextY, w = slot->bitmap.width, h = slot->bitmap.rows;
    for (uint16_t row = 0; row < h; ++row) {
        const uint8_t* src;
        if (slot->bitmap.pitch >= 0)
            src = slot->bitmap.buffer + row * slot->bitmap.pitch;
        else
            src = slot->bitmap.buffer + (h - 1 - row) * (-slot->bitmap.pitch);

        uint8_t* dst = &m_atlasData[(y + row) * m_atlasW + x];
        memcpy(dst, src, w);
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

void CPP_TextRenderPipelineManager::FlushDirtyRects() {
    for (const auto& rect : m_dirtyRects) {
        // Create a tightly packed buffer for the rect
        std::vector<uint8_t> temp(rect.w * rect.h);
        for (uint16_t row = 0; row < rect.h; ++row) {
            memcpy(
                &temp[row * rect.w],
                &m_atlasData[(rect.y + row) * m_atlasW + rect.x],
                rect.w
            );
        }
        bgfx::updateTexture2D(
            m_atlasTex, 0, 0,
            rect.x, rect.y,
            rect.w, rect.h,
            bgfx::copy(temp.data(), (uint32_t)temp.size())
        );
    }
    m_dirtyRects.clear();
}

inline bool is_code_with_prefix(const std::string& token,
                                const std::string& prefix)
{
    // token must be: <prefix> + '=' + 3 uppercase letters
    const std::size_t p = prefix.size();

    // Total length must match exactly
    if (token.size() != p + 1 + 3)
        return false;

    // Check prefix
    if (token.compare(0, p, prefix) != 0)
        return false;

    // Check '='
    if (token[p] != '=')
        return false;

    // Check three uppercase ASCII letters
    unsigned char a = token[p + 1];
    unsigned char b = token[p + 2];
    unsigned char c = token[p + 3];

    return (a >= 'A' && a <= 'Z') &&
           (b >= 'A' && b <= 'Z') &&
           (c >= 'A' && c <= 'Z');
}

void CPP_TextRenderPipelineManager::AddRenderTarget(CPP_TextRenderer* NewObject) {
    string TextContent = NewObject->Text;

    float StartPosition[2];
    NewObject->Position->Get(StartPosition);
    float penX = StartPosition[0], penY = StartPosition[1];

    uint8_t ForegroundColor[4];
    uint8_t BackgroundColor[4];

    NewObject->ForegroundColor->Get_RGBA(ForegroundColor);
    NewObject->BackgroundColor->Get_RGBA(BackgroundColor);

    float ForegroundColorIndex = GetForegroundColorIndex(
        ForegroundColor,
        NewObject->ID
    );

    float BackgroundColorIndex = GetBackgroundColorIndex(
        BackgroundColor,
        NewObject->ID
    );

    TextFormatting formatting(
        ForegroundColorIndex,
        BackgroundColorIndex
    );

    if (!NewObject->GlyphsPrepared) {
        // Ensure all glyphs are prepared
        for (char c : TextContent) {
            EnsureGlyph(c);
        }
        NewObject->GlyphsPrepared = true;
    }

    char32_t prevChar = 0;
    for (size_t i = 0; i < TextContent.size(); ++i) {
        char c = TextContent[i];

        // ---------------------------------------------------------
        // INLINE FORMAT PARSER (single-pass, tokenizing as we scan)
        // ---------------------------------------------------------
        if (c == '$' && i + 1 < TextContent.size() && TextContent[i + 1] == '{') {
            size_t blockStart = i; // for fallback literal rendering
            i += 2; // skip "${"
            std::vector<std::string> tokens;
            size_t tokenStart = i;
            bool malformed = true;

            while (i < TextContent.size()) {
                char ch = TextContent[i];

                if (ch == ';' || ch == '}') {
                    size_t len = i - tokenStart;

                    if (len > 0) {
                        tokens.emplace_back(&TextContent[tokenStart], len);
                    } if (ch == '}') {
                        malformed = false;
                        break;
                    }

                    tokenStart = i + 1; // next token
                } ++i;
            }

            if (malformed) {
                // -------------------------------------------------
                // MALFORMED: render literally "${something"
                // -------------------------------------------------
                for (size_t k = blockStart; k < TextContent.size(); ++k) {
                    if (TextContent[k] == '}' || TextContent[k] == '\n') {
                        break;
                    }

                    char literal;
                    if (formatting.RandomizeText) {
                        literal = GenerateRandomPrintableCharacter();
                    } else {
                        literal = TextContent[k];
                    }

                    if (!m_glyphs.count(literal))
                        continue;

                    const GlyphInfo& g = m_glyphs[literal];
                    float x0 = penX + g.bearingX;
                    float y0 = penY - g.bearingY;
                    float x1 = x0 + g.width;
                    float y1 = y0 + g.height;
                    float u0 = float(g.atlasX) / m_atlasW;
                    float v0 = float(g.atlasY) / m_atlasH;
                    float u1 = float(g.atlasX + g.width) / m_atlasW;
                    float v1 = float(g.atlasY + g.height) / m_atlasH;

                    CharacterRenderData.push_back({ x0, y0, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u0, v0 });
                    CharacterRenderData.push_back({ x1, y0, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u1, v0 });
                    CharacterRenderData.push_back({ x1, y1, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u1, v1 });
                    CharacterRenderData.push_back({ x0, y0, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u0, v0 });
                    CharacterRenderData.push_back({ x1, y1, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u1, v1 });
                    CharacterRenderData.push_back({ x0, y1, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u0, v1 });

                    penX += g.advance;
                } continue;
            }

            // -----------------------------------------------------
            // VALID FORMAT BLOCK — process tokens
            // -----------------------------------------------------

            for (auto token : tokens) {
                if (token == "rst") {
                    formatting.Reset();
                } else if (token == "rnd") {
                    formatting.RandomizeText = !formatting.RandomizeText;
                } else if (is_code_with_prefix(token, "fg")) {
                    // Extract color code
                    string ColorCode = token.substr(3, 3);
                    transform(ColorCode.begin(), ColorCode.end(), ColorCode.begin(), ::tolower); // change to lowercase

                    if (ColorCode == "rst") {
                        formatting.ForegroundColorIndex = formatting.DefaultForegroundColorIndex;
                        continue;
                    }

                    if (CPP_Constants::Colors::ColorMap.find(ColorCode) == CPP_Constants::Colors::ColorMap.end()) { // check it exists
                        PMMA_Core::LoggingManagerInstance->InternalLogError(
                            60,
                            "The color code '" + ColorCode + "' is not recognized."
                        );
                        throw std::runtime_error("Unrecognized color code!");
                    }

                    auto& rgb = CPP_Constants::Colors::ColorMap.at(ColorCode); // find it
                    uint8_t in_color[4] = {rgb[0], rgb[1], rgb[2], 255};

                    float newIndex = GetForegroundColorIndex(
                        in_color,
                        NewObject->ID
                    );

                    if (newIndex != formatting.ForegroundColorIndex) {
                        formatting.ForegroundColorIndex = newIndex;
                    }
                } else if (is_code_with_prefix(token, "bg")) {
                    // Extract color code
                    string ColorCode = token.substr(3, 3);
                    transform(ColorCode.begin(), ColorCode.end(), ColorCode.begin(), ::tolower); // change to lowercase

                    if (ColorCode == "rst") {
                        formatting.BackgroundColorIndex = formatting.DefaultBackgroundColorIndex;
                        continue;
                    }

                    if (CPP_Constants::Colors::ColorMap.find(ColorCode) == CPP_Constants::Colors::ColorMap.end()) { // check it exists
                        PMMA_Core::LoggingManagerInstance->InternalLogError(
                            60,
                            "The color code '" + ColorCode + "' is not recognized."
                        );
                        throw std::runtime_error("Unrecognized color code!");
                    }

                    auto& rgb = CPP_Constants::Colors::ColorMap.at(ColorCode); // find it
                    uint8_t in_color[4] = {rgb[0], rgb[1], rgb[2], 255};

                    float newIndex = GetBackgroundColorIndex(
                        in_color,
                        NewObject->ID
                    );

                    if (newIndex != formatting.BackgroundColorIndex) {
                        formatting.BackgroundColorIndex = newIndex;
                    }
                }
            }

            continue; // skip rendering the formatting block
        }

        // ---------------------------------------------------------
        // NORMAL RENDERING CONTINUES HERE
        // ---------------------------------------------------------
        if (formatting.RandomizeText) {
            c = GenerateRandomPrintableCharacter();
        }

        if (c == '\n') {
            penX = StartPosition[0];
            penY += m_fontSize;
            prevChar = 0;
            continue;
        }

        if (!m_glyphs.count(c)) {
            continue;
        }

        // Kernin
        int kern = 0;
        if (prevChar && FT_HAS_KERNING(m_face)) {
            FT_Vector delta;
            FT_Get_Kerning(
                m_face,
                FT_Get_Char_Index(m_face, prevChar),
                FT_Get_Char_Index(m_face, c),
                FT_KERNING_DEFAULT,
                &delta);

            kern = delta.x >> 6;
        }

        penX += kern;
        const GlyphInfo& g = m_glyphs[c];

        float x0 = penX + g.bearingX;
        float y0 = penY - g.bearingY;
        float x1 = x0 + g.width;
        float y1 = y0 + g.height;
        float u0 = float(g.atlasX) / m_atlasW;
        float v0 = float(g.atlasY) / m_atlasH;
        float u1 = float(g.atlasX + g.width) / m_atlasW;
        float v1 = float(g.atlasY + g.height) / m_atlasH;

        CharacterRenderData.push_back({ x0, y0, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u0, v0 });
        CharacterRenderData.push_back({ x1, y0, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u1, v0 });
        CharacterRenderData.push_back({ x1, y1, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u1, v1 });
        CharacterRenderData.push_back({ x0, y0, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u0, v0 });
        CharacterRenderData.push_back({ x1, y1, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u1, v1 });
        CharacterRenderData.push_back({ x0, y1, formatting.ForegroundColorIndex, formatting.BackgroundColorIndex, u0, v1 });
        penX += g.advance;
        prevChar = c;
    }
}

void CPP_TextRenderPipelineManager::Reset() {
    if (bgfx::isValid(vbh)) {
        bgfx::destroy(vbh);
    }

    LiveForegroundColorCount = 0;
    LiveBackgroundColorCount = 0;

    CharacterRenderData.clear();

    if (UsingComplexForegroundColorInsertion) {
        std::vector<unsigned int> RecycleList;

        for (const auto& [shapeID, slot] : ForegroundColorSlotID) {
            if (ForegroundColorsSeenThisFrame.find(shapeID) == ForegroundColorsSeenThisFrame.end()) {
                ForegroundColorFreeSlots.push_back(slot);
                RecycleList.push_back(shapeID);
            }
        }

        // Batch erase after iteration
        for (unsigned int shapeID : RecycleList) {
            ForegroundColorSlotID.erase(shapeID);
        }
        RecycleList.clear();

        unsigned int SeenThisFrameSize = (unsigned int)ForegroundColorsSeenThisFrame.size();
        ForegroundColorsSeenThisFrame.clear();
        ForegroundColorsSeenThisFrame.reserve(SeenThisFrameSize + 25);
    }

    if (UsingComplexBackgroundColorInsertion) {
        std::vector<unsigned int> RecycleList;

        for (const auto& [shapeID, slot] : BackgroundColorSlotID) {
            if (BackgroundColorsSeenThisFrame.find(shapeID) == BackgroundColorsSeenThisFrame.end()) {
                BackgroundColorFreeSlots.push_back(slot);
                RecycleList.push_back(shapeID);
            }
        }

        // Batch erase after iteration
        for (unsigned int shapeID : RecycleList) {
            BackgroundColorSlotID.erase(shapeID);
        }
        RecycleList.clear();

        unsigned int SeenThisFrameSize = (unsigned int)BackgroundColorsSeenThisFrame.size();
        BackgroundColorsSeenThisFrame.clear();
        BackgroundColorsSeenThisFrame.reserve(SeenThisFrameSize + 25);
    }

    bool PreviouslyUsingComplexForegroundColorInsertion = UsingComplexForegroundColorInsertion;
    bool PreviouslyUsingComplexBackgroundColorInsertion = UsingComplexBackgroundColorInsertion;

    if (!ChangedForegroundColorModes && ForegroundColorsInserted > 0) {
        if (ForegroundColorIndexesChanged / ForegroundColorsInserted > 0.2f) {
            UsingComplexForegroundColorInsertion = true;
        } else {
            UsingComplexForegroundColorInsertion = false;
        }
    }

    if (!ChangedBackgroundColorModes && BackgroundColorsInserted > 0) {
        if (BackgroundColorIndexesChanged / BackgroundColorsInserted > 0.2f) {
            UsingComplexBackgroundColorInsertion = true;
        } else {
            UsingComplexBackgroundColorInsertion = false;
        }
    }

    ForegroundColorIndexesChanged = 0;
    BackgroundColorIndexesChanged = 0;
    ForegroundColorsInserted = 0;
    BackgroundColorsInserted = 0;

    if (UsingComplexForegroundColorInsertion && !PreviouslyUsingComplexForegroundColorInsertion) {
        ForegroundColorSlotID.clear();
        ForegroundColorFreeSlots.clear();
        ForegroundColors.clear();
    }

    if (UsingComplexBackgroundColorInsertion && !PreviouslyUsingComplexBackgroundColorInsertion) {
        BackgroundColorSlotID.clear();
        BackgroundColorFreeSlots.clear();
        BackgroundColors.clear();
    }

    if (UsingComplexForegroundColorInsertion != PreviouslyUsingComplexForegroundColorInsertion) {
        ChangedForegroundColorModes = true;
    } else {
        ChangedForegroundColorModes = false;
    }

    if (UsingComplexBackgroundColorInsertion != PreviouslyUsingComplexBackgroundColorInsertion) {
        ChangedBackgroundColorModes = true;
    } else {
        ChangedBackgroundColorModes = false;
    }
}

void CPP_TextRenderPipelineManager::InternalRender() {
    FlushDirtyRects();

    if (CharacterRenderData.empty()) {
        return;
    }

    // Generate VBO
    vbh = bgfx::createVertexBuffer(
        bgfx::copy(CharacterRenderData.data(), uint32_t(CharacterRenderData.size()*sizeof(CharacterData))), m_layout
    );

    bgfx::setVertexBuffer(0, vbh);

    // Generate Foreground Texture
    ForegroundColors.resize(LiveForegroundColorCount);
    BackgroundColors.resize(LiveBackgroundColorCount);

    // Foreground Texture Management
    uint32_t Foreground_numColors = (uint32_t)ForegroundColors.size() / 4;
    uint32_t Foreground_width  = std::min(PMMA_Core::RenderPipelineCore->MaxWidth, Foreground_numColors);
    uint32_t Foreground_height = (Foreground_numColors + Foreground_width - 1) / Foreground_width;

    size_t expectedSize = Foreground_width * Foreground_height * 4;
    if (ForegroundColors.size() < expectedSize) {
        ForegroundColors.resize(expectedSize, 0); // Pad with transparent black
    }

    // Background Texture Management
    uint32_t Background_numColors = (uint32_t)BackgroundColors.size() / 4;
    uint32_t Background_width  = std::min(PMMA_Core::RenderPipelineCore->MaxWidth, Background_numColors);
    uint32_t Background_height = (Background_numColors + Background_width - 1) / Background_width;

    expectedSize = Background_width * Background_height * 4;
    if (BackgroundColors.size() < expectedSize) {
        BackgroundColors.resize(expectedSize, 0);
    }

    const bgfx::Memory* fg_texMem = bgfx::copy(
        ForegroundColors.data(),
        static_cast<uint32_t>(ForegroundColors.size() * sizeof(uint8_t))
    );

    const bgfx::Memory* bg_texMem = bgfx::copy(
        BackgroundColors.data(),
        static_cast<uint32_t>(BackgroundColors.size() * sizeof(uint8_t))
    );

    // If texture exists but size changed, destroy and recreate it
    if (bgfx::isValid(m_fg_color_tex)) {
        if (m_ForegroundColorTextureWidth != Foreground_width || m_ForegroundColorTextureHeight != Foreground_height) {
            bgfx::destroy(m_fg_color_tex);
            m_fg_color_tex = BGFX_INVALID_HANDLE;
        }
    }
    if (bgfx::isValid(m_bg_color_tex)) {
        if (m_BackgroundColorTextureWidth != Background_width || m_BackgroundColorTextureHeight != Background_height) {
            bgfx::destroy(m_bg_color_tex);
            m_bg_color_tex = BGFX_INVALID_HANDLE;
        }
    }

    // create texture if missing
    if (!bgfx::isValid(m_fg_color_tex)) {
        m_fg_color_tex = bgfx::createTexture2D(
            (uint16_t)Foreground_width, (uint16_t)Foreground_height,
            false,   // hasMips
            1,       // num layers
            bgfx::TextureFormat::RGBA8,
            BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
    }

    if (!bgfx::isValid(m_bg_color_tex)) {
        m_bg_color_tex = bgfx::createTexture2D(
            (uint16_t)Background_width, (uint16_t)Background_height,
            false,   // hasMips
            1,       // num layers
            bgfx::TextureFormat::RGBA8,
            BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);
    }

    bgfx::updateTexture2D(m_fg_color_tex, 0, 0, 0, 0, Foreground_width, Foreground_height, fg_texMem);
    bgfx::updateTexture2D(m_bg_color_tex, 0, 0, 0, 0, Background_width, Background_height, bg_texMem);

    // store width/height for shader normalization
    m_ForegroundColorTextureWidth  = Foreground_width;
    m_ForegroundColorTextureHeight = Foreground_height;
    m_BackgroundColorTextureWidth  = Background_width;
    m_BackgroundColorTextureHeight = Background_height;

    float info[4] = {
        float(m_ForegroundColorTextureWidth),
        float(m_ForegroundColorTextureHeight),
        float(m_BackgroundColorTextureWidth),
        float(m_BackgroundColorTextureHeight)};

    bgfx::setUniform(u_colorInfo, info);

    bgfx::setTexture(0, m_fgColUniform, m_fg_color_tex, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);

    bgfx::setTexture(1, m_bgColUniform, m_bg_color_tex, BGFX_SAMPLER_U_CLAMP | BGFX_SAMPLER_V_CLAMP | BGFX_SAMPLER_POINT);

    // Generate text texture
    bgfx::setTexture(2, m_texUniform, m_atlasTex);

    // Rendering
    bgfx::setState(BGFX_STATE_BLEND_ALPHA | BGFX_STATE_WRITE_RGB | BGFX_STATE_WRITE_A);
    bgfx::submit(0, ShaderProgram->Use());

    glfwPostEmptyEvent();
}
