#include "Internal/Rendering/Core2D/RenderPipelineInstance.hpp"
#include "PMMA_Core.hpp"

void PMMA::Rendering::TwoD::Shapes::Line::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged |= ShapeStart.GetChangedToggle() || ShapeEnd.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *Instance = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->GetInstance();

    if (ShapePropertyChanged) {
        uint16_t start_position[2], end_position[2];
        ShapeStart.Get(start_position);
        ShapeEnd.Get(end_position);

        // 1. Calculate original dimensions
        float orig_size_x = abs((float)end_position[0] - start_position[0]);
        float orig_size_y = abs((float)end_position[1] - start_position[1]);

        if (orig_size_x == 0.0f)
            orig_size_x = 1.0f;
        if (orig_size_y == 0.0f)
            orig_size_y = 1.0f;

        // 2. Expand the bounding box size to include the width padding on all sides
        float padding = (float)Width;
        float size_x = orig_size_x + (padding * 2.0f);
        float size_y = orig_size_y + (padding * 2.0f);

        // 3. Calculate absolute pixel center of this instance quad
        float center_x = (start_position[0] + end_position[0]) / 2.0f;
        float center_y = (start_position[1] + end_position[1]) / 2.0f;

        // 4. Calculate signed pixel distances from the center to endpoints
        float start_offset_x = (float)start_position[0] - center_x;
        float start_offset_y = (float)start_position[1] - center_y;
        float end_offset_x = (float)end_position[0] - center_x;
        float end_offset_y = (float)end_position[1] - center_y;

        // 5. Add a 32768 bias to completely eliminate negative numbers for uint16_t packing
        uint16_t pack_start_x = (uint16_t)(start_offset_x + 32768.0f);
        uint16_t pack_start_y = (uint16_t)(start_offset_y + 32768.0f);
        uint16_t pack_end_x = (uint16_t)(end_offset_x + 32768.0f);
        uint16_t pack_end_y = (uint16_t)(end_offset_y + 32768.0f);

        ShapeInstanceData.position = PMMA::Internal::PackValues((start_position[0] + end_position[0]) / 2, (start_position[1] + end_position[1]) / 2);
        ShapeInstanceData.size = PMMA::Internal::PackValues((uint16_t)size_x, (uint16_t)size_y);
        ShapeInstanceData.point_count_gradient_type = PMMA::Internal::PackValues(0, 0);

        // Pass biased start_x here
        ShapeInstanceData.rotation_shape_property_one = PMMA::Internal::PackValues(Rotation * 182, pack_start_x);

        ShapeInstanceData.shape_type_width = PMMA::Internal::PackValues(4, Width);

        // Pass remaining biased pixel coordinates
        ShapeInstanceData.shape_property_two = PMMA::Internal::PackValues(pack_start_y, pack_end_x);
        ShapeInstanceData.shape_property_three = PMMA::Internal::PackValues(pack_end_y, 0);

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
