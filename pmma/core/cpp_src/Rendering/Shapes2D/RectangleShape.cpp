#include <cmath>

#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/RenderPipelineManager.hpp"
#include "AdvancedMathematics.hpp"
#include "Constants.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_RectangleShape::CPP_RectangleShape() {
    RenderPipelineData = new RenderPipelineDataObject(this);
}

void CPP_RectangleShape::Render(float ShapeQuality) {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (ShapeCentre.x + HalfWidth < 0 ||
            ShapeCentre.x - HalfWidth > DisplayWidth ||
            ShapeCentre.y + HalfHeight < 0 ||
            ShapeCentre.y - HalfHeight > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = (UsingGradients == false);

    if (RenderPipelineCompatible) {
        if (ColorData[0].w == 0) { // Return if shape not visible
            return;
        }

        GLuint newColorIndex = PMMA::RenderPipelineCore->GetColorIndex();
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            Changed = false;

            RenderPipelineColorData = ColorData[0];

            unsigned int InternalWidth = Width;
            if (Width == 0) {
                InternalWidth = max(HalfWidth, HalfHeight);
            }

            if (CornerRadius != 0) {
                unsigned int minimum_radius = min(CornerRadius, min(HalfWidth, HalfHeight));
                float minAngle = asin(1.0f / minimum_radius);
                unsigned int segments = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * ShapeQuality)/4);

                size_t vertexCount = (segments + 1) * 8 + 2;
                RenderPipelineVertexData.resize(vertexCount);

                int outer_radius = min(CornerRadius, min(HalfWidth, HalfHeight));
                int inner_radius = max(outer_radius - (int)InternalWidth, 0);

                int outer_width = ShapeSize.x;
                int outer_height = ShapeSize.y;
                int inner_width = outer_width - 2 * InternalWidth;
                int inner_height = outer_height - 2 * InternalWidth;

                ////

                float SA = CPP_Constants::PI;
                float EA = CPP_Constants::PI * 1.5f;
                float AngleDelta = (EA-SA) / segments;
                float cx = -outer_width / 2 + outer_radius;
                float cy = -outer_height / 2 + outer_radius;

                float icx = -inner_width / 2 + inner_radius;
                float icy = -inner_height / 2 + inner_radius;

                unsigned int index = 0;

                for (unsigned int i = 0; i <= segments; i++) {
                    float angle = SA + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};

                    px = icx + inner_radius * cos(angle);
                    py = icy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};
                }

                ////

                SA = CPP_Constants::PI * 1.5f;
                EA = CPP_Constants::PI * 2;
                AngleDelta = (EA-SA) / segments;
                cx = outer_width / 2 - outer_radius;
                cy = -outer_height / 2 + outer_radius;

                icx = inner_width / 2 - inner_radius;
                icy = -inner_height / 2 + inner_radius;

                index = (segments + 1) * 2;

                for (unsigned int i = 0; i <= segments; i++) {
                    float angle = SA + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};

                    px = icx + inner_radius * cos(angle);
                    py = icy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};
                }

                ////

                SA = 0;
                EA = CPP_Constants::PI * 0.5f;
                AngleDelta = (EA-SA) / segments;
                cx = outer_width / 2 - outer_radius;
                cy = outer_height / 2 - outer_radius;

                icx = inner_width / 2 - inner_radius;
                icy = inner_height / 2 - inner_radius;

                index = (segments + 1) * 4;

                for (unsigned int i = 0; i <= segments; i++) {
                    float angle = SA + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};

                    px = icx + inner_radius * cos(angle);
                    py = icy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};
                }

                ////

                SA = CPP_Constants::PI * 0.5f;
                EA = CPP_Constants::PI;
                AngleDelta = (EA-SA) / segments;
                cx = -outer_width / 2 + outer_radius;
                cy = outer_height / 2 - outer_radius;

                icx = -inner_width / 2 + inner_radius;
                icy = inner_height / 2 - inner_radius;

                index = (segments + 1) * 6;

                for (unsigned int i = 0; i <= segments; i++) {
                    float angle = SA + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};

                    px = icx + inner_radius * cos(angle);
                    py = icy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(ShapeCentre.x + px, ShapeCentre.y + py), ColorIndex};
                }

                RenderPipelineVertexData[vertexCount - 2] = RenderPipelineVertexData[0];
                RenderPipelineVertexData[vertexCount - 1] = RenderPipelineVertexData[1];
            } else {
                if (Width == 0 || Width >= max(HalfWidth, HalfHeight)) {
                    cout << "SW" << endl;
                    RenderPipelineVertexData.resize(4);

                    RenderPipelineVertexData[0] = {glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y - HalfHeight), ColorIndex};
                    RenderPipelineVertexData[1] = {glm::vec2(ShapeCentre.x + HalfWidth, ShapeCentre.y - HalfHeight), ColorIndex};
                    RenderPipelineVertexData[2] = {glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y + HalfHeight), ColorIndex};
                    RenderPipelineVertexData[3] = {glm::vec2(ShapeCentre.x + HalfWidth, ShapeCentre.y + HalfHeight), ColorIndex};
                } else {
                    cout << "CW" << endl;
                    RenderPipelineVertexData.resize(10);

                    int outer_left   = ShapeCentre.x - HalfWidth;
                    int outer_right  = ShapeCentre.x + HalfWidth;
                    int outer_top    = ShapeCentre.y - HalfHeight;
                    int outer_bottom = ShapeCentre.y + HalfHeight;

                    int inner_left   = outer_left   + Width;
                    int inner_right  = outer_right  - Width;
                    int inner_top    = outer_top    + Width;
                    int inner_bottom = outer_bottom - Width;

                    // GL_TRIANGLE_STRIP order: Outer TL, Inner TL, Outer TR, Inner TR, Outer BR, Inner BR, Outer BL, Inner BL
                    RenderPipelineVertexData[0] = {glm::vec2(outer_left,  outer_top),    ColorIndex}; // Outer TL
                    RenderPipelineVertexData[1] = {glm::vec2(inner_left,  inner_top),    ColorIndex}; // Inner TL
                    RenderPipelineVertexData[2] = {glm::vec2(outer_right, outer_top),    ColorIndex}; // Outer TR
                    RenderPipelineVertexData[3] = {glm::vec2(inner_right, inner_top),    ColorIndex}; // Inner TR
                    RenderPipelineVertexData[4] = {glm::vec2(outer_right, outer_bottom), ColorIndex}; // Outer BR
                    RenderPipelineVertexData[5] = {glm::vec2(inner_right, inner_bottom),ColorIndex}; // Inner BR
                    RenderPipelineVertexData[6] = {glm::vec2(outer_left,  outer_bottom),ColorIndex}; // Outer BL
                    RenderPipelineVertexData[7] = {glm::vec2(inner_left,  inner_bottom),ColorIndex}; // Inner BL
                    RenderPipelineVertexData[8] = RenderPipelineVertexData[0];
                    RenderPipelineVertexData[9] = RenderPipelineVertexData[1];
                }
            }
        }
        PMMA::RenderPipelineCore->AddObject(*RenderPipelineData, RenderPipelineCompatible);
    } else {
        if (Changed) {
            // Calculate data and add to buffers, Left intentionally blank for now
        }
        // Do NOTHING.
    }
}

void CPP_RectangleShape::InternalRender() {
    // Left intentionally blank for now
}
