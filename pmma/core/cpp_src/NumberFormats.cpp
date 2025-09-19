#include "PMMA_Core.hpp"

CPP_ColorFormat::CPP_ColorFormat() {
    generator.seed(GetRandomSeed());
    Logger = new CPP_Logger();
}

CPP_DisplayCoordinateFormat::CPP_DisplayCoordinateFormat() {
    generator.seed(GetRandomSeed());
    Logger = new CPP_Logger();
}

void CPP_DisplayCoordinateFormat::Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
    X_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
    Y_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 1);

    X_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);
    Y_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 1, new_octaves, new_frequency, new_amplitude);

    generator.seed(new_seed);
    x_distribution = std::uniform_int_distribution<int>(0, PMMA_Core::DisplayInstance->GetWidth());
    y_distribution = std::uniform_int_distribution<int>(0, PMMA_Core::DisplayInstance->GetHeight());

    seed = new_seed;
    octaves = new_octaves;
    frequency = new_frequency;
    amplitude = new_amplitude;
    Configured = true;
}

void CPP_DisplayCoordinateFormat::GenerateFromRandom() {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    if (PMMA_Core::DisplayInstance->DisplaySizeChanged) {
        x_distribution = std::uniform_int_distribution<int>(0, PMMA_Core::DisplayInstance->GetWidth());
        y_distribution = std::uniform_int_distribution<int>(0, PMMA_Core::DisplayInstance->GetHeight());
    }

    float new_coord[2];
    new_coord[0] = static_cast<float>(x_distribution(generator));
    new_coord[1] = static_cast<float>(y_distribution(generator));

    Set(new_coord);
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

    float new_coord[2];

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_coord[0] = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_coord[1] = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
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

    float new_coord[2];

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
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

    float new_coord[2];

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
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

    float new_coord[2];

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_coord[0] = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_coord[1] = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
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

    float new_coord[2];

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
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

    float new_coord[2];

    float x_range[2] = {0, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = CPP_AdvancedMathematics::Ranger(x_value, noise_range, x_range);

    float y_range[2] = {1, (float)PMMA_Core::DisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = CPP_AdvancedMathematics::Ranger(y_value, noise_range, y_range);

    Set(new_coord);
}