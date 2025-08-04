#include "PMMA_Core.hpp"

using namespace std;

CPP_RectangleShape::CPP_RectangleShape() {
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA::ClassObject_ID_System++;
}

void CPP_RectangleShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA::DisplayInstance->GetWidth();
    DisplayHeight = PMMA::DisplayInstance->GetHeight();

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (!ShapeCenterFormat->GetSet()) {
        throw std::runtime_error("Shape has no center not set");
    }

    if (!ColorFormat->GetSet()) {
        throw std::runtime_error("Shape has no color set");
    }

    glm::vec2 ShapeCenter = ShapeCenterFormat->Get();

    Changed = Changed ||
                ShapeCenterFormat->GetChangedToggle();

    if (ShapeCenter.x + HalfWidth < 0 ||
            ShapeCenter.x - HalfWidth > DisplayWidth ||
            ShapeCenter.y + HalfHeight < 0 ||
            ShapeCenter.y - HalfHeight > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    if (RenderPipelineCompatible) {
        if (ColorFormat->Get_rgba().a == 0.0f) { // Return if shape not visible
            return;
        }

        GLuint newColorIndex = PMMA::RenderPipelineCore->Shape2D_GetColorIndex(ColorFormat->Get_rgba(), ID);
        if (newColorIndex != ColorIndex) {
            Changed = true;
            ColorIndex = newColorIndex;
        }

        if (Changed) {
            unsigned int InternalWidth = Width;
            if (Width == 0) {
                InternalWidth = max(HalfWidth, HalfHeight);
            }

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            if (CornerRadius != 0) {
                if (CornerRadius != 0) {

                    unsigned int radius = min(CornerRadius, min(HalfWidth, HalfHeight));
                    float minAngle = 1.0f / radius;
                    unsigned int segments = max(3u, static_cast<unsigned int>(
                        1 + (CPP_Constants::TAU / asin(minAngle)) * PMMA::CurrentShapeQuality / 4));

                    size_t vertexCount = (segments + 1) * 8 + 2;
                    Shape2D_RenderPipelineData.resize(vertexCount);

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

                            // Rotate around origin, then offset by ShapeCenter
                            glm::vec2 rotated_outer = {
                                RotationCos * outer.x - RotationSin * outer.y,
                                RotationSin * outer.x + RotationCos * outer.y
                            };
                            glm::vec2 rotated_inner = {
                                RotationCos * inner.x - RotationSin * inner.y,
                                RotationSin * inner.x + RotationCos * inner.y
                            };

                            Shape2D_RenderPipelineData[index + i * 2]     = {ShapeCenter + rotated_outer, ColorIndex};
                            Shape2D_RenderPipelineData[index + i * 2 + 1] = {ShapeCenter + rotated_inner, ColorIndex};

                            // rotate (x, y) using rotation matrix
                            float newX = cosD * x - sinD * y;
                            float newY = sinD * x + cosD * y;
                            x = newX;
                            y = newY;
                        }
                    }

                    // Close the loop
                    Shape2D_RenderPipelineData[vertexCount - 2] = Shape2D_RenderPipelineData[0];
                    Shape2D_RenderPipelineData[vertexCount - 1] = Shape2D_RenderPipelineData[1];
                }
            } else {
                if (Width == 0 || Width >= max(HalfWidth, HalfHeight)) {
                    Shape2D_RenderPipelineData.resize(4);

                    glm::vec2 point = glm::vec2(ShapeCenter.x - HalfWidth,
                        ShapeCenter.y - HalfHeight);
                    Shape2D_RenderPipelineData[0] = {
                        SimpleApplyRotation(point, ShapeCenter, RotationSin,
                            RotationCos, HalfWidth, HalfHeight), ColorIndex};

                    point = glm::vec2(ShapeCenter.x + HalfWidth,
                        ShapeCenter.y - HalfHeight);
                    Shape2D_RenderPipelineData[1] = {
                        SimpleApplyRotation(point, ShapeCenter, RotationSin,
                            RotationCos, HalfWidth, HalfHeight), ColorIndex};

                    point = glm::vec2(ShapeCenter.x - HalfWidth,
                        ShapeCenter.y + HalfHeight);
                    Shape2D_RenderPipelineData[2] = {
                        SimpleApplyRotation(point, ShapeCenter, RotationSin,
                            RotationCos, HalfWidth, HalfHeight), ColorIndex};

                    point = glm::vec2(ShapeCenter.x + HalfWidth,
                        ShapeCenter.y + HalfHeight);
                    Shape2D_RenderPipelineData[3] = {
                        SimpleApplyRotation(point, ShapeCenter, RotationSin,
                            RotationCos, HalfWidth, HalfHeight), ColorIndex};
                } else {
                    Shape2D_RenderPipelineData.resize(10);

                    int outer_left = ShapeCenter.x - HalfWidth;
                    int outer_right = ShapeCenter.x + HalfWidth;
                    int outer_top = ShapeCenter.y - HalfHeight;
                    int outer_bottom = ShapeCenter.y + HalfHeight;

                    int inner_left = outer_left + Width;
                    int inner_right = outer_right - Width;
                    int inner_top = outer_top + Width;
                    int inner_bottom = outer_bottom - Width;

                    // GL_TRIANGLE_STRIP order: Outer TL, Inner TL, Outer TR, Inner TR, Outer BR, Inner BR, Outer BL, Inner BL
                    Shape2D_RenderPipelineData[0] = {
                        ComplexApplyRotation(
                            glm::vec2(outer_left, outer_top),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Outer TL
                    Shape2D_RenderPipelineData[1] = {
                        ComplexApplyRotation(
                            glm::vec2(inner_left, inner_top),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Inner TL
                    Shape2D_RenderPipelineData[2] = {
                        ComplexApplyRotation(
                            glm::vec2(outer_right, outer_top),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Outer TR
                    Shape2D_RenderPipelineData[3] = {
                        ComplexApplyRotation(
                            glm::vec2(inner_right, inner_top),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Inner TR
                    Shape2D_RenderPipelineData[4] = {
                        ComplexApplyRotation(
                            glm::vec2(outer_right, outer_bottom),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Outer BR
                    Shape2D_RenderPipelineData[5] = {
                        ComplexApplyRotation(
                            glm::vec2(inner_right, inner_bottom),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Inner BR
                    Shape2D_RenderPipelineData[6] = {
                        ComplexApplyRotation(
                            glm::vec2(outer_left, outer_bottom),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Outer BL
                    Shape2D_RenderPipelineData[7] = {
                        ComplexApplyRotation(
                            glm::vec2(inner_left, inner_bottom),
                            ShapeCenter,
                            RotationSin, RotationCos), ColorIndex}; // Inner BL

                    Shape2D_RenderPipelineData[8] = Shape2D_RenderPipelineData[0];
                    Shape2D_RenderPipelineData[9] = Shape2D_RenderPipelineData[1];
                }
            }
        }
        PMMA::RenderPipelineCore->AddObject(this, RenderPipelineCompatible);
    } else {
        if (Changed) {
            // Calculate data and add to buffers, Left intentionally blank for now
        }
        // Do NOTHING.
    }

    Changed = false;
}

void CPP_RectangleShape::InternalRender() {
    // Left intentionally blank for now
}
