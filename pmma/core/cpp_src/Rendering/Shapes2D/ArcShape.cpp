#include "PMMA_Core.hpp"

using namespace std;

CPP_ArcShape::CPP_ArcShape() {
    Logger = new CPP_Logger();
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
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
            static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality * angle_scale));
    }
    return PointCount;
}

void CPP_ArcShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    if (!ShapeCenterFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `Arc.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Arc.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!StartAngleSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no start angle set, please use `Arc.set_start_angle` to set it.");
        throw runtime_error("Shape has no start angle set");
    }

    if (!EndAngleSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no end angle set, please use `Arc.set_end_angle` to set it.");
        throw runtime_error("Shape has no end angle set");
    }

    if (!RadiusSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no radius set, please use `Arc.set_radius` to set it.");
        throw runtime_error("Shape has no radius set");
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

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);

    if (RenderPipelineCompatible) {
        if (ColorData[3] == 0) { // Return if shape not visible
            return;
        }

        bool ColorIndexChanged = false;
        float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = ColorIndex != 0;
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
                        static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality * angle_scale));
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

                    auto &v0 = Shape2D_RenderPipelineData[index];
                    v0.x = ox; v0.y = oy; v0.s = ColorIndex; v0.t = 0.0f;

                    auto &v1 = Shape2D_RenderPipelineData[index + 1];
                    v1.x = cx; v1.y = cy; v1.s = ColorIndex; v1.t = 0.0f;

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

                    auto &v0 = Shape2D_RenderPipelineData[index];
                    v0.x = ox; v0.y = oy; v0.s = ColorIndex; v0.t = 0.0f;

                    auto &v1 = Shape2D_RenderPipelineData[index + 1];
                    v1.x = cx; v1.y = cy; v1.s = ColorIndex; v1.t = 0.0f;

                    float new_cosA = cosA * cosStep - sinA * sinStep;
                    float new_sinA = sinA * cosStep + cosA * sinStep;
                    cosA = new_cosA;
                    sinA = new_sinA;
                }
            }
        }

        PMMA_Core::RenderPipelineCore->AddObject(this, RenderPipelineCompatible, ColorIndexChanged);
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
