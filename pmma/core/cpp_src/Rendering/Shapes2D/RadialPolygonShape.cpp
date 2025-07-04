#include <cmath>

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/RenderPipelineManager.hpp"
#include "Constants.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    RenderPipelineData = new RenderPipelineDataObject(this);
}

void CPP_RadialPolygonShape::Render(float ShapeQuality) {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    if (ShapeCentre.x + Radius < 0 ||
            ShapeCentre.x - Radius > DisplayWidth ||
            ShapeCentre.y + Radius < 0 ||
            ShapeCentre.y - Radius > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = (UsingGradients == false);

    if (RenderPipelineCompatible) {
        GLuint newColorIndex = PMMA::RenderPipelineCore->GetColorIndex();
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            Changed = false;

            RenderPipelineColorData = ColorData[0];

            unsigned int InternalPointCount = PointCount;
            if (PointCount == 0) {
                float minAngle = asin(1.0f / Radius);
                InternalPointCount = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * ShapeQuality));
            }


            float angleStep = CPP_Constants::TAU / InternalPointCount;

            unsigned int outer_radius = Radius;

            unsigned int inner_radius = max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);
            if (Width == 0) {
                inner_radius = 0;
            }

            // Reserve the exact number of vertices upfront
            size_t vertexCount = InternalPointCount * 2 + 2;
            RenderPipelineVertexData.resize(vertexCount);

            float angle = Rotation;
            float cx = ShapeCentre.x;
            float cy = ShapeCentre.y;
            float cosStep = std::cos(angleStep);
            float sinStep = std::sin(angleStep);
            float cosA = std::cos(angle);
            float sinA = std::sin(angle);

            if (inner_radius == 0) {
                for (unsigned int i = 0; i < InternalPointCount; ++i) {
                    float ox = outer_radius * cosA + cx;
                    float oy = outer_radius * sinA + cy;

                    unsigned int index = i * 2;

                    RenderPipelineVertexData[index] = {glm::vec2(ox, oy), ColorIndex};
                    RenderPipelineVertexData[index + 1] = {glm::vec2(cx, cy), ColorIndex};

                    float new_cosA = cosA * cosStep - sinA * sinStep;
                    float new_sinA = sinA * cosStep + cosA * sinStep;
                    cosA = new_cosA;
                    sinA = new_sinA;
                }
            } else {
                for (unsigned int i = 0; i < InternalPointCount; ++i) {
                    float ox = outer_radius * cosA + cx;
                    float oy = outer_radius * sinA + cy;

                    float ix = inner_radius * cosA + cx;
                    float iy = inner_radius * sinA + cy;

                    unsigned int index = i * 2;

                    RenderPipelineVertexData[index] = {glm::vec2(ox, oy), ColorIndex};
                    RenderPipelineVertexData[index + 1] = {glm::vec2(ix, iy), ColorIndex};

                    float new_cosA = cosA * cosStep - sinA * sinStep;
                    float new_sinA = sinA * cosStep + cosA * sinStep;
                    cosA = new_cosA;
                    sinA = new_sinA;
                }
            }

            // Close the shape by repeating the first pair
            RenderPipelineVertexData[vertexCount - 2] = RenderPipelineVertexData[0];
            RenderPipelineVertexData[vertexCount - 1] = RenderPipelineVertexData[1];
        }

        PMMA::RenderPipelineCore->AddObject(*RenderPipelineData, RenderPipelineCompatible);
    } else {
        if (Changed) {
            // Calculate data and add to buffers
        }
        // Do NOTHING.
    }
}

void CPP_RadialPolygonShape::InternalRender() {
    // Left intentionally blank for now
}
