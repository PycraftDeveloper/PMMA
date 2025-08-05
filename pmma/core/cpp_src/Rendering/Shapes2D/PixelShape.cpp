#include "PMMA_Core.hpp"

using namespace std;

CPP_PixelShape::CPP_PixelShape() {
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_PixelShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    if (!ShapeCenterFormat->GetSet()) {
        throw std::runtime_error("Shape has no center not set");
    }

    if (!ColorFormat->GetSet()) {
        throw std::runtime_error("Shape has no color set");
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

    if (ColorFormat->Get_rgba().a == 0.0f) { // Return if shape not visible
        return;
    }

    bool ColorIndexChanged = false;
    GLuint newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorFormat->Get_rgba(), ID);

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
