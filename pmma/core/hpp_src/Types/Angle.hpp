#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <optional>

#include "Noise/FractalBrownianMotion.hpp"
#include "Noise/PerlinNoise.hpp"

#include "Types/Base.hpp"

#include "Maths.hpp"
#include "Random.hpp"

namespace PMMA::Types {
class EXPORT Angle {
private:
    PMMA::Noise::PerlinNoise *PerlinNoiseGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *FractalBrownianMotionGenerator = nullptr;

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float InternalAngle = 0.f; // Default angle is 0 radians
    const float RADIANS_TO_DEGREES = 180.f / 3.14159265358979323846f;
    const float DEGREES_TO_RADIANS = 3.14159265358979323846f / 180.f;

    const float noise_range[2] = {-1.f, 1.f};
    const float angle_range[2] = {0.f, 3.14159265358979323846f * 2};

    bool Configured = false;
    bool Changed = true;
    bool IsSet = false;

public:
    ~Angle() {
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
        float converted_in_angle = PMMA::Maths::RandomFloat(angle_range);

        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
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

    inline void SetRadians(float in_angle) {
        if (in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = in_angle;
        }

        IsSet = true;
    }

    inline void SetDegrees(float in_angle) {
        float converted_in_angle = in_angle * DEGREES_TO_RADIANS;
        if (converted_in_angle != InternalAngle) {
            Changed = true;
            InternalAngle = converted_in_angle;
        }

        IsSet = true;
    }

    float GetRadians();
    float GetDegrees();
};
} // namespace PMMA::Types