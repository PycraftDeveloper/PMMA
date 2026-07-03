#include "PMMA_Core.hpp"

void PMMA::Rendering::TwoD::CPP_Rectangle::GetSize(uint16_t *out_size) {
    if (!ShapeSizeSet) {
        PMMA_Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a size for the rectangle \
please use `Rectangle.SetSize` to set it before attempting to get it.");
        throw std::runtime_error("Size not set!");
    }
    out_size[0] = ShapeSize[0];
    out_size[1] = ShapeSize[1];
}

void PMMA::Rendering::TwoD::CPP_Rectangle::Render() {
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
        uint16_t Size[2];
        GetSize(Size);

        // Existing packing logic
        ShapeInstanceData.position = rpc->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = rpc->PackValues(Size[0], Size[1]);
        ShapeInstanceData.point_count_gradient_type = rpc->PackValues(0, 0); // no point count here
        ShapeInstanceData.rotation_shape_property_one = rpc->PackValues(Rotation * 182, CornerRadius);
        ShapeInstanceData.shape_type_width = rpc->PackValues(2, Width);
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