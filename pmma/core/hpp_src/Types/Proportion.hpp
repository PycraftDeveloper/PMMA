#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <optional>

#include "Noise/FractalBrownianMotion.hpp"
#include "Noise/PerlinNoise.hpp"

#include "Types/Base.hpp"

#include "Maths.hpp"
#include "Random.hpp"

namespace PMMA::Types {
class EXPORT Proportion {
private:
    PMMA::Noise::PerlinNoise *PerlinNoiseGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *FractalBrownianMotionGenerator = nullptr;

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float InternalProportion = 0.f; // Default proportion is 0 (0%)

    const float noise_range[2] = {-1.f, 1.f};
    const float proportion_range[2] = {0.f, 1.f};

    bool Configured = false;
    bool IsSet = false;
    bool Changed = true;

public:
    ~Proportion() {
        if (Configured) {
            delete PerlinNoiseGenerator;
            delete FractalBrownianMotionGenerator;

            PerlinNoiseGenerator = nullptr;
            FractalBrownianMotionGenerator = nullptr;
        }
    }

    inline void Configure(PMMA::Types::Configure_Kwargs kwargs = {}) {
        uint32_t new_seed;

        if (!kwargs.seed.has_value()) {
            PMMA::FastRandom TempRandomGenerator;
            new_seed = TempRandomGenerator.Next();
        } else {
            new_seed = kwargs.seed.value();
        }

        PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
        FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

        srand(new_seed);

        seed = new_seed;
        octaves = kwargs.octaves;
        frequency = kwargs.frequency;
        amplitude = kwargs.amplitude;
        Configured = true;
    }

    uint32_t GetSeed();
    uint32_t GetOctaves();
    float GetFrequency();
    float GetAmplitude();

    inline void GenerateFromRandom() {
        float converted_in_proportion = PMMA::Maths::RandomFloat(proportion_range);

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline bool GetSet() {
        return IsSet;
    }

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline void SetPercentage(float in_proportion) {
        float converted_in_proportion = in_proportion / 100;

        if (converted_in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = converted_in_proportion;
        }

        IsSet = true;
    }

    inline void SetDecimal(float in_proportion) {
        if (in_proportion != InternalProportion) {
            Changed = true;
            InternalProportion = in_proportion;
        }

        IsSet = true;
    }

    inline float GetPercentage();
    inline float GetDecimal();
};
} // namespace PMMA::Types