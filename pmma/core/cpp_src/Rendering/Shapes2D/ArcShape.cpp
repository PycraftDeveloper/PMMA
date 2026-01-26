#include "PMMA_Core.hpp"

using namespace std;

CPP_ArcShape::CPP_ArcShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

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
    int DisplaySize[2];
    PMMA_Core::DisplayInstance->GetSize(DisplaySize);

    if (!ShapeCenter->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no center set, please use the `Arc.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!Color->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no color set, please use the `Arc.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!StartAngleSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no start angle set, please use `Arc.set_start_angle` to set it.");
        throw runtime_error("Shape has no start angle set");
    }

    if (!EndAngleSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no end angle set, please use `Arc.set_end_angle` to set it.");
        throw runtime_error("Shape has no end angle set");
    }

    if (!RadiusSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogError(
            30,
            "This shape has no radius set, please use `Arc.set_radius` to set it.");
        throw runtime_error("Shape has no radius set");
    }

    float ShapeCenterPosition[2];
    ShapeCenter->Get(ShapeCenterPosition);

    VertexDataChanged = VertexDataChanged ||
                ShapeCenter->GetChangedToggle() ||
                PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenterPosition[0] + Radius < 0 ||
            ShapeCenterPosition[0] - Radius > DisplaySize[0] ||
            ShapeCenterPosition[1] + Radius < 0 ||
            ShapeCenterPosition[1] - Radius > DisplaySize[1]) {
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
            if (PointCount < 3) {
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
            } else {
                float minAngle = asin(1.0f / Radius);
                unsigned int MaxPoints = max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
                if (InternalPointCount > MaxPoints) {
                    InternalPointCount = MaxPoints;
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
            Shape2D_RenderPipelineVertices.resize(vertexCount);

            float angle = Rotation + StartAngle;
            float cx = ShapeCenterPosition[0];
            float cy = ShapeCenterPosition[1];
            float cosStep = std::cos(angleStep);
            float sinStep = std::sin(angleStep);
            float cosA = std::cos(angle);
            float sinA = std::sin(angle);

            Vertex* v = Shape2D_RenderPipelineVertices.data();
            if (inner_radius == 0) {
                auto &v1 = Shape2D_RenderPipelineVertices[1];
                v1.x = cx; v1.y = cy; v1.s = ColorIndex;

                const Vertex Center = Shape2D_RenderPipelineVertices[1];
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

void CPP_ArcShape::InternalRender() {
    // Left intentionally blank for now
}
