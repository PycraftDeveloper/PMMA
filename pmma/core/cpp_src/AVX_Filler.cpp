#include "PMMA_Core.hpp"

#include "AdvancedMathematics.hpp"
#include "PerlinNoise.hpp"

#include <stdexcept>
using namespace std;

void CPP_AdvancedMathematics::ArrayRanger_AVX2(
        const float* values,
        const unsigned int length,
        const float* old_range,
        const float* new_range,
        float* out) {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_AdvancedMathematics::ArrayRanger_AVX512(
        const float* values,
        const unsigned int length,
        const float* old_range,
        const float* new_range,
        float* out) {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::ArrayNoise1D_AVX2(const float* values, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::ArrayNoise2D_AVX2(const float (*values)[2], const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::ArrayNoise3D_AVX2(const float (*values)[3], const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::RangeNoise1D_AVX2(const float* x_range, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::RangeNoise2D_AVX2(const float* x_range, const float* y_range, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::RangeNoise3D_AVX2(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::ArrayNoise1D_AVX512(const float* values, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::ArrayNoise2D_AVX512(const float (*values)[2], const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::ArrayNoise3D_AVX512(const float (*values)[3], const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::RangeNoise1D_AVX512(const float* x_range, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::RangeNoise2D_AVX512(const float* x_range, const float* y_range, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}

void CPP_PerlinNoise::RangeNoise3D_AVX512(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const {
    throw runtime_error("AVX support was disabled automatically for this \
platform in the build process because this platform does not support it. \
Please report any occurrence when this error is observed as it indicated \
an issue with the AVX detection system used by PMMA!");
}