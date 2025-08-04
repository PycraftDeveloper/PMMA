#include "PMMA_Core.hpp"

using namespace std;

CPP_ArcShape::CPP_ArcShape() {
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA::ClassObject_ID_System++;
}

unsigned int CPP_ArcShape::GetPointCount() {
    if (PointCount == 0) {
        float minAngle = asin(1.0f / Radius);
        float angle_scale = (EndAngle - StartAngle)/(CPP_Constants::TAU);
        if (angle_scale <= 0) {
            return 3;
        }
        if (angle_scale > 1) {
            angle_scale = 1;
        }
        return max(
            3,
            static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA::CurrentShapeQuality * angle_scale));
    }
    return PointCount;
}

void CPP_ArcShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    if (!ShapeCenterFormat->GetSet()) {
        throw std::runtime_error("Shape has no center not set");
    }

    if (!ColorFormat->GetSet()) {
        throw std::runtime_error("Shape has no color set");
    }

    glm::vec2 ShapeCenter = ShapeCenterFormat->Get();

    Changed = Changed ||
                ShapeCenterFormat->GetChangedToggle();

    if (ShapeCenter.x + Radius < 0 ||
            ShapeCenter.x - Radius > DisplayWidth ||
            ShapeCenter.y + Radius < 0 ||
            ShapeCenter.y - Radius > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    if (RenderPipelineCompatible) {
        if (ColorFormat->Get_rgba().a == 0.0f) { // Return if shape not visible
            return;
        }

        GLuint newColorIndex = PMMA::RenderPipelineCore->Shape2D_GetColorIndex(ColorFormat->Get_rgba(), ID);
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            unsigned int InternalPointCount = PointCount;
            if (PointCount == 0) {
                float minAngle = asin(1.0f / Radius);
                float angle_scale = (EndAngle - StartAngle)/(CPP_Constants::TAU);
                if (angle_scale <= 0) {
                    InternalPointCount = 3;
                } else {
                    if (angle_scale > 1) {
                        angle_scale = 1;
                    }
                    InternalPointCount = max(
                        3,
                        static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA::CurrentShapeQuality * angle_scale));
                }
            }

            float angleStep = (EndAngle - StartAngle) / InternalPointCount;

            unsigned int outer_radius = Radius;

            unsigned int inner_radius = max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);
            if (Width == 0) {
                inner_radius = 0;
            }

            // Reserve the exact number of vertices upfront
            size_t vertexCount = InternalPointCount * 2;
            Shape2D_RenderPipelineData.resize(vertexCount);

            float angle = Rotation + StartAngle;
            float cx = ShapeCenter.x;
            float cy = ShapeCenter.y;
            float cosStep = std::cos(angleStep);
            float sinStep = std::sin(angleStep);
            float cosA = std::cos(angle);
            float sinA = std::sin(angle);

            if (inner_radius == 0) {
                for (unsigned int i = 0; i < InternalPointCount; ++i) {
                    float ox = outer_radius * cosA + cx;
                    float oy = outer_radius * sinA + cy;

                    unsigned int index = i * 2;

                    Shape2D_RenderPipelineData[index] = {glm::vec2(ox, oy), ColorIndex};
                    Shape2D_RenderPipelineData[index + 1] = {glm::vec2(cx, cy), ColorIndex};

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

                    Shape2D_RenderPipelineData[index] = {glm::vec2(ox, oy), ColorIndex};
                    Shape2D_RenderPipelineData[index + 1] = {glm::vec2(ix, iy), ColorIndex};

                    float new_cosA = cosA * cosStep - sinA * sinStep;
                    float new_sinA = sinA * cosStep + cosA * sinStep;
                    cosA = new_cosA;
                    sinA = new_sinA;
                }
            }
        }

        PMMA::RenderPipelineCore->AddObject(this, RenderPipelineCompatible);
    } else {
        if (Changed) {
            // Calculate data and add to buffers, Left intentionally blank for now
        }
        // Do NOTHING.
    }

    Changed = false;
}

void CPP_ArcShape::InternalRender() {
    // Left intentionally blank for now
}
