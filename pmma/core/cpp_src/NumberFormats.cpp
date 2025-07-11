#include "PMMA_Core.hpp"

void CPP_DisplayCoordinateFormat::GenerateRandomDisplayCoordinate() {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    DisplayCoordinate.x = CPP_AdvancedMathematics::RandomFloat(x_range);

    float y_range[2] = {0, (float)PMMA::DisplayInstance->GetHeight()};
    DisplayCoordinate.y = CPP_AdvancedMathematics::RandomFloat(y_range);
    Set = true;
    Changed = true;
}

void CPP_DisplayCoordinateFormat::GeneratePerlinDisplayCoordinate(float value) {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glm::vec2 new_coordinate;
    float in_range[2] = {-1, 1};

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    float x_value = PerlinNoiseGenerator->Noise2D(0, value + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, in_range, x_range);

    float y_range[2] = {1, (float)PMMA::DisplayInstance->GetWidth()};
    float y_value = PerlinNoiseGenerator->Noise2D(0, value + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, in_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    Set = true;
}

void CPP_DisplayCoordinateFormat::GenerateFractalBrownianMotionDisplayCoordinate(float value) {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glm::vec2 new_coordinate;
    float in_range[2] = {-1, 1};

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    float x_value = FractalBrownianMotionGenerator->Noise2D(0, value + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, in_range, x_range);

    float y_range[2] = {1, (float)PMMA::DisplayInstance->GetWidth()};
    float y_value = FractalBrownianMotionGenerator->Noise2D(0, value + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, in_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    Set = true;
}