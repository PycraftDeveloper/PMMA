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

            if (CornerRadius != 0) {
                unsigned int minimum_radius = min(CornerRadius, min(HalfWidth, HalfHeight));
                float minAngle = asin(1.0f / minimum_radius);
                unsigned int internal_point_count = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * ShapeQuality)/4);

                size_t vertexCount = internal_point_count * 8 + 2;
                RenderPipelineVertexData.resize(vertexCount);

                unsigned int outer_radius = CornerRadius;
                unsigned int inner_radius = CornerRadius - Width;
                unsigned int outer_width = ShapeSize.x;
                unsigned int outer_height = ShapeSize.y;

                ////

                float AngleDelta = (CPP_Constants::PI * 1.5 - CPP_Constants::PI) / internal_point_count;
                float cx = -outer_width / 2 + outer_radius;
                float cy = -outer_height / 2 + outer_radius;

                unsigned int index = 0;

                for (unsigned int i = 0; i <= internal_point_count; i++) {
                    float angle = CPP_Constants::PI + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(px, py), ColorIndex};

                    px = cx + inner_radius * cos(angle);
                    py = cy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(px, py), ColorIndex};
                }

                ////

                AngleDelta = (CPP_Constants::PI * 2 - CPP_Constants::PI * 1.5) / internal_point_count;
                cx = outer_width / 2 - outer_radius;
                cy = -outer_height / 2 - outer_radius;

                index = internal_point_count;

                for (unsigned int i = 0; i <= internal_point_count; i++) {
                    float angle = CPP_Constants::PI + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(px, py), ColorIndex};

                    px = cx + inner_radius * cos(angle);
                    py = cy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(px, py), ColorIndex};
                }

                ////

                AngleDelta = (CPP_Constants::PI * 0.5 - 0) / internal_point_count;
                cx = outer_width / 2 - outer_radius;
                cy = outer_height / 2 - outer_radius;

                index = internal_point_count * 2;

                for (unsigned int i = 0; i <= internal_point_count; i++) {
                    float angle = CPP_Constants::PI + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(px, py), ColorIndex};

                    px = cx + inner_radius * cos(angle);
                    py = cy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(px, py), ColorIndex};
                }

                ////

                AngleDelta = (CPP_Constants::PI - CPP_Constants::PI * 0.5) / internal_point_count;
                cx = -outer_width / 2 + outer_radius;
                cy = outer_height / 2 - outer_radius;

                index = internal_point_count * 3;

                for (unsigned int i = 0; i <= internal_point_count; i++) {
                    float angle = CPP_Constants::PI + i * AngleDelta;
                    float px = cx + outer_radius * cos(angle);
                    float py = cy + outer_radius * sin(angle);
                    unsigned int di = i * 2;
                    RenderPipelineVertexData[index + di] = {glm::vec2(px, py), ColorIndex};

                    px = cx + inner_radius * cos(angle);
                    py = cy + inner_radius * sin(angle);
                    RenderPipelineVertexData[index + di + 1] = {glm::vec2(px, py), ColorIndex};
                }

                RenderPipelineVertexData[vertexCount - 2] = RenderPipelineVertexData[0];
                RenderPipelineVertexData[vertexCount - 1] = RenderPipelineVertexData[1];
            } else {
                RenderPipelineVertexData.resize(4);

                RenderPipelineVertexData[0] = {glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y - HalfHeight), ColorIndex};
                RenderPipelineVertexData[1] = {glm::vec2(ShapeCentre.x + HalfWidth, ShapeCentre.y - HalfHeight), ColorIndex};
                RenderPipelineVertexData[2] = {glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y + HalfHeight), ColorIndex};
                RenderPipelineVertexData[3] = {glm::vec2(ShapeCentre.x + HalfWidth, ShapeCentre.y + HalfHeight), ColorIndex};
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
