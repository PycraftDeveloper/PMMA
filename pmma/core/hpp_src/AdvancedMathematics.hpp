#pragma once
#include "PMMA_Exports.hpp"

#include <cmath>

namespace CPP_AdvancedMathematics {
    EXPORT float PythagoreanDifference(const float x1, const float y1, const float x2, const float y2);

    EXPORT float PythagoreanDistance(const float x, const float y);

    EXPORT float SmoothStep(const float value);

    EXPORT inline float Ranger(const float value, const float* old_range, const float* new_range) {
        return new_range[0] + (value - old_range[0]) * (new_range[1] - new_range[0]) / (old_range[1] - old_range[0]);
    }

    EXPORT void ArrayRanger(const float* values, const unsigned int length, const float* old_range, const float* new_range, float* out);

    EXPORT inline void InPlaceArrayNormalize(float* value) {
        float len = std::sqrt(value[0]*value[0] + value[1]*value[1] + value[2]*value[2]);
        if (len > 1e-6f) {
            value[0] /= len;
            value[1] /= len;
            value[2] /= len;
        }
    }

    EXPORT void ArrayNormalize(const float* value, float* out);

    EXPORT inline void Cross(const float* a, const float* b, float* out) {
        out[0] = a[1]*b[2] - a[2]*b[1];
        out[1] = a[2]*b[0] - a[0]*b[2];
        out[2] = a[0]*b[1] - a[1]*b[0];
    }

    EXPORT inline void Subtract(const float* a, const float* b, float* out) {
        out[0] = a[0] - b[0];
        out[1] = a[1] - b[1];
        out[2] = a[2] - b[2];
    }

    EXPORT inline float Dot(const float* a, const float* b) {
        return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    }

    EXPORT void LookAt(const float* eye, const float* target, const float* up, float* out);

    EXPORT void ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z);

    EXPORT void PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]);

    EXPORT inline float RandomFloat(const float* out_range) {
        float value = (float)rand() / RAND_MAX;
        return Ranger(value, new float[2]{0.0f, 1.0f}, out_range);
    }
}