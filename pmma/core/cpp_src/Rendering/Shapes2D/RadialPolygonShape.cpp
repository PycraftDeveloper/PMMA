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
    int DisplaySize[2];
    PMMA_Core::DisplayInstance->GetSize(DisplaySize);

    if (!ShapeCenterFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `RadialPolygon.shape_center` API to set it.");
        throw std::runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `RadialPolygon.shape_color` API to set it.");
        throw std::runtime_error("Shape has no color set");
    }

    if (!RadiusSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no radius set, please use `RadialPolygon.set_radius` to set it.");
        throw std::runtime_error("Shape has no radius set");
    }

    float ShapeCenter[2];
    ShapeCenterFormat->Get(ShapeCenter);

    VertexDataChanged = VertexDataChanged ||
        ShapeCenterFormat->GetChangedToggle() ||
        PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenter[0] + Radius < 0 ||
        ShapeCenter[0] - Radius > DisplaySize[0] ||
        ShapeCenter[1] + Radius < 0 ||
        ShapeCenter[1] - Radius > DisplaySize[1]) {
        return; // outside screen, skip
    }

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);
    ColorDataChanged = ColorDataChanged || ColorFormat->GetInternalChangedToggle();

    if (ColorData[3] == 0) {
        return; // invisible
    }

    bool ColorIndexChanged = false;
    float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);
    if (newColorIndex != ColorIndex) {
        ColorIndexChanged = true;
        VertexDataChanged = true;
        ColorIndex = newColorIndex;
    }

    if (!VertexDataChanged) {
        PMMA_Core::RenderPipelineCore->Add_2D_Shape_Object(this, true, ColorIndexChanged);
        return;
    }

    // --- Compute radial polygon geometry ---
    unsigned int InternalPointCount = PointCount;
    float minAngle = asin(1.0f / Radius);
    unsigned int MaxPoints = std::max(3, static_cast<int>(1 + (CPP_Constants::TAU / minAngle) * PMMA_Registry::CurrentShapeQuality));
    if (InternalPointCount > MaxPoints || InternalPointCount < 3) {
        InternalPointCount = MaxPoints;
    }
    float angleStep = CPP_Constants::TAU / InternalPointCount;

    unsigned int outer_radius = Radius;
    unsigned int inner_radius = Width == 0 ? 0 : std::max(0, static_cast<int>(Radius) - static_cast<int>(Width) * 2);

    // --- Prepare vertex & index buffers ---
    if (inner_radius == 0) {
        // Simple filled polygon: center + outer ring
        Shape2D_RenderPipelineData.resize(InternalPointCount + 1);
        Shape2D_RenderPipelineIndices.resize(InternalPointCount * 3);

        Vertex* v = Shape2D_RenderPipelineData.data();

        float angle = Rotation;
        float cosStep = std::cos(angleStep);
        float sinStep = std::sin(angleStep);
        float cosA = std::cos(angle);
        float sinA = std::sin(angle);

        // Center vertex
        v[0].x = ShapeCenter[0];
        v[0].y = ShapeCenter[1];
        v[0].s = ColorIndex;

        // Outer vertices
        for (unsigned int i = 0; i < InternalPointCount; ++i) {
            v[i + 1].x = ShapeCenter[0] + outer_radius * cosA;
            v[i + 1].y = ShapeCenter[1] + outer_radius * sinA;
            v[i + 1].s = ColorIndex;

            float new_cosA = cosA * cosStep - sinA * sinStep;
            float new_sinA = sinA * cosStep + cosA * sinStep;
            cosA = new_cosA;
            sinA = new_sinA;
        }

        // Generate indices (fan)
        for (unsigned int i = 0; i < InternalPointCount; ++i) {
            unsigned int next = (i + 1) % InternalPointCount;
            Shape2D_RenderPipelineIndices[i * 3 + 0] = 0;       // center
            Shape2D_RenderPipelineIndices[i * 3 + 1] = i + 1;   // current outer
            Shape2D_RenderPipelineIndices[i * 3 + 2] = next + 1; // next outer
        }
    } else {
        // Ring: outer + inner vertices
        Shape2D_RenderPipelineData.resize(InternalPointCount * 2);
        Shape2D_RenderPipelineIndices.resize(InternalPointCount * 6);

        Vertex* v = Shape2D_RenderPipelineData.data();

        float angle = Rotation;
        float cosStep = std::cos(angleStep);
        float sinStep = std::sin(angleStep);
        float cosA = std::cos(angle);
        float sinA = std::sin(angle);

        for (unsigned int i = 0; i < InternalPointCount; ++i) {
            // Outer vertex
            v[i * 2 + 0].x = ShapeCenter[0] + outer_radius * cosA;
            v[i * 2 + 0].y = ShapeCenter[1] + outer_radius * sinA;
            v[i * 2 + 0].s = ColorIndex;

            // Inner vertex
            v[i * 2 + 1].x = ShapeCenter[0] + inner_radius * cosA;
            v[i * 2 + 1].y = ShapeCenter[1] + inner_radius * sinA;
            v[i * 2 + 1].s = ColorIndex;

            float new_cosA = cosA * cosStep - sinA * sinStep;
            float new_sinA = sinA * cosStep + cosA * sinStep;
            cosA = new_cosA;
            sinA = new_sinA;
        }

        // Generate indices (quad -> 2 triangles)
        for (unsigned int i = 0; i < InternalPointCount; ++i) {
            unsigned int next = (i + 1) % InternalPointCount;
            unsigned int outer0 = i * 2;
            unsigned int inner0 = i * 2 + 1;
            unsigned int outer1 = next * 2;
            unsigned int inner1 = next * 2 + 1;

            // Triangle 1
            Shape2D_RenderPipelineIndices[i * 6 + 0] = outer0;
            Shape2D_RenderPipelineIndices[i * 6 + 1] = inner0;
            Shape2D_RenderPipelineIndices[i * 6 + 2] = outer1;

            // Triangle 2
            Shape2D_RenderPipelineIndices[i * 6 + 3] = outer1;
            Shape2D_RenderPipelineIndices[i * 6 + 4] = inner0;
            Shape2D_RenderPipelineIndices[i * 6 + 5] = inner1;
        }
    }

    PMMA_Core::RenderPipelineCore->Add_2D_Shape_Object(this, true, ColorIndexChanged);

    VertexDataChanged = false;
    ColorDataChanged = false;
}

void CPP_RadialPolygonShape::InternalRender() {
    // Left intentionally blank for now
}
