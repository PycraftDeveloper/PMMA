#include "PMMA_Core.hpp"

using namespace std;

CPP_PolygonShape::CPP_PolygonShape() {
    ID = PMMA::ClassObject_ID_System++;
}

void CPP_PolygonShape::Render(float ShapeQuality) {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    bool RenderPipelineCompatible = (UsingGradients == false);

    if (RenderPipelineCompatible) {
        if (ColorData[0].w == 0) { // Return if shape not visible
            return;
        }

        GLuint newColorIndex = PMMA::RenderPipelineCore->Get_Shape2D_ColorIndex();
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            RenderPipelineColorData = ColorData[0];

            unsigned int InternalWidth = Width;

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            if (Closed) {
                RenderPipelineVertexData.reserve(2 + ShapePoints.size() * 2);
            } else {
                RenderPipelineVertexData.reserve(ShapePoints.size() * 2);
            }

            vector<glm::vec2> RawShapePoints;
            RawShapePoints.reserve(ShapePoints.size() * 2);

            glm::vec2 Center = {0.0f, 0.0f};

            for (unsigned int i = 0; i < ShapePoints.size(); i++) {
                int index = i * 2;
                RawShapePoints[index] = ShapePoints[i];
                RawShapePoints[index + 1] = {ShapePoints[i].x - InternalWidth, ShapePoints[i].y - InternalWidth};
                Center += ShapePoints[i];
            }

            Center /= ShapePoints.size();

            for (unsigned int i = 0; i < RawShapePoints.size(); i++) {
                glm::vec2 Point = RawShapePoints[i];
                Point -= Center;

                Point.x = (Point.x * RotationCos) - (Point.y * RotationSin);
                Point.y = (Point.x * RotationSin) + (Point.y * RotationCos);

                Point += Center;

                RenderPipelineVertexData[i] = {Point, ColorIndex};
            }

            if (Closed) {
                RenderPipelineVertexData[RenderPipelineVertexData.size() - 2] = RenderPipelineVertexData[0];
                RenderPipelineVertexData[RenderPipelineVertexData.size() - 1] = RenderPipelineVertexData[1];
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

void CPP_PolygonShape::InternalRender() {
    // Left intentionally blank for now
}
