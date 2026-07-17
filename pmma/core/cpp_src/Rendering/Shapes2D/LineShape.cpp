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

        float width = abs((float)end_position[0] - start_position[0]);
        float height = abs((float)end_position[1] - start_position[1]);

        if (width == 0.0f)
            width = 1.0f;
        if (height == 0.0f)
            height = 1.0f;

        float rel_start_x = (start_position[0] <= end_position[0]) ? 0.0f : 1.0f;
        float rel_end_x = (start_position[0] <= end_position[0]) ? 1.0f : 0.0f;

        float rel_start_y = (start_position[1] <= end_position[1]) ? 0.0f : 1.0f;
        float rel_end_y = (start_position[1] <= end_position[1]) ? 1.0f : 0.0f;

        auto rpc = PMMA::Core::ActiveDisplayInstance->RenderPipelineCore;

        ShapeInstanceData.position = rpc->PackValues((start_position[0] + end_position[0]) / 2, (start_position[1] + end_position[1]) / 2);
        ShapeInstanceData.size = rpc->PackValues((uint16_t)width, (uint16_t)height);
        ShapeInstanceData.point_count_gradient_type = rpc->PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = rpc->PackValues(Rotation * 182, rel_start_x);

        ShapeInstanceData.shape_type_width = rpc->PackValues(4, Width);
        ShapeInstanceData.texture_position = rpc->PackValues(0, 0);
        ShapeInstanceData.texture_size = rpc->PackValues(0, 0);

        ShapeInstanceData.shape_property_two = rpc->PackValues(rel_start_y, rel_end_x);
        ShapeInstanceData.shape_property_three = rpc->PackValues(rel_end_y, 0);

        ShapeInstanceData.depth = static_cast<float>(Instance->instanceCount) / static_cast<float>(PMMA::Constants::RENDER_PIPELINE_INSTANCE_MAX_SIZE);
    }

    PMMA::Core::ActiveDisplayInstance->RenderPipelineCore->Add(Instance, this);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}
