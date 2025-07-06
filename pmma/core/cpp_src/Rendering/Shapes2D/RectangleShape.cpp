#include <cmath>

#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/RenderPipelineManager.hpp"
#include "AdvancedMathematics.hpp"
#include "Constants.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_RectangleShape::CPP_RectangleShape() {
    RenderPipelineData = new RenderPipelineDataObject(this);
}

void CPP_RectangleShape::Render(float ShapeQuality) {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (ShapeCentre.x + HalfWidth < 0 ||
            ShapeCentre.x - HalfWidth > DisplayWidth ||
            ShapeCentre.y + HalfHeight < 0 ||
            ShapeCentre.y - HalfHeight > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = (UsingGradients == false);

    if (RenderPipelineCompatible) {
        if (ColorData[0].w == 0) { // Return if shape not visible
            return;
        }

        GLuint newColorIndex = PMMA::RenderPipelineCore->GetColorIndex();
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            Changed = false;

            RenderPipelineColorData = ColorData[0];

            unsigned int InternalWidth = Width;
            if (Width == 0) {
                InternalWidth = max(HalfWidth, HalfHeight);
            }

            if (CornerRadius != 0) {
                if (CornerRadius != 0) {
                    unsigned int radius = min(CornerRadius, min(HalfWidth, HalfHeight));
                    float minAngle = 1.0f / radius;
                    unsigned int segments = max(3u, static_cast<unsigned int>(
                        1 + (CPP_Constants::TAU / asin(minAngle)) * ShapeQuality / 4));

                    size_t vertexCount = (segments + 1) * 8 + 2;
                    RenderPipelineVertexData.resize(vertexCount);

                    int outer_radius = radius;
                    int inner_radius = max((int)radius - static_cast<int>(InternalWidth), 0);

                    glm::vec2 vectorized_outer_radius = glm::vec2(outer_radius, outer_radius);
                    glm::vec2 vectorized_inner_radius = glm::vec2(inner_radius, inner_radius);

                    int outer_w = ShapeSize.x;
                    int outer_h = ShapeSize.y;
                    int inner_w = outer_w - 2 * InternalWidth;
                    int inner_h = outer_h - 2 * InternalWidth;

                    const glm::vec2 centers[4] = {
                        {-outer_w / 2 + outer_radius, -outer_h / 2 + outer_radius}, // top-left
                        { outer_w / 2 - outer_radius, -outer_h / 2 + outer_radius}, // top-right
                        { outer_w / 2 - outer_radius,  outer_h / 2 - outer_radius}, // bottom-right
                        {-outer_w / 2 + outer_radius,  outer_h / 2 - outer_radius}  // bottom-left
                    };

                    const glm::vec2 icenters[4] = {
                        {-inner_w / 2 + inner_radius, -inner_h / 2 + inner_radius},
                        { inner_w / 2 - inner_radius, -inner_h / 2 + inner_radius},
                        { inner_w / 2 - inner_radius,  inner_h / 2 - inner_radius},
                        {-inner_w / 2 + inner_radius,  inner_h / 2 - inner_radius}
                    };

                    const float startAngles[4] = {
                        CPP_Constants::PI,             // 180°
                        CPP_Constants::PI * 1.5f,      // 270°
                        0.0f,                          // 0°
                        CPP_Constants::PI * 0.5f       // 90°
                    };

                    for (int corner = 0; corner < 4; ++corner) {
                        glm::vec2 outerCenter = centers[corner];
                        glm::vec2 innerCenter = icenters[corner];

                        // Use rotation matrix to rotate unit vector instead of trig
                        float angle = startAngles[corner];
                        float delta = (CPP_Constants::PI * 0.5f) / segments;

                        float cosD = cos(delta);
                        float sinD = sin(delta);
                        float x = cos(angle);
                        float y = sin(angle);

                        unsigned int index = corner * (segments + 1) * 2;

                        for (unsigned int i = 0; i <= segments; ++i) {
                            glm::vec2 unit = {x, y};

                            glm::vec2 outer = outerCenter + vectorized_outer_radius * unit;
                            glm::vec2 inner = innerCenter + vectorized_inner_radius * unit;

                            RenderPipelineVertexData[index + i * 2] = {ShapeCentre + outer, ColorIndex};
                            RenderPipelineVertexData[index + i * 2 + 1] = {ShapeCentre + inner, ColorIndex};

                            // rotate (x, y) using rotation matrix
                            float newX = cosD * x - sinD * y;
                            float newY = sinD * x + cosD * y;
                            x = newX;
                            y = newY;
                        }
                    }

                    // Close the loop
                    RenderPipelineVertexData[vertexCount - 2] = RenderPipelineVertexData[0];
                    RenderPipelineVertexData[vertexCount - 1] = RenderPipelineVertexData[1];
                }
            } else {
                if (Width == 0 || Width >= max(HalfWidth, HalfHeight)) {
                    RenderPipelineVertexData.resize(4);

                    RenderPipelineVertexData[0] = {glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y - HalfHeight), ColorIndex};
                    RenderPipelineVertexData[1] = {glm::vec2(ShapeCentre.x + HalfWidth, ShapeCentre.y - HalfHeight), ColorIndex};
                    RenderPipelineVertexData[2] = {glm::vec2(ShapeCentre.x - HalfWidth, ShapeCentre.y + HalfHeight), ColorIndex};
                    RenderPipelineVertexData[3] = {glm::vec2(ShapeCentre.x + HalfWidth, ShapeCentre.y + HalfHeight), ColorIndex};
                } else {
                    RenderPipelineVertexData.resize(10);

                    int outer_left   = ShapeCentre.x - HalfWidth;
                    int outer_right  = ShapeCentre.x + HalfWidth;
                    int outer_top    = ShapeCentre.y - HalfHeight;
                    int outer_bottom = ShapeCentre.y + HalfHeight;

                    int inner_left   = outer_left   + Width;
                    int inner_right  = outer_right  - Width;
                    int inner_top    = outer_top    + Width;
                    int inner_bottom = outer_bottom - Width;

                    // GL_TRIANGLE_STRIP order: Outer TL, Inner TL, Outer TR, Inner TR, Outer BR, Inner BR, Outer BL, Inner BL
                    RenderPipelineVertexData[0] = {glm::vec2(outer_left,  outer_top),    ColorIndex}; // Outer TL
                    RenderPipelineVertexData[1] = {glm::vec2(inner_left,  inner_top),    ColorIndex}; // Inner TL
                    RenderPipelineVertexData[2] = {glm::vec2(outer_right, outer_top),    ColorIndex}; // Outer TR
                    RenderPipelineVertexData[3] = {glm::vec2(inner_right, inner_top),    ColorIndex}; // Inner TR
                    RenderPipelineVertexData[4] = {glm::vec2(outer_right, outer_bottom), ColorIndex}; // Outer BR
                    RenderPipelineVertexData[5] = {glm::vec2(inner_right, inner_bottom),ColorIndex}; // Inner BR
                    RenderPipelineVertexData[6] = {glm::vec2(outer_left,  outer_bottom),ColorIndex}; // Outer BL
                    RenderPipelineVertexData[7] = {glm::vec2(inner_left,  inner_bottom),ColorIndex}; // Inner BL
                    RenderPipelineVertexData[8] = RenderPipelineVertexData[0];
                    RenderPipelineVertexData[9] = RenderPipelineVertexData[1];
                }
            }
        }
        PMMA::RenderPipelineCore->AddObject(*RenderPipelineData, RenderPipelineCompatible);
    } else {
        if (Changed) {
            // Calculate data and add to buffers, Left intentionally blank for now
        }
        // Do NOTHING.
    }
}

void CPP_RectangleShape::InternalRender() {
    // Left intentionally blank for now
}
