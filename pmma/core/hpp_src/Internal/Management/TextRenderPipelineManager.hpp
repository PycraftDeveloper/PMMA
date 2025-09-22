#pragma once

#include <vector>

#include <glm/glm.hpp>
#include <ft2build.h>
#include FT_FREETYPE_H

#include "Internal/Utility/FontUtils.hpp"

class CPP_TextRenderer;
class CPP_Shader;

class CPP_TextRendererPipelineManager {
    private:
        CPP_Shader* ShaderProgram = nullptr;

        // BGFX
        bgfx::TextureHandle m_atlasTex = BGFX_INVALID_HANDLE;
        bgfx::VertexLayout  m_layout;
        bgfx::UniformHandle m_texUniform = BGFX_INVALID_HANDLE;

        // Font
        FT_Library m_ft = nullptr;
        FT_Face    m_face = nullptr;
        int        m_fontSize = 0;

        // Atlas
        uint16_t m_maxAtlasDim = 2048; // Settable, can also be queried from BGFX caps if desired
        uint16_t m_atlasW = 512, m_atlasH = 512, m_nextX = 0, m_nextY = 0, m_rowH = 0;
        std::vector<uint8_t> m_atlasData;
        std::unordered_map<char32_t, GlyphInfo> m_glyphs;

        // For partial updates
        struct AtlasDirtyRect { uint16_t x, y, w, h; };
        std::vector<AtlasDirtyRect> m_dirtyRects;

        void ResetAtlas();
        void AddGlyphToAtlas(char32_t codepoint, FT_GlyphSlot slot);
        void FlushDirtyRects();
        void GrowAtlasAndRepack(uint16_t requiredW, uint16_t requiredH, char32_t newCodepoint, FT_GlyphSlot slot);
        void EnsureGlyph(char32_t codepoint);
        void UpdateAtlasTexture();

    public:
        std::string FontPath;
        unsigned int PixelHeight;

        CPP_TextRendererPipelineManager();
        ~CPP_TextRendererPipelineManager();

        TextInstance CreateText(const std::string& text, float x, float y, uint32_t color);

        void DelayedSetup(std::string path, unsigned int pixelHeight);

        void InternalRender(const std::vector<TextInstance>& texts);

        void AddRenderTarget(CPP_TextRenderer* NewObject);

        void Reset();
};