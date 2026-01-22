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
        std::vector<uint8_t> shape_colors;

        std::vector<std::pair<uint64_t, unsigned int>> PreviousRenderContent;
        unsigned int InsertionIndex = 0;

        unsigned int ColorsInserted = 0;
        unsigned int ColorIndexesChanged = 0;
        unsigned int m_vertexCount = 0;

        ska::flat_hash_map<uint64_t, float> ColorSlotID; // needs to be float for bgfx shader access
        ska::flat_hash_set<uint64_t> SeenThisFrame;
        std::vector<float> FreeSlots;

        bgfx::VertexLayout m_layout;
        bgfx::DynamicVertexBufferHandle m_vbh;
        bgfx::TextureHandle m_tex;
        bgfx::UniformHandle s_colorTex;
        bgfx::UniformHandle u_colorInfo;
        uint32_t m_colorTextureWidth = 0;
        uint32_t m_colorTextureHeight = 0;

        unsigned int LiveVertexCount = 0;
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
                std::vector<uint64_t> RecycleList;

                for (const auto& [shapeID, slot] : ColorSlotID) {
                    if (SeenThisFrame.find(shapeID) == SeenThisFrame.end()) {
                        FreeSlots.push_back(static_cast<float>(slot));
                        RecycleList.push_back(shapeID);
                    }
                }

                // Batch erase after iteration
                for (uint64_t shapeID : RecycleList) {
                    ColorSlotID.erase(shapeID);
                }
                RecycleList.clear();

                size_t SeenThisFrameSize = SeenThisFrame.size();
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
                float slotIndex = found->second;
                size_t offset = static_cast<size_t>(slotIndex) * 4;
                if (shape_colors.size() < offset + 4) {
                    shape_colors.resize(offset + 4);
                }

                shape_colors[offset]     = Color[0];
                shape_colors[offset + 1] = Color[1];
                shape_colors[offset + 2] = Color[2];
                shape_colors[offset + 3] = Color[3];

                LiveColorCount += 4;
                return slotIndex;
            }

            // not seen before: reuse a free slot if available
            if (!FreeSlots.empty()) {
                float newSlot = FreeSlots.back();
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

            float slotIndex = static_cast<float>(LiveColorCount / 4);
            ColorSlotID[ShapeID] = slotIndex;

            LiveColorCount += 4;
            return slotIndex;
        }

        template<typename T>
        inline void InternalAddRenderTarget(T* TargetPtr) {
            const bool ShapeVertexDataChanged = TargetPtr->VertexDataChanged;
            VertexDataChanged |= ShapeVertexDataChanged;
            ColorDataChanged |= TargetPtr->ColorDataChanged;

            const size_t currentIndex = InsertionIndex;
            size_t insertPos = LiveVertexCount; // default append

            // Pointers to combined_vertexes for maximum speed
            Vertex* base = combined_vertexes.data();
            Vertex* writePtr = base + LiveVertexCount;

            const auto& vertices = TargetPtr->Shape2D_RenderPipelineData;
            const size_t verticesCount = vertices.size();

            // FAST-PATH: shape unchanged, previous data valid → skip rewrite
            if (currentIndex < PreviousRenderContent.size()) {
                const auto& [existingID, existingOffset] = PreviousRenderContent[currentIndex];
                if (TargetPtr->ID == existingID && !ShapeVertexDataChanged && PreviousFrameDataValid) {

                    if (currentIndex > 0 && verticesCount >= 2 && LiveVertexCount > 0) {
                        // Ensure enough capacity
                        if (LiveVertexCount + 2 > combined_vertexes.size()) {
                            combined_vertexes.resize(LiveVertexCount + 2);
                            base = combined_vertexes.data();
                            writePtr = base + LiveVertexCount;
                        }

                        // Degenerate join
                        *writePtr++ = *(writePtr - 1); // repeat last vertex
                        *writePtr++ = vertices[0];     // first vertex of this shape
                    }

                    InsertionIndex++;
                    LiveVertexCount = static_cast<unsigned int>(existingOffset + verticesCount);
                    return;
                }
            }

            // Ensure enough capacity for degenerate joins + new vertices
            size_t requiredSize = LiveVertexCount + ((currentIndex > 0 && verticesCount >= 2 && LiveVertexCount > 0) ? 2 : 0) + verticesCount;
            if (combined_vertexes.size() < requiredSize) {
                combined_vertexes.resize(requiredSize);
                base = combined_vertexes.data();
                writePtr = base + LiveVertexCount;
            }

            // Degenerate join if needed
            if (currentIndex > 0 && verticesCount >= 2 && LiveVertexCount > 0) {
                *writePtr++ = *(writePtr - 1);
                *writePtr++ = vertices[0];
            }

            // Copy new vertices in bulk
            std::memcpy(writePtr, vertices.data(), verticesCount * sizeof(Vertex));
            writePtr += verticesCount;

            const size_t shapeStartIndex = insertPos;

            // Update PreviousRenderContent
            if (currentIndex < PreviousRenderContent.size()) {
                PreviousRenderContent[currentIndex] = { TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex) };
            } else {
                PreviousRenderContent.emplace_back(TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex));
            }

            InsertionIndex++;
            LiveVertexCount = static_cast<unsigned int>(writePtr - base);
        }
};