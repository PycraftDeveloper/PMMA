#pragma once

#include <vector>
#include <variant>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <cstring>

#include <glm/glm.hpp>
#include <FlatHashMap/flat_hash_map.hpp>
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

#include "Constants.hpp"

class CPP_RadialPolygonShape;
class CPP_RectangleShape;
class CPP_PixelShape;
class CPP_LineShape;
class CPP_ArcShape;
class CPP_EllipseShape;
class CPP_PolygonShape;

#pragma pack(push, 1)
struct Vertex {
    float x, y;      // position
    float s;      // texcoord (s = shape index as float, t unused)
};
#pragma pack(pop)

class CPP_Shape2D_RenderPipelineManager {
    public:
        std::vector<Vertex> combined_vertexes;
        std::vector<uint32_t> combined_indices;
        std::vector<uint8_t> shape_colors;

        std::vector<std::pair<uint64_t, unsigned int>> PreviousRenderContent;
        unsigned int InsertionIndex = 0;

        unsigned int ColorsInserted = 0;
        unsigned int ColorIndexesChanged = 0;
        unsigned int m_vertexCount = 0;
        unsigned int m_indexCount = 0;

        ska::flat_hash_map<uint64_t, float> ColorSlotID; // objectColorSlot
        ska::flat_hash_set<uint64_t> SeenThisFrame;
        std::vector<size_t> FreeSlots;

        bgfx::VertexLayout m_layout;
        bgfx::DynamicVertexBufferHandle m_vbh;
        bgfx::DynamicIndexBufferHandle  m_ibh;
        bgfx::TextureHandle m_tex;
        bgfx::UniformHandle s_colorTex;
        bgfx::UniformHandle u_colorInfo;
        uint32_t m_colorTextureWidth = 0;
        uint32_t m_colorTextureHeight = 0;

        unsigned int LiveVertexCount = 0;
        unsigned int LiveIndexCount = 0;
        unsigned int LiveColorCount = 0;

        bool VertexDataChanged = true;
        bool ColorDataChanged = true;
        bool UsingComplexColorInsertion = false;
        bool ChangedColorModes = true;
        bool PreviousFrameDataValid = false;

        CPP_Shape2D_RenderPipelineManager();
        ~CPP_Shape2D_RenderPipelineManager();

        template<typename T>
        inline void AddRenderTarget(T* shape, bool ColorIndexChanged)
        {
            if (ColorIndexChanged) {
                ++ColorIndexesChanged;
            }
            ++ColorsInserted;

            InternalAddRenderTarget(shape);
        }

        inline void Reset() {
            VertexDataChanged = false;
            ColorDataChanged = false;
            PreviousFrameDataValid = true;
            LiveVertexCount = 0;
            LiveColorCount = 0;

            InsertionIndex = 0;

            if (UsingComplexColorInsertion) {
                std::vector<unsigned int> RecycleList;

                for (const auto& [shapeID, slot] : ColorSlotID) {
                    if (SeenThisFrame.find(shapeID) == SeenThisFrame.end()) {
                        FreeSlots.push_back(slot);
                        RecycleList.push_back(shapeID);
                    }
                }

                // Batch erase after iteration
                for (unsigned int shapeID : RecycleList) {
                    ColorSlotID.erase(shapeID);
                }
                RecycleList.clear();

                unsigned int SeenThisFrameSize = (unsigned int)SeenThisFrame.size();
                SeenThisFrame.clear();
                SeenThisFrame.reserve(SeenThisFrameSize + 25);
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
                ColorSlotID.clear();
                FreeSlots.clear();
                shape_colors.clear();
            }

            if (UsingComplexColorInsertion != PreviouslyUsingComplexColorInsertion) {
                ChangedColorModes = true;
            } else {
                ChangedColorModes = false;
            }
        }

        void InternalRender();

        inline float GetColorIndex(uint8_t* Color, uint64_t ShapeID) {
            if (!UsingComplexColorInsertion) {
                // fast path: append (or overwrite if capacity exists) and return next index
                size_t needBytes = (size_t)LiveColorCount + 4;

                if (shape_colors.size() < needBytes) {
                    // ensure there's space for the 4 bytes we will write
                    shape_colors.resize(needBytes);
                }

                // write the 4 color bytes
                shape_colors[LiveColorCount]     = Color[0];
                shape_colors[LiveColorCount + 1] = Color[1];
                shape_colors[LiveColorCount + 2] = Color[2];
                shape_colors[LiveColorCount + 3] = Color[3];

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
                if (shape_colors.size() < offset + 4) {
                    shape_colors.resize(offset + 4);
                }

                shape_colors[offset]     = Color[0];
                shape_colors[offset + 1] = Color[1];
                shape_colors[offset + 2] = Color[2];
                shape_colors[offset + 3] = Color[3];

                LiveColorCount += 4;
                return static_cast<float>(slotIndex);
            }

            // not seen before: reuse a free slot if available
            if (!FreeSlots.empty()) {
                unsigned int newSlot = FreeSlots.back();
                FreeSlots.pop_back();

                size_t offset = static_cast<size_t>(newSlot) * 4;
                if (shape_colors.size() < offset + 4) {
                    // pad vector so the slot exists (could be reusing a previously freed high index)
                    shape_colors.resize(offset + 4);
                }

                shape_colors[offset]     = Color[0];
                shape_colors[offset + 1] = Color[1];
                shape_colors[offset + 2] = Color[2];
                shape_colors[offset + 3] = Color[3];

                ColorSlotID[ShapeID] = newSlot;

                LiveColorCount += 4;
                return static_cast<float>(newSlot);
            }

            // no free slots: append at the end
            size_t needBytes = (size_t)LiveColorCount + 4;
            if (shape_colors.size() < needBytes) {
                shape_colors.resize(needBytes);
            }

            shape_colors[LiveColorCount]     = Color[0];
            shape_colors[LiveColorCount + 1] = Color[1];
            shape_colors[LiveColorCount + 2] = Color[2];
            shape_colors[LiveColorCount + 3] = Color[3];

            unsigned int slotIndex = static_cast<unsigned int>(LiveColorCount / 4);
            ColorSlotID[ShapeID] = slotIndex;

            LiveColorCount += 4;
            return static_cast<float>(slotIndex);
        }

        template<typename T>
        inline void InternalAddRenderTarget(T* TargetPtr)
        {
            const bool shapeVertexDataChanged = TargetPtr->VertexDataChanged;
            VertexDataChanged |= shapeVertexDataChanged;
            ColorDataChanged  |= TargetPtr->ColorDataChanged;

            const size_t currentIndex = InsertionIndex;

            const auto& shapeVertices = TargetPtr->Shape2D_RenderPipelineData;
            const auto& shapeIndices  = TargetPtr->Shape2D_RenderPipelineIndices;

            const uint32_t vertexCount = static_cast<uint32_t>(shapeVertices.size());
            const uint32_t indexCount  = static_cast<uint32_t>(shapeIndices.size());

            // ---------- FAST PATH (UNCHANGED SHAPE) ----------
            if (currentIndex < PreviousRenderContent.size())
            {
                const auto& [existingID, existingVertexOffset] = PreviousRenderContent[currentIndex];

                if (TargetPtr->ID == existingID &&
                    !shapeVertexDataChanged &&
                    PreviousFrameDataValid)
                {
                    // Just advance live counters
                    LiveVertexCount += vertexCount;
                    LiveIndexCount  += indexCount;
                    ++InsertionIndex;
                    return;
                }
            }

            // ---------- ENSURE CAPACITY ----------
            const uint32_t baseVertex = LiveVertexCount;

            if (combined_vertexes.size() < baseVertex + vertexCount)
                combined_vertexes.resize(baseVertex + vertexCount);

            if (combined_indices.size() < LiveIndexCount + indexCount)
                combined_indices.resize(LiveIndexCount + indexCount);

            // ---------- COPY VERTICES ----------
            std::memcpy(
                combined_vertexes.data() + baseVertex,
                shapeVertices.data(),
                vertexCount * sizeof(Vertex)
            );

            // ---------- COPY & OFFSET INDICES ----------
            uint32_t* dst = combined_indices.data() + LiveIndexCount;
            for (uint32_t i = 0; i < indexCount; ++i)
                dst[i] = baseVertex + shapeIndices[i];

            // ---------- UPDATE PREVIOUS CONTENT ----------
            if (currentIndex < PreviousRenderContent.size())
            {
                PreviousRenderContent[currentIndex] =
                {
                    TargetPtr->ID,
                    baseVertex
                };
            }
            else
            {
                PreviousRenderContent.emplace_back(
                    TargetPtr->ID,
                    baseVertex
                );
            }

            // ---------- ADVANCE COUNTERS ----------
            LiveVertexCount += vertexCount;
            LiveIndexCount  += indexCount;
            ++InsertionIndex;
        }
};