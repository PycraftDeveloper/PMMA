#include "PMMA_Core.hpp"

void CPP_DisplayCoordinateFormat::GenerateRandomDisplayCoordinate() {
    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    DisplayCoordinate.x = CPP_AdvancedMathematics::RandomFloat(x_range);

    float y_range[2] = {0, (float)PMMA::DisplayInstance->GetHeight()};
    DisplayCoordinate.y = CPP_AdvancedMathematics::RandomFloat(y_range);
    DisplayCoordinateSet = true;
}

void CPP_DisplayCoordinateFormat::GeneratePerlinDisplayCoordinate(float value) {
    float in_range[2] = {-1, 1};

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    float x_value = PerlinNoiseGenerator->Noise2D(0, value + x_offset);
    DisplayCoordinate.x = CPP_AdvancedMathematics::Ranger(x_value, in_range, x_range);

    float y_range[2] = {1, (float)PMMA::DisplayInstance->GetWidth()};
    float y_value = PerlinNoiseGenerator->Noise2D(0, value + y_offset);
    DisplayCoordinate.x = CPP_AdvancedMathematics::Ranger(y_value, in_range, y_range);

    DisplayCoordinateSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFractalBrownianMotionDisplayCoordinate(float value) {
    float in_range[2] = {-1, 1};

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    float x_value = FractalBrownianMotionGenerator->Noise2D(0, value + x_offset);
    DisplayCoordinate.x = CPP_AdvancedMathematics::Ranger(x_value, in_range, x_range);

    float y_range[2] = {1, (float)PMMA::DisplayInstance->GetWidth()};
    float y_value = FractalBrownianMotionGenerator->Noise2D(0, value + y_offset);
    DisplayCoordinate.x = CPP_AdvancedMathematics::Ranger(y_value, in_range, y_range);

    DisplayCoordinateSet = true;
}