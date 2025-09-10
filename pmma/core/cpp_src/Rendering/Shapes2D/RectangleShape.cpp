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

    uint8_t ColorData[4];
    ColorFormat->Get_RGBA(ColorData);

    if (RenderPipelineCompatible) {
        if (ColorData == 0) { // Return if shape not visible
            return;
        }

        bool ColorIndexChanged = false;
        GLuint newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = ColorIndex != 0;
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

                        Shape2D_RenderPipelineData[index + i * 2]     = {ShapeCenter.x + rotated_outer[0], ShapeCenter.y + rotated_outer[1], ColorIndex, 0};
                        Shape2D_RenderPipelineData[index + i * 2 + 1] = {ShapeCenter.x + rotated_inner[0], ShapeCenter.y + rotated_inner[1], ColorIndex, 0};

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

                    point[0] = ShapeCenter.x - HalfWidth;
                    point[1] = ShapeCenter.y - HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    Shape2D_RenderPipelineData[0] = {
                        out[0], out[1], ColorIndex, 0};


                    point[0] = ShapeCenter.x + HalfWidth;
                    point[1] = ShapeCenter.y - HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    Shape2D_RenderPipelineData[1] = {
                        out[0], out[1], ColorIndex, 0};


                    point[0] = ShapeCenter.x + HalfWidth;
                    point[1] = ShapeCenter.y + HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    Shape2D_RenderPipelineData[2] = {
                        out[0], out[1], ColorIndex, 0};


                    point[0] = ShapeCenter.x - HalfWidth;
                    point[1] = ShapeCenter.y + HalfHeight;

                    SimpleApplyRotation(point, ShapeCenter, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    Shape2D_RenderPipelineData[3] = {
                        out[0], out[1], ColorIndex, 0};
                } else {
                    float pos[2], out[2];
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
                    pos[0] = outer_left;
                    pos[1] = outer_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[0] = {
                        out[0], out[1], ColorIndex, 0}; // Outer TL

                    pos[0] = inner_left;
                    pos[1] = inner_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[1] = {
                        out[0], out[1], ColorIndex, 0}; // Inner TL

                    pos[0] = outer_right;
                    pos[1] = outer_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[2] = {
                        out[0], out[1], ColorIndex, 0}; // Outer TR

                    pos[0] = inner_right;
                    pos[1] = inner_top;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[3] = {
                        out[0], out[1], ColorIndex, 0}; // Inner TR

                    pos[0] = outer_right;
                    pos[1] = outer_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[4] = {
                        out[0], out[1], ColorIndex, 0}; // Outer BR

                    pos[0] = inner_right;
                    pos[1] = inner_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[5] = {
                        out[0], out[1], ColorIndex, 0}; // Inner BR

                    pos[0] = outer_left;
                    pos[1] = outer_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[6] = {
                        out[0], out[1], ColorIndex, 0}; // Outer BL

                    pos[0] = inner_left;
                    pos[1] = inner_bottom;

                    ComplexApplyRotation(pos, ShapeCenter,
                        RotationSin, RotationCos, out);

                    Shape2D_RenderPipelineData[7] = {
                        out[0], out[1], ColorIndex, 0}; // Inner BL

                    Shape2D_RenderPipelineData[8] = Shape2D_RenderPipelineData[0];
                    Shape2D_RenderPipelineData[9] = Shape2D_RenderPipelineData[1];
                }
            }
        }
        PMMA_Core::RenderPipelineCore->AddObject(this, RenderPipelineCompatible, ColorIndexChanged);
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
