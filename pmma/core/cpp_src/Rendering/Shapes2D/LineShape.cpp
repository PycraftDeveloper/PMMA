#include "PMMA_Core.hpp"

using namespace std;

CPP_LineShape::CPP_LineShape() {
    Logger = new CPP_Logger();
    ShapeStart = new CPP_DisplayCoordinateFormat();
    ShapeEnd = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_LineShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Line.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!ShapeStart->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no start position set, please use the `Line.shape_start` \
API to set it.");
        throw runtime_error("Shape start position not set");
    }

    if (!ShapeEnd->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no end position set, please use the `Line.shape_end` \
API to set it.");
        throw runtime_error("Shape end position not set");
    }

    Changed = Changed ||
                ShapeStart->GetChangedToggle() ||
                ShapeEnd->GetChangedToggle();

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
            glm::vec2 StartPosition = ShapeStart->Get();
            glm::vec2 EndPosition = ShapeEnd->Get();

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

            Shape2D_RenderPipelineData.resize(4);
            Shape2D_RenderPipelineData[0] = {{RotatedStart - Normal}, ColorIndex};
            Shape2D_RenderPipelineData[1] = {{RotatedStart + Normal}, ColorIndex};
            Shape2D_RenderPipelineData[2] = {{RotatedEnd - Normal}, ColorIndex};
            Shape2D_RenderPipelineData[3] = {{RotatedEnd + Normal}, ColorIndex};
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

void CPP_LineShape::InternalRender() {
    // Left intentionally blank for now
}
