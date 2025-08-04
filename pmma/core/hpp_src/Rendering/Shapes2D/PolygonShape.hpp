#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_PolygonShape {
    public:
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> Shape2D_RenderPipelineData;

        std::vector<glm::vec2> ShapePoints;

        float Rotation = 0;

        unsigned int Width = 1;

        uint64_t ID;
        GLuint ColorIndex;

        bool PointsSet = false;
        bool HasAlpha = false;
        bool Changed = true;
        bool Closed = false;

        CPP_PolygonShape();

        ~CPP_PolygonShape() {
            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();

        inline void SetPoints(unsigned int (*in_points)[2], unsigned int count) {
            std::vector<glm::vec2> NewShapePoints;

            for (unsigned int i = 0; i < count; i++) {
                NewShapePoints.push_back(glm::vec2(in_points[i][0], in_points[i][1]));
            }

            if (PointsSet && (count != NewShapePoints.size() * 2 || ShapePoints.size() != NewShapePoints.size() || !std::equal(ShapePoints.begin(), ShapePoints.end(), NewShapePoints.begin()))) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            ShapePoints = NewShapePoints;
            PointsSet = true;
        }

        inline void GetPoints(unsigned int (*out_points)[2]) {
            if (!PointsSet) {
                throw std::runtime_error("Points not set!");
            }

            for (unsigned int i = 0; i < ShapePoints.size(); i++) {
                out_points[i][0] = static_cast<unsigned int>(ShapePoints[i].x);
                out_points[i][1] = static_cast<unsigned int>(ShapePoints[i].y);
            }
        }

        inline unsigned int GetPointCount() const {
            if (!PointsSet) {
                throw std::runtime_error("Points not set!");
            }
            return static_cast<unsigned int>(ShapePoints.size());
        }

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Width = in_width;
        };

        inline unsigned int GetWidth() const {
            return Width;
        }

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }

        inline void SetClosed(bool in_closed) {
            if (in_closed != Closed) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Closed = in_closed;
        }

        inline bool GetClosed() const {
            return Closed;
        }
};