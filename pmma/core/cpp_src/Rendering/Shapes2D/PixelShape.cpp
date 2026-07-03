#include "PMMA_Core.hpp"

void PMMA::Rendering::TwoD::CPP_Pixel::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.Get(start_position);

        auto rpc = PMMA_Core::ActiveDisplayInstance->RenderPipelineCore;

        // Existing packing logic
        ShapeInstanceData.position = rpc->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = rpc->PackValues(1, 1);
        ShapeInstanceData.point_count_gradient_type = rpc->PackValues(0, 0);
        ShapeInstanceData.rotation_shape_property_one = rpc->PackValues(0, 0);
        ShapeInstanceData.shape_type_width = rpc->PackValues(0, 0);
        ShapeInstanceData.texture_position = rpc->PackValues(0, 0);
        ShapeInstanceData.texture_size = rpc->PackValues(0, 0);
    }

    PMMA_Core::ActiveDisplayInstance->RenderPipelineCore->Add(this);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}
