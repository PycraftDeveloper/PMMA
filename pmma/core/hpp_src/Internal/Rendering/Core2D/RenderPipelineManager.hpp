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

class RenderPipelineManager {
private:
    std::vector<PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *> RenderPipelineInstances;
    std::vector<PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *> CachedRenderPipelineInstances;

public:
    ~RenderPipelineManager();

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *GetInstance(PMMA::Internal::Rendering::Core2D::CompressedTextureProperty *Texture, uint16_t *TextureSize, unsigned char Channels);

    PMMA::Internal::Rendering::Core2D::RenderPipelineInstance *GetInstance();

    void Reset();

    void Render();
};
} // namespace PMMA::Internal::Rendering::Core2D