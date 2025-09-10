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
        float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = ColorIndex != 0;
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            float StartPosition[2], EndPosition[2], LineCenter[2], TranslatedStart[2], TranslatedEnd[2], RotatedStart[2], RotatedEnd[2], Direction[2], Normal[2];
            ShapeStart->Get(StartPosition);
            ShapeEnd->Get(EndPosition);

            unsigned int InternalWidth = Width;

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            LineCenter[0] = (StartPosition[0] + EndPosition[0]) / 2;
            LineCenter[1] = (StartPosition[1] + EndPosition[1]) / 2;

            TranslatedStart[0] = StartPosition[0] - LineCenter[0];
            TranslatedStart[1] = StartPosition[1] - LineCenter[1];

            RotatedStart[0] = LineCenter[0] + (RotationCos * TranslatedStart[0] - RotationSin * TranslatedStart[1]);
            RotatedStart[1] = LineCenter[1] + (RotationSin * TranslatedStart[0] + RotationCos * TranslatedStart[1]);

            TranslatedEnd[0] = EndPosition[0] - LineCenter[0];
            TranslatedEnd[1] = EndPosition[1] - LineCenter[1];

            RotatedEnd[0] = LineCenter[0] + (RotationCos * TranslatedEnd[0] - RotationSin * TranslatedEnd[1]);
            RotatedEnd[1] = LineCenter[1] + (RotationSin * TranslatedEnd[0] + RotationCos * TranslatedEnd[1]);

            Direction[0] = RotatedEnd[0] - RotatedStart[0];
            Direction[1] = RotatedEnd[1] - RotatedStart[1];

            CPP_AdvancedMathematics::InPlaceArrayNormalize2D(Direction);

            Normal[0] = (-Direction[1]) * 0.5f * InternalWidth;
            Normal[1] = Direction[0] * 0.5f * InternalWidth;

            Shape2D_RenderPipelineData.resize(4);
            Shape2D_RenderPipelineData[0] = {RotatedStart[0] - Normal[0], RotatedStart[1] - Normal[1], ColorIndex, 0};
            Shape2D_RenderPipelineData[1] = {RotatedStart[0] + Normal[0], RotatedStart[1] + Normal[1], ColorIndex, 0};
            Shape2D_RenderPipelineData[2] = {RotatedEnd[0] - Normal[0], RotatedEnd[1] - Normal[1], ColorIndex, 0};
            Shape2D_RenderPipelineData[3] = {RotatedEnd[0] + Normal[0], RotatedEnd[1] + Normal[1], ColorIndex, 0};
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
