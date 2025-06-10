#pragma once
#include "PMMA_Exports.hpp"

#include <array>

#include "PerlinNoise.hpp"

using namespace std;

class EXPORT CPP_FractalBrownianMotion {
    private:
        uint32_t Seed;
        uint32_t Octaves;
        float Lacunarity;
        float Gain;

        CPP_PerlinNoise* CPP_PerlinNoise_ptr = nullptr;

    public:
        CPP_FractalBrownianMotion(const uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude);

        inline uint32_t GetSeed() const noexcept {
            return Seed;
        }

        inline uint32_t GetOctaves() const noexcept {
            return Octaves;
        }

        inline float GetLacunarity() const noexcept {
            return Lacunarity;
        }

        inline float GetGain() const noexcept {
            return Gain;
        }

        inline float Noise1D(const float x) const noexcept {
            float total = 0.0f;
            float frequency = 1.0f;
            float amplitude = 1.0f;
            float max_amplitude = 0.0f;

            for (uint32_t i = 0; i < Octaves; i++) {
                total += CPP_PerlinNoise_ptr->Noise1D(x * frequency) * amplitude;
                max_amplitude += amplitude;
                frequency *= Lacunarity;
                amplitude *= Gain;
            }

            return total / max_amplitude;
        }

        inline float Noise2D(const float x, const float y) const noexcept {
            float total = 0.0f;
            float frequency = 1.0f;
            float amplitude = 1.0f;
            float max_amplitude = 0.0f;

            for (uint32_t i = 0; i < Octaves; i++) {
                total += CPP_PerlinNoise_ptr->Noise2D(x * frequency, y * frequency) * amplitude;
                max_amplitude += amplitude;
                frequency *= Lacunarity;
                amplitude *= Gain;
            }

            return total / max_amplitude;
        }

        inline float Noise3D(const float x, const float y, const float z) const noexcept {
            float total = 0.0f;
            float frequency = 1.0f;
            float amplitude = 1.0f;
            float max_amplitude = 0.0f;

            for (uint32_t i = 0; i < Octaves; i++) {
                total += CPP_PerlinNoise_ptr->Noise3D(x * frequency, y * frequency, z * frequency) * amplitude;
                max_amplitude += amplitude;
                frequency *= Lacunarity;
                amplitude *= Gain;
            }

            return total / max_amplitude;
        }

        void ArrayNoise1D(const float* values, const unsigned int length, float* out) const noexcept;

        void ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) const noexcept;

        void ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) const noexcept;

        void RangeNoise1D(const float* x_range, const unsigned int length, float* out) const noexcept;

        void RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept;

        void RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept;
};