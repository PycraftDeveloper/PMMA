#include "Internal/Core/PMMA_Core.hpp"

#include "Internal/LoggingManager.hpp"

#include "Types/Proportion.hpp"

inline void ProportionConfiguredCheck(bool Configured) {
    if (!Configured) {
        PMMA::Core::LoggingManagerInstance->InternalLogError(
            13,
            "You need to configure this component before calling this.");
        throw std::runtime_error("You need to configure this component first!");
    }
}

inline void ProportionSetCheck(bool IsSet) {
    if (!IsSet) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            30,
            "You have not set a proportion - please set a proportion \
before attempting to get it.");

        throw std::runtime_error("Proportion not set!");
    }
}

uint32_t PMMA::Types::Proportion::GetSeed() {
    ProportionConfiguredCheck(Configured);
    return seed;
}

uint32_t PMMA::Types::Proportion::GetOctaves() {
    ProportionConfiguredCheck(Configured);
    return octaves;
}

float PMMA::Types::Proportion::GetFrequency() {
    ProportionConfiguredCheck(Configured);
    return frequency;
}

float PMMA::Types::Proportion::GetAmplitude() {
    ProportionConfiguredCheck(Configured);
    return amplitude;
}

void PMMA::Types::Proportion::GenerateFrom1DPerlinNoise(float value) {
    ProportionConfiguredCheck(Configured);

    InternalProportion = PerlinNoiseGenerator->Noise1D(value);
    float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

    if (converted_in_proportion != InternalProportion) {
        Changed = true;
        InternalProportion = converted_in_proportion;
    }

    IsSet = true;
}

void PMMA::Types::Proportion::GenerateFrom2DPerlinNoise(float value_one, float value_two) {
    ProportionConfiguredCheck(Configured);

    InternalProportion = PerlinNoiseGenerator->Noise2D(value_one, value_two);
    float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

    if (converted_in_proportion != InternalProportion) {
        Changed = true;
        InternalProportion = converted_in_proportion;
    }

    IsSet = true;
}

void PMMA::Types::Proportion::GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) {
    ProportionConfiguredCheck(Configured);

    InternalProportion = PerlinNoiseGenerator->Noise3D(value_one, value_two, value_three);
    float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

    if (converted_in_proportion != InternalProportion) {
        Changed = true;
        InternalProportion = converted_in_proportion;
    }

    IsSet = true;
}

void PMMA::Types::Proportion::GenerateFrom1DFractalBrownianMotion(float value) {
    ProportionConfiguredCheck(Configured);

    InternalProportion = FractalBrownianMotionGenerator->Noise1D(value);
    float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

    if (converted_in_proportion != InternalProportion) {
        Changed = true;
        InternalProportion = converted_in_proportion;
    }

    IsSet = true;
}

void PMMA::Types::Proportion::GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) {
    ProportionConfiguredCheck(Configured);

    InternalProportion = FractalBrownianMotionGenerator->Noise2D(value_one, value_two);
    float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

    if (converted_in_proportion != InternalProportion) {
        Changed = true;
        InternalProportion = converted_in_proportion;
    }

    IsSet = true;
}

void PMMA::Types::Proportion::GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) {
    ProportionConfiguredCheck(Configured);

    InternalProportion = FractalBrownianMotionGenerator->Noise3D(value_one, value_two, value_three);
    float converted_in_proportion = PMMA::Maths::Ranger(InternalProportion, noise_range, proportion_range);

    if (converted_in_proportion != InternalProportion) {
        Changed = true;
        InternalProportion = converted_in_proportion;
    }

    IsSet = true;
}

float PMMA::Types::Proportion::GetPercentage() {
    ProportionSetCheck(IsSet);
    return InternalProportion * 100;
}

float PMMA::Types::Proportion::GetDecimal() {
    ProportionSetCheck(IsSet);
    return InternalProportion;
}