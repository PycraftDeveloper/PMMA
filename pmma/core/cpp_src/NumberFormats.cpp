#include "PMMA_Core.hpp"

void CPP_DisplayCoordinateFormat::GenerateFromRandom() {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    DisplayCoordinate.x = CPP_AdvancedMathematics::RandomFloat(x_range);

    float y_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetHeight()};
    DisplayCoordinate.y = CPP_AdvancedMathematics::RandomFloat(y_range);
    IsSet = true;
    Changed = true;
}

void CPP_DisplayCoordinateFormat::GenerateFrom1DPerlinNoise(float value) {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this."
        );
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this."
        );
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this."
        );
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFrom1DFractalBrownianMotion(float value) {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this."
        );
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this."
        );
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}

void CPP_DisplayCoordinateFormat::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }
    if (!Configured) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this."
        );
        throw runtime_error("You need to configure this component first!");
    }

    glm::vec2 new_coordinate;

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coordinate.x = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coordinate.y = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    if (new_coordinate != DisplayCoordinate) {
        DisplayCoordinate = new_coordinate;
        Changed = true;
    }

    IsSet = true;
}