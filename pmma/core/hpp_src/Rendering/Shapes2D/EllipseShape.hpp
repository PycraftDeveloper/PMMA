#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Constants.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

class EXPORT CPP_EllipseShape {
    public:
        CPP_Logger* Logger;
        CPP_DisplayCoordinate* ShapeCenterFormat;
        CPP_Color* Color;

        std::vector<glm::vec2> VertexData;

        std::vector<Vertex> Shape2D_RenderPipelineData;

        glm::vec2 ShapeSize;

        float Rotation = 0;

        uint64_t ID;
        float ColorIndex;
        unsigned int Width = 0;
        unsigned int PointCount = 0;

        bool SizeSet = false;
        bool HasAlpha = false;
        bool VertexDataChanged = true;
        bool ColorDataChanged = true;

        CPP_EllipseShape();

        ~CPP_EllipseShape() {
            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
            }

            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete Color;
            Color = nullptr;
        }

        void Render();

        void InternalRender();

        inline void SetSize(unsigned int* in_size) {
            if (SizeSet && (in_size[0] != ShapeSize.x || in_size[1] != ShapeSize.y)) {
                VertexDataChanged = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            ShapeSize = glm::vec2(in_size[0], in_size[1]);
            SizeSet = true;
        };

        inline void GetSize(unsigned int* out_size) {
            if (!SizeSet) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogWarn(
                    30,
                    "This shape has no size set, please use `Ellipse.set_size` to set it.");
                throw std::runtime_error("Size not set");
            }

            out_size[0] = (unsigned int)ShapeSize.x;
            out_size[1] = (unsigned int)ShapeSize.y;
        }

        inline void SetWidth(unsigned int in_width) {
            if (in_width != Width) {
                VertexDataChanged = true;
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
                VertexDataChanged = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }

        inline void SetPointCount(unsigned int in_point_count) {
            if (in_point_count != PointCount) {
                VertexDataChanged = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            PointCount = in_point_count;
        }

        unsigned int GetPointCount();
};