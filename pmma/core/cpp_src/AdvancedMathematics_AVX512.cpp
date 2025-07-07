#include <cmath>
#include <immintrin.h>
#include <iostream>

#include "AdvancedMathematics.hpp"

using namespace std;

void CPP_AdvancedMathematics::ArrayRanger_AVX512(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out) {

    const unsigned int vec_size = 16; // AVX-512 processes 16 floats at a time
    unsigned int i = 0;

    // Load scalar range values into AVX-512 registers
    __m512 old_min = _mm512_set1_ps(old_range[0]);
    __m512 old_max = _mm512_set1_ps(old_range[1]);
    __m512 new_min = _mm512_set1_ps(new_range[0]);
    __m512 new_max = _mm512_set1_ps(new_range[1]);

    __m512 old_diff = _mm512_sub_ps(old_max, old_min);
    __m512 new_diff = _mm512_sub_ps(new_max, new_min);

    for (; i + vec_size <= length; i += vec_size) {
        // Load 16 floats from the input array
        __m512 input = _mm512_loadu_ps(&values[i]);

        // Apply the Ranger transformation
        __m512 norm = _mm512_div_ps(_mm512_sub_ps(input, old_min), old_diff);
        __m512 scaled = _mm512_add_ps(_mm512_mul_ps(norm, new_diff), new_min);

        // Store the result
        _mm512_storeu_ps(&out[i], scaled);
    }

    // Handle remaining elements
    for (; i < length; ++i) {
        out[i] = CPP_AdvancedMathematics::Ranger(values[i], old_range, new_range);
    }
}