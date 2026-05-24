#include "PMMA_Core.hpp"

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_RadialPolygonShape::Render() {
    PMMA_Core::RenderPipelineCore->Add(this);
    ColorDataChanged = false;
    ShapePropertyChanged = false;
}