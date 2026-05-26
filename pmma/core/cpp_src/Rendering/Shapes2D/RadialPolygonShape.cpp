#include "PMMA_Core.hpp"

CPP_RadialPolygonShape::CPP_RadialPolygonShape() {
    ID = reinterpret_cast<uintptr_t>(this);
}

uint16_t CPP_RadialPolygonShape::GetRadius() {
    if (!RadiusSet) {
        PMMA_Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not specified a radius for the arc \
please use `RadialPolygon.set_radius` to set it before attempting to get it.");
        throw std::runtime_error("Radius not set");
    }
    return Radius;
};

void CPP_RadialPolygonShape::Render() {
    if (!ShapePropertyChanged) {
        ShapePropertyChanged = ShapeCenter.GetChangedToggle();
    }

    if (!ColorDataChanged) {
        ColorDataChanged = Color.GetInternalChangedToggle();
    }

    if (ShapePropertyChanged) {
        uint16_t start_position[2];
        ShapeCenter.Get(start_position);
        uint16_t radius = Radius * 2;

        auto rpc = PMMA_Core::RenderPipelineCore;

        // Existing packing logic
        ShapeInstanceData.position = rpc->PackValues(start_position[0], start_position[1]);
        ShapeInstanceData.size = rpc->PackValues(radius, radius);
        ShapeInstanceData.point_count_gradient_type = rpc->PackValues(PointCount, 0);
        ShapeInstanceData.rotation_shape_property_one = rpc->PackValues(Rotation * 182, 0);
        ShapeInstanceData.shape_type_width = rpc->PackValues(0, Width);
        ShapeInstanceData.texture_position = rpc->PackValues(0, 0);
        ShapeInstanceData.texture_size = rpc->PackValues(0, 0);
    }

    PMMA_Core::RenderPipelineCore->Add(this);

    if (ColorDataChanged) {
        ColorDataChanged = false;
    }
    if (ShapePropertyChanged) {
        ShapePropertyChanged = false;
    }
}