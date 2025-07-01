#include <cmath>

#include "RadialPolygonShape.hpp"
#include "RenderPipelineManager.hpp"
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

    bool RenderPipelineCompatible = (HasAlpha == false && UsingGradients == false);

    if (RenderPipelineCompatible) {
        RenderPipelineVertexData.clear();
        RenderPipelineColorData = ColorData[0];

        unsigned int InternalPointCount = PointCount;
        if (PointCount == 0) {
            float minAngle = asin(1.0f / Radius);
            InternalPointCount = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * ShapeQuality));
        }

        GLuint ColorIndex = PMMA::RenderPipelineCore->GetColorIndex();
        float angleStep = CPP_Constants::TAU / InternalPointCount;

        unsigned int outer_radius = Radius;
        unsigned int inner_radius = max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);

        // Reserve the exact number of vertices upfront
        size_t vertexCount = InternalPointCount * 2 + 2;
        RenderPipelineVertexData.reserve(vertexCount);

        float angle = Rotation;
        float cx = ShapeCentre.x;
        float cy = ShapeCentre.y;

        if (inner_radius == 0) {
            for (unsigned int i = 0; i < InternalPointCount; ++i) {
                float cosA = std::cos(angle);
                float sinA = std::sin(angle);

                float ox = outer_radius * cosA + cx;
                float oy = outer_radius * sinA + cy;

                RenderPipelineVertexData.emplace_back(glm::vec2(ox, oy), ColorIndex);
                RenderPipelineVertexData.emplace_back(glm::vec2(cx, cy), ColorIndex);

                angle += angleStep;
            }
        } else {
            for (unsigned int i = 0; i < InternalPointCount; ++i) {
                float cosA = cos(angle);
                float sinA = sin(angle);

                float ox = outer_radius * cosA + cx;
                float oy = outer_radius * sinA + cy;

                float ix = inner_radius * cosA + cx;
                float iy = inner_radius * sinA + cy;

                RenderPipelineVertexData.emplace_back(glm::vec2(ox, oy), ColorIndex);
                RenderPipelineVertexData.emplace_back(glm::vec2(ix, iy), ColorIndex);

                angle += angleStep;
            }
        }

        // Close the shape by repeating the first pair
        RenderPipelineVertexData.emplace_back(RenderPipelineVertexData[0]);
        RenderPipelineVertexData.emplace_back(RenderPipelineVertexData[1]);

        PMMA::RenderPipelineCore->AddObject(RenderPipelineData, RenderPipelineCompatible);
    } else {
        VertexData.clear();
    }
}

void CPP_RadialPolygonShape::InternalRender() {
    // Left intentionally blank for now
}
