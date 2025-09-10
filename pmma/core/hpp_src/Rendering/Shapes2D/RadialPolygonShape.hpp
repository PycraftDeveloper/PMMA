#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Constants.hpp"
#include "NumberFormats.hpp"
#include "Logger.hpp"

class EXPORT CPP_RadialPolygonShape {
    public:
        CPP_Logger* Logger;
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> Shape2D_RenderPipelineData;

        float Rotation = 0;

        uint64_t ID;
        float ColorIndex = 0;
        unsigned int Radius;
        unsigned int Width = 0;
        unsigned int PointCount = 0;

        bool RadiusSet = false;
        bool WidthSet = true;
        bool HasAlpha = false;
        bool PointCountSet = true;
        bool Changed = true;

        CPP_RadialPolygonShape();

        ~CPP_RadialPolygonShape() {
            delete Logger;
            Logger = nullptr;

            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();

        inline void SetRadius(unsigned int in_radius) {
            if (RadiusSet && in_radius != Radius) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Radius = in_radius;
            RadiusSet = true;
        };

        inline unsigned int GetRadius() {
            if (!RadiusSet) {
                Logger->InternalLogWarn(
                    30,
                    "You have not specified a radius for the arc \
please use `RadialPolygon.set_radius` to set it before attempting to get it.");
                throw std::runtime_error("Radius not set");
            }
            return Radius;
        };

        inline void SetPointCount(unsigned int in_pointCount) {
            if (PointCountSet && in_pointCount != PointCount) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            PointCount = in_pointCount;
            PointCountSet = true;
        };

        unsigned int GetPointCount();

        inline void SetWidth(unsigned int in_width) {
            if (WidthSet && in_width != Width) {
                Changed = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Width = in_width;
            WidthSet = true;
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
};