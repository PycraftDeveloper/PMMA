#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_ArcShape {
    public:
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;

        std::vector<Vertex> RenderPipelineVertexData;

        float Rotation = 0;
        float StartAngle;
        float EndAngle;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 0;
        unsigned int PointCount = 0;
        unsigned int Radius;

        bool HasAlpha = false;
        bool Changed = true;
        bool StartAngleSet = false;
        bool EndAngleSet = false;
        bool RadiusSet = false;

        CPP_ArcShape();

        ~CPP_ArcShape() {
            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();

        inline void SetStartAngle(float in_start_angle) {
            if (StartAngleSet && (in_start_angle != StartAngle)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            StartAngle = in_start_angle;
            StartAngleSet = true;
        };

        inline float GetStartAngle() const {
            if (!StartAngleSet) {
                throw std::runtime_error("Start angle not set!");
            }
            return StartAngle;
        }

        inline void SetEndAngle(float in_end_angle) {
            if (EndAngleSet && (in_end_angle != EndAngle)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            EndAngle = in_end_angle;
            EndAngleSet = true;
        };

        inline float GetEndAngle() const {
            if (!EndAngleSet) {
                throw std::runtime_error("End angle not set!");
            }
            return EndAngle;
        }

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Width = in_width;
        };

        inline unsigned int GetWidth() const {
            return Width;
        }

        inline void SetRadius(unsigned int in_radius) {
            if (in_radius != Radius) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Radius = in_radius;
        };

        inline unsigned int GetRadius() const {
            if (!RadiusSet) {
                throw std::runtime_error("Radius not set!");
            }
            return Radius;
        }

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }

        inline void SetPointCount(unsigned int in_point_count) {
            if (in_point_count != PointCount) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            PointCount = in_point_count;
        }

        unsigned int GetPointCount();
};