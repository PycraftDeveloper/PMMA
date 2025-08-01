#include "PMMA_Core.hpp"

using namespace std;

CPP_LineShape::CPP_LineShape() {
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA::ClassObject_ID_System++;
}

void CPP_LineShape::Render(float ShapeQuality) {
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

        GLuint newColorIndex = PMMA::RenderPipelineCore->Get_Shape2D_ColorIndex(ColorFormat->Get_rgba(), 4);
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            unsigned int InternalWidth = Width;

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            glm::vec2 LineCenter = {(StartPosition.x + EndPosition.x) / 2, (StartPosition.y + EndPosition.y) / 2};

            glm::vec2 TranslatedStart = {StartPosition.x - LineCenter.x, StartPosition.y - LineCenter.y};
            glm::vec2 RotatedStart = {
                LineCenter.x + (RotationCos * TranslatedStart.x - RotationSin * TranslatedStart.y),
                LineCenter.y + (RotationSin * TranslatedStart.x + RotationCos * TranslatedStart.y)};

            glm::vec2 TranslatedEnd = {EndPosition.x - LineCenter.x, EndPosition.y - LineCenter.y};
            glm::vec2 RotatedEnd = {
                LineCenter.x + (RotationCos * TranslatedEnd.x - RotationSin * TranslatedEnd.y),
                LineCenter.y + (RotationSin * TranslatedEnd.x + RotationCos * TranslatedEnd.y)};

            glm::vec2 Direction = RotatedEnd - RotatedStart;
            Direction = glm::normalize(Direction);

            glm::vec2 Normal = {-Direction.y, Direction.x};
            Normal *= 0.5f * InternalWidth;

            RenderPipelineVertexData.resize(4);
            RenderPipelineVertexData[0] = {{RotatedStart - Normal}, ColorIndex};
            RenderPipelineVertexData[1] = {{RotatedStart + Normal}, ColorIndex};
            RenderPipelineVertexData[2] = {{RotatedEnd - Normal}, ColorIndex};
            RenderPipelineVertexData[3] = {{RotatedEnd + Normal}, ColorIndex};
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

void CPP_LineShape::InternalRender() {
    // Left intentionally blank for now
}
