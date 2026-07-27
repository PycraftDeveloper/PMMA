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

uint16_t PMMA::Rendering::TwoD::Shapes::Arc::GetRadius() {
    if (!RadiusSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a radius for the arc \
please use `Arc.set_radius` to set it before attempting to get it.");
        throw std::runtime_error("Radius not set!");
    }
    return Radius;
}

void PMMA::Rendering::TwoD::Shapes::Arc::GetSize(uint16_t *out_size) {
    if (!(RadiusSet || ShapeSize.GetSet() || Texture.IsLoaded())) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a size for the arc \
please use 'Arc.ShapeSize' or 'Arc.SetRadius' or set a texture before \
attempting to get it.");
        throw std::runtime_error("Size not set!");
    }

    if (UseTextureSize) {
        Texture.GetSize(out_size);
    } else if (RadiusSet) {
        uint16_t radius = GetRadius() * 2;
        out_size[0] = radius;
        out_size[1] = radius;
    } else {
        ShapeSize.Get(out_size);
    }
}

void PMMA::Rendering::TwoD::Shapes::Arc::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged |= ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance();

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.Get(start_position);

        uint16_t size[2];
        GetSize(size);

        // Existing packing logic
        ShapeInstanceData.position = PMMA::Internal::PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA::Internal::PackValues(size[0], size[1]);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::PackValues(Rotation * 182, GetStartAngle() * 182);

        ShapeInstanceData.shape_type_width = PMMA::Internal::PackValues(3, Width);

        ShapeInstanceData.shape_property_two = PMMA::Internal::PackValues(GetEndAngle() * 182, 0);
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