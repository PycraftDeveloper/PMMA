#include "PMMA_Core.hpp"

CPP_Color::CPP_Color() {
    RandomColorGenerator = new CPP_FastRandom();
}

void CPP_Color::Set_ColorName(std::string color_name) {
    if (CPP_Constants::Colors::ColorMap.find(color_name) == CPP_Constants::Colors::ColorMap.end()) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            60,
            "The color name '" + color_name + "' is not recognized."
        );
        throw std::runtime_error("Unrecognized color name!");
    }

    auto& rgb = CPP_Constants::Colors::ColorMap.at(color_name);
    uint8_t in_color[4] = {rgb[0], rgb[1], rgb[2], 255};
    Set_RGBA(in_color);
}

CPP_DisplayCoordinate::CPP_DisplayCoordinate() {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    RandomCoordGenerator = new CPP_FastRandom();
    Logger = new CPP_Logger();

    PMMA_Core::DisplayInstance->GetSize(DisplaySize);
}

void CPP_DisplayCoordinate::Configure(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
    X_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed);
    Y_PerlinNoiseGenerator = new CPP_PerlinNoise(new_seed + 1);

    X_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed, new_octaves, new_frequency, new_amplitude);
    Y_FractalBrownianMotionGenerator = new CPP_FractalBrownianMotion(new_seed + 1, new_octaves, new_frequency, new_amplitude);

    RandomCoordGenerator->SetSeed(new_seed);

    seed = new_seed;
    octaves = new_octaves;
    frequency = new_frequency;
    amplitude = new_amplitude;
    Configured = true;
}

void CPP_DisplayCoordinate::SetCentered() {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    if (PMMA_Core::DisplayInstance->DisplaySizeChanged) {
        PMMA_Core::DisplayInstance->GetSize(DisplaySize);
    }

    unsigned int new_coord[2];
    PMMA_Core::DisplayInstance->GetCenterPosition(new_coord);

    float coord_float[2];
    coord_float[0] = static_cast<float>(new_coord[0]);
    coord_float[1] = static_cast<float>(new_coord[1]);

    Set(coord_float);
}

void CPP_DisplayCoordinate::GenerateFromRandom() {
    if (PMMA_Core::DisplayInstance == nullptr) {
        PMMA_Core::LoggingManagerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    if (PMMA_Core::DisplayInstance->DisplaySizeChanged) {
        PMMA_Core::DisplayInstance->GetSize(DisplaySize);
    }

    float new_coord[2];
    new_coord[0] = RandomCoordGenerator->Next(DisplaySize[0]);
    new_coord[1] = RandomCoordGenerator->Next(DisplaySize[1]);

    Set(new_coord);
}

void CPP_DisplayCoordinate::GenerateFrom1DPerlinNoise(float value) {
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

void CPP_DisplayCoordinate::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
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

void CPP_DisplayCoordinate::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
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

void CPP_DisplayCoordinate::GenerateFrom1DFractalBrownianMotion(float value) {
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

void CPP_DisplayCoordinate::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
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

void CPP_DisplayCoordinate::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
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