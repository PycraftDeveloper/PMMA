#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

class CPP_Core2D_RenderPipelineInstance;

class CPP_LineShape;
class CPP_RadialPolygonShape;
class CPP_ArcShape;
class CPP_EllipseShape;

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

    void Add(CPP_LineShape *lineShape);
    void Add(CPP_RadialPolygonShape *radialPolygonShape);
    void Add(CPP_ArcShape *arcShape);
    void Add(CPP_EllipseShape *ellipseShape);

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