#include "PMMA_Core.hpp"

using namespace std;

CPP_PixelShape::CPP_PixelShape() {
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_PixelShape::Render() {
    int DisplaySize[2];
    PMMA_Core::DisplayInstance->GetSize(DisplaySize);

    if (!ShapeCenterFormat->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `Pixel.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Pixel.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    float ShapeCenter[2];
    ShapeCenterFormat->Get(ShapeCenter);

    VertexDataChanged = VertexDataChanged ||
                ShapeCenterFormat->GetChangedToggle() ||
                PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenter[0] + 0.5f < 0 ||
            ShapeCenter[0] - 0.5f > DisplaySize[0] ||
            ShapeCenter[1] + 0.5f < 0 ||
            ShapeCenter[1] - 0.5f > DisplaySize[1]) {
        return;
    }

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);

    if (ColorData[3] == 0) { // Return if shape not visible
        return;
    }

    ColorDataChanged = ColorDataChanged || ColorFormat->GetInternalChangedToggle();

    bool ColorIndexChanged = false;
    float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

    if (newColorIndex != ColorIndex) {
        ColorIndexChanged = true;
        VertexDataChanged = true;
        ColorIndex = newColorIndex;
    }

    if (VertexDataChanged) {
        Shape2D_RenderPipelineData.resize(4);
        float x = ShapeCenter[0];
        float y = ShapeCenter[1];

        auto &v0 = Shape2D_RenderPipelineData[0];
        v0.x = x - 0.5f; v0.y = y - 0.5f; v0.s = ColorIndex;

        auto &v1 = Shape2D_RenderPipelineData[1];
        v1.x = x + 0.5f; v1.y = y - 0.5f; v1.s = ColorIndex;

        auto &v2 = Shape2D_RenderPipelineData[2];
        v2.x = x - 0.5f; v2.y = y + 0.5f; v2.s = ColorIndex;

        auto &v3 = Shape2D_RenderPipelineData[3];
        v3.x = x + 0.5f; v3.y = y + 0.5f; v3.s = ColorIndex;
    }
    PMMA_Core::RenderPipelineCore->Add_2D_Shape_Object(this, true, ColorIndexChanged);

    VertexDataChanged = false;
    ColorDataChanged = false;
}

void CPP_PixelShape::InternalRender() {
    // Left intentionally blank
}
