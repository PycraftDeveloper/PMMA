#include "PMMA_Core.hpp"

CPP_LineShape::CPP_LineShape() {
    ShapeStart = new CPP_DisplayCoordinate();
    ShapeEnd = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = reinterpret_cast<uintptr_t>(this);
}

void CPP_LineShape::Render() {
    if (ShapePropertyChanged) {
        uint16_t start_position[2], end_position[2];
        ShapeStart->Get(start_position);
        ShapeEnd->Get(end_position);

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

        ShapeInstanceData.position = PMMA_Core::RenderPipelineCore->PackValues((start_position[0] + end_position[0]) / 2, (start_position[1] + end_position[1]) / 2);
        ShapeInstanceData.size = PMMA_Core::RenderPipelineCore->PackValues((uint16_t)width, (uint16_t)height);
        ShapeInstanceData.point_count_gradient_type = PMMA_Core::RenderPipelineCore->PackValues(0, 0);
        ShapeInstanceData.rotation_shape_property = PMMA_Core::RenderPipelineCore->PackValues(GetRotation() * 182, 0);

        ShapeInstanceData.shape_type_width = PMMA_Core::RenderPipelineCore->PackValues(3, GetWidth());
        ShapeInstanceData.texture_position = PMMA_Core::RenderPipelineCore->PackValues(0, 0);
        ShapeInstanceData.texture_size = PMMA_Core::RenderPipelineCore->PackValues(0, 0);

        ShapeInstanceData.line_start = PMMA_Core::RenderPipelineCore->PackValues(rel_start_x, rel_start_y);
        ShapeInstanceData.line_end = PMMA_Core::RenderPipelineCore->PackValues(rel_end_x, rel_end_y);
    }

    PMMA_Core::RenderPipelineCore->Add(this);
    ColorDataChanged = false;
    ShapePropertyChanged = false;
}
