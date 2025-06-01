#pragma once

namespace CPP_AdvancedMathematics {
    float PythagoreanDifference(const float x1, const float y1, const float x2, const float y2);

    float PythagoreanDistance(const float x, const float y);

    float SmoothStep(const float value);

    inline float Ranger(const float value, const float* old_range, const float* new_range) {
        return new_range[0] + (value - old_range[0]) * (new_range[1] - new_range[0]) / (old_range[1] - old_range[0]);
    }

    void ArrayRanger(const float* values, const int length, const float* old_range, const float* new_range, float* out);

    inline void InPlaceArrayNormalize(float* value) {
        float len = std::sqrt(value[0]*value[0] + value[1]*value[1] + value[2]*value[2]);
        if (len > 1e-6f) {
            value[0] /= len;
            value[1] /= len;
            value[2] /= len;
        }
    }

    void ArrayNormalize(const float* value, float* out);

    inline void Cross(const float* a, const float* b, float* out) {
        out[0] = a[1]*b[2] - a[2]*b[1];
        out[1] = a[2]*b[0] - a[0]*b[2];
        out[2] = a[0]*b[1] - a[1]*b[0];
    }

    inline void Subtract(const float* a, const float* b, float* out) {
        out[0] = a[0] - b[0];
        out[1] = a[1] - b[1];
        out[2] = a[2] - b[2];
    }

    inline float Dot(const float* a, const float* b) {
        return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
    }

    void LookAt(const float* eye, const float* target, const float* up, float* out);

    void ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z);

    void PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]);
}