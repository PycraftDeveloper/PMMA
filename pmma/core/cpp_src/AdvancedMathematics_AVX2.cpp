#include <immintrin.h>

#include "PMMA_Core.hpp"

using namespace std;

void CPP_AdvancedMathematics::ArrayRanger_AVX2(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out) {

    const float old_min = old_range[0];
    const float old_max = old_range[1];
    const float new_min = new_range[0];
    const float new_max = new_range[1];

    const float old_diff = old_max - old_min;
    const float new_diff = new_max - new_min;

    // Broadcast constants into AVX2 registers
    __m256 v_old_min = _mm256_set1_ps(old_min);
    __m256 v_old_diff = _mm256_set1_ps(old_diff);
    __m256 v_new_min = _mm256_set1_ps(new_min);
    __m256 v_new_diff = _mm256_set1_ps(new_diff);

    unsigned int i = 0;
    for (; i + 7 < length; i += 8) {
        // Load 8 floats
        __m256 v = _mm256_loadu_ps(&values[i]);

        // Normalize to 0–1
        __m256 norm = _mm256_div_ps(_mm256_sub_ps(v, v_old_min), v_old_diff);

        // Scale to new range
        __m256 result = _mm256_add_ps(_mm256_mul_ps(norm, v_new_diff), v_new_min);

        // Store result
        _mm256_storeu_ps(&out[i], result);
    }

    // Handle remaining values
    for (; i < length; ++i) {
        out[i] = Ranger(values[i], old_range, new_range);
    }
}