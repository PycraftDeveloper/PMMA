#include "PMMA_Core.hpp"

using namespace std;

CPP_PolygonShape::CPP_PolygonShape() {
    Logger = new CPP_Logger();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_PolygonShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Polygon.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!PointsSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no points set, please use `Polygon.set_points` to set it."
        );
        throw runtime_error("Shape has no points set");
    }

    Changed = Changed;

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
        GLuint newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = ColorIndex != 0;
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            unsigned int segmentCount = ShapePoints.size();
            if (!Closed) {
                segmentCount--;
            }

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            glm::vec2 Center = {0.0f, 0.0f};

            for (unsigned int i = 0; i < ShapePoints.size(); i++) {
                Center += ShapePoints[i];
            }

            Center /= ShapePoints.size(); // calculate center using averages

            float HalfWidth = Width * 0.5f;

            Shape2D_RenderPipelineData.resize(segmentCount * 6);

            for (unsigned int i = 0; i < segmentCount; i++) {
                float P0[2], P1[2], local0[2], local1[2], rot0[2], rot1[2], D[2], N[2], A[2], B[2], C[2], Dp[2], PDiff[2];
                unsigned int index = i * 6;

                P0[0] = ShapePoints[i].x;
                P0[1] = ShapePoints[i].y;

                P1[0] = ShapePoints[(i + 1) % ShapePoints.size()].x;
                P1[1] = ShapePoints[(i + 1) % ShapePoints.size()].y;

                // Apply rotation to both
                local0[0] = P0[0] - Center.x;
                local0[1] = P0[1] - Center.y;

                local1[0] = P1[0] - Center.x;
                local1[1] = P1[1] - Center.y;

                rot0[0] = local0[0] * RotationCos - local0[1] * RotationSin;
                rot0[1] = local0[0] * RotationSin + local0[1] * RotationCos;

                rot1[0] = local1[0] * RotationCos - local1[1] * RotationSin;
                rot1[1] = local1[0] * RotationSin + local1[1] * RotationCos;

                P0[0] = Center.x + rot0[0];
                P0[1] = Center.y + rot0[1];

                P1[0] = Center.x + rot1[0];
                P1[1] = Center.y + rot1[1];

                PDiff[0] = P1[0] - P0[0];
                PDiff[1] = P1[1] - P0[1];

                CPP_AdvancedMathematics::ArrayNormalize_2D(PDiff, D);
                N[0] = -D[1];
                N[1] = D[0];

                A[0] = P0[0] + N[0] * HalfWidth;
                A[1] = P0[1] + N[1] * HalfWidth;

                B[0] = P0[0] - N[0] * HalfWidth;
                B[0] = P0[1] - N[1] * HalfWidth;

                C[0] = P1[0] + N[0] * HalfWidth;
                C[1] = P1[1] + N[1] * HalfWidth;

                Dp[0] = P1[0] - N[0] * HalfWidth;
                Dp[1] = P1[1] - N[1] * HalfWidth;

                // Add two triangles: A-B-C and C-B-D
                Shape2D_RenderPipelineData[index] = {A[0], A[1], ColorIndex, 0};
                Shape2D_RenderPipelineData[index + 1] = {B[0], B[1], ColorIndex, 0};
                Shape2D_RenderPipelineData[index + 2] = {C[0], C[1], ColorIndex, 0};

                Shape2D_RenderPipelineData[index + 3] = {C[0], C[1], ColorIndex, 0};
                Shape2D_RenderPipelineData[index + 4] = {B[0], B[1], ColorIndex, 0};
                Shape2D_RenderPipelineData[index + 5] = {Dp[0], Dp[1], ColorIndex, 0};
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

void CPP_PolygonShape::InternalRender() {
    // Left intentionally blank for now
}
