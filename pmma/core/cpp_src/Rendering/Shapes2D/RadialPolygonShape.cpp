#include "PMMA_Core.hpp"

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = reinterpret_cast<uintptr_t>(this);
}

void CPP_RadialPolygonShape::Render() {
    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter->Get(start_position);
        unsigned int radius = GetRadius() * 2;

        // Existing packing logic
        ShapeInstanceData.position = PMMA_Core::RenderPipelineCore->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA_Core::RenderPipelineCore->PackValues((uint16_t)radius, (uint16_t)radius);
        ShapeInstanceData.point_count_gradient_type = PMMA_Core::RenderPipelineCore->PackValues(0, 0);
        ShapeInstanceData.rotation_shape_property = PMMA_Core::RenderPipelineCore->PackValues(GetRotation() * 182, 0);
        ShapeInstanceData.shape_type_width = PMMA_Core::RenderPipelineCore->PackValues(0, GetWidth());
        ShapeInstanceData.texture_position = PMMA_Core::RenderPipelineCore->PackValues(0, 0);
        ShapeInstanceData.texture_size = PMMA_Core::RenderPipelineCore->PackValues(0, 0);
    }

    PMMA_Core::RenderPipelineCore->Add(this);
    ColorDataChanged = false;
    ShapePropertyChanged = false;
}