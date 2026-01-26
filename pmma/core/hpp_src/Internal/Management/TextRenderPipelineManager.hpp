#pragma once

#include <vector>

#include <glm/glm.hpp>

#include "Internal/Utility/FontUtils.hpp"
#include "Random.hpp"

class CPP_TextRenderer;
class CPP_Shader;

typedef struct FT_LibraryRec_ *FT_Library;
typedef struct FT_FaceRec_ *FT_Face;
typedef struct FT_GlyphSlotRec_ *FT_GlyphSlot;

struct TextFormatting {
    float DefaultForegroundColorIndex = 0.0f;
    float ForegroundColorIndex = 0.0f;

    float DefaultBackgroundColorIndex = 0.0f;
    float BackgroundColorIndex = 0.0f;

    bool RandomizeText = false;

    TextFormatting(float default_foreground_color_index, float default_background_color_index) {
        DefaultForegroundColorIndex = default_foreground_color_index;
        ForegroundColorIndex = DefaultForegroundColorIndex;

        DefaultBackgroundColorIndex = default_background_color_index;
        BackgroundColorIndex = DefaultBackgroundColorIndex;
    }

    void Reset() {
        RandomizeText = false;
    }
};

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
        uint32_t m_ForegroundColorTextureWidth = 0;
        uint32_t m_ForegroundColorTextureHeight = 0;
        uint32_t m_BackgroundColorTextureWidth = 0;
        uint32_t m_BackgroundColorTextureHeight = 0;

        // Font
        FT_Library m_ft = nullptr;
        FT_Face    m_face = nullptr;
        int        m_fontSize = 0;

        // Atlas
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

        bool UsingComplexForegroundColorInsertion = false;
        bool UsingComplexBackgroundColorInsertion = false;
        bool ChangedForegroundColorModes = true;
        bool ChangedBackgroundColorModes = true;

        ska::flat_hash_map<uint64_t, float> ForegroundColorSlotID; // objectColorSlot
        ska::flat_hash_map<uint64_t, float> BackgroundColorSlotID; // objectColorSlot
        ska::flat_hash_set<uint64_t> ForegroundColorsSeenThisFrame;
        ska::flat_hash_set<uint64_t> BackgroundColorsSeenThisFrame;
        std::vector<size_t> ForegroundColorFreeSlots;
        std::vector<size_t> BackgroundColorFreeSlots;
        std::vector<CharacterData> CharacterRenderData;

        CPP_FastRandom* RandomCharacterGenerator = nullptr;

        bgfx::VertexBufferHandle vbh = BGFX_INVALID_HANDLE;

        unsigned int ForegroundColorsInserted = 0;
        unsigned int ForegroundColorIndexesChanged = 0;

        unsigned int BackgroundColorsInserted = 0;
        unsigned int BackgroundColorIndexesChanged = 0;

        std::vector<uint8_t> ForegroundColors;
        std::vector<uint8_t> BackgroundColors;

        unsigned int LiveForegroundColorCount = 0;
        unsigned int LiveBackgroundColorCount = 0;

        std::string FontPath;
        unsigned int PixelHeight;

        CPP_TextRenderPipelineManager();
        ~CPP_TextRenderPipelineManager();

        void DelayedSetup(std::string path, unsigned int pixelHeight);

        void InternalRender();

        void AddRenderTarget(CPP_TextRenderer* NewObject);

        void Reset();

        inline char GenerateRandomPrintableCharacter() {
            static const std::string chars =
                "0123456789"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "abcdefghijklmnopqrstuvwxyz"
                "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ";

            if (RandomCharacterGenerator == nullptr) {
                RandomCharacterGenerator = new CPP_FastRandom();
            }

            uint32_t index = RandomCharacterGenerator->Next(static_cast<uint32_t>(chars.size() - 1));

            char literal = chars[index];

            EnsureGlyph(literal);

            return literal;
        }

        inline float GetForegroundColorIndex(uint8_t* ForegroundColor, uint64_t ShapeID) {
            if (!UsingComplexForegroundColorInsertion) {
                // fast path: append (or overwrite if capacity exists) and return next index
                size_t needBytes = (size_t)LiveForegroundColorCount + 4;

                if (ForegroundColors.size() < needBytes) {
                    // ensure there's space for the 4 bytes we will write
                    ForegroundColors.resize(needBytes);
                }

                // write the 4 color bytes
                ForegroundColors[LiveForegroundColorCount]     = ForegroundColor[0];
                ForegroundColors[LiveForegroundColorCount + 1] = ForegroundColor[1];
                ForegroundColors[LiveForegroundColorCount + 2] = ForegroundColor[2];
                ForegroundColors[LiveForegroundColorCount + 3] = ForegroundColor[3];

                // compute slot index (slot is number of color entries before this write)
                unsigned int slotIndex = static_cast<unsigned int>(LiveForegroundColorCount / 4);

                LiveForegroundColorCount += 4;

                return static_cast<float>(slotIndex);
            }

            // --- Complex insertion path: try to preserve indexes ---
            ForegroundColorsSeenThisFrame.insert(ShapeID);

            auto found = ForegroundColorSlotID.find(ShapeID);
            if (found != ForegroundColorSlotID.end()) {
                // already have a slot for this shape: overwrite it
                unsigned int slotIndex = found->second;
                size_t offset = static_cast<size_t>(slotIndex) * 4;
                if (ForegroundColors.size() < offset + 4) {
                    ForegroundColors.resize(offset + 4);
                }

                ForegroundColors[offset]     = ForegroundColor[0];
                ForegroundColors[offset + 1] = ForegroundColor[1];
                ForegroundColors[offset + 2] = ForegroundColor[2];
                ForegroundColors[offset + 3] = ForegroundColor[3];

                LiveForegroundColorCount += 4;
                return static_cast<float>(slotIndex);
            }

            // not seen before: reuse a free slot if available
            if (!ForegroundColorFreeSlots.empty()) {
                unsigned int newSlot = ForegroundColorFreeSlots.back();
                ForegroundColorFreeSlots.pop_back();

                size_t offset = static_cast<size_t>(newSlot) * 4;
                if (ForegroundColors.size() < offset + 4) {
                    // pad vector so the slot exists (could be reusing a previously freed high index)
                    ForegroundColors.resize(offset + 4);
                }

                ForegroundColors[offset]     = ForegroundColor[0];
                ForegroundColors[offset + 1] = ForegroundColor[1];
                ForegroundColors[offset + 2] = ForegroundColor[2];
                ForegroundColors[offset + 3] = ForegroundColor[3];

                ForegroundColorSlotID[ShapeID] = newSlot;

                LiveForegroundColorCount += 4;
                return static_cast<float>(newSlot);
            }

            // no free slots: append at the end
            size_t needBytes = (size_t)LiveForegroundColorCount + 4;
            if (ForegroundColors.size() < needBytes) {
                ForegroundColors.resize(needBytes);
            }

            ForegroundColors[LiveForegroundColorCount]     = ForegroundColor[0];
            ForegroundColors[LiveForegroundColorCount + 1] = ForegroundColor[1];
            ForegroundColors[LiveForegroundColorCount + 2] = ForegroundColor[2];
            ForegroundColors[LiveForegroundColorCount + 3] = ForegroundColor[3];

            unsigned int slotIndex = static_cast<unsigned int>(LiveForegroundColorCount / 4);
            ForegroundColorSlotID[ShapeID] = slotIndex;

            LiveForegroundColorCount += 4;
            return static_cast<float>(slotIndex);
        }

        inline float GetBackgroundColorIndex(uint8_t* BackgroundColor, uint64_t ShapeID) {
            if (!UsingComplexBackgroundColorInsertion) {
                // fast path: append (or overwrite if capacity exists) and return next index
                size_t needBytes = (size_t)LiveBackgroundColorCount + 4;

                if (BackgroundColors.size() < needBytes) {
                    // ensure there's space for the 4 bytes we will write
                    BackgroundColors.resize(needBytes);
                }

                // write the 4 color bytes
                BackgroundColors[LiveBackgroundColorCount]     = BackgroundColor[0];
                BackgroundColors[LiveBackgroundColorCount + 1] = BackgroundColor[1];
                BackgroundColors[LiveBackgroundColorCount + 2] = BackgroundColor[2];
                BackgroundColors[LiveBackgroundColorCount + 3] = BackgroundColor[3];

                // compute slot index (slot is number of color entries before this write)
                unsigned int slotIndex = static_cast<unsigned int>(LiveBackgroundColorCount / 4);

                LiveBackgroundColorCount += 4;

                return static_cast<float>(slotIndex);
            }

            // --- Complex insertion path: try to preserve indexes ---
            BackgroundColorsSeenThisFrame.insert(ShapeID);

            auto found = BackgroundColorSlotID.find(ShapeID);
            if (found != BackgroundColorSlotID.end()) {
                // already have a slot for this shape: overwrite it
                unsigned int slotIndex = found->second;
                size_t offset = static_cast<size_t>(slotIndex) * 4;
                if (BackgroundColors.size() < offset + 4) {
                    BackgroundColors.resize(offset + 4);
                }

                BackgroundColors[offset]     = BackgroundColor[0];
                BackgroundColors[offset + 1] = BackgroundColor[1];
                BackgroundColors[offset + 2] = BackgroundColor[2];
                BackgroundColors[offset + 3] = BackgroundColor[3];

                LiveBackgroundColorCount += 4;
                return static_cast<float>(slotIndex);
            }

            // not seen before: reuse a free slot if available
            if (!BackgroundColorFreeSlots.empty()) {
                unsigned int newSlot = BackgroundColorFreeSlots.back();
                BackgroundColorFreeSlots.pop_back();

                size_t offset = static_cast<size_t>(newSlot) * 4;
                if (BackgroundColors.size() < offset + 4) {
                    // pad vector so the slot exists (could be reusing a previously freed high index)
                    BackgroundColors.resize(offset + 4);
                }

                BackgroundColors[offset]     = BackgroundColor[0];
                BackgroundColors[offset + 1] = BackgroundColor[1];
                BackgroundColors[offset + 2] = BackgroundColor[2];
                BackgroundColors[offset + 3] = BackgroundColor[3];

                BackgroundColorSlotID[ShapeID] = newSlot;

                LiveBackgroundColorCount += 4;
                return static_cast<float>(newSlot);
            }

            // no free slots: append at the end
            size_t needBytes = (size_t)LiveBackgroundColorCount + 4;
            if (BackgroundColors.size() < needBytes) {
                BackgroundColors.resize(needBytes);
            }

            BackgroundColors[LiveBackgroundColorCount]     = BackgroundColor[0];
            BackgroundColors[LiveBackgroundColorCount + 1] = BackgroundColor[1];
            BackgroundColors[LiveBackgroundColorCount + 2] = BackgroundColor[2];
            BackgroundColors[LiveBackgroundColorCount + 3] = BackgroundColor[3];

            unsigned int slotIndex = static_cast<unsigned int>(LiveBackgroundColorCount / 4);
            BackgroundColorSlotID[ShapeID] = slotIndex;

            LiveBackgroundColorCount += 4;
            return static_cast<float>(slotIndex);
        }
};