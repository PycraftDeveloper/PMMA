#include "PMMA_Core.hpp"

using namespace std;

CPP_EllipseShape::CPP_EllipseShape() {
    Logger = new CPP_Logger();
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

unsigned int CPP_EllipseShape::GetPointCount() {
    if (PointCount == 0) {
        unsigned int Radius = CPP_AdvancedMathematics::PythagoreanDistance(ShapeSize.x, ShapeSize.y);
        float minAngle = asin(1.0f / Radius);
        return max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
    }
    return PointCount;
}

void CPP_EllipseShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (!ShapeCenterFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `Ellipse.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Ellipse.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!SizeSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no size set, please use `Ellipse.`set_size` to set it.");
        throw runtime_error("Shape has no size set");
    }

    float ShapeCenter[2];
    ShapeCenterFormat->Get(ShapeCenter);

    VertexDataChanged = VertexDataChanged ||
                ShapeCenterFormat->GetChangedToggle() ||
                PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenter[0] + HalfWidth < 0 ||
            ShapeCenter[0] - HalfWidth > DisplayWidth ||
            ShapeCenter[1] + HalfHeight < 0 ||
            ShapeCenter[1] - HalfHeight > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);

    ColorDataChanged = ColorDataChanged || ColorFormat->GetInternalChangedToggle();

    if (RenderPipelineCompatible) {
        if (ColorData[3] == 0) { // Return if shape not visible
            return;
        }

        bool ColorIndexChanged = false;
        float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = ColorIndex != 0;
            VertexDataChanged = true;
            ColorIndex = newColorIndex;
        }

        if (VertexDataChanged) {
            unsigned int InternalPointCount = PointCount;
            unsigned int Radius = CPP_AdvancedMathematics::PythagoreanDistance(ShapeSize.x, ShapeSize.y);

            if (PointCount == 0) {
                float minAngle = asin(1.0f / Radius);
                InternalPointCount = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
            }
            float angleStep = CPP_Constants::TAU / InternalPointCount;

            unsigned int outer_radius = Radius;

            unsigned int inner_radius = max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);
            if (Width == 0) {
                inner_radius = 0;
            }

            // Reserve the exact number of vertices upfront
            size_t vertexCount = InternalPointCount * 2 + 2;
            Shape2D_RenderPipelineData.resize(vertexCount);

            float cx = ShapeCenter[0];
            float cy = ShapeCenter[1];

            float a_outer = ShapeSize.x / 2.0f; // semi-major axis (horizontal)
            float b_outer = ShapeSize.y / 2.0f; // semi-minor axis (vertical)

            float a_inner = (Width == 0) ? 0.0f : a_outer - Width;
            float b_inner = (Width == 0) ? 0.0f : b_outer - Width;

            float cosRot = cos(Rotation);
            float sinRot = sin(Rotation);

            if (Width > 0) {
                for (unsigned int i = 0; i <= InternalPointCount; ++i) {
                    float angle = i * angleStep;

                    float cosAngle = cos(angle);
                    float sinAngle = sin(angle);

                    // Outer point
                    float x_outer = a_outer * cosAngle;
                    float y_outer = b_outer * sinAngle;

                    float x_rot_outer = x_outer * cosRot - y_outer * sinRot;
                    float y_rot_outer = x_outer * sinRot + y_outer * cosRot;

                    auto &v0 = Shape2D_RenderPipelineData[i * 2];
                    v0.x = cx + x_rot_outer; v0.y = cy + y_rot_outer; v0.s = ColorIndex;

                    // Inner point (ring)
                    float x_inner = a_inner * cosAngle;
                    float y_inner = b_inner * sinAngle;

                    float x_rot_inner = x_inner * cosRot - y_inner * sinRot;
                    float y_rot_inner = x_inner * sinRot + y_inner * cosRot;

                    auto &v1 = Shape2D_RenderPipelineData[i * 2 + 1];
                    v1.x = cx + x_rot_inner; v1.y = cy + y_rot_inner; v1.s = ColorIndex;
                }
            } else {
                for (unsigned int i = 0; i <= InternalPointCount; ++i) {
                    float angle = i * angleStep;

                    float cosAngle = cos(angle);
                    float sinAngle = sin(angle);

                    // Outer point
                    float x_outer = a_outer * cosAngle;
                    float y_outer = b_outer * sinAngle;

                    float x_rot_outer = x_outer * cosRot - y_outer * sinRot;
                    float y_rot_outer = x_outer * sinRot + y_outer * cosRot;

                    auto &v0 = Shape2D_RenderPipelineData[i * 2];
                    v0.x = cx + x_rot_outer; v0.y = cy + y_rot_outer; v0.s = ColorIndex;

                    auto &v1 = Shape2D_RenderPipelineData[i * 2 + 1];
                    v1.x = cx; v1.y = cy; v1.s = ColorIndex;
                }
            }
        }

        PMMA_Core::RenderPipelineCore->AddObject(this, RenderPipelineCompatible, ColorIndexChanged);
    } else {
        if (VertexDataChanged) {
            // Calculate data and add to buffers, Left intentionally blank for now
        }
        // Do NOTHING.
    }

    VertexDataChanged = false;
    ColorDataChanged = false;
}

void CPP_EllipseShape::InternalRender() {
    // Left intentionally blank for now
}
