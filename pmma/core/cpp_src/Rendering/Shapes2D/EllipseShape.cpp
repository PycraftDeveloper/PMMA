#include "PMMA_Core.hpp"

using namespace std;

CPP_EllipseShape::CPP_EllipseShape() {
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA::ClassObject_ID_System++;
}

void CPP_EllipseShape::Render(float ShapeQuality) {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (!ShapeCenterFormat->GetSet()) {
        throw std::runtime_error("Shape has no center not set");
    }

    if (!ColorFormat->GetSet()) {
        throw std::runtime_error("Shape has no color set");
    }

    glm::vec2 ShapeCenter = ShapeCenterFormat->Get();

    Changed = Changed ||
                ShapeCenterFormat->GetChangedToggle() ||
                ColorFormat->GetChangedToggle();

    if (ShapeCenter.x + HalfWidth < 0 ||
            ShapeCenter.x - HalfWidth > DisplayWidth ||
            ShapeCenter.y + HalfHeight < 0 ||
            ShapeCenter.y - HalfHeight > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    if (RenderPipelineCompatible) {
        if (ColorFormat->Get_rgba().r == 0.0f) { // Return if shape not visible
            return;
        }

        GLuint newColorIndex = PMMA::RenderPipelineCore->Get_Shape2D_ColorIndex();
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            unsigned int InternalPointCount = PointCount;
            unsigned int Radius = CPP_AdvancedMathematics::PythagoreanDistance(ShapeSize.x, ShapeSize.y);

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

            float cx = ShapeCenter.x;
            float cy = ShapeCenter.y;

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

                    RenderPipelineVertexData[i * 2 + 0] = {
                        {cx + x_rot_outer, cy + y_rot_outer}, ColorIndex};

                    // Inner point (ring)
                    float x_inner = a_inner * cosAngle;
                    float y_inner = b_inner * sinAngle;

                    float x_rot_inner = x_inner * cosRot - y_inner * sinRot;
                    float y_rot_inner = x_inner * sinRot + y_inner * cosRot;

                    RenderPipelineVertexData[i * 2 + 1] = {
                        {cx + x_rot_inner, cy + y_rot_inner}, ColorIndex};
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

                    RenderPipelineVertexData[i * 2 + 0] = {
                        {cx + x_rot_outer, cy + y_rot_outer}, ColorIndex};

                    // Filled ellipse: collapse inner to center
                    RenderPipelineVertexData[i * 2 + 1] = {{cx, cy}, ColorIndex};
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

void CPP_EllipseShape::InternalRender() {
    // Left intentionally blank for now
}
