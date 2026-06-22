#include "PMMA_Core.hpp"

void CPP_RectangleShape::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.Get(start_position);

        auto rpc = PMMA_Core::RenderPipelineCore;

        // Existing packing logic
        ShapeInstanceData.position = rpc->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = rpc->PackValues(ShapeSize[0], ShapeSize[1]);
        ShapeInstanceData.point_count_gradient_type = rpc->PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = rpc->PackValues(Rotation * 182, CornerRadius);
        ShapeInstanceData.shape_type_width = rpc->PackValues(1, Width);
        ShapeInstanceData.texture_position = rpc->PackValues(0, 0);
        ShapeInstanceData.texture_size = rpc->PackValues(0, 0);
    }

    PMMA_Core::RenderPipelineCore->Add(this);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}