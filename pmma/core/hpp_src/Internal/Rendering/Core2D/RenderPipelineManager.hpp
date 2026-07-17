#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

namespace PMMA::Rendering::TwoD::Shapes {
class Line;
class Arc;
class Ellipse;
class RadialPolygon;
class Rectangle;
class Pixel;
} // namespace PMMA::Rendering::TwoD::Shapes

namespace PMMA::Internal::Rendering::Core2D {
class RenderPipelineInstance;

struct Vertex {
    float x, y, u, v;
};

struct InstanceData {
    float position, size;
    float point_count_gradient_type, rotation_shape_property_one;
    float color_index, shape_type_width;
    float texture_position, texture_size;
    float shape_property_two = 0, shape_property_three = 0;
    float depth = 0, unused = 0;
};

class RenderPipelineManager {
private:
    std::vector<PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *> RenderPipelineInstances;
    std::vector<PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *> CachedRenderPipelineInstances;

public:
    ~RenderPipelineManager();

    void Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Line *lineShape);
    void Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::RadialPolygon *radialPolygonShape);
    void Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Arc *arcShape);
    void Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Ellipse *ellipseShape);
    void Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Rectangle *rectangleShape);
    void Add(PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *lastInstance, PMMA::Rendering::TwoD::Shapes::Pixel *pixelShape);

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *GetInstance();

    inline float PackValues(uint16_t value_one, uint16_t value_two) {
        uint32_t bits = (uint32_t(value_two) << 16) | uint32_t(value_one);
        float packed;
        std::memcpy(&packed, &bits, sizeof(float));
        return packed;
    }

    inline float PackValues(uint8_t value_one, uint8_t value_two, uint8_t value_three) {
        uint32_t bits = (static_cast<uint32_t>(value_three) << 24) |
                        (static_cast<uint32_t>(value_two) << 16) |
                        (static_cast<uint32_t>(value_one) << 8); // Leaving lowest 8 bits empty/0

        float packed;
        std::memcpy(&packed, &bits, sizeof(float));
        return packed;
    }

    void Reset();

    void Render();
};
} // namespace PMMA::Internal::Rendering::Core2D