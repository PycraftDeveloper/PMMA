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

using Shape2D_RenderObject = std::variant<
    CPP_RadialPolygonShape*,
    CPP_RectangleShape*,
    CPP_PixelShape*,
    CPP_LineShape*,
    CPP_PolygonShape*,
    CPP_EllipseShape*,
    CPP_ArcShape*>;

struct Vertex {
    float x, y;      // position
    float s; float t = 0.f;      // texcoord (s = shape index as float, t unused)
};

class CPP_Shape2D_RenderPipelineManager {
    public:
        std::vector<Shape2D_RenderObject> RenderPipelineComponents;
        std::vector<Vertex> combined_vertexes;
        std::vector<uint8_t> shape_colors;

        std::vector<std::pair<uint64_t, unsigned int>> PreviousRenderContent;
        unsigned int InsertionIndex = 0;

        unsigned int ColorsInserted = 0;
        unsigned int ColorIndexesChanged = 0;
        unsigned int m_vertexCount = 0;

        ska::flat_hash_map<unsigned int, GLuint> ColorSlotID; // objectColorSlot
        ska::flat_hash_set<unsigned int> SeenThisFrame;
        std::vector<GLuint> FreeSlots;

        bgfx::VertexLayout m_layout;
        bgfx::DynamicVertexBufferHandle m_vbh;
        bgfx::TextureHandle m_tex;
        bgfx::UniformHandle s_colorTex;
        bgfx::UniformHandle u_colorInfo;
        uint32_t m_colorTextureWidth = 0;
        uint32_t m_colorTextureHeight = 0;

        unsigned int PaddingStartPosition = 0;
        unsigned int LiveVertexCount = 0;

        bool VertexDataChanged = true;
        bool ColorDataChanged = true;
        bool UsingComplexColorInsertion = false;
        bool ChangedColorModes = true;
        bool PreviousFrameDataValid = false;

        CPP_Shape2D_RenderPipelineManager();
        ~CPP_Shape2D_RenderPipelineManager();

        inline void AddRenderTarget(const Shape2D_RenderObject& NewObject, bool ColorIndexChanged) {
            if (ColorIndexChanged) {
                ColorIndexesChanged++;
            }
            ColorsInserted++;

            if (auto actualPtr = std::get_if<CPP_RadialPolygonShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            } else if (auto actualPtr = std::get_if<CPP_RectangleShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            } else if (auto actualPtr = std::get_if<CPP_PixelShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            } else if (auto actualPtr = std::get_if<CPP_LineShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            } else if (auto actualPtr = std::get_if<CPP_PolygonShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            } else if (auto actualPtr = std::get_if<CPP_ArcShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            } else if (auto actualPtr = std::get_if<CPP_EllipseShape*>(&NewObject)) {
                InternalAddRenderTarget(*actualPtr);
            }
        }

        inline void Reset() {
            VertexDataChanged = false;
            ColorDataChanged = false;
            PreviousFrameDataValid = true;
            LiveVertexCount = 0;

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
            } else {
                unsigned int size = (unsigned int)shape_colors.size();
                shape_colors.clear();
                shape_colors.reserve(size + 25);
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

        inline float GetColorIndex(uint8_t* Color, unsigned int ShapeID) {
            if (!UsingComplexColorInsertion) {
                size_t size_of_shape_colors = (size_t)shape_colors.size();

                float index = (float)size_of_shape_colors;

                shape_colors.insert(shape_colors.end(), Color, Color + 4);
                return index / 4.0f;
            }

            SeenThisFrame.insert(ShapeID);

            auto found = ColorSlotID.find(ShapeID);
            if (found != ColorSlotID.end()) {
                GLuint slot = found->second;
                size_t offset = slot * 4;

                if (shape_colors[offset + 0] != Color[0] ||
                    shape_colors[offset + 1] != Color[1] ||
                    shape_colors[offset + 2] != Color[2] ||
                    shape_colors[offset + 3] != Color[3])
                {
                    shape_colors[offset + 0] = Color[0];
                    shape_colors[offset + 1] = Color[1];
                    shape_colors[offset + 2] = Color[2];
                    shape_colors[offset + 3] = Color[3];
                }

                ColorIndexesChanged++;
                return (float)(slot);
            }

            GLuint newSlot;
            if (!FreeSlots.empty()) {
                newSlot = FreeSlots.back();
                FreeSlots.pop_back();
                size_t offset = newSlot * 4;

                // Overwrite existing slot (whether real or padded)
                shape_colors[offset + 0] = Color[0];
                shape_colors[offset + 1] = Color[1];
                shape_colors[offset + 2] = Color[2];
                shape_colors[offset + 3] = Color[3];

                ColorSlotID[ShapeID] = newSlot;

                ColorIndexesChanged++;
                return (float)(newSlot);
            } else {
                size_t offset = shape_colors.size();

                if (offset < PaddingStartPosition) {
                    shape_colors.insert(shape_colors.end(), Color, Color + 4);
                } else {
                    // We're inside padded region—overwrite instead
                    shape_colors[offset + 0] = Color[0];
                    shape_colors[offset + 1] = Color[1];
                    shape_colors[offset + 2] = Color[2];
                    shape_colors[offset + 3] = Color[3];

                    PaddingStartPosition = (unsigned int)offset + 4;
                }

                ColorSlotID[ShapeID] = newSlot;
                return (float)(offset);
            }
        }

        template<typename T>
        inline void InternalAddRenderTarget(T* TargetPtr) {
            const bool ShapeVertexDataChanged = TargetPtr->VertexDataChanged;
            VertexDataChanged |= ShapeVertexDataChanged;
            ColorDataChanged |= TargetPtr->ColorDataChanged;

            const size_t currentIndex = InsertionIndex;
            size_t insertPos = LiveVertexCount; // default append

            // Fast-path: shape unchanged, previous data valid → skip rewrite
            if (currentIndex < PreviousRenderContent.size()) {
                const auto& [existingID, existingOffset] = PreviousRenderContent[currentIndex];
                if (TargetPtr->ID == existingID && !ShapeVertexDataChanged && PreviousFrameDataValid) {
                    InsertionIndex++;
                    LiveVertexCount = (unsigned int)(existingOffset + TargetPtr->Shape2D_RenderPipelineData.size());
                    return;
                }
            }

            const auto& vertices = TargetPtr->Shape2D_RenderPipelineData;

            // Ensure enough capacity — only grow, never shrink here
            if (combined_vertexes.size() < insertPos + vertices.size() + 2) {
                combined_vertexes.resize(insertPos + vertices.size() + 2);
            }

            size_t writePos = insertPos;

            // Optional: add degenerate join for continuity
            if (currentIndex > 0 && vertices.size() >= 2 && writePos > 0) {
                combined_vertexes[writePos++] = combined_vertexes[writePos - 1];
                combined_vertexes[writePos++] = vertices[0];
            }

            // Copy new vertices directly
            std::memcpy(
                combined_vertexes.data() + writePos,
                vertices.data(),
                vertices.size() * sizeof(Vertex)
            );

            const size_t shapeStartIndex = writePos;

            if (currentIndex < PreviousRenderContent.size()) {
                PreviousRenderContent[currentIndex] = { TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex) };
            } else {
                PreviousRenderContent.emplace_back(TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex));
            }

            InsertionIndex++;
            LiveVertexCount = (unsigned int)(writePos + vertices.size());
        }
};