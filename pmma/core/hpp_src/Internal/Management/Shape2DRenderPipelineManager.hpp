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

class CPP_Shader;

using Shape2D_RenderObject = std::variant<
    CPP_RadialPolygonShape*,
    CPP_RectangleShape*,
    CPP_PixelShape*,
    CPP_LineShape*,
    CPP_PolygonShape*,
    CPP_EllipseShape*,
    CPP_ArcShape*>;

struct Vertex {
    glm::vec2 position;
    GLuint shape_id;
};

struct BgfxVertex {
    float x, y;      // position
    float s, t;      // texcoord (s = shape index as float, t unused)
};

class CPP_Shape2D_RenderPipelineManager {
    public:
        std::vector<Shape2D_RenderObject> RenderPipelineComponents;
        std::vector<Vertex> combined_vertexes;
        std::vector<glm::vec4> shape_colors;

        std::vector<std::pair<uint64_t, unsigned int>> PreviousRenderContent;
        unsigned int InsertionIndex = 0;

        unsigned int ColorsInserted = 0;
        unsigned int ColorIndexesChanged = 0;

        ska::flat_hash_map<unsigned int, GLuint> ColorSlotID; // objectColorSlot
        ska::flat_hash_set<unsigned int> SeenThisFrame;
        std::vector<GLuint> FreeSlots;

        bgfx::VertexLayout m_layout;
        bgfx::DynamicVertexBufferHandle m_vbh;
        bgfx::TextureHandle m_tex;
        bgfx::UniformHandle s_colorTex;
        bgfx::UniformHandle u_colorInfo;
        uint32_t m_colorTextureWidth = 0;

        bool Changed = true;
        bool HasAlpha = false;
        bool UsingComplexColorInsertion = false;
        bool ChangedColorModes = true;

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

            if (!ChangedColorModes) {
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

        inline GLuint GetColorIndex(glm::vec4 Color, unsigned int ShapeID) {
            if (!UsingComplexColorInsertion) {
                GLuint size = (GLuint)shape_colors.size();
                shape_colors.push_back(Color);
                return size;
            }

            SeenThisFrame.insert(ShapeID);

            auto found = ColorSlotID.find(ShapeID);
            if (found != ColorSlotID.end()) {
                GLuint slot = found->second;
                if (shape_colors[slot] != Color)
                    shape_colors[slot] = Color; // Avoid unnecessary writes
                ColorIndexesChanged++; // Would otherwise have changed
                return slot;
            }

            GLuint newSlot;
            if (!FreeSlots.empty()) {
                newSlot = FreeSlots.back();
                FreeSlots.pop_back();
                shape_colors[newSlot] = Color;
                ColorIndexesChanged++; // Would otherwise have changed
            } else {
                newSlot = static_cast<GLuint>(shape_colors.size());
                shape_colors.push_back(Color);
            }

            ColorSlotID[ShapeID] = newSlot;
            return newSlot;
        }

        template<typename T>
        inline void InternalAddRenderTarget(T* TargetPtr) {
            const bool shapeChanged = TargetPtr->Changed;
            const size_t currentIndex = InsertionIndex;
            size_t insertPos = combined_vertexes.size();

            if (currentIndex < PreviousRenderContent.size()) {
                const auto& [existingID, existingOffset] = PreviousRenderContent[currentIndex];

                if (TargetPtr->ID == existingID) {
                    if (!shapeChanged) {
                        InsertionIndex++;
                        return;
                    } else {
                        PreviousRenderContent.erase(PreviousRenderContent.begin() + currentIndex, PreviousRenderContent.end());
                        combined_vertexes.erase(combined_vertexes.begin() + existingOffset, combined_vertexes.end());
                        insertPos = existingOffset;
                    }
                } else {
                    PreviousRenderContent.erase(PreviousRenderContent.begin() + currentIndex, PreviousRenderContent.end());
                    combined_vertexes.erase(combined_vertexes.begin() + existingOffset, combined_vertexes.end());
                    insertPos = existingOffset;
                }
            }

            Changed = true;

            const auto& vertices = TargetPtr->Shape2D_RenderPipelineData;

            if (insertPos < combined_vertexes.size()) {
                combined_vertexes.resize(insertPos);
            }

            if (currentIndex > 0 && vertices.size() >= 2 && !combined_vertexes.empty()) {
                combined_vertexes.push_back(combined_vertexes.back());
                combined_vertexes.push_back(vertices[0]);
            }

            const size_t shapeStartIndex = combined_vertexes.size();
            combined_vertexes.resize(combined_vertexes.size() + vertices.size());
            std::memcpy(
                combined_vertexes.data() + combined_vertexes.size() - vertices.size(),
                vertices.data(),
                vertices.size() * sizeof(Vertex)
            );
            //combined_vertexes.insert(combined_vertexes.end(), vertices.begin(), vertices.end()); // very slow

            if (currentIndex < PreviousRenderContent.size()) {
                PreviousRenderContent[currentIndex] = { TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex) };
            } else {
                PreviousRenderContent.emplace_back(TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex));
            }

            InsertionIndex++;
        }
};