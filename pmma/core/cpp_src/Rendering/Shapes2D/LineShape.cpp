#include "PMMA_Core.hpp"

CPP_LineShape::CPP_LineShape() {
    ShapeStart = new CPP_DisplayCoordinate();
    ShapeEnd = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_LineShape::Render() {
    PMMA_Core::RenderPipelineCore->Add(this);
}
