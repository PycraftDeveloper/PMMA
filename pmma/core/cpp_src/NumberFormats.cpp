#include "PMMA_Core.hpp"

void CPP_DisplayCoordinateFormat::GenerateFromRandom() {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    DisplayCoordinate.x = CPP_AdvancedMathematics::RandomFloat(x_range);

    float y_range[2] = {0, (float)PMMA::DisplayInstance->GetHeight()};
    DisplayCoordinate.y = CPP_AdvancedMathematics::RandomFloat(y_range);
    IsSet = true;
    Changed = true;
}

void CPP_DisplayCoordinateFormat::GenerateFromPerlinNoise(float value) {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFromFractalBrownianMotion(float value) {
    if (PMMA::DisplayInstance == nullptr) {
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}