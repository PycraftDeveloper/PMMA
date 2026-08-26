#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include "Noise/FractalBrownianMotion.hpp"
#include "Noise/PerlinNoise.hpp"

#include "Types/Base.hpp"
#include "Types/Proportion.hpp"
#include "Types/Texture.hpp"

#include "Maths.hpp"
#include "Random.hpp"

namespace PMMA::Types::TwoD {

class EXPORT Size {
public:
    PMMA::Types::Texture *Texture;
    PMMA::Types::Proportion HorizontalScale;
    PMMA::Types::Proportion VerticalScale;

private:
    PMMA::Noise::PerlinNoise *X_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *Y_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *X_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *Y_FractalBrownianMotionGenerator = nullptr;

    PMMA::FastRandom *RandomSizeGenerator = nullptr;

    uint16_t size[2] = {0, 0}; // Default display coordinate is (0, 0)
    uint16_t scaled_size[2] = {0, 0};
    uint16_t DisplaySize[2];

    uint32_t seed;
    uint32_t octaves;
    float frequency;
    float amplitude;

    float offset_range[2] = {0.f, 1.f};
    float x_offset = PMMA::Maths::RandomFloat(offset_range);
    float y_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};

    uint16_t Radius = 0;

    bool X_IsSet = false;
    bool Y_IsSet = false;
    bool Changed = true;
    bool ScaledSizeSet = false;
    bool Configured = false;

public:
    Size();

    ~Size() {
        if (Configured) {
            delete X_PerlinNoiseGenerator;
            delete Y_PerlinNoiseGenerator;

            delete X_FractalBrownianMotionGenerator;
            delete Y_FractalBrownianMotionGenerator;

            X_PerlinNoiseGenerator = nullptr;
            Y_PerlinNoiseGenerator = nullptr;

            X_FractalBrownianMotionGenerator = nullptr;
            Y_FractalBrownianMotionGenerator = nullptr;

            delete RandomSizeGenerator;
            RandomSizeGenerator = nullptr;
        }
    }

    void Configure(PMMA::Types::Configure_Kwargs kwargs = {});

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline bool GetScaledChangedToggle() {
        bool ScaleChanged = HorizontalScale.GetChangedToggle() || VerticalScale.GetChangedToggle();
        if (ScaleChanged) {
            ScaledSizeSet = false;
        }
        bool OldChanged = Changed || ScaleChanged;
        Changed = false;
        return OldChanged;
    }

    inline bool GetSizeSet() {
        return X_IsSet && Y_IsSet;
    }

    inline bool GetWidthSet() {
        return X_IsSet;
    }

    inline bool GetHeightSet() {
        return Y_IsSet;
    }

    uint32_t GetSeed();
    uint32_t GetOctaves();
    float GetFrequency();
    float GetAmplitude();

    void GenerateFromRandom();

    void GenerateFrom1DPerlinNoise(float value);
    void GenerateFrom2DPerlinNoise(float value_one, float value_two);
    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three);

    void GenerateFrom1DFractalBrownianMotion(float value);
    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two);
    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three);

    inline void SetSize(uint16_t *in_size) {
        if (in_size[0] != size[0] || in_size[1] != size[1]) {
            Changed = true;
            ScaledSizeSet = false;
            size[0] = in_size[0];
            size[1] = in_size[1];

            Radius = static_cast<uint16_t>(PMMA::Maths::PythagoreanDistance(size[0], size[1]));
        }

        X_IsSet = true;
        Y_IsSet = true;
    }

    inline void SetWidth(uint16_t in_size) {
        if (in_size != size[0]) {
            Changed = true;
            ScaledSizeSet = false;
            size[0] = in_size;

            Radius = static_cast<uint16_t>(PMMA::Maths::PythagoreanDistance(size[0], size[1]));
        }

        X_IsSet = true;
    }

    inline void SetHeight(uint16_t in_size) {
        if (in_size != size[1]) {
            Changed = true;
            ScaledSizeSet = false;
            size[1] = in_size;

            Radius = static_cast<uint16_t>(PMMA::Maths::PythagoreanDistance(size[0], size[1]));
        }

        Y_IsSet = true;
    }

    void SetSizeToTextureSize();
    void SetWidthToTextureWidth();
    void SetWidthToTextureHeight();

    void GetSize(uint16_t *out);
    uint16_t GetWidth();
    uint16_t GetHeight();

    void GetScaledSize(uint16_t *out);
    uint16_t GetScaledWidth();
    uint16_t GetScaledHeight();

    inline uint16_t GetRadius() {
        return Radius;
    }

    inline void SetRadius(uint16_t in_radius) {
        in_radius *= 2;
        uint16_t new_size[2] = {in_radius, in_radius};
        SetSize(new_size);
    }
};
}; // namespace PMMA::Types::TwoD