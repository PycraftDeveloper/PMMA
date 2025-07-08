#include <immintrin.h>

#include "PMMA_Core.hpp"

using namespace std;

__m512 Fade_AVX512(__m512 t) noexcept {
    __m512 t2 = _mm512_mul_ps(t, t);
    __m512 t3 = _mm512_mul_ps(t2, t);
    __m512 t4 = _mm512_mul_ps(t2, t2);
    __m512 t5 = _mm512_mul_ps(t4, t);

    return _mm512_add_ps(
        _mm512_add_ps(
            _mm512_mul_ps(_mm512_set1_ps(6.0f), t5),
            _mm512_mul_ps(_mm512_set1_ps(-15.0f), t4)
        ),
        _mm512_mul_ps(_mm512_set1_ps(10.0f), t3)
    );
}

__m512 Lerp_AVX512(__m512 t, __m512 a, __m512 b) noexcept {
    return _mm512_add_ps(a, _mm512_mul_ps(t, _mm512_sub_ps(b, a)));
}

__m512 Grad1D_AVX512(__m512i hash, __m512 x) noexcept {
    __m512i h = _mm512_and_si512(hash, _mm512_set1_epi32(15)); // h & 15
    __m512 sign = _mm512_castsi512_ps(_mm512_slli_epi32(_mm512_and_si512(h, _mm512_set1_epi32(8)), 28)); // get sign bit
    __m512 x_signed = _mm512_xor_ps(x, sign); // flip sign
    return x_signed;
}

__m512 Grad2D_AVX512(__m512i hash, __m512 x, __m512 y) noexcept {

    // h = hash & 7
    __m512i h = _mm512_and_epi32(hash, _mm512_set1_epi32(7));

    // u: choose x when (h&1)==0, else y
    __mmask16 mu = _mm512_cmpeq_epi32_mask(
                       _mm512_and_epi32(h, _mm512_set1_epi32(1)),
                       _mm512_setzero_epi32());
    __m512 u = _mm512_mask_blend_ps(mu, y, x);

    // v: choose y when (h&2)!=0, else x
    // equivalently: choose x when (h&2)==0
    __mmask16 mv = _mm512_cmpeq_epi32_mask(
                       _mm512_and_epi32(h, _mm512_set1_epi32(2)),
                       _mm512_setzero_epi32());
    __m512 v = _mm512_mask_blend_ps(mv, x, y);

    // apply sign flips
    __m512 sign_u = _mm512_castsi512_ps(
                        _mm512_slli_epi32(
                            _mm512_and_epi32(h, _mm512_set1_epi32(4)),
                            29));
    __m512 sign_v = _mm512_castsi512_ps(
                        _mm512_slli_epi32(
                            _mm512_and_epi32(h, _mm512_set1_epi32(8)),
                            28));

    u = _mm512_xor_ps(u, sign_u);
    v = _mm512_xor_ps(v, sign_v);

    return _mm512_add_ps(u, v);
}

__m512 Grad3D_AVX512(__m512i hash,
                            __m512 x,
                            __m512 y,
                            __m512 z) noexcept
{
    // h = hash & 15
    __m512i h = _mm512_and_epi32(hash, _mm512_set1_epi32(15));

    // hf = float(h)
    __m512 hf = _mm512_cvtepi32_ps(h);

    // mask_u = (h > 7.5)
    __mmask16 mask_u = _mm512_cmp_ps_mask(hf,
                                          _mm512_set1_ps(7.5f),
                                          _CMP_GT_OQ);

    // u = mask_u ? x : y
    __m512 u = _mm512_mask_blend_ps(mask_u, y, x);

    // mask bits for v: (h&1)==0 OR (h&2)==0
    __mmask16 m1_zero = _mm512_cmpeq_epi32_mask(
                           _mm512_and_epi32(h, _mm512_set1_epi32(1)),
                           _mm512_setzero_epi32());
    __mmask16 m2_zero = _mm512_cmpeq_epi32_mask(
                           _mm512_and_epi32(h, _mm512_set1_epi32(2)),
                           _mm512_setzero_epi32());
    __mmask16 mask_v = m1_zero | m2_zero;

    // v = mask_v ? z : y
    __m512 v = _mm512_mask_blend_ps(mask_v, y, z);

    // sign masks: h&8 → sign of u, h&4 → sign of v
    __m512i smu = _mm512_slli_epi32(
                      _mm512_and_epi32(h, _mm512_set1_epi32(8)), 28);
    __m512i smv = _mm512_slli_epi32(
                      _mm512_and_epi32(h, _mm512_set1_epi32(4)), 29);

    // xor to flip sign bits
    u = _mm512_xor_ps(u, _mm512_castsi512_ps(smu));
    v = _mm512_xor_ps(v, _mm512_castsi512_ps(smv));

    // return u + v
    return _mm512_add_ps(u, v);
}

__m512i GatherPerm_AVX512(const array<uint32_t, 512>& Permutations, __m512i indices) noexcept {
    // Mask indices to [0..511]
    __m512i masked = _mm512_and_epi32(indices, _mm512_set1_epi32(511));

    // Gather from Permutations directly
    return _mm512_i32gather_epi32(masked, Permutations.data(), 4);
}

__m512 Noise1D_AVX512(const array<uint32_t, 512>& Permutations, const __m512 x_vec) noexcept {
    // floor(x)
    __m512 cx_f = _mm512_floor_ps(x_vec);
    __m512i cx = _mm512_cvttps_epi32(cx_f);
    __m512 fx = _mm512_sub_ps(x_vec, cx_f);

    // X = CX & 255
    __m512i X = _mm512_and_si512(cx, _mm512_set1_epi32(255));

    // u = Fade(fx)
    __m512 u = Fade_AVX512(fx);

    // Compute indices A and B: perm[X] and perm[X+1]
    __m512i XP1 = _mm512_add_epi32(X, _mm512_set1_epi32(1));
    __m512i permX = GatherPerm_AVX512(Permutations, X);
    __m512i permX1 = GatherPerm_AVX512(Permutations, XP1);
    __m512i permA = GatherPerm_AVX512(Permutations, permX);
    __m512i permB = GatherPerm_AVX512(Permutations, permX1);

    // compute fx-1
    __m512 fxm1 = _mm512_sub_ps(fx, _mm512_set1_ps(1.0f));

    // Perform gradients
    __m512 gA = Grad1D_AVX512(permA, fx);
    __m512 gB = Grad1D_AVX512(permB, fxm1);

    // Lerp
    __m512 res = Lerp_AVX512(u, gA, gB);
    return res;
}

__m512 Noise2D_AVX512(const array<uint32_t, 512>& Permutations, const float F2, const __m512 x_vec, const __m512 y_vec) noexcept {
    // floor(x)
    __m512 cx_f = _mm512_floor_ps(x_vec);
    __m512i cx = _mm512_cvttps_epi32(cx_f);
    __m512 fx = _mm512_sub_ps(x_vec, cx_f);
    // floor(y)
    __m512 cy_f = _mm512_floor_ps(y_vec);
    __m512i cy = _mm512_cvttps_epi32(cy_f);
    __m512 fy = _mm512_sub_ps(y_vec, cy_f);

    // X, Y = floor & 255
    __m512i X = _mm512_and_si512(cx, _mm512_set1_epi32(255));
    __m512i Y = _mm512_and_si512(cy, _mm512_set1_epi32(255));
    __m512i XP1 = _mm512_add_epi32(X, _mm512_set1_epi32(1));
    __m512i YP1 = _mm512_add_epi32(Y, _mm512_set1_epi32(1));

    // fade
    __m512 u = Fade_AVX512(fx), v = Fade_AVX512(fy);

    // compute perm[A], perm[B], perm[A+1], perm[B+1]
    // A = perm[X] + Y
    __m512i pX = GatherPerm_AVX512(Permutations, X);
    __m512i pX1 = GatherPerm_AVX512(Permutations, XP1);
    __m512i A = _mm512_add_epi32(pX, Y);
    __m512i B = _mm512_add_epi32(pX1, Y);
    __m512i A1 = _mm512_add_epi32(A, _mm512_set1_epi32(1));
    __m512i B1 = _mm512_add_epi32(B, _mm512_set1_epi32(1));

    // fetch perms
    __m512i PA = GatherPerm_AVX512(Permutations, A), PB = GatherPerm_AVX512(Permutations, B);
    __m512i PA1 = GatherPerm_AVX512(Permutations, A1), PB1 = GatherPerm_AVX512(Permutations, B1);

    // gradient values
    __m512 g00 = Grad2D_AVX512(PA, fx, fy);
    __m512 g10 = Grad2D_AVX512(PB, _mm512_sub_ps(fx, _mm512_set1_ps(1)), fy);
    __m512 g01 = Grad2D_AVX512(PA1, fx, _mm512_sub_ps(fy, _mm512_set1_ps(1)));
    __m512 g11 = Grad2D_AVX512(PB1, _mm512_sub_ps(fx, _mm512_set1_ps(1)), _mm512_sub_ps(fy, _mm512_set1_ps(1)));

    // lerp along x, then y
    __m512 lerpX0 = Lerp_AVX512(u, g00, g10);
    __m512 lerpX1 = Lerp_AVX512(u, g01, g11);
    __m512 res = _mm512_mul_ps( Lerp_AVX512(v, lerpX0, lerpX1), _mm512_set1_ps(F2) );

    return res;
}

__m512 Noise3D_AVX512(const array<uint32_t, 512>& Permutations, const float F3, const __m512 x_vec, const __m512 y_vec, const __m512 z_vec) noexcept {
    // floor(x)
    __m512 cx_f = _mm512_floor_ps(x_vec);
    __m512i cx = _mm512_cvttps_epi32(cx_f);
    __m512 fx = _mm512_sub_ps(x_vec, cx_f);
    // floor(y)
    __m512 cy_f = _mm512_floor_ps(y_vec);
    __m512i cy = _mm512_cvttps_epi32(cy_f);
    __m512 fy = _mm512_sub_ps(y_vec, cy_f);
    // floor(z)
    __m512 cz_f = _mm512_floor_ps(z_vec);
    __m512i cz = _mm512_cvttps_epi32(cz_f);
    __m512 fz = _mm512_sub_ps(z_vec, cz_f);

    __m512i X = _mm512_and_si512(cx, _mm512_set1_epi32(255));
    __m512i Y = _mm512_and_si512(cy, _mm512_set1_epi32(255));
    __m512i Z = _mm512_and_si512(cz, _mm512_set1_epi32(255));
    __m512i XP1 = _mm512_add_epi32(X, _mm512_set1_epi32(1));
    __m512i YP1 = _mm512_add_epi32(Y, _mm512_set1_epi32(1));
    __m512i ZP1 = _mm512_add_epi32(Z, _mm512_set1_epi32(1));

    __m512 u = Fade_AVX512(fx), v = Fade_AVX512(fy), w = Fade_AVX512(fz);

    // compute corner perms
    __m512i pX = GatherPerm_AVX512(Permutations, X), pX1 = GatherPerm_AVX512(Permutations, XP1);
    __m512i A   = _mm512_add_epi32(pX, Y), B  = _mm512_add_epi32(pX1, Y);
    __m512i AA  = _mm512_add_epi32(GatherPerm_AVX512(Permutations, A), Z),
            AB  = _mm512_add_epi32(GatherPerm_AVX512(Permutations, A), ZP1);
    __m512i BA  = _mm512_add_epi32(GatherPerm_AVX512(Permutations, B), Z),
            BB  = _mm512_add_epi32(GatherPerm_AVX512(Permutations, B), ZP1);

    // fetch all permutation values
    __m512i P_AA  = GatherPerm_AVX512(Permutations, AA), PB_AA1 = GatherPerm_AVX512(Permutations, _mm512_add_epi32(AA, _mm512_set1_epi32(1)));
    __m512i P_AB  = GatherPerm_AVX512(Permutations, AB), PB_AB1 = GatherPerm_AVX512(Permutations, _mm512_add_epi32(AB, _mm512_set1_epi32(1)));
    __m512i P_BA  = GatherPerm_AVX512(Permutations, BA), PB_BA1 = GatherPerm_AVX512(Permutations, _mm512_add_epi32(BA, _mm512_set1_epi32(1)));
    __m512i P_BB  = GatherPerm_AVX512(Permutations, BB), PB_BB1 = GatherPerm_AVX512(Permutations, _mm512_add_epi32(BB, _mm512_set1_epi32(1)));

    // Pre-calc offsets
    __m512 fxm1 = _mm512_sub_ps(fx, _mm512_set1_ps(1));
    __m512 fym1 = _mm512_sub_ps(fy, _mm512_set1_ps(1));
    __m512 fzm1 = _mm512_sub_ps(fz, _mm512_set1_ps(1));

    // corners: (fx,fy,fz), (fx-1,fy,fz), (fx,fy-1,fz), etc...
    __m512 g000 = Grad3D_AVX512(P_AA, fx, fy, fz);
    __m512 g100 = Grad3D_AVX512(P_BA, fxm1, fy, fz);
    __m512 g010 = Grad3D_AVX512(P_AB, fx, fym1, fz);
    __m512 g110 = Grad3D_AVX512(P_BB, fxm1, fym1, fz);

    __m512 g001 = Grad3D_AVX512(PB_AA1, fx, fy, fzm1);
    __m512 g101 = Grad3D_AVX512(PB_BA1, fxm1, fy, fzm1);
    __m512 g011 = Grad3D_AVX512(PB_AB1, fx, fym1, fzm1);
    __m512 g111 = Grad3D_AVX512(PB_BB1, fxm1, fym1, fzm1);

    // combine via trilinear lerp
    __m512 lerpX00 = Lerp_AVX512(u, g000, g100);
    __m512 lerpX10 = Lerp_AVX512(u, g010, g110);
    __m512 lerpX01 = Lerp_AVX512(u, g001, g101);
    __m512 lerpX11 = Lerp_AVX512(u, g011, g111);

    __m512 lerpY0 = Lerp_AVX512(v, lerpX00, lerpX10);
    __m512 lerpY1 = Lerp_AVX512(v, lerpX01, lerpX11);

    __m512 res = _mm512_mul_ps(Lerp_AVX512(w, lerpY0, lerpY1), _mm512_set1_ps(F3));
    return res;
}

void CPP_PerlinNoise::ArrayNoise1D_AVX512(const float* values, const unsigned int length, float* out) const noexcept {
    unsigned int i = 0;
    for (; i + 16 <= length; i += 16) {
        __m512 x = _mm512_loadu_ps(&values[i]);
        __m512 r = Noise1D_AVX512(Permutations, x);
        _mm512_storeu_ps(&out[i], r);
    }

    for (; i < length; ++i) {
        out[i] = Noise1D(values[i]);
    }
}

void CPP_PerlinNoise::ArrayNoise2D_AVX512(const float (*values)[2], const unsigned int length, float* out) const noexcept {
    unsigned int i = 0;
    for (; i + 16 <= length; i += 16) {
        __m512 x, y;
        x = _mm512_set_ps(
            values[i+15][0], values[i+14][0], values[i+13][0], values[i+12][0],
            values[i+11][0], values[i+10][0], values[i+9][0],  values[i+8][0],
            values[i+7][0],  values[i+6][0],  values[i+5][0],  values[i+4][0],
            values[i+3][0],  values[i+2][0],  values[i+1][0],  values[i+0][0]
        );
        y = _mm512_set_ps(
            values[i+15][1], values[i+14][1], values[i+13][1], values[i+12][1],
            values[i+11][1], values[i+10][1], values[i+9][1],  values[i+8][1],
            values[i+7][1],  values[i+6][1],  values[i+5][1],  values[i+4][1],
            values[i+3][1],  values[i+2][1],  values[i+1][1],  values[i+0][1]
        );

        __m512 r = Noise2D_AVX512(Permutations, F2, x, y);  // Assume AVX implementation exists
        _mm512_storeu_ps(&out[i], r);
    }

    for (; i < length; ++i) {
        out[i] = Noise2D(values[i][0], values[i][1]);
    }
}

void CPP_PerlinNoise::ArrayNoise3D_AVX512(const float (*values)[3], const unsigned int length, float* out) const noexcept {
    unsigned int i = 0;
    for (; i + 16 <= length; i += 16) {
        __m512 x, y, z;
        x = _mm512_set_ps(
            values[i+15][0], values[i+14][0], values[i+13][0], values[i+12][0],
            values[i+11][0], values[i+10][0], values[i+9][0],  values[i+8][0],
            values[i+7][0],  values[i+6][0],  values[i+5][0],  values[i+4][0],
            values[i+3][0],  values[i+2][0],  values[i+1][0],  values[i+0][0]
        );
        y = _mm512_set_ps(
            values[i+15][1], values[i+14][1], values[i+13][1], values[i+12][1],
            values[i+11][1], values[i+10][1], values[i+9][1],  values[i+8][1],
            values[i+7][1],  values[i+6][1],  values[i+5][1],  values[i+4][1],
            values[i+3][1],  values[i+2][1],  values[i+1][1],  values[i+0][1]
        );
        z = _mm512_set_ps(
            values[i+15][2], values[i+14][2], values[i+13][2], values[i+12][2],
            values[i+11][2], values[i+10][2], values[i+9][2],  values[i+8][2],
            values[i+7][2],  values[i+6][2],  values[i+5][2],  values[i+4][2],
            values[i+3][2],  values[i+2][2],  values[i+1][2],  values[i+0][2]
        );

        __m512 r = Noise3D_AVX512(Permutations, F3, x, y, z);
        _mm512_storeu_ps(&out[i], r);
    }

    for (; i < length; ++i) {
        out[i] = Noise3D(values[i][0], values[i][1], values[i][2]);
    }
}

void CPP_PerlinNoise::RangeNoise1D_AVX512(const float* x_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];
    float dx = (x_range[1] - x_range[0]) / length;

    unsigned int i = 0;

    __m512 offset = _mm512_set_ps(
        15.f, 14.f, 13.f, 12.f, 11.f, 10.f, 9.f, 8.f,
        7.f,  6.f,  5.f,  4.f,  3.f,  2.f, 1.f, 0.f
    );

    for (; i + 16 <= length; i += 8) {
        __m512 dx_vec = _mm512_set1_ps(dx);
        __m512 x_base = _mm512_set1_ps(x);
        __m512 x_vec = _mm512_fmadd_ps(offset, dx_vec, x_base);

        __m512 r = Noise1D_AVX512(Permutations, x_vec);
        _mm512_storeu_ps(&out[i], r);

        x += dx * 16;
    }

    for (; i < length; ++i) {
        out[i] = Noise1D(x);
        x += dx;
    }
}

void CPP_PerlinNoise::RangeNoise2D_AVX512(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];
    float y = y_range[0];
    float dx = (x_range[1] - x_range[0]) / length;
    float dy = (y_range[1] - y_range[0]) / length;

    unsigned int i = 0;

    __m512 offset = _mm512_set_ps(
        15.f, 14.f, 13.f, 12.f, 11.f, 10.f, 9.f, 8.f,
        7.f,  6.f,  5.f,  4.f,  3.f,  2.f, 1.f, 0.f
    );

    for (; i + 16 <= length; i += 16) {
        __m512 dx_vec = _mm512_set1_ps(dx);
        __m512 dy_vec = _mm512_set1_ps(dy);
        __m512 x_vec = _mm512_fmadd_ps(offset, dx_vec, _mm512_set1_ps(x));
        __m512 y_vec = _mm512_fmadd_ps(offset, dy_vec, _mm512_set1_ps(y));

        __m512 r = Noise2D_AVX512(Permutations, F2, x_vec, y_vec);
        _mm512_storeu_ps(&out[i], r);

        x += dx * 16;
        y += dy * 16;
    }

    for (; i < length; ++i) {
        out[i] = Noise2D(x, y);
        x += dx;
        y += dy;
    }
}

void CPP_PerlinNoise::RangeNoise3D_AVX512(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept {
    float x = x_range[0];
    float y = y_range[0];
    float z = z_range[0];
    float dx = (x_range[1] - x_range[0]) / length;
    float dy = (y_range[1] - y_range[0]) / length;
    float dz = (z_range[1] - z_range[0]) / length;

    unsigned int i = 0;

    // Create offset vector: lanes from 0 to 15
    __m512 offset = _mm512_set_ps(
        15.f, 14.f, 13.f, 12.f, 11.f, 10.f, 9.f, 8.f,
        7.f,  6.f,  5.f,  4.f,  3.f,  2.f, 1.f, 0.f
    );

    for (; i + 16 <= length; i += 16) {
        __m512 dx_vec = _mm512_set1_ps(dx);
        __m512 dy_vec = _mm512_set1_ps(dy);
        __m512 dz_vec = _mm512_set1_ps(dz);
        __m512 x_base = _mm512_set1_ps(x);
        __m512 y_base = _mm512_set1_ps(y);
        __m512 z_base = _mm512_set1_ps(z);

        __m512 x_vec = _mm512_fmadd_ps(offset, dx_vec, x_base); // x + offset*dx
        __m512 y_vec = _mm512_fmadd_ps(offset, dy_vec, y_base);
        __m512 z_vec = _mm512_fmadd_ps(offset, dz_vec, z_base);

        __m512 r = Noise3D_AVX512(Permutations, F3, x_vec, y_vec, z_vec);
        _mm512_storeu_ps(&out[i], r);

        x += dx * 16;
        y += dy * 16;
        z += dz * 16;
    }

    // Scalar remainder
    for (; i < length; ++i) {
        out[i] = Noise3D(x, y, z);
        x += dx;
        y += dy;
        z += dz;
    }
}