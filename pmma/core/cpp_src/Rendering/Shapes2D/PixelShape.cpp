#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"

#define PMMA_ALLOW_UMBRELLA_HEADER
#include "PMMA_Core.hpp"

PMMA::Rendering::TwoD::Shapes::Pixel::Pixel() {
    ID = reinterpret_cast<uintptr_t>(this);

    ShapeCenter = new PMMA::Types::TwoD::Coordinate();
    Color = new PMMA::Types::Color();
    Texture = new PMMA::Types::Texture();
}

void PMMA::Rendering::TwoD::Shapes::Pixel::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter->GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color->GetInternalChangedToggle();
    }

    if (ColorDataChanged) {
        if (Color->IsClear()) {
            ColorDataChanged = false;
            return; // Invisible
        }
    }

    int16_t start_position[2];

    if (ShapePropertyChanged) {
        ShapeCenter->GetCoordinate(start_position);

        uint16_t display_size[2];
        PMMA::Core::ActiveDisplayInstance->GetSize(display_size);

        if ((start_position[0] >= display_size[0]) || // Completely past right edge
            (start_position[1] >= display_size[1]) || // Completely past bottom edge
            (start_position[0] <= 0) ||               // Completely past left edge
            (start_position[1] <= 0)) {               // Completely past top edge
            ShapePropertyChanged = false;
            return; // Early exit: Shape is completely off-screen
        }
    }

    uint16_t TextureSize[2] = {0, 0};
    unsigned char Channels;
    if (Texture->IsEnabled()) {
        Texture->GetSize(TextureSize);
        Channels = Texture->GetChannels();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance(Texture->TextureProperties, TextureSize, Channels);

    if (ShapePropertyChanged) {
        // Existing packing logic
        ShapeInstanceData.position = PMMA::Internal::PackSignedValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = PMMA::Internal::PackValues(1, 1);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::PackValues(0, 0);
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::PackValues(0, 0);
        ShapeInstanceData.shape_type_width = PMMA::Internal::PackValues(0, 0);

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
