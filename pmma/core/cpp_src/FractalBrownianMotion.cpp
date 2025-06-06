#include "PerlinNoise.hpp"

#include "FractalBrownianMotion.hpp"

CPP_FractalBrownianMotion::CPP_FractalBrownianMotion(const uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
    CPP_PerlinNoise_ptr = new CPP_PerlinNoise(new_seed);

    Seed = new_seed;
    Octaves = new_octaves;
    Lacunarity = new_frequency;
    Gain = new_amplitude;
}

void CPP_FractalBrownianMotion::ArrayNoise1D(const float* values, const unsigned int length, float* out) const noexcept {
    for (unsigned int i = 0; i < length; ++i) {
        out[i] = Noise1D(values[i]);
    }
}

void CPP_FractalBrownianMotion::ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) const noexcept {
    for (unsigned int i = 0; i < length; i ++) {
        out[i] = Noise2D(values[i][0], values[i][1]);
    }
}

void CPP_FractalBrownianMotion::ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) const noexcept {
    for (unsigned int i = 0; i < length; i ++) {
        out[i] = Noise3D(values[i][0], values[i][1], values[i][2]);
    }
}

void CPP_FractalBrownianMotion::RangeNoise1D(const float* x_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];

    float dx = (x_range[1] - x_range[0])/length;

    for (unsigned int i = 0; i < length; ++i) {
        out[i] = Noise1D(x);
        x += dx;
    }
}

void CPP_FractalBrownianMotion::RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];
    float y = y_range[0];

    float dx = (x_range[1] - x_range[0])/length;
    float dy = (y_range[1] - y_range[0])/length;

    for (unsigned int i = 0; i < length; ++i) {
        out[i] = Noise2D(x, y);
        x += dx;
        y += dy;
    }
}

void CPP_FractalBrownianMotion::RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];
    float y = y_range[0];
    float z = z_range[0];

    float dx = (x_range[1] - x_range[0])/length;
    float dy = (y_range[1] - y_range[0])/length;
    float dz = (z_range[1] - z_range[0])/length;

    for (unsigned int i = 0; i < length; ++i) {
        out[i] = Noise3D(x, y, z);
        x += dx;
        y += dy;
        z += dz;
    }
}