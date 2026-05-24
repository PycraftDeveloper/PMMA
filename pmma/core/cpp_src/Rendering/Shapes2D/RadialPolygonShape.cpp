#include "PMMA_Core.hpp"

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = reinterpret_cast<uintptr_t>(this);
}

void CPP_RadialPolygonShape::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter->GetChangedToggle();
    }
    if (!ColorDataChanged) {
        ColorDataChanged = Color->GetChangedToggle();
    }

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter->Get(start_position);
        unsigned int radius = GetRadius() * 2;

        auto rpc = PMMA_Core::RenderPipelineCore;
        uint32_t packedZero = rpc->PackValues(0, 0);

        ShapeInstanceData.position = rpc->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = rpc->PackValues((uint16_t)radius, (uint16_t)radius);
        ShapeInstanceData.point_count_gradient_type = packedZero;
        ShapeInstanceData.rotation_shape_property = rpc->PackValues(static_cast<uint16_t>(GetRotation() * 182), 0);
        ShapeInstanceData.shape_type_width = rpc->PackValues(0, GetWidth());
        ShapeInstanceData.texture_position = packedZero;
        ShapeInstanceData.texture_size = packedZero;
    }

    PMMA_Core::RenderPipelineCore->Add(this);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}