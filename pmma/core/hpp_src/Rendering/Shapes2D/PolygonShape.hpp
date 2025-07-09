#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"

class EXPORT CPP_PolygonShape {
    public:
        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec4 RenderPipelineColorData;
        std::vector<glm::vec2> ShapePoints;

        float Rotation = 0;

        unsigned int Width = 0;

        uint64_t ID;
        GLuint ColorIndex;

        bool ColorSet = false;
        bool PointsSet = false;
        bool UsingGradients = false;
        bool HasAlpha = false;
        bool Changed = true;
        bool Closed = false;

        CPP_PolygonShape();

        void Render(float ShapeQuality);

        void InternalRender();

        inline void SetColor(float* in_color, unsigned int size) {
            UsingGradients = size > 4; // (determine if multiple colors inputted)

            std::vector<glm::vec4> NewColorData;

            HasAlpha = false;
            for (unsigned int i = 0; i < size; i += 4) { // Color will be in form rgba
                NewColorData.push_back(glm::vec4(in_color[i], in_color[i + 1], in_color[i + 2], in_color[i + 3]));
                if (in_color[i + 3] != 1.0f) {
                    HasAlpha = true;
                }
            }

            if (ColorSet && (size != NewColorData.size() * 4 || ColorData.size() != NewColorData.size() || !std::equal(ColorData.begin(), ColorData.end(), NewColorData.begin()))) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ColorSet = true;
            ColorData = NewColorData;
        };

        inline void SetPoints(unsigned int (*in_points)[2], unsigned int count) {
            std::vector<glm::vec2> NewShapePoints;

            for (unsigned int i = 0; i < count; i += 2) {
                NewShapePoints.push_back(glm::vec2(in_points[i][0], in_points[i + 1][1]));
            }

            if (PointsSet && (count != NewShapePoints.size() * 2 || ShapePoints.size() != NewShapePoints.size() || !std::equal(ShapePoints.begin(), ShapePoints.end(), NewShapePoints.begin()))) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapePoints = NewShapePoints;
            PointsSet = true;
        }

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Width = in_width;
        };

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline void SetClosed(bool in_closed) {
            if (in_closed != Closed) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Closed = in_closed;
        }
};