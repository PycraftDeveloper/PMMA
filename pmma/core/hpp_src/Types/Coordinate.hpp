#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include "Noise/FractalBrownianMotion.hpp"
#include "Noise/PerlinNoise.hpp"

#include "Types/Base.hpp"

#include "Maths.hpp"
#include "Random.hpp"

namespace PMMA::Types::TwoD {
class EXPORT Coordinate {
private:
    PMMA::Noise::PerlinNoise *X_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *Y_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *X_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *Y_FractalBrownianMotionGenerator = nullptr;

    PMMA::FastRandom *RandomCoordGenerator = nullptr;

    int16_t coordinate[2] = {0, 0}; // Default display coordinate is (0, 0)
    uint16_t DisplaySize[2];

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float offset_range[2] = {0.f, 1.f};
    float x_offset = PMMA::Maths::RandomFloat(offset_range);
    float y_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};

    bool X_IsSet = false;
    bool Y_IsSet = false;
    bool Changed = true;
    bool Configured = false;

public:
    Coordinate();

    ~Coordinate() {
        if (Configured) {
            delete X_PerlinNoiseGenerator;
            delete Y_PerlinNoiseGenerator;

            delete X_FractalBrownianMotionGenerator;
            delete Y_FractalBrownianMotionGenerator;

            X_PerlinNoiseGenerator = nullptr;
            Y_PerlinNoiseGenerator = nullptr;

            X_FractalBrownianMotionGenerator = nullptr;
            Y_FractalBrownianMotionGenerator = nullptr;

            delete RandomCoordGenerator;
            RandomCoordGenerator = nullptr;
        }
    }

    void Configure(PMMA::Types::Configure_Kwargs kwargs = {});

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline bool GetCoordinateSet() {
        return X_IsSet && Y_IsSet;
    }

    inline bool Get_X_Set() {
        return X_IsSet;
    }

    inline bool Get_Y_Set() {
        return Y_IsSet;
    }

    uint32_t GetSeed();
    uint32_t GetOctaves();
    float GetFrequency();
    float GetAmplitude();

    void Center();
    void CenterHorizontal();
    void CenterVertical();

    void GenerateFromRandom();

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline void SetCoordinate(int16_t *in_coordinate) {
        if (in_coordinate[0] != coordinate[0] || in_coordinate[1] != coordinate[1]) {
            Changed = true;
            coordinate[0] = in_coordinate[0];
            coordinate[1] = in_coordinate[1];
        }

        X_IsSet = true;
        Y_IsSet = true;
    }

    inline void SetX(int16_t in_coordinate) {
        if (in_coordinate != coordinate[0]) {
            Changed = true;
            coordinate[0] = in_coordinate;
        }

        X_IsSet = true;
    }

    inline void SetY(int16_t in_coordinate) {
        if (in_coordinate != coordinate[1]) {
            Changed = true;
            coordinate[1] = in_coordinate;
        }

        Y_IsSet = true;
    }

    void GetCoordinate(int16_t *out);
    int16_t GetX();
    int16_t GetY();
};
} // namespace PMMA::Types::TwoD