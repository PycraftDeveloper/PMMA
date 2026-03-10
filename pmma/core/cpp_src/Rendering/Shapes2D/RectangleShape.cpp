#include "PMMA_Core.hpp"

CPP_RectangleShape::CPP_RectangleShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();

    ID = PMMA_Registry::ClassObject_ID_System++;
}

void CPP_RectangleShape::Render() {
    int DisplaySize[2];
    PMMA_Core::DisplayInstance->GetSize(DisplaySize);

    unsigned int HalfWidth = ShapeSize.x / 2;
    unsigned int HalfHeight = ShapeSize.y / 2;

    if (!ShapeCenter->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }

        Logger->InternalLogError(
            30,
            "This shape has no center set, please use the `Rectangle.shape_center` \
API to set it.");
        throw std::runtime_error("Shape has no center set");
    }

    if (!Color->GetSet()) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }

        Logger->InternalLogError(
            30,
            "This shape has no color set, please use the `Rectangle.shape_color` \
API to set it.");
        throw std::runtime_error("Shape has no color set");
    }

    if (!SizeSet) {
        if (Logger == nullptr) {
            Logger = new CPP_Logger();
        }

        Logger->InternalLogError(
            30,
            "This shape has no size set, please use `Rectangle.set_size` to set it.");
        throw std::runtime_error("Shape has no size set");
    }

    float ShapeCenterPosition[2];
    ShapeCenter->Get(ShapeCenterPosition);

    VertexDataChanged = VertexDataChanged ||
        ShapeCenter->GetChangedToggle() ||
        PMMA_Core::DisplayInstance->DisplaySizeChanged;

    if (ShapeCenterPosition[0] + HalfWidth < 0 ||
            ShapeCenterPosition[0] - HalfWidth > DisplaySize[0] ||
            ShapeCenterPosition[1] + HalfHeight < 0 ||
            ShapeCenterPosition[1] - HalfHeight > DisplaySize[1]) {
        return;
    }

    bool RenderPipelineCompatible = true;
    // check here if the gradient has been set, if has then check it fits into the render pipeline
    // otherwise render it as a normal shape.

    uint8_t ColorData[4];
    Color->Get_RGBA(ColorData);

    ColorDataChanged = ColorDataChanged || Color->GetInternalChangedToggle();

    if (RenderPipelineCompatible) {
        if (ColorData[3] == 0) { // Return if shape not visible
            return;
        }

        bool ColorIndexChanged = false;
        float newColorIndex = PMMA_Core::RenderPipelineCore->Shape2D_GetColorIndex(ColorData, ID);

        if (newColorIndex != ColorIndex) {
            ColorIndexChanged = true;
            VertexDataChanged = true;
            ColorIndex = newColorIndex;
        }

        if (VertexDataChanged) {
            unsigned int InternalWidth = Width;
            if (Width == 0) {
                InternalWidth = std::max(HalfWidth, HalfHeight);
            }

            float RotationSin = sin(Rotation);
            float RotationCos = cos(Rotation);

            if (CornerRadius != 0) {
                if (Width == 0) { // This works but needs simplifying
                    unsigned int maxRadius = std::min(CornerRadius, std::min(HalfWidth, HalfHeight));

                    // For filled shapes, ensure inner radius doesn't go negative
                    unsigned int outerRadius = maxRadius;
                    unsigned int innerRadius = 0;

                    if (Width > 0) {
                        innerRadius = (maxRadius > InternalWidth) ? (maxRadius - InternalWidth) : 0;
                    } else {
                        innerRadius = maxRadius;
                    }

                    float minAngle = 1.0f / std::max(outerRadius, 1u);
                    unsigned int segments = std::max(3u, static_cast<unsigned int>(
                        1 + (CPP_Constants::TAU / asin(minAngle)) * PMMA_Registry::CurrentShapeQuality / 4));

                    size_t vertexCount = (segments + 1) * 8 + 2;
                    Shape2D_RenderPipelineVertices.resize(vertexCount);

                    int outerRad = outerRadius;
                    int innerRad = innerRadius;

                    glm::vec2 vecOuterRad = glm::vec2(outerRad, outerRad);
                    glm::vec2 vecInnerRad = glm::vec2(innerRad, innerRad);

                    int outerW = ShapeSize.x;
                    int outerH = ShapeSize.y;
                    int innerW = outerW - 2 * InternalWidth;
                    int innerH = outerH - 2 * InternalWidth;

                    // Clamp inner dimensions to prevent negative values
                    innerW = std::max(innerW, 0);
                    innerH = std::max(innerH, 0);

                    const glm::vec2 outerCenters[4] = {
                        {-outerW / 2.0f + outerRad, -outerH / 2.0f + outerRad}, // top-left
                        { outerW / 2.0f - outerRad, -outerH / 2.0f + outerRad}, // top-right
                        { outerW / 2.0f - outerRad,  outerH / 2.0f - outerRad}, // bottom-right
                        {-outerW / 2.0f + outerRad,  outerH / 2.0f - outerRad}  // bottom-left
                    };

                    const glm::vec2 innerCenters[4] = {
                        {-innerW / 2.0f + innerRad, -innerH / 2.0f + innerRad},
                        { innerW / 2.0f - innerRad, -innerH / 2.0f + innerRad},
                        { innerW / 2.0f - innerRad,  innerH / 2.0f - innerRad},
                        {-innerW / 2.0f + innerRad,  innerH / 2.0f - innerRad}
                    };

                    const float startAngles[4] = {
                        CPP_Constants::PI,             // 180°
                        CPP_Constants::PI * 1.5f,      // 270°
                        0.0f,                          // 0°
                        CPP_Constants::PI * 0.5f       // 90°
                    };

                    // Precompute rotation matrix increments
                    float cosD = cos((CPP_Constants::PI * 0.5f) / segments);
                    float sinD = sin((CPP_Constants::PI * 0.5f) / segments);

                    for (int corner = 0; corner < 4; ++corner) {
                        glm::vec2 outerCenter = outerCenters[corner];
                        glm::vec2 innerCenter = innerCenters[corner];

                        float angle = startAngles[corner];
                        float x = cos(angle);
                        float y = sin(angle);

                        unsigned int index = corner * (segments + 1) * 2;

                        for (unsigned int i = 0; i <= segments; ++i) {
                            // Calculate outer point
                            float outerX = outerCenter.x + vecOuterRad.x * x;
                            float outerY = outerCenter.y + vecOuterRad.y * y;

                            // Calculate inner point
                            float innerX = innerCenter.x + vecInnerRad.x * x;
                            float innerY = innerCenter.y + vecInnerRad.y * y;

                            // Apply rotation
                            float rotOuterX = RotationCos * outerX - RotationSin * outerY;
                            float rotOuterY = RotationSin * outerX + RotationCos * outerY;

                            float rotInnerX = RotationCos * innerX - RotationSin * innerY;
                            float rotInnerY = RotationSin * innerX + RotationCos * innerY;

                            // Store vertices
                            auto &v0 = Shape2D_RenderPipelineVertices[index + i * 2];
                            v0.x = ShapeCenterPosition[0] + rotOuterX;
                            v0.y = ShapeCenterPosition[1] + rotOuterY;
                            v0.s = ColorIndex;

                            auto &v1 = Shape2D_RenderPipelineVertices[index + i * 2 + 1];
                            v1.x = ShapeCenterPosition[0];
                            v1.y = ShapeCenterPosition[1];
                            v1.s = ColorIndex;

                            // Rotate unit vector using matrix
                            float newX = cosD * x - sinD * y;
                            float newY = sinD * x + cosD * y;
                            x = newX;
                            y = newY;
                        }
                    }

                    // Close the loop
                    Shape2D_RenderPipelineVertices[vertexCount - 2] = Shape2D_RenderPipelineVertices[0];
                    Shape2D_RenderPipelineVertices[vertexCount - 1] = Shape2D_RenderPipelineVertices[1];
                } else {
                    unsigned int maxRadius = std::min(CornerRadius, std::min(HalfWidth, HalfHeight));

                // For filled shapes, ensure inner radius doesn't go negative
                unsigned int outerRadius = maxRadius;
                unsigned int innerRadius = 0;

                if (Width > 0) {
                    innerRadius = (maxRadius > InternalWidth) ? (maxRadius - InternalWidth) : 0;
                } else {
                    innerRadius = maxRadius;
                }

                float minAngle = 1.0f / std::max(outerRadius, 1u);
                unsigned int segments = std::max(3u, static_cast<unsigned int>(
                    1 + (CPP_Constants::TAU / asin(minAngle)) * PMMA_Registry::CurrentShapeQuality / 4));

                size_t vertexCount = (segments + 1) * 8 + 2;
                Shape2D_RenderPipelineVertices.resize(vertexCount);

                int outerRad = outerRadius;
                int innerRad = innerRadius;

                glm::vec2 vecOuterRad = glm::vec2(outerRad, outerRad);
                glm::vec2 vecInnerRad = glm::vec2(innerRad, innerRad);

                int outerW = ShapeSize.x;
                int outerH = ShapeSize.y;
                int innerW = outerW - 2 * InternalWidth;
                int innerH = outerH - 2 * InternalWidth;

                // Clamp inner dimensions to prevent negative values
                innerW = std::max(innerW, 0);
                innerH = std::max(innerH, 0);

                const glm::vec2 outerCenters[4] = {
                    {-outerW / 2.0f + outerRad, -outerH / 2.0f + outerRad}, // top-left
                    { outerW / 2.0f - outerRad, -outerH / 2.0f + outerRad}, // top-right
                    { outerW / 2.0f - outerRad,  outerH / 2.0f - outerRad}, // bottom-right
                    {-outerW / 2.0f + outerRad,  outerH / 2.0f - outerRad}  // bottom-left
                };

                const glm::vec2 innerCenters[4] = {
                    {-innerW / 2.0f + innerRad, -innerH / 2.0f + innerRad},
                    { innerW / 2.0f - innerRad, -innerH / 2.0f + innerRad},
                    { innerW / 2.0f - innerRad,  innerH / 2.0f - innerRad},
                    {-innerW / 2.0f + innerRad,  innerH / 2.0f - innerRad}
                };

                const float startAngles[4] = {
                    CPP_Constants::PI,             // 180°
                    CPP_Constants::PI * 1.5f,      // 270°
                    0.0f,                          // 0°
                    CPP_Constants::PI * 0.5f       // 90°
                };

                // Precompute rotation matrix increments
                float cosD = cos((CPP_Constants::PI * 0.5f) / segments);
                float sinD = sin((CPP_Constants::PI * 0.5f) / segments);

                for (int corner = 0; corner < 4; ++corner) {
                    glm::vec2 outerCenter = outerCenters[corner];
                    glm::vec2 innerCenter = innerCenters[corner];

                    float angle = startAngles[corner];
                    float x = cos(angle);
                    float y = sin(angle);

                    unsigned int index = corner * (segments + 1) * 2;

                    for (unsigned int i = 0; i <= segments; ++i) {
                        // Calculate outer point
                        float outerX = outerCenter.x + vecOuterRad.x * x;
                        float outerY = outerCenter.y + vecOuterRad.y * y;

                        // Calculate inner point
                        float innerX = innerCenter.x + vecInnerRad.x * x;
                        float innerY = innerCenter.y + vecInnerRad.y * y;

                        // Apply rotation
                        float rotOuterX = RotationCos * outerX - RotationSin * outerY;
                        float rotOuterY = RotationSin * outerX + RotationCos * outerY;

                        float rotInnerX = RotationCos * innerX - RotationSin * innerY;
                        float rotInnerY = RotationSin * innerX + RotationCos * innerY;

                        // Store vertices
                        auto &v0 = Shape2D_RenderPipelineVertices[index + i * 2];
                        v0.x = ShapeCenterPosition[0] + rotOuterX;
                        v0.y = ShapeCenterPosition[1] + rotOuterY;
                        v0.s = ColorIndex;

                        auto &v1 = Shape2D_RenderPipelineVertices[index + i * 2 + 1];
                        v1.x = ShapeCenterPosition[0] + rotInnerX;
                        v1.y = ShapeCenterPosition[1] + rotInnerY;
                        v1.s = ColorIndex;

                        // Rotate unit vector using matrix
                        float newX = cosD * x - sinD * y;
                        float newY = sinD * x + cosD * y;
                        x = newX;
                        y = newY;
                    }
                }

                // Close the loop
                Shape2D_RenderPipelineVertices[vertexCount - 2] = Shape2D_RenderPipelineVertices[0];
                Shape2D_RenderPipelineVertices[vertexCount - 1] = Shape2D_RenderPipelineVertices[1];
                }

            } else {
                if (Width == 0 || Width >= std::max(HalfWidth, HalfHeight)) {
                    float point[2], out[2];
                    Shape2D_RenderPipelineVertices.resize(4);

                    point[0] = ShapeCenterPosition[0] - HalfWidth;
                    point[1] = ShapeCenterPosition[1] - HalfHeight;

                    SimpleApplyRotation(point, ShapeCenterPosition, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v0 = Shape2D_RenderPipelineVertices[0];
                    v0.x = out[0]; v0.y = out[1]; v0.s = ColorIndex;

                    point[0] = ShapeCenterPosition[0] + HalfWidth;
                    point[1] = ShapeCenterPosition[1] - HalfHeight;

                    SimpleApplyRotation(point, ShapeCenterPosition, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v1 = Shape2D_RenderPipelineVertices[1];
                    v1.x = out[0]; v1.y = out[1]; v1.s = ColorIndex;

                    point[0] = ShapeCenterPosition[0] - HalfWidth;
                    point[1] = ShapeCenterPosition[1] + HalfHeight;

                    SimpleApplyRotation(point, ShapeCenterPosition, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v2 = Shape2D_RenderPipelineVertices[2];
                    v2.x = out[0]; v2.y = out[1]; v2.s = ColorIndex;

                    point[0] = ShapeCenterPosition[0] + HalfWidth;
                    point[1] = ShapeCenterPosition[1] + HalfHeight;

                    SimpleApplyRotation(point, ShapeCenterPosition, RotationSin,
                        RotationCos, HalfWidth, HalfHeight, out);

                    auto &v3 = Shape2D_RenderPipelineVertices[3];
                    v3.x = out[0]; v3.y = out[1]; v3.s = ColorIndex;
                } else {
                    float pos[2], out[2];
                    Shape2D_RenderPipelineVertices.resize(10);

                    int outer_left = ShapeCenterPosition[0] - HalfWidth;
                    int outer_right = ShapeCenterPosition[0] + HalfWidth;
                    int outer_top = ShapeCenterPosition[1] - HalfHeight;
                    int outer_bottom = ShapeCenterPosition[1] + HalfHeight;

                    int inner_left = outer_left + Width;
                    int inner_right = outer_right - Width;
                    int inner_top = outer_top + Width;
                    int inner_bottom = outer_bottom - Width;

                    // GL_TRIANGLE_STRIP order: Outer TL, Inner TL, Outer TR, Inner TR, Outer BR, Inner BR, Outer BL, Inner BL
                    pos[0] = outer_left;
                    pos[1] = outer_top;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v0 = Shape2D_RenderPipelineVertices[0];
                    v0.x = out[0]; v0.y = out[1]; v0.s = ColorIndex;

                    pos[0] = inner_left;
                    pos[1] = inner_top;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v1 = Shape2D_RenderPipelineVertices[1];
                    v1.x = out[0]; v1.y = out[1]; v1.s = ColorIndex;

                    pos[0] = outer_right;
                    pos[1] = outer_top;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v2 = Shape2D_RenderPipelineVertices[2];
                    v2.x = out[0]; v2.y = out[1]; v2.s = ColorIndex;

                    pos[0] = inner_right;
                    pos[1] = inner_top;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v3 = Shape2D_RenderPipelineVertices[3];
                    v3.x = out[0]; v3.y = out[1]; v3.s = ColorIndex;

                    pos[0] = outer_right;
                    pos[1] = outer_bottom;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v4 = Shape2D_RenderPipelineVertices[4];
                    v4.x = out[0]; v4.y = out[1]; v4.s = ColorIndex;

                    pos[0] = inner_right;
                    pos[1] = inner_bottom;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v5 = Shape2D_RenderPipelineVertices[5];
                    v5.x = out[0]; v5.y = out[1]; v5.s = ColorIndex;

                    pos[0] = outer_left;
                    pos[1] = outer_bottom;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v6 = Shape2D_RenderPipelineVertices[6];
                    v6.x = out[0]; v6.y = out[1]; v6.s = ColorIndex;

                    pos[0] = inner_left;
                    pos[1] = inner_bottom;

                    ComplexApplyRotation(pos, ShapeCenterPosition,
                        RotationSin, RotationCos, out);

                    auto &v7 = Shape2D_RenderPipelineVertices[7];
                    v7.x = out[0]; v7.y = out[1]; v7.s = ColorIndex;

                    Shape2D_RenderPipelineVertices[8] = Shape2D_RenderPipelineVertices[0];
                    Shape2D_RenderPipelineVertices[9] = Shape2D_RenderPipelineVertices[1];
                }
            }
        }
        PMMA_Core::RenderPipelineCore->Add_2D_Shape_Object(this, RenderPipelineCompatible, ColorIndexChanged);
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