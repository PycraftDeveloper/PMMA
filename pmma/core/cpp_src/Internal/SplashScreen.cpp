#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/ParallelWorker.hpp"
#include "Internal/SplashScreen.hpp"

#include "Rendering/Shapes2D/LineShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"

#include "Display.hpp"
#include "General.hpp"

void PMMA::Internal::SplashScreen::Play() {
    // ------------------------------------------------------------
    // Progress bar dimensions
    // ------------------------------------------------------------

    uint16_t display_size[2];
    PMMA::Core::MasterDisplayInstance->GetSize(display_size);

    uint16_t maxProgressBarWidth =
        static_cast<uint16_t>(display_size[0] * 0.8f);

    uint16_t borderWidth = 3;
    uint16_t gap = 1;

    uint16_t barHeight = std::clamp(
        static_cast<int>(25 * (display_size[1] / 700.0f)),
        3 + (borderWidth + gap) * 2,
        25);

    // ------------------------------------------------------------
    // Outer bar positioning
    // ------------------------------------------------------------

    float barX = display_size[0] / 2.0f;
    float barY =
        display_size[1] -
        ((display_size[0] - maxProgressBarWidth) / 2.0f) -
        ((barHeight + borderWidth * 2) / 2.0f);

    uint16_t maskWidth =
        maxProgressBarWidth + (borderWidth * 2);

    uint16_t maskHeight =
        barHeight + (borderWidth * 2);

    // ------------------------------------------------------------
    // Colours
    // ------------------------------------------------------------

    uint8_t WindowColor[3];
    PMMA::Core::MasterDisplayInstance->WindowFillColor->Get_RGB(WindowColor);
    uint8_t AccentColor[3];
    AccentColor[0] = 255 - WindowColor[0];
    AccentColor[1] = 255 - WindowColor[1];
    AccentColor[2] = 255 - WindowColor[2];

    uint8_t TextureColor[3] = {176, 46, 12};
    uint8_t ShaderColor[3] = {147, 183, 190};
    uint8_t FontColor[3] = {169, 219, 184};

    // ------------------------------------------------------------
    // Inner bars
    // ------------------------------------------------------------

    PMMA::Rendering::TwoD::Shapes::Line InnerTexturesLine;
    InnerTexturesLine.Color.Set_RGB(TextureColor);
    InnerTexturesLine.SetWidth(barHeight * 0.5f);

    PMMA::Rendering::TwoD::Shapes::Line InnerShadersLine;
    InnerShadersLine.Color.Set_RGB(ShaderColor);
    InnerShadersLine.SetWidth(barHeight * 0.5f);

    PMMA::Rendering::TwoD::Shapes::Line InnerFontsLine;
    InnerFontsLine.Color.Set_RGB(FontColor);
    InnerFontsLine.SetWidth(barHeight * 0.5f);

    // ------------------------------------------------------------
    // Mask
    // ------------------------------------------------------------

    PMMA::Rendering::TwoD::Shapes::Rectangle RectMask;

    RectMask.ShapeCenter.SetX(barX);
    RectMask.ShapeCenter.SetY(barY);

    RectMask.Color.Set_RGB(WindowColor);

    RectMask.ShapeSize.SetSize(
        new uint16_t[2]{
            maskWidth,
            maskHeight});

    RectMask.SetCornerRadius(9999);
    RectMask.SetWidth(8);

    // ------------------------------------------------------------
    // Outline
    // ------------------------------------------------------------

    PMMA::Rendering::TwoD::Shapes::Rectangle Outline;

    Outline.ShapeCenter.SetX(barX);
    Outline.ShapeCenter.SetY(barY);

    // Use one consistent outline colour.
    Outline.Color.Set_RGB(AccentColor);

    Outline.ShapeSize.SetSize(
        new uint16_t[2]{
            maxProgressBarWidth,
            barHeight});

    Outline.SetWidth(borderWidth);
    Outline.SetCornerRadius(12);

    // ------------------------------------------------------------
    // Progress
    // ------------------------------------------------------------

    float progress = 0.0f;

    while (
        PMMA::General::IsApplicationRunning() &&
        progress < 1.0f) {
        PMMA::Core::MasterDisplayInstance->Clear();

        PMMA::Internal::ParallelWorker &ParallelWorker =
            *PMMA::Core::ParallelWorkerInstance;

        const uint32_t total =
            ParallelWorker.ShadersToLoad +
            ParallelWorker.TexturesToLoad +
            ParallelWorker.FontsToLoad;

        const uint32_t loaded =
            ParallelWorker.ShadersLoaded +
            ParallelWorker.TexturesLoaded +
            ParallelWorker.FontsLoaded;

        if (total > 0) {
            progress = std::clamp(
                static_cast<float>(loaded) /
                    static_cast<float>(total),
                0.0f,
                1.0f);
        } else {
            progress = 1.0f;
        }

        // --------------------------------------------------------
        // Inner progress dimensions
        // --------------------------------------------------------

        const uint16_t innerHeight =
            barHeight -
            ((borderWidth + gap) * 2);

        const uint16_t innerMaxWidth =
            maxProgressBarWidth -
            ((borderWidth + gap) * 2);

        // Left edge of the actual inner bar.
        //
        // This is the important part:
        //
        //        |<------ outer bar ------>|
        //        |  |<--- inner bar --->|  |
        //
        const float innerLeft =
            barX -
            (innerMaxWidth / 2.0f);

        // --------------------------------------------------------
        // Calculate individual progress segments
        // --------------------------------------------------------

        const float textureProgress =
            total > 0
                ? static_cast<float>(ParallelWorker.TexturesLoaded) /
                      static_cast<float>(total)
                : 0.0f;

        const float shaderProgress =
            total > 0
                ? static_cast<float>(ParallelWorker.ShadersLoaded) /
                      static_cast<float>(total)
                : 0.0f;

        const float fontProgress =
            total > 0
                ? static_cast<float>(ParallelWorker.FontsLoaded) /
                      static_cast<float>(total)
                : 0.0f;

        // --------------------------------------------------------
        // Calculate widths
        // --------------------------------------------------------

        const float textureWidth =
            innerMaxWidth * textureProgress;

        const float shaderWidth =
            innerMaxWidth * shaderProgress;

        const float fontWidth =
            innerMaxWidth * fontProgress;

        // --------------------------------------------------------
        // Textures
        // --------------------------------------------------------

        if (textureWidth > 0.0f) {
            int16_t start[2] = {
                static_cast<int16_t>(innerLeft),
                static_cast<int16_t>(barY)};

            int16_t end[2] = {
                static_cast<int16_t>(innerLeft + textureWidth),
                static_cast<int16_t>(barY)};

            InnerTexturesLine.ShapeStart.SetCoordinate(start);
            InnerTexturesLine.ShapeEnd.SetCoordinate(end);
        }

        // --------------------------------------------------------
        // Shaders
        // --------------------------------------------------------

        if (shaderWidth > 0.0f) {
            const float shaderStartX =
                innerLeft + textureWidth - 1.0f; // Overlap by 1 pixel

            int16_t start[2] = {
                static_cast<int16_t>(shaderStartX),
                static_cast<int16_t>(barY)};

            int16_t end[2] = {
                static_cast<int16_t>(shaderStartX + shaderWidth),
                static_cast<int16_t>(barY)};

            InnerShadersLine.ShapeStart.SetCoordinate(start);
            InnerShadersLine.ShapeEnd.SetCoordinate(end);
        }

        // --------------------------------------------------------
        // Fonts
        // --------------------------------------------------------

        if (fontWidth > 0.0f) {
            const float fontStartX =
                innerLeft +
                textureWidth +
                shaderWidth - 1.0f; // Overlap by 1 pixel

            int16_t start[2] = {
                static_cast<int16_t>(fontStartX),
                static_cast<int16_t>(barY)};

            int16_t end[2] = {
                static_cast<int16_t>(fontStartX + fontWidth),
                static_cast<int16_t>(barY)};

            InnerFontsLine.ShapeStart.SetCoordinate(start);
            InnerFontsLine.ShapeEnd.SetCoordinate(end);
        }

        // --------------------------------------------------------
        // Render order
        //
        // Inner bars first
        // Mask over them
        // Outline on top
        // --------------------------------------------------------

        if (textureWidth > 0.0f)
            InnerTexturesLine.Render();

        if (shaderWidth > 0.0f)
            InnerShadersLine.Render();

        if (fontWidth > 0.0f)
            InnerFontsLine.Render();

        RectMask.Render();
        Outline.Render();

        PMMA::Core::MasterDisplayInstance->Refresh();
    }
}