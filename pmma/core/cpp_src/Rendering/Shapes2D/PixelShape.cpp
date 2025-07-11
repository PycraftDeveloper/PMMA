#include "PMMA_Core.hpp"

using namespace std;

CPP_PixelShape::CPP_PixelShape() {
    ShapeCentreFormat = new CPP_DisplayCoordinateFormat();
    ID = PMMA::ClassObject_ID_System++;
}

void CPP_PixelShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    if (!ShapeCentreFormat->GetSet()) {
        throw std::runtime_error("Shape has no center not set");
    }
    glm::vec2 ShapeCentre = ShapeCentreFormat->GetDisplayCoordinate();

    Changed = Changed || ShapeCentreFormat->GetChangedToggle();

    if (ShapeCentre.x < 0 ||
            ShapeCentre.x > DisplayWidth ||
            ShapeCentre.y < 0 ||
            ShapeCentre.y > DisplayHeight) {
        return;
    }

    if (RenderPipelineColorData.w == 0) { // Return if shape not visible
        return;
    }

    GLuint newColorIndex = PMMA::RenderPipelineCore->Get_Shape2D_ColorIndex();
    if (newColorIndex != ColorIndex) {
        Changed = true;
        ColorIndex = newColorIndex;
    }

    if (Changed) {
        RenderPipelineVertexData.resize(4);
        float x = ShapeCentre.x;
        float y = ShapeCentre.y;
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
