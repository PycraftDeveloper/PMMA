#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_RadialPolygonShape {
    public:
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex = 0;
        unsigned int Radius;
        unsigned int Width = 0;
        unsigned int PointCount = 0;

        bool CenterSet = false;
        bool RadiusSet = false;
        bool WidthSet = true;
        bool HasAlpha = false;
        bool PointCountSet = true;
        bool Changed = true;

        CPP_RadialPolygonShape();

        ~CPP_RadialPolygonShape() {
            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render(float ShapeQuality);

        void InternalRender();

        inline void SetRadius(unsigned int in_radius) {
            if (RadiusSet && in_radius != Radius) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Radius = in_radius;
            RadiusSet = true;
        };

        inline void SetPointCount(unsigned int in_pointCount) {
            if (PointCountSet && in_pointCount != PointCount) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            PointCount = in_pointCount;
            PointCountSet = true;
        };

        inline void SetWidth(unsigned int in_width) {
            if (WidthSet && in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Width = in_width;
            WidthSet = true;
        };

        inline void SetRotation(float in_rotation) {
            if (in_rotation != Rotation) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }
};