#include "PMMA_Core.hpp"

CPP_RectangleShape::CPP_RectangleShape() {
    ShapeCenter = new CPP_DisplayCoordinate();
    Color = new CPP_Color();
    ID = PMMA_Registry::ClassObject_ID_System++;
}

inline void EnsureLogger(CPP_Logger *&logger) {
    if (!logger)
        logger = new CPP_Logger();
}

void CPP_RectangleShape::Render() {
    auto *display = PMMA_Core::DisplayInstance;
    auto *pipeline = PMMA_Core::RenderPipelineCore;

    int displaySize[2];
    display->GetSize(displaySize);

    const unsigned int halfW = ShapeSize.x / 2;
    const unsigned int halfH = ShapeSize.y / 2;

    if (!ShapeCenter->GetSet()) {
        EnsureLogger(Logger);
        Logger->InternalLogError(30,
                                 "This shape has no center set, please use Rectangle.shape_center");
        throw std::runtime_error("Shape has no center set");
    }

    if (!Color->GetSet()) {
        EnsureLogger(Logger);
        Logger->InternalLogError(30,
                                 "This shape has no color set, please use Rectangle.shape_color");
        throw std::runtime_error("Shape has no color set");
    }

    if (!SizeSet) {
        EnsureLogger(Logger);
        Logger->InternalLogError(30,
                                 "This shape has no size set, please use Rectangle.set_size");
        throw std::runtime_error("Shape has no size set");
    }

    float center[2];
    ShapeCenter->Get(center);

    VertexDataChanged |= ShapeCenter->GetChangedToggle() || display->DisplaySizeChanged;

    if (center[0] + halfW < 0 ||
        center[0] - halfW > displaySize[0] ||
        center[1] + halfH < 0 ||
        center[1] - halfH > displaySize[1])
        return;

    uint8_t colorData[4];
    Color->Get_RGBA(colorData);

    ColorDataChanged |= Color->GetInternalChangedToggle();

    if (colorData[3] == 0)
        return;

    bool colorIndexChanged = false;
    float newColorIndex = pipeline->Shape2D_GetColorIndex(colorData, ID);

    if (newColorIndex != ColorIndex) {
        ColorIndex = newColorIndex;
        VertexDataChanged = true;
        colorIndexChanged = true;
    }

    if (VertexDataChanged) {

        const unsigned int internalWidth = Width ? Width : std::max(halfW, halfH);

        const float sinR = sin(Rotation);
        const float cosR = cos(Rotation);

        /* =========================
           ROUNDED CORNERS
           ========================= */
        if (CornerRadius) {
            const unsigned int maxRadius = std::min(CornerRadius, std::min(halfW, halfH));

            unsigned int outerRadius = maxRadius;
            unsigned int innerRadius = (Width > 0)
                                           ? (maxRadius > internalWidth ? maxRadius - internalWidth : 0)
                                           : maxRadius;

            float minAngle = 1.0f / std::max(outerRadius, 1u);

            unsigned int segments = std::max(
                3u,
                (unsigned int)(1 + (CPP_Constants::TAU / asin(minAngle)) *
                                       PMMA_Registry::CurrentShapeQuality / 4));

            size_t vertexCount = (segments + 1) * 8 + 2;
            Shape2D_RenderPipelineVertices.resize(vertexCount);

            const int outerW = ShapeSize.x;
            const int outerH = ShapeSize.y;

            int innerW = std::max(outerW - 2 * internalWidth, 0u);
            int innerH = std::max(outerH - 2 * internalWidth, 0u);

            const glm::vec2 outerCenters[4] = {
                {-outerW / 2.f + outerRadius, -outerH / 2.f + outerRadius},
                {outerW / 2.f - outerRadius, -outerH / 2.f + outerRadius},
                {outerW / 2.f - outerRadius, outerH / 2.f - outerRadius},
                {-outerW / 2.f + outerRadius, outerH / 2.f - outerRadius}};

            const glm::vec2 innerCenters[4] = {
                {-innerW / 2.f + innerRadius, -innerH / 2.f + innerRadius},
                {innerW / 2.f - innerRadius, -innerH / 2.f + innerRadius},
                {innerW / 2.f - innerRadius, innerH / 2.f - innerRadius},
                {-innerW / 2.f + innerRadius, innerH / 2.f - innerRadius}};

            const float startAngles[4] = {
                CPP_Constants::PI,
                CPP_Constants::PI * 1.5f,
                0.0f,
                CPP_Constants::PI * 0.5f};

            const float cosD = cos((CPP_Constants::PI * 0.5f) / segments);
            const float sinD = sin((CPP_Constants::PI * 0.5f) / segments);

            for (int corner = 0; corner < 4; ++corner) {

                float x = cos(startAngles[corner]);
                float y = sin(startAngles[corner]);

                unsigned int base = corner * (segments + 1) * 2;

                for (unsigned int i = 0; i <= segments; ++i) {

                    float outerX = outerCenters[corner].x + outerRadius * x;
                    float outerY = outerCenters[corner].y + outerRadius * y;

                    float innerX = innerCenters[corner].x + innerRadius * x;
                    float innerY = innerCenters[corner].y + innerRadius * y;

                    float rotOuterX = cosR * outerX - sinR * outerY;
                    float rotOuterY = sinR * outerX + cosR * outerY;

                    float rotInnerX = cosR * innerX - sinR * innerY;
                    float rotInnerY = sinR * innerX + cosR * innerY;

                    auto &v0 = Shape2D_RenderPipelineVertices[base + i * 2];
                    v0.x = center[0] + rotOuterX;
                    v0.y = center[1] + rotOuterY;
                    v0.color = ColorIndex;

                    auto &v1 = Shape2D_RenderPipelineVertices[base + i * 2 + 1];

                    if (Width == 0) {
                        v1.x = center[0];
                        v1.y = center[1];
                    } else {
                        v1.x = center[0] + rotInnerX;
                        v1.y = center[1] + rotInnerY;
                    }

                    v1.color = ColorIndex;

                    float nx = cosD * x - sinD * y;
                    y = sinD * x + cosD * y;
                    x = nx;
                }
            }

            Shape2D_RenderPipelineVertices[vertexCount - 2] =
                Shape2D_RenderPipelineVertices[0];

            Shape2D_RenderPipelineVertices[vertexCount - 1] =
                Shape2D_RenderPipelineVertices[1];
        }

        /* =========================
           NON-ROUNDED RECTANGLE
           ========================= */
        else {
            /* FILLED RECTANGLE */
            if (Width == 0 || Width >= std::max(halfW, halfH)) {

                Shape2D_RenderPipelineVertices.resize(4);

                float pts[4][2] = {
                    {center[0] - halfW, center[1] - halfH},
                    {center[0] + halfW, center[1] - halfH},
                    {center[0] - halfW, center[1] + halfH},
                    {center[0] + halfW, center[1] + halfH}};

                for (int i = 0; i < 4; ++i) {

                    float out[2];

                    SimpleApplyRotation(
                        pts[i], center, sinR, cosR,
                        halfW, halfH, out);

                    auto &v = Shape2D_RenderPipelineVertices[i];
                    v.x = out[0];
                    v.y = out[1];
                    v.color = ColorIndex;
                }
            }

            /* BORDER RECTANGLE */
            else {

                Shape2D_RenderPipelineVertices.resize(10);

                int outer_left = center[0] - halfW;
                int outer_right = center[0] + halfW;
                int outer_top = center[1] - halfH;
                int outer_bottom = center[1] + halfH;

                int inner_left = outer_left + Width;
                int inner_right = outer_right - Width;
                int inner_top = outer_top + Width;
                int inner_bottom = outer_bottom - Width;

                float pos[2], out[2];

                const int coords[8][2] = {
                    {outer_left, outer_top},
                    {inner_left, inner_top},
                    {outer_right, outer_top},
                    {inner_right, inner_top},
                    {outer_right, outer_bottom},
                    {inner_right, inner_bottom},
                    {outer_left, outer_bottom},
                    {inner_left, inner_bottom}};

                for (int i = 0; i < 8; ++i) {

                    pos[0] = coords[i][0];
                    pos[1] = coords[i][1];

                    ComplexApplyRotation(
                        pos, center, sinR, cosR, out);

                    auto &v = Shape2D_RenderPipelineVertices[i];
                    v.x = out[0];
                    v.y = out[1];
                    v.color = ColorIndex;
                }

                Shape2D_RenderPipelineVertices[8] =
                    Shape2D_RenderPipelineVertices[0];

                Shape2D_RenderPipelineVertices[9] =
                    Shape2D_RenderPipelineVertices[1];
            }
        }
    }

    pipeline->Add_2D_Shape_Object(this, true, colorIndexChanged);

    VertexDataChanged = false;
    ColorDataChanged = false;
}

void CPP_RectangleShape::InternalRender() {}