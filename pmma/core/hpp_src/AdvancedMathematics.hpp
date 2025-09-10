#pragma once
#include "PMMA_Exports.hpp"

#include <cmath>
#include <cstring>

namespace CPP_AdvancedMathematics {
    EXPORT inline float PythagoreanDifference(
            const float x1,
            const float y1,
            const float x2,
            const float y2) {

        return (float)std::sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));
    };

    EXPORT inline float PythagoreanDistance(const float x, const float y) {
        return (float)std::sqrt(std::pow(x, 2) + std::pow(y, 2));
    };

    EXPORT inline float SmoothStep(const float value) {
        return value * value * (3 - 2 * value);
    };

    EXPORT inline float Ranger(
            const float value,
            const float* old_range,
            const float* new_range) {

        return new_range[0] + (value - old_range[0]) * (new_range[1] - new_range[0]) / (old_range[1] - old_range[0]);
    }

    void ArrayRanger_BASE(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out);

    void ArrayRanger_AVX2(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out);

    void ArrayRanger_AVX512(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out);

    EXPORT void ArrayRanger(
            const float* values,
            const unsigned int length,
            const float* old_range,
            const float* new_range,
            float* out);

    EXPORT inline void InPlaceArrayNormalize3D(float* value) {
        float len = std::sqrt(value[0]*value[0] + value[1]*value[1] + value[2]*value[2]);
        if (len > 1e-6f) {
            value[0] /= len;
            value[1] /= len;
            value[2] /= len;
        }
    }

    EXPORT inline void InPlaceArrayNormalize2D(float* value) {
        float len = std::sqrt(value[0]*value[0] + value[1]*value[1]);
        if (len > 1e-6f) {
            value[0] /= len;
            value[1] /= len;
        }
    }

    EXPORT inline float Lerp(float start, float end, float duration, float current_duration) {
        if (current_duration > duration) {
            return end;
        }

        if (current_duration < 0.0f) {
            return start;
        }

        return (end - start) * (current_duration / duration) + start;
    }

    EXPORT inline void ArrayNormalize_3D(const float* value, float* out) {
        out[0] = value[0];
        out[1] = value[1];
        out[2] = value[2];
        float len = std::sqrt(out[0]*out[0] + out[1]*out[1] + out[2]*out[2]);
        if (len > 1e-6f) {
            out[0] /= len;
            out[1] /= len;
            out[2] /= len;
        }
    }

    EXPORT inline void ArrayNormalize_2D(const float* value, float* out) {
        out[0] = value[0];
        out[1] = value[1];
        float len = std::sqrt(out[0]*out[0] + out[1]*out[1]);
        if (len > 1e-6f) {
            out[0] /= len;
            out[1] /= len;
        }
    }

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

    EXPORT inline void LookAt(
            const float* eye,
            const float* target,
            const float* up,
            float* out) {

        float f[3];
        CPP_AdvancedMathematics::Subtract(target, eye, f);
        CPP_AdvancedMathematics::InPlaceArrayNormalize3D(f);

        float upn[3] = {up[0], up[1], up[2]};
        CPP_AdvancedMathematics::InPlaceArrayNormalize3D(upn);

        float s[3];
        CPP_AdvancedMathematics::Cross(f, upn, s);
        CPP_AdvancedMathematics::InPlaceArrayNormalize3D(s);

        float u[3];
        CPP_AdvancedMathematics::Cross(s, f, u);

        float m[16] = {
            s[0], u[0], -f[0], 0.0f,
            s[1], u[1], -f[1], 0.0f,
            s[2], u[2], -f[2], 0.0f,
            -CPP_AdvancedMathematics::Dot(s, eye), -CPP_AdvancedMathematics::Dot(u, eye), CPP_AdvancedMathematics::Dot(f, eye), 1.0f
        };
        std::memcpy(out, m, sizeof(float) * 16);
    }

    EXPORT inline void ComputePosition(
            const float* position,
            const float* target,
            const float* up,
            float* out_x,
            float* out_y,
            float* out_z) {

        CPP_AdvancedMathematics::Subtract(position, target, out_z);
        CPP_AdvancedMathematics::InPlaceArrayNormalize3D(out_z);

        CPP_AdvancedMathematics::Cross(up, out_z, out_x);
        CPP_AdvancedMathematics::InPlaceArrayNormalize3D(out_x);

        CPP_AdvancedMathematics::Cross(out_z, out_x, out_y);
    }

    EXPORT void PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]);

    EXPORT inline float RandomFloat(const float* out_range) {
        float value = (float)rand() / RAND_MAX;
        float default_range[2] = {0.0f, 1.0f};
        return CPP_AdvancedMathematics::Ranger(value, default_range, out_range);
    }

    EXPORT inline void Linespace(const float start, const float end, const unsigned int samples, float* out) {
        float offset = (end - start) / samples;
        for (unsigned int i = 0; i < samples; i++) {
            out[i] = start + offset * i;
        }
    }
}