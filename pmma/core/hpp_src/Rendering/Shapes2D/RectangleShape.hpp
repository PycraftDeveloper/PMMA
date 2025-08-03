#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_RectangleShape {
    public:
        CPP_DisplayCoordinateFormat* ShapeCenterFormat;
        CPP_ColorFormat* ColorFormat;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec2 ShapeSize;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 0;
        unsigned int CornerRadius = 0;

        bool SizeSet = false;
        bool WidthSet = true;
        bool HasAlpha = false;
        bool Changed = true;
        bool CornerRadiusSet = true;

        CPP_RectangleShape();

        ~CPP_RectangleShape() {
            delete ShapeCenterFormat;
            ShapeCenterFormat = nullptr;

            delete ColorFormat;
            ColorFormat = nullptr;
        }

        void Render(float ShapeQuality);

        void InternalRender();

        inline glm::vec2 SimpleApplyRotation(glm::vec2 position, glm::vec2 shape_center, float RotationSin, float RotationCos, unsigned int HalfWidth, unsigned int HalfHeight) {
            glm::vec2 tl = glm::vec2(shape_center.x - HalfWidth, shape_center.y - HalfHeight);
            glm::vec2 pos = tl - shape_center;
            glm::vec2 rotated = {
                RotationCos * pos.x - RotationSin * pos.y,
                RotationSin * pos.x + RotationCos * pos.y
            };
            return shape_center + rotated;
        }

        inline glm::vec2 ComplexApplyRotation(glm::vec2 point, glm::vec2 shape_center, float RotationSin, float RotationCos) {
            // Translate point to origin
            point -= shape_center;

            // Rotate
            float xnew = point.x * RotationCos - point.y * RotationSin;
            float ynew = point.x * RotationSin + point.y * RotationCos;

            // Translate back
            return glm::vec2(xnew, ynew) + shape_center;
        }

        inline void SetSize(unsigned int* in_size) {
            if (SizeSet && (in_size[0] != ShapeSize.x || in_size[1] != ShapeSize.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapeSize = glm::vec2(in_size[0], in_size[1]);
            SizeSet = true;
        };

        inline void GetSize(unsigned int* out_size) {
            if (!SizeSet) {
                throw std::runtime_error("Size not set!");
            }

            out_size[0] = static_cast<unsigned int>(ShapeSize.x);
            out_size[1] = static_cast<unsigned int>(ShapeSize.y);
        }

        inline void SetWidth(unsigned int in_width) {
            if (WidthSet && in_width != Width) {
                Changed = true;
                RenderPipelineVertexData.clear();
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
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            Rotation = in_rotation;
        }

        inline float GetRotation() const {
            return Rotation;
        }

        inline void SetCornerRadius(unsigned int in_corner_radius) {
            if (in_corner_radius != CornerRadius) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            CornerRadius = in_corner_radius;
        }

        inline unsigned int GetCornerRadius() const {
            return CornerRadius;
        }
};