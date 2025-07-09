#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <cstdint>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/Shape2DRenderPipelineManager.hpp"

class EXPORT CPP_RectangleShape {
    public:
        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec4 RenderPipelineColorData;
        glm::vec2 ShapeCentre;
        glm::vec2 ShapeSize;

        float Rotation = 0;

        uint64_t ID;
        GLuint ColorIndex;
        unsigned int Width = 0;
        unsigned int CornerRadius = 0;

        bool ColorSet = false;
        bool CentreSet = false;
        bool SizeSet = false;
        bool WidthSet = true;
        bool UsingGradients = false;
        bool HasAlpha = false;
        bool Changed = true;
        bool CornerRadiusSet = true;

        CPP_RectangleShape();

        void Render(float ShapeQuality);

        void InternalRender();

        inline glm::vec2 SimpleApplyRotation(glm::vec2 position, float RotationSin, float RotationCos, unsigned int HalfWidth, unsigned int HalfHeight) {
            glm::vec2 tl = glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y - HalfHeight);
            glm::vec2 pos = tl - ShapeCentre;
            glm::vec2 rotated = {
                RotationCos * pos.x - RotationSin * pos.y,
                RotationSin * pos.x + RotationCos * pos.y
            };
            return ShapeCentre + rotated;
        }

        inline glm::vec2 ComplexApplyRotation(glm::vec2 point, float RotationSin, float RotationCos) {
            // Translate point to origin
            point -= ShapeCentre;

            // Rotate
            float xnew = point.x * RotationCos - point.y * RotationSin;
            float ynew = point.x * RotationSin + point.y * RotationCos;

            // Translate back
            return glm::vec2(xnew, ynew) + ShapeCentre;
        }

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

        inline void SetCentre(unsigned int* in_position) {
            if (CentreSet && (in_position[0] != ShapeCentre.x || in_position[1] != ShapeCentre.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapeCentre = glm::vec2(in_position[0], in_position[1]);
            CentreSet = true;
        };

        inline void SetSize(unsigned int* in_size) {
            if (SizeSet && (in_size[0] != ShapeSize.x || in_size[1] != ShapeSize.y)) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapeSize = glm::vec2(in_size[0], in_size[1]);
            SizeSet = true;
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

        inline void SetCornerRadius(unsigned int in_corner_radius) {
            if (in_corner_radius != CornerRadius) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            CornerRadius = in_corner_radius;
        }
};