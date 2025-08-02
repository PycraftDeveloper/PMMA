#include "PMMA_Core.hpp"

using namespace std;

CPP_PolygonShape::CPP_PolygonShape() {
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA::ClassObject_ID_System++;
}

void CPP_PolygonShape::Render(float ShapeQuality) {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    if (!ColorFormat->GetSet()) {
        throw std::runtime_error("Shape has no color set");
    }

    Changed = Changed ||
                ColorFormat->GetChangedToggle();

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

            RenderPipelineVertexData.resize(segmentCount * 6);

            for (unsigned int i = 0; i < segmentCount; i++) {
                unsigned int index = i * 6;
                glm::vec2 P0 = ShapePoints[i];
                glm::vec2 P1 = ShapePoints[(i + 1) % ShapePoints.size()];

                // Apply rotation to both
                glm::vec2 local0 = P0 - Center;
                glm::vec2 local1 = P1 - Center;

                glm::vec2 rot0 = {
                    local0.x * RotationCos - local0.y * RotationSin,
                    local0.x * RotationSin + local0.y * RotationCos
                };
                glm::vec2 rot1 = {
                    local1.x * RotationCos - local1.y * RotationSin,
                    local1.x * RotationSin + local1.y * RotationCos
                };

                P0 = Center + rot0;
                P1 = Center + rot1;

                // Direction and normal
                glm::vec2 D = glm::normalize(P1 - P0);
                glm::vec2 N = glm::vec2(-D.y, D.x);  // Perpendicular

                glm::vec2 A = P0 + N * HalfWidth;
                glm::vec2 B = P0 - N * HalfWidth;
                glm::vec2 C = P1 + N * HalfWidth;
                glm::vec2 Dp = P1 - N * HalfWidth;

                // Add two triangles: A-B-C and C-B-D
                RenderPipelineVertexData[index] = {A, ColorIndex};
                RenderPipelineVertexData[index + 1] = {B, ColorIndex};
                RenderPipelineVertexData[index + 2] = {C, ColorIndex};

                RenderPipelineVertexData[index + 3] = {C, ColorIndex};
                RenderPipelineVertexData[index + 4] = {B, ColorIndex};
                RenderPipelineVertexData[index + 5] = {Dp, ColorIndex};
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
