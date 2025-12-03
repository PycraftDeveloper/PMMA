#include "PMMA_Core.hpp"

using namespace std;

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    Logger = new CPP_Logger();
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

unsigned int CPP_RadialPolygonShape::GetPointCount() {
    if (!RadiusSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no radius set, please use `RadialPolygon.set_radius` to set it.");
        throw runtime_error("Shape has no radius set");
    }

    if (PointCount == 0) {
        float minAngle = asin(1.0f / Radius);
        return max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
    }
    return PointCount;
}

void CPP_RadialPolygonShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    if (!ShapeCenterFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `RadialPolygon.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `RadialPolygon.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!RadiusSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no radius set, please use `RadialPolygon.set_radius` to set it.");
        throw runtime_error("Shape has no radius set");
    }

    float ShapeCenter[2];
    ShapeCenterFormat->Get(ShapeCenter);

    VertexDataChanged = VertexDataChanged ||
                ShapeCenterFormat->GetChangedToggle() ||
                PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenter[0] + Radius < 0 ||
            ShapeCenter[0] - Radius > DisplayWidth ||
            ShapeCenter[1] + Radius < 0 ||
            ShapeCenter[1] - Radius > DisplayHeight) {
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
            ColorIndexChanged = true;
            VertexDataChanged = true;
            ColorIndex = newColorIndex;
        }

        if (VertexDataChanged) {
            unsigned int InternalPointCount = PointCount;
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
            Shape2D_RenderPipelineData.resize(vertexCount);

            float angle = Rotation;
            float cx = ShapeCenter[0];
            float cy = ShapeCenter[1];
            float cosStep = std::cos(angleStep);
            float sinStep = std::sin(angleStep);
            float cosA = std::cos(angle);
            float sinA = std::sin(angle);

            Vertex* v = Shape2D_RenderPipelineData.data();
            if (inner_radius == 0) {
                auto &v1 = Shape2D_RenderPipelineData[1];
                v1.x = cx; v1.y = cy; v1.s = ColorIndex;

                const Vertex Center = Shape2D_RenderPipelineData[1];
                for (unsigned int i = 0; i < InternalPointCount; ++i) {
                    v[0].x = outer_radius * cosA + cx;
                    v[0].y = outer_radius * sinA + cy;
                    v[0].s = ColorIndex;

                    v[1] = Center; // center vertex
                    v += 2;

                    float new_cosA = cosA * cosStep - sinA * sinStep;
                    float new_sinA = sinA * cosStep + cosA * sinStep;
                    cosA = new_cosA;
                    sinA = new_sinA;
                }
            } else {
                for (unsigned int i = 0; i < InternalPointCount; ++i) {
                    v[0].x = outer_radius * cosA + cx;
                    v[0].y = outer_radius * sinA + cy;
                    v[0].s = ColorIndex;

                    v[1].x = inner_radius * cosA + cx;
                    v[1].y = inner_radius * sinA + cy;
                    v[1].s = ColorIndex;

                    v += 2;

                    float new_cosA = cosA * cosStep - sinA * sinStep;
                    float new_sinA = sinA * cosStep + cosA * sinStep;
                    cosA = new_cosA;
                    sinA = new_sinA;
                }
            }

            // Close the shape by repeating the first pair
            Shape2D_RenderPipelineData[vertexCount - 2] = Shape2D_RenderPipelineData[0];
            Shape2D_RenderPipelineData[vertexCount - 1] = Shape2D_RenderPipelineData[1];
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

void CPP_RadialPolygonShape::InternalRender() {
    // Left intentionally blank for now
}
