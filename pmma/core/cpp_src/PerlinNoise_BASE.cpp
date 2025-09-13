#include <random>

#include "PMMA_Core.hpp"

using namespace std;

const float CPP_PerlinNoise::F2 = 1.0f / sqrt(2.0f);
const float CPP_PerlinNoise::F3 = 1.0f / sqrt(3.0f);

CPP_PerlinNoise::CPP_PerlinNoise(const uint32_t seed) {
    array<uint32_t, 256> perm;
    for (int i = 0; i < 256; ++i) {
        perm[i] = i;
    }

    std::mt19937 rng(seed);
    for (int i = 255; i > 0; --i) {
        std::uniform_int_distribution<int> dist(0, i);
        swap(perm[i], perm[dist(rng)]);
    }

    for (int i = 0; i < 256; ++i) {
        Permutations[i] = Permutations[i + 256] = perm[i];
    }
}

void CPP_PerlinNoise::ArrayNoise1D(const float* values, const unsigned int length, float* out) const noexcept {
    if (PMMA_Registry::CPU_Supports_AVX512) {
        ArrayNoise1D_AVX512(values, length, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        ArrayNoise1D_AVX2(values, length, out);
    } else {
        ArrayNoise1D_BASE(values, length, out);
    }
}

void CPP_PerlinNoise::ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) const noexcept {
    if (PMMA_Registry::CPU_Supports_AVX512) {
        ArrayNoise2D_AVX512(values, length, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        ArrayNoise2D_AVX2(values, length, out);
    } else {
        ArrayNoise2D_BASE(values, length, out);
    }
}

void CPP_PerlinNoise::ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) const noexcept {
    if (PMMA_Registry::CPU_Supports_AVX512) {
        ArrayNoise3D_AVX512(values, length, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        ArrayNoise3D_AVX2(values, length, out);
    } else {
        ArrayNoise3D_BASE(values, length, out);
    }
}

void CPP_PerlinNoise::RangeNoise1D(const float* x_range, const unsigned int length, float* out) const noexcept {
    if (PMMA_Registry::CPU_Supports_AVX512) {
        RangeNoise1D_AVX512(x_range, length, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        RangeNoise1D_AVX2(x_range, length, out);
    } else {
        RangeNoise1D_BASE(x_range, length, out);
    }
}

void CPP_PerlinNoise::RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept {
    if (PMMA_Registry::CPU_Supports_AVX512) {
        RangeNoise2D_AVX512(x_range, y_range, length, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        RangeNoise2D_AVX2(x_range, y_range, length, out);
    } else {
        RangeNoise2D_BASE(x_range, y_range, length, out);
    }
}

void CPP_PerlinNoise::RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept {
    if (PMMA_Registry::CPU_Supports_AVX512) {
        RangeNoise3D_AVX512(x_range, y_range, z_range, length, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        RangeNoise3D_AVX2(x_range, y_range, z_range, length, out);
    } else {
        RangeNoise3D_BASE(x_range, y_range, z_range, length, out);
    }
}

void CPP_PerlinNoise::ArrayNoise1D_BASE(const float* values, const unsigned int length, float* out) const noexcept {
    for (unsigned int i = 0; i < length; ++i) {
        out[i] = Noise1D(values[i]);
    }
}

void CPP_PerlinNoise::ArrayNoise2D_BASE(const float (*values)[2], const unsigned int length, float* out) const noexcept {
    for (unsigned int i = 0; i < length; i ++) {
        out[i] = Noise2D(values[i][0], values[i][1]);
    }
}

void CPP_PerlinNoise::ArrayNoise3D_BASE(const float (*values)[3], const unsigned int length, float* out) const noexcept {
    for (unsigned int i = 0; i < length; i ++) {
        out[i] = Noise3D(values[i][0], values[i][1], values[i][2]);
    }
}

void CPP_PerlinNoise::RangeNoise1D_BASE(const float* x_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];

    float dx = (x_range[1] - x_range[0])/length;

    for (unsigned int i = 0; i < length; ++i) {
        out[i] = Noise1D(x);
        x += dx;
    }
}

void CPP_PerlinNoise::RangeNoise2D_BASE(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept {
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

void CPP_PerlinNoise::RangeNoise3D_BASE(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept {
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