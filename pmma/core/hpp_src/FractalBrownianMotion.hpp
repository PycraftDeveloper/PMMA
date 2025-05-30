#pragma once

#include <array>

#include "PerlinNoise.hpp"

using namespace std;

class CPP_FractalBrownianMotion {
    private:
        uint32_t Octaves;
        float Lacunarity;
        float Gain;

        CPP_PerlinNoise* PerlinNoise;

    public:
        CPP_FractalBrownianMotion(const uint32_t seed, uint32_t new_octaves, float new_frequency, float new_amplitude);

        inline float CPP_FractalBrownianMotion1D(const float x) const noexcept {
            float total = 0.0f;
            float frequency = 1.0f;
            float amplitude = 1.0f;
            float max_amplitude = 0.0f;

            for (uint32_t i = 0; i < Octaves; i++) {
                total += PerlinNoise->CPP_Noise1D(x * frequency) * amplitude;
                max_amplitude += amplitude;
                frequency *= Lacunarity;
                amplitude *= Gain;
            }

            return total / max_amplitude;
        }

        inline float CPP_FractalBrownianMotion2D(const float x, const float y) const noexcept {
            float total = 0.0f;
            float frequency = 1.0f;
            float amplitude = 1.0f;
            float max_amplitude = 0.0f;

            for (uint32_t i = 0; i < Octaves; i++) {
                total += PerlinNoise->CPP_Noise2D(x * frequency, y * frequency) * amplitude;
                max_amplitude += amplitude;
                frequency *= Lacunarity;
                amplitude *= Gain;
            }

            return total / max_amplitude;
        }

        inline float CPP_FractalBrownianMotion3D(const float x, const float y, const float z) const noexcept {
            float total = 0.0f;
            float frequency = 1.0f;
            float amplitude = 1.0f;
            float max_amplitude = 0.0f;

            for (uint32_t i = 0; i < Octaves; i++) {
                total += PerlinNoise->CPP_Noise3D(x * frequency, y * frequency, z * frequency) * amplitude;
                max_amplitude += amplitude;
                frequency *= Lacunarity;
                amplitude *= Gain;
            }

            return total / max_amplitude;
        }

        void CPP_ArrayFractalBrownianMotion1D(const float* values, const unsigned int length, float* out) const noexcept;

        void CPP_ArrayFractalBrownianMotion2D(const float (*values)[2], const unsigned int length, float* out) const noexcept;

        void CPP_ArrayFractalBrownianMotion3D(const float (*values)[3], const unsigned int length, float* out) const noexcept;

        void CPP_RangeFractalBrownianMotion1D(const float* x_range, const unsigned int length, float* out) const noexcept;

        void CPP_RangeFractalBrownianMotion2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept;

        void CPP_RangeFractalBrownianMotion3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept;
};