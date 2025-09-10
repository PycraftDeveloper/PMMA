#include "PMMA_Core.hpp"

using namespace std;

CPP_PixelShape::CPP_PixelShape() {
    Logger = new CPP_Logger();
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_PixelShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    if (!ShapeCenterFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `Pixel.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Pixel.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    glm::vec2 ShapeCenter = ShapeCenterFormat->Get();

    Changed = Changed ||
                ShapeCenterFormat->GetChangedToggle();

    if (ShapeCenter.x < 0 ||
            ShapeCenter.x > DisplayWidth ||
            ShapeCenter.y < 0 ||
            ShapeCenter.y > DisplayHeight) {
        return;
    }

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);

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
        Shape2D_RenderPipelineData.resize(4);
        float x = ShapeCenter.x;
        float y = ShapeCenter.y;
        Shape2D_RenderPipelineData[0] = {{x - 0.5f, y - 0.5f}, ColorIndex}; // Top-left
        Shape2D_RenderPipelineData[1] = {{x + 0.5f, y - 0.5f}, ColorIndex}; // Top-right
        Shape2D_RenderPipelineData[2] = {{x - 0.5f, y + 0.5f}, ColorIndex}; // Bottom-left
        Shape2D_RenderPipelineData[3] = {{x + 0.5f, y + 0.5f}, ColorIndex}; // Bottom-right
    }
    PMMA_Core::RenderPipelineCore->AddObject(this, true, ColorIndexChanged);

    Changed = false;
}

void CPP_PixelShape::InternalRender() {
    // Left intentionally blank
}
