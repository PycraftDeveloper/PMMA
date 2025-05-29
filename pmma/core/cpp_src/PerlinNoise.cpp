#include "PerlinNoise.hpp"

const float CPP_PerlinNoise::F2 = 1.0f / sqrt(2.0f);
const float CPP_PerlinNoise::F3 = 1.0f / sqrt(3.0f);

CPP_PerlinNoise::CPP_PerlinNoise(uint32_t seed) {
    array<uint8_t, 256> perm;
    for (int i = 0; i < 256; ++i) {
        perm[i] = i;
    }

    srand(seed);
    for (int i = 255; i > 0; --i) {
        swap(Permutations[i], Permutations[rand() % (i + 1)]);
    }

    for (int i = 0; i < 256; ++i) {
        Permutations[i] = Permutations[i + 256] = perm[i];
    }
}

float CPP_PerlinNoise::CPP_Noise1D(float x) const noexcept {
    int CX = CPP_FastFloor(x);
    int X = CX & 255;
    float fx = x - CX;
    float u = CPP_Fade(fx);

    int A = Permutations[X];
    int B = Permutations[X + 1];

    float res = CPP_Lerp(u, CPP_Grad1D(Permutations[A], fx), CPP_Grad1D(Permutations[B], fx - 1));

    return res;
}

float CPP_PerlinNoise::CPP_Noise2D(float x, float y) const noexcept {
    int CX = CPP_FastFloor(x);
    int CY = CPP_FastFloor(y);

    int X = CX & 255;
    int Y = CY & 255;

    float fx = x - CX;
    float fy = y - CY;

    float u = CPP_Fade(fx);
    float v = CPP_Fade(fy);

    int A = Permutations[X] + Y;
    int B = Permutations[X + 1] + Y;

    float res = CPP_Lerp(v, CPP_Lerp(u, CPP_Grad2D(Permutations[A], fx, fy), CPP_Grad2D(Permutations[B], fx - 1, fy)),
                        CPP_Lerp(u, CPP_Grad2D(Permutations[A + 1], fx, fy - 1), CPP_Grad2D(Permutations[B + 1], fx - 1, fy - 1)));

    return res * F2;
}

float CPP_PerlinNoise::CPP_Noise3D(float x, float y, float z) const noexcept {
    int CX = CPP_FastFloor(x);
    int CY = CPP_FastFloor(y);
    int CZ = CPP_FastFloor(z);

    int X = CX & 255;
    int Y = CY & 255;
    int Z = CZ & 255;

    float fx = x - CX;
    float fy = y - CY;
    float fz = z - CZ;

    float u = CPP_Fade(fx);
    float v = CPP_Fade(fy);
    float w = CPP_Fade(fz);

    int A = Permutations[X] + Y;
    int AA = Permutations[A] + Z;
    int AB = Permutations[A + 1] + Z;
    int B = Permutations[X + 1] + Y;
    int BA = Permutations[B] + Z;
    int BB = Permutations[B + 1] + Z;

    float res = CPP_Lerp(w, CPP_Lerp(v, CPP_Lerp(u, CPP_Grad3D(Permutations[AA], fx, fy, fz),
                                        CPP_Grad3D(Permutations[BA], fx - 1, fy, fz)),
                                CPP_Lerp(u, CPP_Grad3D(Permutations[AB], fx, fy - 1, fz),
                                        CPP_Grad3D(Permutations[BB], fx - 1, fy - 1, fz))),
                        CPP_Lerp(v, CPP_Lerp(u, CPP_Grad3D(Permutations[AA + 1], fx, fy, fz - 1),
                                        CPP_Grad3D(Permutations[BA + 1], fx - 1, fy, fz - 1)),
                                CPP_Lerp(u, CPP_Grad3D(Permutations[AB + 1], fx, fy - 1, fz - 1),
                                        CPP_Grad3D(Permutations[BB + 1], fx - 1, fy - 1, fz - 1))));

    return res * F3;
}