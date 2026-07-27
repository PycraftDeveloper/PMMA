#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

void PMMA::Rendering::TwoD::Shapes::Rectangle::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance();

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.GetCoordinate(start_position);

        uint16_t Size[2];
        ShapeSize.GetSize(Size);

        // Existing packing logic
        ShapeInstanceData.position = PMMA::Internal::PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA::Internal::PackValues(Size[0], Size[1]);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::PackValues(0, 0); // no point count here
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::PackValues(Rotation * 182, CornerRadius);
        ShapeInstanceData.shape_type_width = PMMA::Internal::PackValues(2, Width);

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