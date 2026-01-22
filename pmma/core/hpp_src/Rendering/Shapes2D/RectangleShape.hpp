#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Internal/Management/Shape2DRenderPipelineManager.hpp"
#include "Constants.hpp"
#include "NumberFormats.hpp"
#include "Logger.hpp"

class EXPORT CPP_RectangleShape {
    public:
        CPP_Logger* Logger;
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> Shape2D_RenderPipelineData;
        std::vector<uint32_t> Shape2D_RenderPipelineIndices;

        glm::vec2 ShapeSize;

        float Rotation = 0;

        uint64_t ID;
        float ColorIndex;
        unsigned int Width = 0;
        unsigned int CornerRadius = 0;

        bool SizeSet = false;
        bool WidthSet = true;
        bool HasAlpha = false;
        bool VertexDataChanged = true;
        bool ColorDataChanged = true;
        bool CornerRadiusSet = true;

        CPP_RectangleShape();

        ~CPP_RectangleShape() {
            delete Logger;
            Logger = nullptr;

            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render();

        void InternalRender();

        inline void SimpleApplyRotation(float* position, float* shape_center, float RotationSin, float RotationCos, unsigned int HalfWidth, unsigned int HalfHeight, float* out) {
            float pos[2], rotated[2];
            pos[0] = position[0] - shape_center[0];
            pos[1] = position[1] - shape_center[1];

            rotated[0] = RotationCos * pos[0] - RotationSin * pos[1];
            rotated[1] = RotationSin * pos[0] + RotationCos * pos[1];

            out[0] = rotated[0] + shape_center[0];
            out[1] = rotated[1] + shape_center[1];
        }

        inline void ComplexApplyRotation(float* point, float* shape_center, float RotationSin, float RotationCos, float* out) {
            // Translate point to origin
            point[0] -= shape_center[0];
            point[1] -= shape_center[1];

            // Rotate
            float xnew = point[0] * RotationCos - point[1] * RotationSin;
            float ynew = point[0] * RotationSin + point[1] * RotationCos;

            // Translate back
            out[0] = xnew + shape_center[0];
            out[1] = ynew + shape_center[1];
        }

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
                Logger->InternalLogWarn(
                    30,
                    "This shape has no size set, please use `Rectangle.set_size` to set it.");
                throw std::runtime_error("Size not set");
            }

            out_size[0] = static_cast<unsigned int>(ShapeSize.x);
            out_size[1] = static_cast<unsigned int>(ShapeSize.y);
        }

        inline void SetWidth(unsigned int in_width) {
            if (WidthSet && in_width != Width) {
                VertexDataChanged = true;
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
                VertexDataChanged = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }

        inline void SetCornerRadius(unsigned int in_corner_radius) {
            if (in_corner_radius != CornerRadius) {
                VertexDataChanged = true;
                Shape2D_RenderPipelineData.clear();
                VertexData.clear();
            }

            CornerRadius = in_corner_radius;
        }

        inline unsigned int GetCornerRadius() const {
            return CornerRadius;
        }
};