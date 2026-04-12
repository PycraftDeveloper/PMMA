#pragma once

#include <cstring>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <variant>
#include <vector>

#include <FlatHashMap/flat_hash_map.hpp>
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>
#include <glm/glm.hpp>

#include "Constants.hpp"

struct Vertex {
    float x, y; // position
    float s;    // texcoord (s = shape index as float, t unused)
};

class CPP_Shape2D_RenderPipelineManager {
public:
    std::array<std::vector<Vertex>, 4> combined_vertexes;
    std::array<std::vector<uint8_t>, 4> shape_colors;

    std::array<std::vector<std::pair<uint64_t, unsigned int>>, 4> PreviousRenderContent;
    std::vector<std::pair<uint64_t, unsigned int>> NewRenderContent;

    unsigned int ColorsInserted = 0;
    unsigned int ColorIndexesChanged = 0;
    unsigned int m_vertexCount = 0;

    unsigned int NextReserveSize = 0;

    std::array<ska::flat_hash_map<uint64_t, float>, 4> ColorSlotID; // needs to be float for bgfx shader access
    std::array<ska::flat_hash_set<uint64_t>, 4> SeenThisFrame;
    std::array<std::vector<float>, 4> FreeSlots;

    bgfx::VertexLayout m_layout;
    bgfx::DynamicVertexBufferHandle m_vbh;
    bgfx::TextureHandle m_tex;
    bgfx::UniformHandle s_colorTex;
    bgfx::UniformHandle u_colorInfo;
    uint32_t m_colorTextureWidth = 0;
    uint32_t m_colorTextureHeight = 0;

    unsigned int LiveColorCount = 0;

    short int LiveBufferCount = 0;
    short int LiveColorBufferCount = 0;
    short int LivePreviousRenderContent = 0;

    bool VertexDataChanged = true;
    bool ColorDataChanged = true;
    bool UsingComplexColorInsertion = false;
    bool ChangedColorModes = true;

    CPP_Shape2D_RenderPipelineManager();
    ~CPP_Shape2D_RenderPipelineManager();

    inline void Reset() {
        VertexDataChanged = false;
        ColorDataChanged = false;
        LiveColorCount = 0;

        NextReserveSize = 0;

        PreviousRenderContent[LivePreviousRenderContent] = NewRenderContent;
        NewRenderContent.clear();

        LivePreviousRenderContent++;
        if (LivePreviousRenderContent > 3) {
            LivePreviousRenderContent = 0;
        }

        if (UsingComplexColorInsertion) {
            std::vector<uint64_t> RecycleList;

            for (const auto &[shapeID, slot] : ColorSlotID[LiveColorBufferCount]) {
                if (SeenThisFrame[LiveColorBufferCount].find(shapeID) == SeenThisFrame[LiveColorBufferCount].end()) {
                    FreeSlots[LiveColorBufferCount].push_back(static_cast<float>(slot));
                    RecycleList.push_back(shapeID);
                }
            }

            // Batch erase after iteration
            for (uint64_t shapeID : RecycleList) {
                ColorSlotID[LiveColorBufferCount].erase(shapeID);
            }
            RecycleList.clear();

            size_t SeenThisFrameSize = SeenThisFrame[LiveColorBufferCount].size();
            SeenThisFrame[LiveColorBufferCount].clear();
            SeenThisFrame[LiveColorBufferCount].reserve(SeenThisFrameSize + 25);
        }

        bool PreviouslyUsingComplexColorInsertion = UsingComplexColorInsertion;

        if (!ChangedColorModes && ColorsInserted > 0) {
            if (ColorIndexesChanged / ColorsInserted > 0.2f) {
                UsingComplexColorInsertion = true;
            } else {
                UsingComplexColorInsertion = false;
            }
        }

        ColorIndexesChanged = 0;
        ColorsInserted = 0;

        if (UsingComplexColorInsertion && !PreviouslyUsingComplexColorInsertion) {
            ColorSlotID[LiveColorBufferCount].clear();
            FreeSlots[LiveColorBufferCount].clear();
            shape_colors[LiveColorBufferCount].clear();
        }

        if (UsingComplexColorInsertion != PreviouslyUsingComplexColorInsertion) {
            ChangedColorModes = true;
        } else {
            ChangedColorModes = false;
        }
    }

    void InternalRender();

    inline float GetColorIndex(uint8_t *Color, uint64_t ShapeID) {
        if (!UsingComplexColorInsertion) {
            // fast path: append (or overwrite if capacity exists) and return next index
            size_t needBytes = (size_t)LiveColorCount + 4;

            if (shape_colors[LiveColorBufferCount].size() < needBytes) {
                // ensure there's space for the 4 bytes we will write
                shape_colors[LiveColorBufferCount].resize(needBytes);
            }

            // write the 4 color bytes
            shape_colors[LiveColorBufferCount][LiveColorCount] = Color[0];
            shape_colors[LiveColorBufferCount][LiveColorCount + 1] = Color[1];
            shape_colors[LiveColorBufferCount][LiveColorCount + 2] = Color[2];
            shape_colors[LiveColorBufferCount][LiveColorCount + 3] = Color[3];

            // compute slot index (slot is number of color entries before this write)
            unsigned int slotIndex = static_cast<unsigned int>(LiveColorCount / 4);

            LiveColorCount += 4;

            return static_cast<float>(slotIndex);
        }

        // --- Complex insertion path: try to preserve indexes ---
        SeenThisFrame[LiveColorBufferCount].insert(ShapeID);

        auto found = ColorSlotID[LiveColorBufferCount].find(ShapeID);
        if (found != ColorSlotID[LiveColorBufferCount].end()) {
            // already have a slot for this shape: overwrite it
            float slotIndex = found->second;
            size_t offset = static_cast<size_t>(slotIndex) * 4;
            if (shape_colors[LiveColorBufferCount].size() < offset + 4) {
                shape_colors[LiveColorBufferCount].resize(offset + 4);
            }

            shape_colors[LiveColorBufferCount][offset] = Color[0];
            shape_colors[LiveColorBufferCount][offset + 1] = Color[1];
            shape_colors[LiveColorBufferCount][offset + 2] = Color[2];
            shape_colors[LiveColorBufferCount][offset + 3] = Color[3];

            LiveColorCount += 4;
            return slotIndex;
        }

        // not seen before: reuse a free slot if available
        if (!FreeSlots[LiveColorBufferCount].empty()) {
            float newSlot = FreeSlots[LiveColorBufferCount].back();
            FreeSlots[LiveColorBufferCount].pop_back();

            size_t offset = static_cast<size_t>(newSlot) * 4;
            if (shape_colors[LiveColorBufferCount].size() < offset + 4) {
                // pad vector so the slot exists (could be reusing a previously freed high index)
                shape_colors[LiveColorBufferCount].resize(offset + 4);
            }

            shape_colors[LiveColorBufferCount][offset] = Color[0];
            shape_colors[LiveColorBufferCount][offset + 1] = Color[1];
            shape_colors[LiveColorBufferCount][offset + 2] = Color[2];
            shape_colors[LiveColorBufferCount][offset + 3] = Color[3];

            ColorSlotID[LiveColorBufferCount][ShapeID] = newSlot;

            LiveColorCount += 4;
            return static_cast<float>(newSlot);
        }

        // no free slots: append at the end
        size_t needBytes = (size_t)LiveColorCount + 4;
        if (shape_colors[LiveColorBufferCount].size() < needBytes) {
            shape_colors[LiveColorBufferCount].resize(needBytes);
        }

        shape_colors[LiveColorBufferCount][LiveColorCount] = Color[0];
        shape_colors[LiveColorBufferCount][LiveColorCount + 1] = Color[1];
        shape_colors[LiveColorBufferCount][LiveColorCount + 2] = Color[2];
        shape_colors[LiveColorBufferCount][LiveColorCount + 3] = Color[3];

        float slotIndex = static_cast<float>(LiveColorCount / 4);
        ColorSlotID[LiveColorBufferCount][ShapeID] = slotIndex;

        LiveColorCount += 4;
        return slotIndex;
    }
};