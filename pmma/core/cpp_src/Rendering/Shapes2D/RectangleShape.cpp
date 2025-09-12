#include "PMMA_Core.hpp"

using namespace std;

CPP_RectangleShape::CPP_RectangleShape() {
    Logger = new CPP_Logger();
    ShapeCenterFormat = new CPP_DisplayCoordinateFormat();
    ColorFormat = new CPP_ColorFormat();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_RectangleShape::Render() {
    unsigned int DisplayWidth, DisplayHeight;
    DisplayWidth = PMMA_Core::DisplayInstance->GetWidth();
    DisplayHeight = PMMA_Core::DisplayInstance->GetHeight();

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (!ShapeCenterFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no center set, please use the `Rectangle.shape_center` \
API to set it.");
        throw runtime_error("Shape has no center set");
    }

    if (!ColorFormat->GetSet()) {
        Logger->InternalLogWarn(
            30,
            "This shape has no color set, please use the `Rectangle.shape_color` \
API to set it.");
        throw runtime_error("Shape has no color set");
    }

    if (!SizeSet) {
        Logger->InternalLogWarn(
            30,
            "This shape has no size set, please use `Rectangle.set_size` to set it.");
        throw runtime_error("Shape has no size set");
    }

    float ShapeCenter[2];
    ShapeCenterFormat->Get(ShapeCenter);

    VertexDataChanged = VertexDataChanged ||
        ShapeCenterFormat->GetChangedToggle() ||
        PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenter[0] + HalfWidth < 0 ||
            ShapeCenter[0] - HalfWidth > DisplayWidth ||
            ShapeCenter[1] + HalfHeight < 0 ||
            ShapeCenter[1] - HalfHeight > DisplayHeight) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);

    ColorDataChanged = ColorDataChanged || ColorFormat->GetInternalChangedToggle();

    if (RenderPipelineCompatible) {
        if (ColorData == 0) { // Return if shape not visible
            return;
        }

        bool ColorIndexChanged = false;
        GLuint newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = ColorIndex != 0;
            VertexDataChanged = true;
            ColorIndex = newColorIndex;
        }

        if (VertexDataChanged) {
            unsigned int InternalWidth = Width;
            if (Width == 0) {
                InternalWidth = max(HalfWidth, HalfHeight);
            }

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            if (CornerRadius != 0) {
                unsigned int radius = min(CornerRadius, min(HalfWidth, HalfHeight));
                float minAngle = 1.0f / radius;
                unsigned int segments = max(3u, static_cast<unsigned int>(
                    1 + (CPP_Constants::TAU / asin(minAngle)) * PMMA_Registry::CurrentShapeQuality / 4));

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
                        float unit[2], outer[2], inner[2], rotated_outer[2], rotated_inner[2];
                        unit[0] = x;
                        unit[1] = y;

                        outer[0] = outerCenter.x + vectorized_outer_radius.x * unit[0];
                        outer[1] = outerCenter.y + vectorized_outer_radius.y * unit[1];

                        inner[0] = innerCenter.x + vectorized_inner_radius.x * unit[0];
                        inner[1] = innerCenter.y + vectorized_inner_radius.y * unit[1];

                        rotated_outer[0] = RotationCos * outer[0] - RotationSin * outer[1];
                        rotated_outer[1] = RotationSin * outer[0] + RotationCos * outer[1];

                        rotated_inner[0] = RotationCos * inner[0] - RotationSin * inner[1];
                        rotated_inner[1] = RotationSin * inner[0] + RotationCos * inner[1];

                        auto &v0 = Shape2D_RenderPipelineData[index + i * 2];
                        v0.x = ShapeCenter[0] + rotated_outer[0]; v0.y = ShapeCenter[1] + rotated_outer[1]; v0.s = ColorIndex;

                        auto &v1 = Shape2D_RenderPipelineData[index + i * 2 + 1];
                        v1.x = ShapeCenter[0] + rotated_inner[0]; v1.y = ShapeCenter[1] + rotated_inner[1]; v1.s = ColorIndex;

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
            } else {
                if (Width == 0 || Width >= max(HalfWidth, HalfHeight)) {
                    float point[2], out[2];
                    Shape2D_RenderPipelineData.resize(4);

                    point[0] = ShapeCenter[0] - HalfWidth;
                    point[1] = ShapeCenter[1] - HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v0 = Shape2D_RenderPipelineData[0];
                    v0.x = out[0]; v0.y = out[1]; v0.s = ColorIndex;

                    point[0] = ShapeCenter[0] + HalfWidth;
                    point[1] = ShapeCenter[1] - HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v1 = Shape2D_RenderPipelineData[1];
                    v1.x = out[0]; v1.y = out[1]; v1.s = ColorIndex;

                    point[0] = ShapeCenter[0] + HalfWidth;
                    point[1] = ShapeCenter[1] + HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v2 = Shape2D_RenderPipelineData[2];
                    v2.x = out[0]; v2.y = out[1]; v2.s = ColorIndex;

                    point[0] = ShapeCenter[0] - HalfWidth;
                    point[1] = ShapeCenter[1] + HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v3 = Shape2D_RenderPipelineData[3];
                    v3.x = out[0]; v3.y = out[1]; v3.s = ColorIndex;
                } else {
                    float pos[2], out[2];
                    Shape2D_RenderPipelineData.resize(10);

                    int outer_left = ShapeCenter[0] - HalfWidth;
                    int outer_right = ShapeCenter[0] + HalfWidth;
                    int outer_top = ShapeCenter[1] - HalfHeight;
                    int outer_bottom = ShapeCenter[1] + HalfHeight;

                    int inner_left = outer_left + Width;
                    int inner_right = outer_right - Width;
                    int inner_top = outer_top + Width;
                    int inner_bottom = outer_bottom - Width;

                    // GL_TRIANGLE_STRIP order: Outer TL, Inner TL, Outer TR, Inner TR, Outer BR, Inner BR, Outer BL, Inner BL
                    pos[0] = outer_left;
                    pos[1] = outer_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v0 = Shape2D_RenderPipelineData[0];
                    v0.x = out[0]; v0.y = out[1]; v0.s = ColorIndex;

                    pos[0] = inner_left;
                    pos[1] = inner_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v1 = Shape2D_RenderPipelineData[1];
                    v1.x = out[0]; v1.y = out[1]; v1.s = ColorIndex;

                    pos[0] = outer_right;
                    pos[1] = outer_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v2 = Shape2D_RenderPipelineData[2];
                    v2.x = out[0]; v2.y = out[1]; v2.s = ColorIndex;

                    pos[0] = inner_right;
                    pos[1] = inner_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v3 = Shape2D_RenderPipelineData[3];
                    v3.x = out[0]; v3.y = out[1]; v3.s = ColorIndex;

                    pos[0] = outer_right;
                    pos[1] = outer_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v4 = Shape2D_RenderPipelineData[4];
                    v4.x = out[0]; v4.y = out[1]; v4.s = ColorIndex;

                    pos[0] = inner_right;
                    pos[1] = inner_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v5 = Shape2D_RenderPipelineData[5];
                    v5.x = out[0]; v5.y = out[1]; v5.s = ColorIndex;

                    pos[0] = outer_left;
                    pos[1] = outer_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v6 = Shape2D_RenderPipelineData[6];
                    v6.x = out[0]; v6.y = out[1]; v6.s = ColorIndex;

                    pos[0] = inner_left;
                    pos[1] = inner_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    auto &v7 = Shape2D_RenderPipelineData[7];
                    v7.x = out[0]; v7.y = out[1]; v7.s = ColorIndex;

                    Shape2D_RenderPipelineData[8] = Shape2D_RenderPipelineData[0];
                    Shape2D_RenderPipelineData[9] = Shape2D_RenderPipelineData[1];
                }
            }
        }
        PMMA_Core::RenderPipelineCore->AddObject(this, RenderPipelineCompatible, ColorIndexChanged);
    } else {
        if (VertexDataChanged) {
            // Calculate data and add to buffers, Left intentionally blank for now
        }
        // Do NOTHING.
    }

    VertexDataChanged = false;
    ColorDataChanged = false;
}

void CPP_RectangleShape::InternalRender() {
    // Left intentionally blank for now
}
