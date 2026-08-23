
#include "Internal/SplashScreen.hpp"
#include "PMMA_Core.hpp"

void PMMA::Internal::SplashScreen::Play() {
    // ------------------------------------------------------------
    // Progress bar dimensions
    // ------------------------------------------------------------

    uint16_t display_size[2];
    PMMA::Core::MasterDisplayInstance->GetSize(display_size);

    // uint16_t innerHeight = barHeight - ((borderWidth + gap) * 2);

    uint16_t maxProgressBarWidth = static_cast<uint16_t>(display_size[0] * 0.8f);
    uint16_t borderWidth = 3;
    uint16_t gap = 1;
    uint16_t barHeight = std::clamp(static_cast<int>(25 * (display_size[1] / 700.0f)), 3 + (borderWidth + gap) * 2, 25);

    // 1. Calculate side distance (startX is the start of the inner bar)
    float startX = (display_size[0] - maxProgressBarWidth) / 2.0f;
    uint16_t maskWidth = maxProgressBarWidth + (borderWidth * 2);
    uint16_t maskHeight = barHeight + (borderWidth * 2);

    // Total horizontal padding from the edge of the screen to the mask edge
    float sideDistance = (display_size[0] - maskWidth) / 2.0f;

    // 2. Set barY so the bottom mask edge sits exactly 'sideDistance' away from the screen bottom
    float barY = display_size[1] - sideDistance - (maskHeight / 2.0f);

    // ------------------------------------------------------------
    // InnerBar: INNER
    //
    // Square corners.
    // It extends underneath the mask.
    // ------------------------------------------------------------

    PMMA::Rendering::TwoD::Shapes::Rectangle InnerBar;

    InnerBar.Color->SetColorName(
        PMMA::Constants::Colors::BLACK);

    PMMA::Rendering::TwoD::Shapes::Rectangle RectMask;

    RectMask.ShapeCenter->SetX(display_size[0] / 2.0f);
    RectMask.ShapeCenter->SetY(barY);

    RectMask.Color->SetColorName(PMMA::Constants::Colors::WHITE);

    RectMask.ShapeSize->SetSize(
        new uint16_t[2]{
            maskWidth,
            maskHeight});

    RectMask.SetCornerRadius(9999);
    RectMask.SetWidth(8);

    // ------------------------------------------------------------
    // Outline: OUTER
    // ------------------------------------------------------------

    PMMA::Rendering::TwoD::Shapes::Rectangle Outline;

    Outline.ShapeCenter->CenterHorizontal();
    Outline.ShapeCenter->SetY(barY);

    Outline.Color->SetColorName(
        PMMA::Constants::Colors::BLACK);

    Outline.ShapeSize->SetSize(
        new uint16_t[2]{
            maxProgressBarWidth,
            barHeight});

    Outline.SetWidth(borderWidth);
    Outline.SetCornerRadius(12);

    // Deliberately NO SetCornerRadius().
    // This is a square rectangle.

    float progress = 0.0f;

    // ------------------------------------------------------------
    // Main loop
    // ------------------------------------------------------------

    while (PMMA::General::IsApplicationRunning()) {
        PMMA::Core::MasterDisplayInstance->Clear();

        progress += PMMA::Core::MasterDisplayInstance->GetFrameTime() * 0.1f;

        if (progress > 1.0f)
            progress = 0.0f;

        // --------------------------------------------------------
        // Inner progress dimensions
        // --------------------------------------------------------

        uint16_t innerHeight =
            barHeight - ((borderWidth + gap) * 2);

        uint16_t innerMaxWidth =
            maxProgressBarWidth -
            ((borderWidth + gap) * 2);

        uint16_t currentWidth =
            static_cast<uint16_t>(
                innerMaxWidth * progress);

        // --------------------------------------------------------
        // Position the inner rectangle
        // --------------------------------------------------------

        InnerBar.ShapeSize->SetSize(
            new uint16_t[2]{
                currentWidth,
                innerHeight});

        InnerBar.ShapeCenter->SetY(barY);

        InnerBar.ShapeCenter->SetX(
            startX +
            borderWidth +
            gap +
            (currentWidth / 2.0f));

        // --------------------------------------------------------
        // Render order:
        //
        // INNER → MASK → OUTER
        // --------------------------------------------------------

        InnerBar.Render();
        RectMask.Render();
        Outline.Render();

        PMMA::Core::MasterDisplayInstance->Refresh({.LimitRefreshRate = false});
    }
}