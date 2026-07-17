#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

void PMMA::Rendering::TwoD::Shapes::Ellipse::GetSize(uint16_t *out_size) {
    if (!ShapeSizeSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a size for the ellipse \
please use `Ellipse.SetSize` to set it before attempting to get it.");
        throw std::runtime_error("Size not set!");
    }
    out_size[0] = ShapeSize[0];
    out_size[1] = ShapeSize[1];
}

void PMMA::Rendering::TwoD::Shapes::Ellipse::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance();

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.Get(start_position);

        auto rpc = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore;
        uint16_t Size[2];
        GetSize(Size);

        // Existing packing logic
        ShapeInstanceData.position = rpc->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = rpc->PackValues(Size[0], Size[1]);
        ShapeInstanceData.point_count_gradient_type = rpc->PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = rpc->PackValues(Rotation * 182, 0);
        ShapeInstanceData.shape_type_width = rpc->PackValues(1, Width);
        ShapeInstanceData.texture_position = rpc->PackValues(0, 0);
        ShapeInstanceData.texture_size = rpc->PackValues(0, 0);

        ShapeInstanceData.depth = 1.0f - (static_cast<float>(Instance->OpaqueInstanceCount + Instance->TransparentInstanceCount) / static_cast<float>(PMMA::Constants::RENDER_PIPELINE_INSTANCE_MAX_SIZE));
    }

    PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->Add(Instance, this);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}