#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

uint16_t PMMA::Rendering::TwoD::Shapes::RadialPolygon::GetRadius() {
    if (!RadiusSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a radius for the arc \
please use `Arc.set_radius` to set it before attempting to get it.");
        throw std::runtime_error("Radius not set!");
    }
    return Radius;
}

void PMMA::Rendering::TwoD::Shapes::RadialPolygon::GetSize(uint16_t *out_size) {
    if (!(RadiusSet || ShapeSizeSet || Texture.IsLoaded())) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a size for the radial polygon \
please use 'RadialPolygon.SetSize' or 'RadialPolygon.SetRadius' or set a texture before \
attempting to get it.");
        throw std::runtime_error("Size not set!");
    }

    if (RadiusSet) {
        uint16_t radius = GetRadius() * 2;
        out_size[0] = radius;
        out_size[1] = radius;
    } else if (ShapeSizeSet) {
        out_size[0] = ShapeSize[0];
        out_size[1] = ShapeSize[1];
    } else {
        Texture.GetSize(out_size);
    }
}

void PMMA::Rendering::TwoD::Shapes::RadialPolygon::Render() {
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

        uint16_t size[2];
        GetSize(size);

        // Existing packing logic
        ShapeInstanceData.position = PMMA::Internal::PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA::Internal::PackValues(size[0], size[1]);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::PackValues(Rotation * 182, 0);
        ShapeInstanceData.shape_type_width = PMMA::Internal::PackValues(1, Width);

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