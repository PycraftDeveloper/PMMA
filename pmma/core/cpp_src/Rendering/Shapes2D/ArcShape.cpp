#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

float PMMA::Rendering::TwoD::Shapes::Arc::GetStartAngle() {
    if (!StartAngleSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a starting angle for the arc \
please use `Arc.set_start_angle` to set it before attempting to get it.");
        throw std::runtime_error("Start angle not set!");
    }
    return StartAngle;
}

float PMMA::Rendering::TwoD::Shapes::Arc::GetEndAngle() {
    if (!EndAngleSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified an ending angle for the arc \
please use `Arc.set_start_angle` to set it before attempting to get it.");
        throw std::runtime_error("End angle not set!");
    }
    return EndAngle;
}

void PMMA::Rendering::TwoD::Shapes::Arc::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged |= ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    uint16_t TextureSize[2] = {0, 0};
    unsigned char Channels;
    if (Texture.IsEnabled()) {
        Texture.GetSize(TextureSize);
        Channels = Texture.GetChannels();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance(TextureSize, Channels);

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.GetCoordinate(start_position);

        uint16_t size[2];
        ShapeSize.GetSize(size);

        // Existing packing logic
        ShapeInstanceData.position = PMMA::Internal::PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA::Internal::PackValues(size[0], size[1]);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::PackValues(Rotation * 182, GetStartAngle() * 182);

        ShapeInstanceData.shape_type_width = PMMA::Internal::PackValues(3, Width);

        ShapeInstanceData.shape_property_two = PMMA::Internal::PackValues(GetEndAngle() * 182, 0);
        ShapeInstanceData.depth = 1.0f - (static_cast<float>(Instance->OpaqueInstanceCount + Instance->TransparentInstanceCount) / static_cast<float>(PMMA::Constants::RENDER_PIPELINE_INSTANCE_MAX_SIZE));
    }

    Instance->Add(this, TextureSize, Channels);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}