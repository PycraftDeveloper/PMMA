#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/Internal.hpp"
#include "Internal/LoggingManager.hpp"

#include "Types/Coordinate.hpp"

#include "Display.hpp"

inline void CoordinateConfiguredCheck(bool Configured) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
}

PMMA::Types::TwoD::Coordinate::Coordinate() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    RandomCoordGenerator = PMMA::Core::RandomGenerator;

    PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
}

void PMMA::Types::TwoD::Coordinate::GetCoordinate(int16_t *out) {
    if (!GetCoordinateSet()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    out[0] = coordinate[0];
    out[1] = coordinate[1];
}

int16_t PMMA::Types::TwoD::Coordinate::GetX() {
    if (!Get_X_Set()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    return coordinate[0];
}

int16_t PMMA::Types::TwoD::Coordinate::GetY() {
    if (!Get_Y_Set()) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a display coordinate - please set a \
display coordinate before attempting to get it.");
        throw std::runtime_error("Display coordinate not set!");
    }

    return coordinate[1];
}

uint32_t PMMA::Types::TwoD::Coordinate::GetSeed() {
    CoordinateConfiguredCheck(Configured);
    return seed;
}

uint32_t PMMA::Types::TwoD::Coordinate::GetOctaves() {
    CoordinateConfiguredCheck(Configured);
    return octaves;
}

float PMMA::Types::TwoD::Coordinate::GetFrequency() {
    CoordinateConfiguredCheck(Configured);
    return frequency;
}

float PMMA::Types::TwoD::Coordinate::GetAmplitude() {
    CoordinateConfiguredCheck(Configured);
    return amplitude;
}

void PMMA::Types::TwoD::Coordinate::Configure(PMMA::Types::Configure_Kwargs kwargs) {
    uint32_t new_seed;

    if (!kwargs.seed.has_value()) {
        PMMA::FastRandom TempRandomGenerator;
        new_seed = TempRandomGenerator.Next();
    } else {
        new_seed = kwargs.seed.value();
    }

    X_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
    Y_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 1);

    X_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
    Y_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 1, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

    RandomCoordGenerator = new PMMA::FastRandom();
    RandomCoordGenerator->SetSeed(new_seed);

    seed = new_seed;
    octaves = kwargs.octaves;
    frequency = kwargs.frequency;
    amplitude = kwargs.amplitude;
    Configured = true;
}

void PMMA::Types::TwoD::Coordinate::Center() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    uint16_t new_coord[2];
    PMMA::Core::ActiveDisplayInstance->GetCenterPosition(new_coord);

    int16_t coord_float[2];
    coord_float[0] = new_coord[0];
    coord_float[1] = new_coord[1];

    SetCoordinate(coord_float);
}

void PMMA::Types::TwoD::Coordinate::CenterHorizontal() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    int16_t center = PMMA::Core::ActiveDisplayInstance->GetHorizontalCenterPosition();

    SetX(center);
}

void PMMA::Types::TwoD::Coordinate::CenterVertical() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    int16_t center = PMMA::Core::ActiveDisplayInstance->GetVerticalCenterPosition();

    SetY(center);
}

void PMMA::Types::TwoD::Coordinate::GenerateFromRandom() {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);

    if (PMMA::Core::ActiveDisplayInstance->DisplaySizeChanged) {
        PMMA::Core::ActiveDisplayInstance->GetSize(DisplaySize);
    }

    int16_t new_coord[2];
    new_coord[0] = RandomCoordGenerator->Next(DisplaySize[0]);
    new_coord[1] = RandomCoordGenerator->Next(DisplaySize[1]);

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom1DPerlinNoise(float value) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    CoordinateConfiguredCheck(Configured);

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise1D(value + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise1D(value + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    CoordinateConfiguredCheck(Configured);

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    CoordinateConfiguredCheck(Configured);

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_PerlinNoiseGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_PerlinNoiseGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom1DFractalBrownianMotion(float value) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    CoordinateConfiguredCheck(Configured);

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise1D(value + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise1D(value + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    CoordinateConfiguredCheck(Configured);

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise2D(value_one + x_offset, value_two + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise2D(value_one + y_offset, value_two + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

    SetCoordinate(new_coord);
}

void PMMA::Types::TwoD::Coordinate::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    PMMA::Internal::DisplayExistsCheck(PMMA::Core::ActiveDisplayInstance);
    CoordinateConfiguredCheck(Configured);

    int16_t new_coord[2];

    float x_range[2] = {0, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float x_value = X_FractalBrownianMotionGenerator->Noise3D(value_one + x_offset, value_two + x_offset, value_three + x_offset);
    new_coord[0] = static_cast<int16_t>(PMMA::Maths::Ranger(x_value, noise_range, x_range));

    float y_range[2] = {1, (float)PMMA::Core::ActiveDisplayInstance->GetWidth()};
    float y_value = Y_FractalBrownianMotionGenerator->Noise3D(value_one + y_offset, value_two + y_offset, value_three + y_offset);
    new_coord[1] = static_cast<int16_t>(PMMA::Maths::Ranger(y_value, noise_range, y_range));

    SetCoordinate(new_coord);
}