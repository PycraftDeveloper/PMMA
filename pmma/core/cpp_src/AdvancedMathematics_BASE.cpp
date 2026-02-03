#include "PMMA_Core.hpp"

void CPP_AdvancedMathematics::PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]) {
    float f = 1.0f / tan(fov * 0.5f);
    float nf = 1.0f / (near - far);

    out[0][0] = f / aspect_ratio;

    out[1][1] = f;

    out[2][2] = (far + near) * nf;
    out[2][3] = (2.0f * far * near) * nf;

    out[3][2] = -1.0f;
}

void CPP_AdvancedMathematics::ArrayRanger(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out) {

    if (PMMA_Registry::CPU_Supports_AVX512) {
        ArrayRanger_AVX512(values, length, old_range, new_range, out);
    } else if (PMMA_Registry::CPU_Supports_AVX2) {
        ArrayRanger_AVX2(values, length, old_range, new_range, out);
    } else {
        ArrayRanger_BASE(values, length, old_range, new_range, out);
    }
}

void CPP_AdvancedMathematics::ArrayRanger_BASE(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out) {

    for (unsigned int i = 0; i < length; i++) {
        out[i] = CPP_AdvancedMathematics::Ranger(values[i], old_range, new_range);
    }
}