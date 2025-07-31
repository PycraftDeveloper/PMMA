#include "PMMA_Core.hpp"

using namespace std;

CPP_PixelShape::CPP_PixelShape() {
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA::ClassObject_ID_System++;
}

void CPP_PixelShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    if (!ShapeCenterFormat->GetSet()) {
        throw std::runtime_error("Shape has no center not set");
    }

    if (!ColorFormat->GetSet()) {
        throw std::runtime_error("Shape has no color set");
    }

    glm::vec2 ShapeCenter = ShapeCenterFormat->Get();

    Changed = Changed ||
                ShapeCenterFormat->GetChangedToggle() ||
                ColorFormat->GetChangedToggle();

    if (ShapeCenter.x < 0 ||
            ShapeCenter.x > DisplayWidth ||
            ShapeCenter.y < 0 ||
            ShapeCenter.y > DisplayHeight) {
        return;
    }

    if (ColorFormat->Get_rgba().r == 0.0f) { // Return if shape not visible
        return;
    }

    GLuint newColorIndex = PMMA::RenderPipelineCore->Get_Shape2D_ColorIndex();
    if (newColorIndex != ColorIndex) {
        Changed = true;
        ColorIndex = newColorIndex;
    }

    if (Changed) {
        RenderPipelineVertexData.resize(4);
        float x = ShapeCenter.x;
        float y = ShapeCenter.y;
        RenderPipelineVertexData[0] = {{x - 0.5f, y - 0.5f}, ColorIndex}; // Top-left
        RenderPipelineVertexData[1] = {{x + 0.5f, y - 0.5f}, ColorIndex}; // Top-right
        RenderPipelineVertexData[2] = {{x - 0.5f, y + 0.5f}, ColorIndex}; // Bottom-left
        RenderPipelineVertexData[3] = {{x + 0.5f, y + 0.5f}, ColorIndex}; // Bottom-right
    }
    PMMA::RenderPipelineCore->AddObject(this, true);

    Changed = false;
}

void CPP_PixelShape::InternalRender() {
    // Left intentionally blank
}
