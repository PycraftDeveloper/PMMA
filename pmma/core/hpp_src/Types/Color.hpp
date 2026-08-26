#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include "Noise/FractalBrownianMotion.hpp"
#include "Noise/PerlinNoise.hpp"

#include "Types/Base.hpp"

#include "Maths.hpp"
#include "Random.hpp"

namespace PMMA::Types {
class EXPORT Color {
private:
    PMMA::Noise::PerlinNoise *R_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *G_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *B_PerlinNoiseGenerator = nullptr;
    PMMA::Noise::PerlinNoise *A_PerlinNoiseGenerator = nullptr;

    PMMA::Noise::FractalBrownianMotion *R_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *G_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *B_FractalBrownianMotionGenerator = nullptr;
    PMMA::Noise::FractalBrownianMotion *A_FractalBrownianMotionGenerator = nullptr;

    PMMA::FastRandom *RandomColorGenerator = nullptr;

    uint8_t InternalColor[4] = {0, 0, 0, 255}; // Default is black with full opacity

    uint32_t seed;
    uint32_t octaves;

    float frequency;
    float amplitude;
    float half_color_max = 255.f / 2.f;

    float offset_range[2] = {0.f, 1.f};
    float r_offset = PMMA::Maths::RandomFloat(offset_range);
    float g_offset = PMMA::Maths::RandomFloat(offset_range);
    float b_offset = PMMA::Maths::RandomFloat(offset_range);
    float a_offset = PMMA::Maths::RandomFloat(offset_range);

    const float noise_range[2] = {-1.f, 1.f};
    const float color_range[2] = {0, 255};

    bool Configured = false;
    bool IsSet = false;
    bool Changed = true;
    bool InternalChanged = true;

public:
    bool LinkedToDisplayBackground = false;

    Color();

    ~Color() {
        if (Configured) {
            delete R_PerlinNoiseGenerator;
            delete G_PerlinNoiseGenerator;
            delete B_PerlinNoiseGenerator;
            delete A_PerlinNoiseGenerator;

            delete R_FractalBrownianMotionGenerator;
            delete G_FractalBrownianMotionGenerator;
            delete B_FractalBrownianMotionGenerator;
            delete A_FractalBrownianMotionGenerator;

            R_PerlinNoiseGenerator = nullptr;
            G_PerlinNoiseGenerator = nullptr;
            B_PerlinNoiseGenerator = nullptr;
            A_PerlinNoiseGenerator = nullptr;

            R_FractalBrownianMotionGenerator = nullptr;
            G_FractalBrownianMotionGenerator = nullptr;
            B_FractalBrownianMotionGenerator = nullptr;
            A_FractalBrownianMotionGenerator = nullptr;

            delete RandomColorGenerator;
            RandomColorGenerator = nullptr;
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

        R_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed);
        G_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 1);
        B_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 2);
        A_PerlinNoiseGenerator = new PMMA::Noise::PerlinNoise(new_seed + 3);

        R_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
        G_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 1, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
        B_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 2, kwargs.octaves, kwargs.frequency, kwargs.amplitude);
        A_FractalBrownianMotionGenerator = new PMMA::Noise::FractalBrownianMotion(new_seed + 3, kwargs.octaves, kwargs.frequency, kwargs.amplitude);

        RandomColorGenerator = new PMMA::FastRandom();
        RandomColorGenerator->SetSeed(new_seed);

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

    inline void GenerateFromRandom(bool GenerateAlpha = true) {
        uint8_t in_color[4];
        uint32_t packedColor = RandomColorGenerator->Next();

        in_color[0] = static_cast<uint8_t>((packedColor >> 24) & 0xFF); // R
        in_color[1] = static_cast<uint8_t>((packedColor >> 16) & 0xFF); // G
        in_color[2] = static_cast<uint8_t>((packedColor >> 8) & 0xFF);  // B

        if (GenerateAlpha) {
            in_color[3] = static_cast<uint8_t>(packedColor & 0xFF);
        } else {
            in_color[3] = 255;
        }

        Set_RGBA(in_color);
    }

    void GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha = true);

    void GenerateFrom2DPerlinNoise(float value_one, float value_two, bool GenerateAlpha = true);

    void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three, bool GenerateAlpha = true);

    void GenerateFrom1DFractalBrownianMotion(float value, bool GenerateAlpha = true);

    void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two, bool GenerateAlpha = true);

    void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three, bool GenerateAlpha = true);

    inline bool GetSet() {
        return IsSet;
    }

    inline bool GetChangedToggle() {
        bool OldChanged = Changed;
        Changed = false;
        return OldChanged;
    }

    inline bool GetInternalChangedToggle() {
        bool OldChanged = InternalChanged;
        InternalChanged = false;
        return OldChanged;
    }

    void SetColorName(std::string color_name);
    void SetColorName(std::string_view color_name);

    void Set_RGBA(uint8_t *in_color);
    void Set_RGB(uint8_t *in_color);

    void Set_HEX(std::string input_color);
    void Set_HEXA(std::string input_color);

    void Get_RGBA(uint8_t *out_color);
    void Get_RGB(uint8_t *out_color);

    std::string Get_HEXA();
    std::string Get_HEX();

    bool IsTransparent();
    bool IsOpaque();
    bool IsClear();
};
} // namespace PMMA::Types