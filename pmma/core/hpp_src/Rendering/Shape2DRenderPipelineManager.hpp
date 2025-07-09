#pragma once

#include <vector>
#include <variant>
#include <iostream>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "OpenGL.hpp"

class CPP_RadialPolygonShape;
class CPP_RectangleShape;
class CPP_PixelShape;
// To-DO:
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
    glm::vec2 position;
    GLuint shape_id;
};

class CPP_Shape2D_RenderPipelineManager {
    public:
        std::vector<Shape2D_RenderObject> RenderPipelineComponents;
        std::vector<Vertex> combined_vertexes;
        std::vector<glm::vec4> shape_colors;

        std::vector<std::pair<uint64_t, unsigned int>> PreviousRenderContent;
        unsigned int InsertionIndex = 0;

        GLuint vao, vbo, ubo;

        bool Changed = true;
        bool HasAlpha = false;

        CPP_Shape2D_RenderPipelineManager();
        ~CPP_Shape2D_RenderPipelineManager();

        void AddRenderTarget(const Shape2D_RenderObject& NewObject);

        void Reset();

        void InternalRender();

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
                        shape_colors.resize(currentIndex);
                        insertPos = existingOffset;
                    }
                } else {
                    PreviousRenderContent.erase(PreviousRenderContent.begin() + currentIndex, PreviousRenderContent.end());
                    combined_vertexes.erase(combined_vertexes.begin() + existingOffset, combined_vertexes.end());
                    shape_colors.resize(currentIndex);
                    insertPos = existingOffset;
                }
            }

            Changed = true;

            const glm::vec4 color = TargetPtr->RenderPipelineColorData;

            if (currentIndex < shape_colors.size()) {
                shape_colors[currentIndex] = color;
            } else {
                shape_colors.emplace_back(color);
            }

            const auto& vertices = TargetPtr->RenderPipelineVertexData;

            if (insertPos < combined_vertexes.size()) {
                combined_vertexes.resize(insertPos);
            }

            if (currentIndex > 0 && vertices.size() >= 2 && !combined_vertexes.empty()) {
                combined_vertexes.emplace_back(combined_vertexes.back());
                combined_vertexes.emplace_back(vertices[0]);
            }

            const size_t shapeStartIndex = combined_vertexes.size();
            combined_vertexes.insert(combined_vertexes.end(), vertices.begin(), vertices.end());

            if (currentIndex < PreviousRenderContent.size()) {
                PreviousRenderContent[currentIndex] = { TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex) };
            } else {
                PreviousRenderContent.emplace_back(TargetPtr->ID, static_cast<unsigned int>(shapeStartIndex));
            }

            InsertionIndex++;
        }
};