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
        CPP_DisplayCoordinateFormat* ShapeCentreFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec4 RenderPipelineColorData;

        float Rotation = 0;
        float StartAngle;
        float EndAngle;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 0;
        unsigned int PointCount = 0;
        unsigned int Radius;

        bool ColorSet = false;
        bool UsingGradients = false;
        bool HasAlpha = false;
        bool Changed = true;
        bool StartAngleSet = false;
        bool EndAngleSet = false;
        bool RadiusSet = false;

        CPP_ArcShape();

        ~CPP_ArcShape() {
            delete ShapeCentreFormat;
            ShapeCentreFormat = nullptr;
        }

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

        inline void SetStartAngle(float in_start_angle) {
            if (StartAngleSet && (in_start_angle != StartAngle)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            StartAngle = in_start_angle;
            StartAngleSet = true;
        };

        inline void SetEndAngle(float in_end_angle) {
            if (EndAngleSet && (in_end_angle != EndAngle)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            EndAngle = in_end_angle;
            EndAngleSet = true;
        };

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Width = in_width;
        };

        inline void SetRadius(unsigned int in_radius) {
            if (in_radius != Radius) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Radius = in_radius;
        };

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline void SetPointCount(unsigned int in_point_count) {
            if (in_point_count != PointCount) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            PointCount = in_point_count;
        }
};