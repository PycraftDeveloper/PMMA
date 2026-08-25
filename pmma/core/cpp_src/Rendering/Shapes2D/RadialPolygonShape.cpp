#include "Internal/Rendering/Core2D/Internal.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"

#include "Display.hpp"
#include "Types.hpp"

void PMMA::Rendering::TwoD::Shapes::RadialPolygonBase::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter.GetChangedToggle() || ShapeSize.GetScaledChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    if (ColorDataChanged) {
        if (Color.IsClear()) {
            ColorDataChanged = false;
            return; // Invisible
        }
    }

    int16_t start_position[2];
    uint16_t size[2];

    if (ShapePropertyChanged) {
        ShapeCenter.GetCoordinate(start_position);
        ShapeSize.GetScaledSize(size);

        uint16_t display_size[2];
        PMMA::Core::ActiveDisplayInstance->GetSize(display_size);

        if ((start_position[0] >= display_size[0]) || // Completely past right edge
            (start_position[1] >= display_size[1]) || // Completely past bottom edge
            ((start_position[0] + size[0]) <= 0) ||   // Completely past left edge
            ((start_position[1] + size[1]) <= 0)) {   // Completely past top edge
            ShapePropertyChanged = false;
            return; // Early exit: Shape is completely off-screen
        }
    }

    uint16_t TextureSize[2] = {0, 0};
    unsigned char Channels = 0;
    if (Texture.IsEnabled()) {
        Texture.GetSize(TextureSize);
        Channels = Texture.GetChannels();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance(Texture.TextureProperties, TextureSize, Channels);

    if (ShapePropertyChanged) {
        // Existing packing logic
        ShapeInstanceData.position = PMMA::Internal::Rendering::Core2D::PackSignedValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA::Internal::Rendering::Core2D::PackValues(size[0], size[1]);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::Rendering::Core2D::PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::Rendering::Core2D::PackValues(Rotation * 182, 0);
        ShapeInstanceData.shape_type_width = PMMA::Internal::Rendering::Core2D::PackValues(1, Width);

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