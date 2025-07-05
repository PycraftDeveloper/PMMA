#pragma once
#include "PMMA_Exports.hpp"

#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "Rendering/RenderPipelineManager.hpp"

class EXPORT CPP_RadialPolygonShape {
    public:
        RenderPipelineDataObject* RenderPipelineData;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        std::vector<Vertex> RenderPipelineVertexData;

        glm::vec4 RenderPipelineColorData;
        glm::vec2 ShapeCentre;

        unsigned int Radius;
        unsigned int Width = 0;
        unsigned int PointCount = 0;
        GLuint ColorIndex;

        float Rotation = 0;

        bool ColorSet = false;
        bool CentreSet = false;
        bool RadiusSet = false;
        bool WidthSet = true;
        bool UsingGradients = false;
        bool HasAlpha = false;
        bool PointCountSet = true;
        bool Changed = true;

        CPP_RadialPolygonShape();

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

        inline void SetCentre(unsigned int* in_position) {
            if (CentreSet && in_position[0] != ShapeCentre.x || in_position[1] != ShapeCentre.y) {
                Changed = true;
                RenderPipelineVertexData.clear();
                VertexData.clear();
            }

            ShapeCentre = glm::vec2(in_position[0], in_position[1]);
            CentreSet = true;
        };

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