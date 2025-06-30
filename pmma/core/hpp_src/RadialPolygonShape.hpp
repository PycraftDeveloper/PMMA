#pragma once
#include "PMMA_Exports.hpp"

#include <vector>

#include <glm/glm.hpp>

#include "Constants.hpp"
#include "RenderPipelineManager.hpp"

class EXPORT CPP_RadialPolygonShape {
    public:
        unsigned int type = CPP_Constants::TYPE_RADIAL_POLYGON_SHAPE;

        RenderPipelineDataObject* RenderPipelineData;

        std::vector<glm::vec2> VertexData;
        std::vector<glm::vec4> ColorData;

        glm::vec2 ShapeCentre;
        unsigned int Radius;
        unsigned int Width;
        unsigned int PointCount = 0;
        float Rotation = 0;

        bool ColorSet = false;
        bool CentreSet = false;
        bool RadiusSet = false;
        bool WidthSet = false;
        bool UsingGradients = false;
        bool HasAlpha = false;
        bool PointCountSet = false;

        CPP_RadialPolygonShape();

        void Render(float ShapeQuality);

        void InternalRender();

        void SetColor(float* in_color, unsigned int size) {
            UsingGradients = size > 4; // (determine if multiple colors inputted)

            ColorData.clear();
            HasAlpha = false;
            for (int i = 0; i < size; i += 4) { // Color will be in form rgba
                ColorData.push_back(glm::vec4(in_color[i], in_color[i + 1], in_color[i + 2], in_color[i + 3]));
                if (in_color[i + 3] != 1.0f) {
                    HasAlpha = true;
                }
            }

            ColorSet = true;
        }

        void SetCentre(unsigned int* in_position) {
            ShapeCentre = glm::vec2(in_position[0], in_position[1]);
            CentreSet = true;
        }

        void SetRadius(unsigned int in_radius) {
            Radius = in_radius;
            RadiusSet = true;
        }

        void SetPointCount(unsigned int in_pointCount) {
            PointCount = in_pointCount;
            PointCountSet = true;
        }

        void SetWidth(unsigned int in_width) {
            Width = in_width;
            WidthSet = true;
        }
};