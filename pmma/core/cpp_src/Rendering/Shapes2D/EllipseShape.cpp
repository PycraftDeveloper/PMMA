#include "Rendering/Shapes2D/EllipseShape.hpp"
#include "Display.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_EllipseShape::CPP_EllipseShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

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
    int DisplaySize[2];
    PMMA_Core::DisplayInstance->GetSize(DisplaySize);

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (!ShapeCenter->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no center set, please use the `Ellipse.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!Color->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no color set, please use the `Ellipse.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!SizeSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no size set, please use `Ellipse.`set_size` to set it.");
        throw runtime_error("Shape has no size set");
    }

    float ShapeCenterPosition[2];
    ShapeCenter->Get(ShapeCenterPosition);

    VertexDataChanged = VertexDataChanged ||
                ShapeCenter->GetChangedToggle() ||
                PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenterPosition[0] + HalfWidth < 0 ||
            ShapeCenterPosition[0] - HalfWidth > DisplaySize[0] ||
            ShapeCenterPosition[1] + HalfHeight < 0 ||
            ShapeCenterPosition[1] - HalfHeight > DisplaySize[1]) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    uint8_t ColorData[4];
    Color->Get_RGBA(ColorData);

    ColorDataChanged = ColorDataChanged || Color->GetInternalChangedToggle();

    if (RenderPipelineCompatible) {
        if (ColorData[3] == 0) { // Return if shape not visible
            return;
        }

        bool ColorIndexChanged = false;
        float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = true;
            VertexDataChanged = true;
            ColorIndex = newColorIndex;
        }

        if (VertexDataChanged) {
            unsigned int InternalPointCount = PointCount;
            unsigned int Radius = CPP_AdvancedMathematics::PythagoreanDistance(ShapeSize.x, ShapeSize.y);

            float minAngle = asin(1.0f / Radius);
            unsigned int MaxPoints = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
            if (InternalPointCount > MaxPoints || InternalPointCount < 3) {
                InternalPointCount = MaxPoints;
            }

            float angleStep = CPP_Constants::TAU / InternalPointCount;

            unsigned int outer_radius = Radius;

            unsigned int inner_radius = max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);
            if (Width == 0) {
                inner_radius = 0;
            }

            // Reserve the exact number of vertices upfront
            size_t vertexCount = InternalPointCount * 2 + 2;
            Shape2D_RenderPipelineVertices.resize(vertexCount);

            float cx = ShapeCenterPosition[0];
            float cy = ShapeCenterPosition[1];

            float a_outer = ShapeSize.x / 2.0f; // semi-major axis (horizontal)
            float b_outer = ShapeSize.y / 2.0f; // semi-minor axis (vertical)

            float a_inner = (Width == 0) ? 0.0f : a_outer - Width;
            float b_inner = (Width == 0) ? 0.0f : b_outer - Width;

            float cosRot = cos(Rotation);
            float sinRot = sin(Rotation);

            Vertex* v = Shape2D_RenderPipelineVertices.data();
            if (Width < 0) {
                auto &v1 = Shape2D_RenderPipelineVertices[1];
                v1.x = cx; v1.y = cy; v1.s = ColorIndex;

                const Vertex Center = Shape2D_RenderPipelineVertices[1];
                for (unsigned int i = 0; i <= InternalPointCount; ++i) {
                    float angle = i * angleStep;

                    float cosAngle = cos(angle);
                    float sinAngle = sin(angle);

                    // Outer point
                    float x_outer = a_outer * cosAngle;
                    float y_outer = b_outer * sinAngle;

                    float x_rot_outer = x_outer * cosRot - y_outer * sinRot;
                    float y_rot_outer = x_outer * sinRot + y_outer * cosRot;

                    auto &v1 = Shape2D_RenderPipelineVertices[i * 2 + 1];
                    v1.x = cx; v1.y = cy; v1.s = ColorIndex;

                    v[0].x = cx + x_rot_outer;
                    v[0].y = cy + y_rot_outer;
                    v[0].s = ColorIndex;

                    v[1] = Center; // center vertex

                    v += 2;
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

                    // Inner point (ring)
                    float x_inner = a_inner * cosAngle;
                    float y_inner = b_inner * sinAngle;

                    float x_rot_inner = x_inner * cosRot - y_inner * sinRot;
                    float y_rot_inner = x_inner * sinRot + y_inner * cosRot;

                    v[0].x = cx + x_rot_outer;
                    v[0].y = cy + y_rot_outer;
                    v[0].s = ColorIndex;

                    v[1].x = cx + x_rot_inner;
                    v[1].y = cy + y_rot_inner;
                    v[1].s = ColorIndex;

                    v += 2;
                }
            }
        }

        PMMA_Core::RenderPipelineCore->Add_2D_Shape_Object(this, RenderPipelineCompatible, ColorIndexChanged);
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
