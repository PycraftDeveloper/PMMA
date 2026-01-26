#include <immintrin.h>
#include <array>
#include <cstdint>

#include "PerlinNoise.hpp"

using namespace std;

__m256 Fade_AVX2(__m256 t) noexcept {
    __m256 t2 = _mm256_mul_ps(t, t);
    __m256 t3 = _mm256_mul_ps(t2, t);
    __m256 t4 = _mm256_mul_ps(t2, t2);
    __m256 t5 = _mm256_mul_ps(t4, t);

    return _mm256_add_ps(
        _mm256_add_ps(
            _mm256_mul_ps(_mm256_set1_ps(6.0f), t5),
            _mm256_mul_ps(_mm256_set1_ps(-15.0f), t4)
        ),
        _mm256_mul_ps(_mm256_set1_ps(10.0f), t3)
    );
}

__m256 Lerp_AVX2(__m256 t, __m256 a, __m256 b) noexcept {
    return _mm256_add_ps(a, _mm256_mul_ps(t, _mm256_sub_ps(b, a)));
}

__m256 Grad1D_AVX2(__m256i hash, __m256 x) noexcept {
    __m256i bit3 = _mm256_and_si256(hash, _mm256_set1_epi32(8)); // either 0 or 8
    __m256i sign = _mm256_slli_epi32(bit3, 28); // 8 << 28 = 0x80000000 (sign bit)
    __m256 sign_ps = _mm256_castsi256_ps(sign);
    __m256 x_signed = _mm256_xor_ps(x, sign_ps);
    return x_signed;
}

__m256 Grad2D_AVX2(__m256i hash, __m256 x, __m256 y) noexcept {
    __m256i h = _mm256_and_si256(hash, _mm256_set1_epi32(7));  // h & 7

    // u = (h & 1) ? y : x
    __m256i bit0_mask = _mm256_and_si256(h, _mm256_set1_epi32(1));
    __m256 mask_u = _mm256_castsi256_ps(_mm256_cmpeq_epi32(bit0_mask, _mm256_setzero_si256()));
    __m256 u = _mm256_blendv_ps(y, x, mask_u);

    // v = (h & 2) ? y : x
    __m256i bit1_mask = _mm256_and_si256(h, _mm256_set1_epi32(2));
    __m256 mask_v = _mm256_castsi256_ps(_mm256_cmpeq_epi32(bit1_mask, _mm256_setzero_si256()));
    __m256 v = _mm256_blendv_ps(y, x, mask_v);

    // sign masks: bit 2 and bit 3 decide sign for u and v
    __m256i bit2 = _mm256_and_si256(h, _mm256_set1_epi32(4));  // bit 2 mask
    __m256i bit3 = _mm256_and_si256(h, _mm256_set1_epi32(8));  // bit 3 mask

    __m256i sign_u_mask = _mm256_slli_epi32(_mm256_srli_epi32(bit2, 2), 31); // move bit 2 to sign bit
    __m256i sign_v_mask = _mm256_slli_epi32(_mm256_srli_epi32(bit3, 3), 31); // move bit 3 to sign bit

    // flip sign bits by XORing
    u = _mm256_xor_ps(u, _mm256_castsi256_ps(sign_u_mask));
    v = _mm256_xor_ps(v, _mm256_castsi256_ps(sign_v_mask));

    return _mm256_add_ps(u, v);
}

__m256 Grad3D_AVX2(__m256i hash, __m256 x, __m256 y, __m256 z) noexcept {
    __m256i h = _mm256_and_si256(hash, _mm256_set1_epi32(15));  // h & 15
    __m256 hf = _mm256_cvtepi32_ps(h);

    // u = (h > 7.5) ? x : y
    __m256 mask_u = _mm256_cmp_ps(hf, _mm256_set1_ps(7.5f), _CMP_GT_OQ);
    __m256 u = _mm256_blendv_ps(y, x, mask_u);

    // v = (bit0 == 0 or bit1 == 0) ? z : y
    __m256i bit0 = _mm256_and_si256(h, _mm256_set1_epi32(1));
    __m256i bit1 = _mm256_and_si256(h, _mm256_set1_epi32(2));
    __m256i cond0 = _mm256_cmpeq_epi32(bit0, _mm256_setzero_si256());
    __m256i cond1 = _mm256_cmpeq_epi32(bit1, _mm256_setzero_si256());
    __m256i vcond = _mm256_or_si256(cond0, cond1);
    __m256 vmask = _mm256_castsi256_ps(vcond);
    __m256 v = _mm256_blendv_ps(y, z, vmask);

    // Sign masks from bits 3 and 2
    __m256i bit3 = _mm256_and_si256(h, _mm256_set1_epi32(8));
    __m256i bit2 = _mm256_and_si256(h, _mm256_set1_epi32(4));

    __m256i smask_u = _mm256_slli_epi32(_mm256_srli_epi32(bit3, 3), 31);
    __m256i smask_v = _mm256_slli_epi32(_mm256_srli_epi32(bit2, 2), 31);

    u = _mm256_xor_ps(u, _mm256_castsi256_ps(smask_u));
    v = _mm256_xor_ps(v, _mm256_castsi256_ps(smask_v));

    return _mm256_add_ps(u, v);
}

__m256i GatherPerm_AVX2(const std::array<uint32_t, 512>& Permutations, __m256i indices) noexcept {
    // Mask indices to [0..511]
    __m256i masked = _mm256_and_si256(indices, _mm256_set1_epi32(511));

    // Gather with cast to const int*
    return _mm256_i32gather_epi32(reinterpret_cast<const int*>(Permutations.data()), masked, 4);
}

__m256 Noise1D_AVX2(const array<uint32_t, 512>& Permutations, const __m256 x_vec) noexcept {
    // floor(x)
    __m256 cx_f = _mm256_floor_ps(x_vec);
    __m256i cx = _mm256_cvttps_epi32(cx_f);
    __m256 fx = _mm256_sub_ps(x_vec, cx_f);

    // X = CX & 255
    __m256i X = _mm256_and_si256(cx, _mm256_set1_epi32(255));

    // u = Fade(fx)
    __m256 u = Fade_AVX2(fx);

    // Compute indices A and B: perm[X] and perm[X+1]
    __m256i XP1 = _mm256_add_epi32(X, _mm256_set1_epi32(1));
    __m256i permX = GatherPerm_AVX2(Permutations, X);
    __m256i permX1 = GatherPerm_AVX2(Permutations, XP1);
    __m256i permA = GatherPerm_AVX2(Permutations, permX);
    __m256i permB = GatherPerm_AVX2(Permutations, permX1);

    // compute fx-1
    __m256 fxm1 = _mm256_sub_ps(fx, _mm256_set1_ps(1.0f));

    // Perform gradients
    __m256 gA = Grad1D_AVX2(permA, fx);
    __m256 gB = Grad1D_AVX2(permB, fxm1);

    // Lerp
    __m256 res = Lerp_AVX2(u, gA, gB);
    return res;
}

__m256 Noise2D_AVX2(const array<uint32_t, 512>& Permutations, const float F2, const __m256 x_vec, const __m256 y_vec) noexcept {
    __m256 cx_f = _mm256_floor_ps(x_vec);
    __m256i cx = _mm256_cvttps_epi32(cx_f);
    __m256 fx = _mm256_sub_ps(x_vec, cx_f);

    __m256 cy_f = _mm256_floor_ps(y_vec);
    __m256i cy = _mm256_cvttps_epi32(cy_f);
    __m256 fy = _mm256_sub_ps(y_vec, cy_f);

    __m256i mask255 = _mm256_set1_epi32(255);

    __m256i X = _mm256_and_si256(cx, mask255);
    __m256i Y = _mm256_and_si256(cy, mask255);
    __m256i XP1 = _mm256_and_si256(_mm256_add_epi32(X, _mm256_set1_epi32(1)), mask255);
    __m256i YP1 = _mm256_and_si256(_mm256_add_epi32(Y, _mm256_set1_epi32(1)), mask255);

    __m256 u = Fade_AVX2(fx);
    __m256 v = Fade_AVX2(fy);

    __m256i pX = GatherPerm_AVX2(Permutations, X);
    __m256i pX1 = GatherPerm_AVX2(Permutations, XP1);

    __m256i A = _mm256_and_si256(_mm256_add_epi32(pX, Y), mask255);
    __m256i B = _mm256_and_si256(_mm256_add_epi32(pX1, Y), mask255);
    __m256i A1 = _mm256_and_si256(_mm256_add_epi32(A, _mm256_set1_epi32(1)), mask255);
    __m256i B1 = _mm256_and_si256(_mm256_add_epi32(B, _mm256_set1_epi32(1)), mask255);

    __m256i PA = GatherPerm_AVX2(Permutations, A);
    __m256i PB = GatherPerm_AVX2(Permutations, B);
    __m256i PA1 = GatherPerm_AVX2(Permutations, A1);
    __m256i PB1 = GatherPerm_AVX2(Permutations, B1);

    __m256 g00 = Grad2D_AVX2(PA, fx, fy);
    __m256 g10 = Grad2D_AVX2(PB, _mm256_sub_ps(fx, _mm256_set1_ps(1.0f)), fy);
    __m256 g01 = Grad2D_AVX2(PA1, fx, _mm256_sub_ps(fy, _mm256_set1_ps(1.0f)));
    __m256 g11 = Grad2D_AVX2(PB1, _mm256_sub_ps(fx, _mm256_set1_ps(1.0f)), _mm256_sub_ps(fy, _mm256_set1_ps(1.0f)));

    __m256 lerpX0 = Lerp_AVX2(u, g00, g10);
    __m256 lerpX1 = Lerp_AVX2(u, g01, g11);

    __m256 res = _mm256_mul_ps(Lerp_AVX2(v, lerpX0, lerpX1), _mm256_set1_ps(F2));

    return res;
}

__m256 Noise3D_AVX2(const array<uint32_t, 512>& Permutations, const float F3,
                    const __m256 x_vec, const __m256 y_vec, const __m256 z_vec) noexcept {

    // floor(x,y,z)
    __m256 cx_f = _mm256_floor_ps(x_vec);
    __m256i cx = _mm256_cvttps_epi32(cx_f);
    __m256 fx = _mm256_sub_ps(x_vec, cx_f);

    __m256 cy_f = _mm256_floor_ps(y_vec);
    __m256i cy = _mm256_cvttps_epi32(cy_f);
    __m256 fy = _mm256_sub_ps(y_vec, cy_f);

    __m256 cz_f = _mm256_floor_ps(z_vec);
    __m256i cz = _mm256_cvttps_epi32(cz_f);
    __m256 fz = _mm256_sub_ps(z_vec, cz_f);

    // Wrap to 0..255 for permutation indexing
    __m256i mask255 = _mm256_set1_epi32(255);

    __m256i X = _mm256_and_si256(cx, mask255);
    __m256i Y = _mm256_and_si256(cy, mask255);
    __m256i Z = _mm256_and_si256(cz, mask255);

    __m256i XP1 = _mm256_and_si256(_mm256_add_epi32(X, _mm256_set1_epi32(1)), mask255);
    __m256i YP1 = _mm256_and_si256(_mm256_add_epi32(Y, _mm256_set1_epi32(1)), mask255);
    __m256i ZP1 = _mm256_and_si256(_mm256_add_epi32(Z, _mm256_set1_epi32(1)), mask255);

    // Fade curves for interpolation weights
    __m256 u = Fade_AVX2(fx);
    __m256 v = Fade_AVX2(fy);
    __m256 w = Fade_AVX2(fz);

    // Hash coordinate of cube corners

    // perm(X)
    __m256i permX  = GatherPerm_AVX2(Permutations, X);
    __m256i permXP1 = GatherPerm_AVX2(Permutations, XP1);

    // perm(X) + Y wrapped by 255
    __m256i A  = _mm256_and_si256(_mm256_add_epi32(permX, Y), mask255);
    __m256i B  = _mm256_and_si256(_mm256_add_epi32(permXP1, Y), mask255);
    __m256i A1 = _mm256_and_si256(_mm256_add_epi32(permX, YP1), mask255);
    __m256i B1 = _mm256_and_si256(_mm256_add_epi32(permXP1, YP1), mask255);

    // perm(perm(X) + Y) + Z wrapped by 255
    __m256i AA = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, A), Z), mask255);
    __m256i BA = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, B), Z), mask255);
    __m256i AB = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, A1), Z), mask255);
    __m256i BB = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, B1), Z), mask255);

    __m256i AA1 = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, A), ZP1), mask255);
    __m256i BA1 = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, B), ZP1), mask255);
    __m256i AB1 = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, A1), ZP1), mask255);
    __m256i BB1 = _mm256_and_si256(_mm256_add_epi32(GatherPerm_AVX2(Permutations, B1), ZP1), mask255);

    // Calculate offsets for gradient calculation
    __m256 fxm1 = _mm256_sub_ps(fx, _mm256_set1_ps(1));
    __m256 fym1 = _mm256_sub_ps(fy, _mm256_set1_ps(1));
    __m256 fzm1 = _mm256_sub_ps(fz, _mm256_set1_ps(1));

    // Compute gradients at the eight corners
    __m256 g000 = Grad3D_AVX2(AA,  fx,   fy,   fz);
    __m256 g100 = Grad3D_AVX2(BA,  fxm1, fy,   fz);
    __m256 g010 = Grad3D_AVX2(AB,  fx,   fym1, fz);
    __m256 g110 = Grad3D_AVX2(BB,  fxm1, fym1, fz);

    __m256 g001 = Grad3D_AVX2(AA1, fx,   fy,   fzm1);
    __m256 g101 = Grad3D_AVX2(BA1, fxm1, fy,   fzm1);
    __m256 g011 = Grad3D_AVX2(AB1, fx,   fym1, fzm1);
    __m256 g111 = Grad3D_AVX2(BB1, fxm1, fym1, fzm1);

    // Trilinear interpolation
    __m256 lerpX00 = Lerp_AVX2(u, g000, g100);
    __m256 lerpX10 = Lerp_AVX2(u, g010, g110);
    __m256 lerpX01 = Lerp_AVX2(u, g001, g101);
    __m256 lerpX11 = Lerp_AVX2(u, g011, g111);

    __m256 lerpY0 = Lerp_AVX2(v, lerpX00, lerpX10);
    __m256 lerpY1 = Lerp_AVX2(v, lerpX01, lerpX11);

    __m256 res = _mm256_mul_ps(Lerp_AVX2(w, lerpY0, lerpY1), _mm256_set1_ps(F3));

    return res;
}

void CPP_PerlinNoise::ArrayNoise1D_AVX2(const float* values, const unsigned int length, float* out) const {
    unsigned int i = 0;
    for (; i + 8 <= length; i += 8) {
        __m256 x = _mm256_loadu_ps(&values[i]);
        __m256 r = Noise1D_AVX2(Permutations, x);
        _mm256_storeu_ps(&out[i], r);
    }

    for (; i < length; ++i) {
        out[i] = Noise1D(values[i]);
    }
}

void CPP_PerlinNoise::ArrayNoise2D_AVX2(const float (*values)[2], const unsigned int length, float* out) const {
    unsigned int i = 0;
    for (; i + 8 <= length; i += 8) {
        __m256 x, y;
        x = _mm256_set_ps(values[i+7][0], values[i+6][0], values[i+5][0], values[i+4][0],
                          values[i+3][0], values[i+2][0], values[i+1][0], values[i+0][0]);
        y = _mm256_set_ps(values[i+7][1], values[i+6][1], values[i+5][1], values[i+4][1],
                          values[i+3][1], values[i+2][1], values[i+1][1], values[i+0][1]);

        __m256 r = Noise2D_AVX2(Permutations, F2, x, y);  // Assume AVX implementation exists
        _mm256_storeu_ps(&out[i], r);
    }

    for (; i < length; ++i) {
        out[i] = Noise2D(values[i][0], values[i][1]);
    }
}

void CPP_PerlinNoise::ArrayNoise3D_AVX2(const float (*values)[3], const unsigned int length, float* out) const {
    unsigned int i = 0;
    for (; i + 8 <= length; i += 8) {
        __m256 x, y, z;
        x = _mm256_set_ps(values[i+7][0], values[i+6][0], values[i+5][0], values[i+4][0],
                          values[i+3][0], values[i+2][0], values[i+1][0], values[i+0][0]);
        y = _mm256_set_ps(values[i+7][1], values[i+6][1], values[i+5][1], values[i+4][1],
                          values[i+3][1], values[i+2][1], values[i+1][1], values[i+0][1]);
        z = _mm256_set_ps(values[i+7][2], values[i+6][2], values[i+5][2], values[i+4][2],
                          values[i+3][2], values[i+2][2], values[i+1][2], values[i+0][2]);

        __m256 r = Noise3D_AVX2(Permutations, F3, x, y, z);
        _mm256_storeu_ps(&out[i], r);
    }

    for (; i < length; ++i) {
        out[i] = Noise3D(values[i][0], values[i][1], values[i][2]);
    }
}

void CPP_PerlinNoise::RangeNoise1D_AVX2(const float* x_range, const unsigned int length, float* out) const {
    float x = x_range[0];
    float dx = (x_range[1] - x_range[0]) / length;

    unsigned int i = 0;

    __m256 offset = _mm256_set_ps(7, 6, 5, 4, 3, 2, 1, 0);

    for (; i + 8 <= length; i += 8) {
        __m256 dx_vec = _mm256_set1_ps(dx);
        __m256 x_base = _mm256_set1_ps(x);
        __m256 x_vec = _mm256_fmadd_ps(offset, dx_vec, x_base);

        __m256 r = Noise1D_AVX2(Permutations, x_vec);
        _mm256_storeu_ps(&out[i], r);

        x += dx * 8;
    }

    for (; i < length; ++i) {
        out[i] = Noise1D(x);
        x += dx;
    }
}

void CPP_PerlinNoise::RangeNoise2D_AVX2(const float* x_range, const float* y_range, const unsigned int length, float* out) const {
    float x = x_range[0];
    float y = y_range[0];
    float dx = (x_range[1] - x_range[0]) / length;
    float dy = (y_range[1] - y_range[0]) / length;

    unsigned int i = 0;

    __m256 offset = _mm256_set_ps(7, 6, 5, 4, 3, 2, 1, 0);

    for (; i + 8 <= length; i += 8) {
        __m256 dx_vec = _mm256_set1_ps(dx);
        __m256 dy_vec = _mm256_set1_ps(dy);
        __m256 x_vec = _mm256_fmadd_ps(offset, dx_vec, _mm256_set1_ps(x));
        __m256 y_vec = _mm256_fmadd_ps(offset, dy_vec, _mm256_set1_ps(y));

        __m256 r = Noise2D_AVX2(Permutations, F2, x_vec, y_vec);
        _mm256_storeu_ps(&out[i], r);

        x += dx * 8;
        y += dy * 8;
    }

    for (; i < length; ++i) {
        out[i] = Noise2D(x, y);
        x += dx;
        y += dy;
    }
}

void CPP_PerlinNoise::RangeNoise3D_AVX2(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const {
    float x = x_range[0];
    float y = y_range[0];
    float z = z_range[0];
    float dx = (x_range[1] - x_range[0]) / length;
    float dy = (y_range[1] - y_range[0]) / length;
    float dz = (z_range[1] - z_range[0]) / length;

    unsigned int i = 0;

    __m256 offset = _mm256_set_ps(7, 6, 5, 4, 3, 2, 1, 0);

    for (; i + 8 <= length; i += 8) {
        __m256 x_vec = _mm256_fmadd_ps(offset, _mm256_set1_ps(dx), _mm256_set1_ps(x));
        __m256 y_vec = _mm256_fmadd_ps(offset, _mm256_set1_ps(dy), _mm256_set1_ps(y));
        __m256 z_vec = _mm256_fmadd_ps(offset, _mm256_set1_ps(dz), _mm256_set1_ps(z));

        __m256 r = Noise3D_AVX2(Permutations, F3, x_vec, y_vec, z_vec);
        _mm256_storeu_ps(&out[i], r);

        x += dx * 8;
        y += dy * 8;
        z += dz * 8;
    }

    for (; i < length; ++i) {
        out[i] = Noise3D(x, y, z);
        x += dx;
        y += dy;
        z += dz;
    }
}