#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/LoggingManager.hpp"

#include "Types/Angle.hpp"

inline void AngleConfiguredCheck(bool Configured) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
}

inline void AngleSetCheck(bool IsSet) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set an angle - please set an angle \
before attempting to get it.");

        throw std::runtime_error("Angle not set!");
    }
}

uint32_t PMMA::Types::Angle::GetSeed() {
    AngleConfiguredCheck(Configured);
    return seed;
}

uint32_t PMMA::Types::Angle::GetOctaves() {
    AngleConfiguredCheck(Configured);
    return octaves;
}

float PMMA::Types::Angle::GetFrequency() {
    AngleConfiguredCheck(Configured);
    return frequency;
}

float PMMA::Types::Angle::GetAmplitude() {
    AngleConfiguredCheck(Configured);
    return amplitude;
}

void PMMA::Types::Angle::GenerateFrom1DPerlinNoise(float value) {
    AngleConfiguredCheck(Configured);

    InternalAngle = PerlinNoiseGenerator->Noise1D(value);
    float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

    if (converted_in_angle != InternalAngle) {
        Changed = true;
        InternalAngle = converted_in_angle;
    }

    IsSet = true;
}

void PMMA::Types::Angle::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    AngleConfiguredCheck(Configured);

    InternalAngle = PerlinNoiseGenerator->Noise2D(value_one, value_two);
    float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

    if (converted_in_angle != InternalAngle) {
        Changed = true;
        InternalAngle = converted_in_angle;
    }

    IsSet = true;
}

void PMMA::Types::Angle::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    AngleConfiguredCheck(Configured);

    InternalAngle = PerlinNoiseGenerator->Noise3D(value_one, value_two, value_three);
    float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

    if (converted_in_angle != InternalAngle) {
        Changed = true;
        InternalAngle = converted_in_angle;
    }

    IsSet = true;
}

void PMMA::Types::Angle::GenerateFrom1DFractalBrownianMotion(float value) {
    AngleConfiguredCheck(Configured);

    InternalAngle = FractalBrownianMotionGenerator->Noise1D(value);
    float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

    if (converted_in_angle != InternalAngle) {
        Changed = true;
        InternalAngle = converted_in_angle;
    }

    IsSet = true;
}

void PMMA::Types::Angle::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    AngleConfiguredCheck(Configured);

    InternalAngle = FractalBrownianMotionGenerator->Noise2D(value_one, value_two);
    float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

    if (converted_in_angle != InternalAngle) {
        Changed = true;
        InternalAngle = converted_in_angle;
    }

    IsSet = true;
}

void PMMA::Types::Angle::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    AngleConfiguredCheck(Configured);

    InternalAngle = FractalBrownianMotionGenerator->Noise3D(value_one, value_two, value_three);
    float converted_in_angle = PMMA::Maths::Ranger(InternalAngle, noise_range, angle_range);

    if (converted_in_angle != InternalAngle) {
        Changed = true;
        InternalAngle = converted_in_angle;
    }

    IsSet = true;
}

float PMMA::Types::Angle::GetRadians() {
    AngleSetCheck(IsSet);
    return InternalAngle;
}

float PMMA::Types::Angle::GetDegrees() {
    AngleSetCheck(IsSet);
    return InternalAngle * RADIANS_TO_DEGREES;
}