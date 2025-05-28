#include <cmath>

#include "AdvancedMathematics.hpp"

using namespace std;

float CPP_PythagoreanDifference(const float x1, const float y1, const float x2, const float y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

float CPP_PythagoreanDistance(const float x, const float y) {
    return sqrt(pow(x, 2) + pow(y, 2));
}

float CPP_SmoothStep(const float value) {
    return value * value * (3 - 2 * value);
}

float CPP_Ranger(const float value, const float* old_range, const float* new_range) { // Ensure both lengths are 2
    return new_range[0] + (value - old_range[0]) * (new_range[1] - new_range[0]) / (old_range[1] - old_range[0]);
}

float CPP_ArrayRanger(float* values, const int length, const float* old_range, const float* new_range) { // Ensure both lengths are 2
    for (int i = 0; i < length; i++) {
        values[i] = Ranger(values[i], old_range, new_range);
    }
}

void CPP_ArrayNormalize(float* value) { // Ensure the array has 3 elements
    float len = std::sqrt(value[0]*value[0] + value[1]*value[1] + value[2]*value[2]);
    if (len > 1e-6f) {
        value[0] /= len;
        value[1] /= len;
        value[2] /= len;
    }
}

void CPP_Cross(const float* a, const float* b, float* out) {
    out[0] = a[1]*b[2] - a[2]*b[1];
    out[1] = a[2]*b[0] - a[0]*b[2];
    out[2] = a[0]*b[1] - a[1]*b[0];
}

void CPP_Subtract(const float* a, const float* b, float* out) {
    out[0] = a[0] - b[0];
    out[1] = a[1] - b[1];
    out[2] = a[2] - b[2];
}

float CPP_Dot(const float* a, const float* b) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

void CPP_LookAt(const float* eye, const float* target, const float* up, float* out) {
    float f[3];
    Subtract(target, eye, f);
    ArrayNormalize(f);

    float upn[3] = {up[0], up[1], up[2]};
    ArrayNormalize(upn);

    float s[3];
    Cross(f, upn, s);
    ArrayNormalize(s);

    float u[3];
    Cross(s, f, u);

    float m[16] = {
        s[0], u[0], -f[0], 0.0f,
        s[1], u[1], -f[1], 0.0f,
        s[2], u[2], -f[2], 0.0f,
        -Dot(s, eye), -Dot(u, eye), Dot(f, eye), 1.0f
    };
    memcpy(out, m, sizeof(float) * 16);
}

void CPP_ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z) {
    Subtract(position, target, out_z);
    ArrayNormalize(out_z);

    Cross(up, out_z, out_x);
    ArrayNormalize(out_x);

    Cross(out_z, out_x, out_y);
}

void CPP_PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]) {
    float f = 1.0f / tan(fov * 0.5f);
    float nf = 1.0f / (near - far);

    out[0][0] = f / aspect_ratio;

    out[1][1] = f;

    out[2][2] = (far + near) * nf;
    out[2][3] = (2.0f * far * near) * nf;

    out[3][2] = -1.0f;
}