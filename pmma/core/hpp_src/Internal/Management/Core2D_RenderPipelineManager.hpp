#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

class CPP_Core2D_RenderPipelineInstance;

namespace PMMA::Rendering::TwoD {
class CPP_Line;
class CPP_Arc;
class CPP_Ellipse;
class CPP_RadialPolygon;
class CPP_Rectangle;
class CPP_Pixel;
} // namespace PMMA::Rendering::TwoD

struct Vertex {
    float x, y, u, v;
};

struct InstanceData {
    float position, size;
    float point_count_gradient_type, rotation_shape_property_one;
    float color_index, shape_type_width;
    float texture_position, texture_size;
    float shape_property_two = 0, shape_property_three = 0;
    float shape_property_four = 0, shape_property_five = 0;
};

class CPP_Core2D_RenderPipelineManager {
private:
    std::vector<CPP_Core2D_RenderPipelineInstance *> RenderPipelineInstances;
    std::vector<CPP_Core2D_RenderPipelineInstance *> CachedRenderPipelineInstances;

public:
    ~CPP_Core2D_RenderPipelineManager();

    void Add(PMMA::Rendering::TwoD::CPP_Line *lineShape);
    void Add(PMMA::Rendering::TwoD::CPP_RadialPolygon *radialPolygonShape);
    void Add(PMMA::Rendering::TwoD::CPP_Arc *arcShape);
    void Add(PMMA::Rendering::TwoD::CPP_Ellipse *ellipseShape);
    void Add(PMMA::Rendering::TwoD::CPP_Rectangle *rectangleShape);
    void Add(PMMA::Rendering::TwoD::CPP_Pixel *pixelShape);

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