#pragma once

#include <vector>

#include <glm/glm.hpp>

#include "Internal/Utility/FontUtils.hpp"

class CPP_TextRenderer;
class CPP_Shader;

typedef struct FT_LibraryRec_ *FT_Library;
typedef struct FT_FaceRec_ *FT_Face;
typedef struct FT_GlyphSlotRec_ *FT_GlyphSlot;

class CPP_TextRenderPipelineManager {
    public:
        CPP_Shader* ShaderProgram = nullptr;

        // BGFX
        bgfx::TextureHandle m_atlasTex = BGFX_INVALID_HANDLE;
        bgfx::TextureHandle m_fg_color_tex = BGFX_INVALID_HANDLE;
        bgfx::TextureHandle m_bg_color_tex = BGFX_INVALID_HANDLE;
        bgfx::VertexLayout  m_layout;
        bgfx::UniformHandle m_texUniform = BGFX_INVALID_HANDLE;
        bgfx::UniformHandle m_fgColUniform = BGFX_INVALID_HANDLE;
        bgfx::UniformHandle m_bgColUniform = BGFX_INVALID_HANDLE;
        uint32_t m_colorTextureWidth = 0;
        uint32_t m_colorTextureHeight = 0;

        // Font
        FT_Library m_ft = nullptr;
        FT_Face    m_face = nullptr;
        int        m_fontSize = 0;

        // Atlas
        uint16_t m_maxAtlasDim = 2048; // Settable, can also be queried from BGFX caps if desired
        uint16_t m_atlasW = 512, m_atlasH = 512, m_nextX = 0, m_nextY = 0, m_rowH = 0;
        std::vector<uint8_t> m_atlasData;
        std::unordered_map<char32_t, GlyphInfo> m_glyphs;
        bgfx::UniformHandle u_colorInfo;

        // For partial updates
        struct AtlasDirtyRect { uint16_t x, y, w, h; };
        std::vector<AtlasDirtyRect> m_dirtyRects;

        void ResetAtlas();
        void AddGlyphToAtlas(char32_t codepoint, FT_GlyphSlot slot);
        void FlushDirtyRects();
        void GrowAtlasAndRepack(uint16_t requiredW, uint16_t requiredH, char32_t newCodepoint, FT_GlyphSlot slot);
        void EnsureGlyph(char32_t codepoint);
        void UpdateAtlasTexture();

        bool UsingComplexColorInsertion = false;
        bool ChangedColorModes = true;

        ska::flat_hash_map<uint64_t, float> ColorSlotID; // objectColorSlot
        ska::flat_hash_set<uint64_t> SeenThisFrame;
        std::vector<size_t> FreeSlots;
        std::vector<CharacterData> CharacterRenderData;

        bgfx::VertexBufferHandle vbh = BGFX_INVALID_HANDLE;

        unsigned int ColorsInserted = 0;
        unsigned int ColorIndexesChanged = 0;

        std::vector<uint8_t> ForegroundColors;
        std::vector<uint8_t> BackgroundColors;

        unsigned int LiveColorCount = 0;

        std::string FontPath;
        unsigned int PixelHeight;

        CPP_TextRenderPipelineManager();
        ~CPP_TextRenderPipelineManager();

        void DelayedSetup(std::string path, unsigned int pixelHeight);

        void InternalRender();

        void AddRenderTarget(CPP_TextRenderer* NewObject);

        void Reset();

        inline float GetColorIndex(uint8_t* ForegroundColor, uint8_t* BackgroundColor, uint64_t ShapeID) {
            if (!UsingComplexColorInsertion) {
                // fast path: append (or overwrite if capacity exists) and return next index
                size_t needBytes = (size_t)LiveColorCount + 4;

                if (ForegroundColors.size() < needBytes) {
                    // ensure there's space for the 4 bytes we will write
                    ForegroundColors.resize(needBytes);
                    BackgroundColors.resize(needBytes);
                }

                // write the 4 color bytes
                ForegroundColors[LiveColorCount]     = ForegroundColor[0];
                ForegroundColors[LiveColorCount + 1] = ForegroundColor[1];
                ForegroundColors[LiveColorCount + 2] = ForegroundColor[2];
                ForegroundColors[LiveColorCount + 3] = ForegroundColor[3];

                BackgroundColors[LiveColorCount]     = BackgroundColor[0];
                BackgroundColors[LiveColorCount + 1] = BackgroundColor[1];
                BackgroundColors[LiveColorCount + 2] = BackgroundColor[2];
                BackgroundColors[LiveColorCount + 3] = BackgroundColor[3];

                // compute slot index (slot is number of color entries before this write)
                unsigned int slotIndex = static_cast<unsigned int>(LiveColorCount / 4);

                LiveColorCount += 4;

                return static_cast<float>(slotIndex);
            }

            // --- Complex insertion path: try to preserve indexes ---
            SeenThisFrame.insert(ShapeID);

            auto found = ColorSlotID.find(ShapeID);
            if (found != ColorSlotID.end()) {
                // already have a slot for this shape: overwrite it
                unsigned int slotIndex = found->second;
                size_t offset = static_cast<size_t>(slotIndex) * 4;
                if (ForegroundColors.size() < offset + 4) {
                    ForegroundColors.resize(offset + 4);
                    BackgroundColors.resize(offset + 4);
                }

                ForegroundColors[offset]     = ForegroundColor[0];
                ForegroundColors[offset + 1] = ForegroundColor[1];
                ForegroundColors[offset + 2] = ForegroundColor[2];
                ForegroundColors[offset + 3] = ForegroundColor[3];

                BackgroundColors[offset]     = BackgroundColor[0];
                BackgroundColors[offset + 1] = BackgroundColor[1];
                BackgroundColors[offset + 2] = BackgroundColor[2];
                BackgroundColors[offset + 3] = BackgroundColor[3];

                LiveColorCount += 4;
                return static_cast<float>(slotIndex);
            }

            // not seen before: reuse a free slot if available
            if (!FreeSlots.empty()) {
                unsigned int newSlot = FreeSlots.back();
                FreeSlots.pop_back();

                size_t offset = static_cast<size_t>(newSlot) * 4;
                if (ForegroundColors.size() < offset + 4) {
                    // pad vector so the slot exists (could be reusing a previously freed high index)
                    ForegroundColors.resize(offset + 4);
                    BackgroundColors.resize(offset + 4);
                }

                ForegroundColors[offset]     = ForegroundColor[0];
                ForegroundColors[offset + 1] = ForegroundColor[1];
                ForegroundColors[offset + 2] = ForegroundColor[2];
                ForegroundColors[offset + 3] = ForegroundColor[3];

                BackgroundColors[offset]     = BackgroundColor[0];
                BackgroundColors[offset + 1] = BackgroundColor[1];
                BackgroundColors[offset + 2] = BackgroundColor[2];
                BackgroundColors[offset + 3] = BackgroundColor[3];

                ColorSlotID[ShapeID] = newSlot;

                LiveColorCount += 4;
                return static_cast<float>(newSlot);
            }

            // no free slots: append at the end
            size_t needBytes = (size_t)LiveColorCount + 4;
            if (ForegroundColors.size() < needBytes) {
                ForegroundColors.resize(needBytes);
                BackgroundColors.resize(needBytes);
            }

            ForegroundColors[LiveColorCount]     = ForegroundColor[0];
            ForegroundColors[LiveColorCount + 1] = ForegroundColor[1];
            ForegroundColors[LiveColorCount + 2] = ForegroundColor[2];
            ForegroundColors[LiveColorCount + 3] = ForegroundColor[3];

            BackgroundColors[LiveColorCount]     = BackgroundColor[0];
            BackgroundColors[LiveColorCount + 1] = BackgroundColor[1];
            BackgroundColors[LiveColorCount + 2] = BackgroundColor[2];
            BackgroundColors[LiveColorCount + 3] = BackgroundColor[3];

            unsigned int slotIndex = static_cast<unsigned int>(LiveColorCount / 4);
            ColorSlotID[ShapeID] = slotIndex;

            LiveColorCount += 4;
            return static_cast<float>(slotIndex);
        }
};