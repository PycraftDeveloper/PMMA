#include <cmath>
#include <cstring>

#include "AdvancedMathematics.hpp"

using namespace std;

float CPP_AdvancedMathematics::PythagoreanDifference(const float x1, const float y1, const float x2, const float y2) {
    return (float)sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

float CPP_AdvancedMathematics::PythagoreanDistance(const float x, const float y) {
    return (float)sqrt(pow(x, 2) + pow(y, 2));
}

float CPP_AdvancedMathematics::SmoothStep(const float value) {
    return value * value * (3 - 2 * value);
}

void CPP_AdvancedMathematics::ArrayRanger(const float* values, const unsigned int length, const float* old_range, const float* new_range, float* out) { // Ensure both lengths are 2
    for (unsigned int i = 0; i < length; i++) {
        out[i] = CPP_AdvancedMathematics::Ranger(values[i], old_range, new_range);
    }
}

void CPP_AdvancedMathematics::ArrayNormalize(const float* value, float* out) { // Ensure the array has 3 elements
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

void CPP_AdvancedMathematics::LookAt(const float* eye, const float* target, const float* up, float* out) {
    float f[3];
    CPP_AdvancedMathematics::Subtract(target, eye, f);
    CPP_AdvancedMathematics::InPlaceArrayNormalize(f);

    float upn[3] = {up[0], up[1], up[2]};
    CPP_AdvancedMathematics::InPlaceArrayNormalize(upn);

    float s[3];
    CPP_AdvancedMathematics::Cross(f, upn, s);
    CPP_AdvancedMathematics::InPlaceArrayNormalize(s);

    float u[3];
    CPP_AdvancedMathematics::Cross(s, f, u);

    float m[16] = {
        s[0], u[0], -f[0], 0.0f,
        s[1], u[1], -f[1], 0.0f,
        s[2], u[2], -f[2], 0.0f,
        -CPP_AdvancedMathematics::Dot(s, eye), -CPP_AdvancedMathematics::Dot(u, eye), CPP_AdvancedMathematics::Dot(f, eye), 1.0f
    };
    memcpy(out, m, sizeof(float) * 16);
}

void CPP_AdvancedMathematics::ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z) {
    CPP_AdvancedMathematics::Subtract(position, target, out_z);
    CPP_AdvancedMathematics::InPlaceArrayNormalize(out_z);

    CPP_AdvancedMathematics::Cross(up, out_z, out_x);
    CPP_AdvancedMathematics::InPlaceArrayNormalize(out_x);

    CPP_AdvancedMathematics::Cross(out_z, out_x, out_y);
}

void CPP_AdvancedMathematics::PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]) {
    float f = 1.0f / tan(fov * 0.5f);
    float nf = 1.0f / (near - far);

    out[0][0] = f / aspect_ratio;

    out[1][1] = f;

    out[2][2] = (far + near) * nf;
    out[2][3] = (2.0f * far * near) * nf;

    out[3][2] = -1.0f;
}