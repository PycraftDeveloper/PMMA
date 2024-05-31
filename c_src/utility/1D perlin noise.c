// perlin_noise_1d.c
#include <math.h>
#include <stdlib.h>

// Permutation table
static int perm[] = {151, 160, 137, 91, 90, 15, 131, 13, 201, 95,
                     96, 53, 194, 233, 7, 225, 140, 36, 103, 30,
                     69, 142, 8, 99, 37, 240, 21, 10, 23, 190,
                     6, 148, 247, 120, 234, 75, 0, 26, 197, 62,
                     94, 252, 219, 203, 117, 35, 11, 32, 57, 177,
                     33, 88, 237, 149, 56, 87, 174, 20, 125, 136,
                     171, 168, 68, 175, 74, 165, 71, 134, 139, 48,
                     27, 166, 77, 146, 158, 231, 83, 111, 229, 122,
                     60, 211, 133, 230, 220, 105, 92, 41, 55, 46,
                     245, 40, 244, 102, 143, 54, 65, 25, 63, 161,
                     1, 216, 80, 73, 209, 76, 132, 187, 208, 89,
                     18, 169, 200, 196, 135, 130, 116, 188, 159, 86,
                     164, 100, 109, 198, 173, 186, 3, 64, 52, 217,
                     226, 250, 124, 123, 5, 202, 38, 147, 118, 126,
                     255, 82, 85, 212, 207, 206, 59, 227, 47, 16,
                     58, 17, 182, 189, 28, 42, 223, 183, 170, 213,
                     119, 248, 152, 2, 44, 154, 163, 70, 221, 153,
                     101, 155, 167, 43, 172, 9, 129, 22, 39, 253,
                     19, 98, 108, 110, 79, 113, 224, 232, 178, 185,
                     112, 104, 218, 246, 97, 228, 251, 34, 242, 193,
                     238, 210, 144, 12, 191, 179, 162, 241, 81, 51,
                     145, 235, 249, 14, 239, 107, 49, 192, 214, 31,
                     181, 199, 106, 157, 184, 84, 204, 176, 115, 121,
                     50, 45, 127, 4, 150, 254, 138, 236, 205, 93,
                     222, 114, 67, 29, 24, 72, 243, 141, 128, 195,
                     78, 66, 215, 61, 156, 180};

// Helper functions for Perlin noise

static int hash(int x) {
    return perm[x & 255];
}

static float fade(float t) {
    return t * t * t * (t * (t * 6 - 15) + 10);
}

static float lerp(float t, float a, float b) {
    return a + t * (b - a);
}

static float grad(int hash, float x) {
    int h = hash & 15;
    float grad = 1.0 + (h & 7); // Gradient value is one of 1.0, 2.0, ..., 8.0
    if (h & 8) grad = -grad;    // and a random sign for the gradient.
    return grad * x;            // Compute the dot product
}

float perlin1d(float x, int seed) {
    // Adjust the seed by modifying the permutation table
    srand(seed);
    for (int i = 0; i < 256; i++) {
        perm[i] = rand() % 256;
        perm[256 + i] = perm[i];
    }

    int X = (int)floor(x) & 255;

    x -= floor(x);

    float u = fade(x);

    int A = hash(X);
    int B = hash(X + 1);

    float res = lerp(u, grad(A, x), grad(B, x - 1));
    return (res + 1.0) / 2.0;  // Normalize to [0, 1]
}

#ifdef BUILD_DLL
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT float generate_perlin_noise_1d(float x, int seed) {
    return perlin1d(x, seed);
}
