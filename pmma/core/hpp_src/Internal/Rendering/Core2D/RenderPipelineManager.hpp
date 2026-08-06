#pragma once
#include <cstdint>
#include <vector>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

namespace PMMA::Rendering::TwoD::Shapes {
class Line;
class Arc;
class Ellipse;
class RadialPolygonBase;
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
    float texture_position = 0, texture_size = 0;
    float shape_property_two = 0, shape_property_three = 0;
    float depth = 0, unused = 0;
};

class RenderPipelineManager {
private:
    std::vector<PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *> RenderPipelineInstances;
    std::vector<PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *> CachedRenderPipelineInstances;

public:
    ~RenderPipelineManager();

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *GetInstance(PMMA::Internal::TextureProperty *Texture, uint16_t *TextureSize, unsigned char Channels);

    void Reset();

    void Render();
};
} // namespace PMMA::Internal::Rendering::Core2D