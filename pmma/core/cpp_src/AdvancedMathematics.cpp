#include <cmath>
#include <cstring>

#include "AdvancedMathematics.hpp"

using namespace std;

void CPP_AdvancedMathematics::PerspectiveFOV(const float fov, const float aspect_ratio, const float near, const float far, float (*out)[4]) {
    float f = 1.0f / tan(fov * 0.5f);
    float nf = 1.0f / (near - far);

    out[0][0] = f / aspect_ratio;

    out[1][1] = f;

    out[2][2] = (far + near) * nf;
    out[2][3] = (2.0f * far * near) * nf;

    out[3][2] = -1.0f;
}