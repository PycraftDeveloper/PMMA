#pragma once
#include "PMMA_Exports.hpp"

#include <array>
#include <cstdint>

using namespace std;

class EXPORT CPP_PerlinNoise {
    private:
        array<uint8_t, 512> Permutations;

        static const float F2;
        static const float F3;

        static inline float Fade(float t) noexcept {
            return t * t * t * (t * (t * 6 - 15) + 10);
        }

        static inline float Lerp(float t, float a, float b) noexcept {
            return a + t * (b - a);
        }

        static inline float Grad1D(int hash, float x) noexcept {
            return (hash & 1) ? x : -x;
        }

        static inline float Grad2D(int hash, float x, float y) noexcept {
            const int r = hash & 3;
            if (r == 0) return x + y;
            if (r == 1) return -x + y;
            if (r == 2) return x - y;
            return -x - y;
        }

        static inline float Grad3D(int hash, float x, float y, float z) noexcept {
            const float u = (hash < 8) ? x : y;
            const float v = (hash < 4) ? y : ((hash == 12 || hash == 14) ? x : z);
            return ((hash & 1) ? -u : u) + ((hash & 2) ? -v : v);
        }

        static inline int FastFloor(float x) noexcept {
            int xi = static_cast<int>(x);
            return (x < xi) ? xi - 1 : xi;
        }

    public:
        CPP_PerlinNoise(const uint32_t seed);

        inline float Noise1D(const float x) const noexcept {
            int CX = FastFloor(x);
            int X = CX & 255;
            float fx = x - CX;
            float u = Fade(fx);

            int A = Permutations[X];
            int B = Permutations[X + 1];

            float res = Lerp(u, Grad1D(Permutations[A], fx), Grad1D(Permutations[B], fx - 1));

            return res;
        }

        inline float Noise2D(const float x, const float y) const noexcept {
            int CX = FastFloor(x);
            int CY = FastFloor(y);

            int X = CX & 255;
            int Y = CY & 255;

            float fx = x - CX;
            float fy = y - CY;

            float u = Fade(fx);
            float v = Fade(fy);

            int A = Permutations[X] + Y;
            int B = Permutations[X + 1] + Y;

            float res = Lerp(v, Lerp(u, Grad2D(Permutations[A], fx, fy), Grad2D(Permutations[B], fx - 1, fy)),
                                Lerp(u, Grad2D(Permutations[A + 1], fx, fy - 1), Grad2D(Permutations[B + 1], fx - 1, fy - 1)));

            return res * F2;
        }

        inline float Noise3D(const float x, const float y, const float z) const noexcept {
            int CX = FastFloor(x);
            int CY = FastFloor(y);
            int CZ = FastFloor(z);

            int X = CX & 255;
            int Y = CY & 255;
            int Z = CZ & 255;

            float fx = x - CX;
            float fy = y - CY;
            float fz = z - CZ;

            float u = Fade(fx);
            float v = Fade(fy);
            float w = Fade(fz);

            int A = Permutations[X] + Y;
            int AA = Permutations[A] + Z;
            int AB = Permutations[A + 1] + Z;
            int B = Permutations[X + 1] + Y;
            int BA = Permutations[B] + Z;
            int BB = Permutations[B + 1] + Z;

            float res = Lerp(w, Lerp(v, Lerp(u, Grad3D(Permutations[AA], fx, fy, fz),
                                                Grad3D(Permutations[BA], fx - 1, fy, fz)),
                                        Lerp(u, Grad3D(Permutations[AB], fx, fy - 1, fz),
                                                Grad3D(Permutations[BB], fx - 1, fy - 1, fz))),
                                Lerp(v, Lerp(u, Grad3D(Permutations[AA + 1], fx, fy, fz - 1),
                                                Grad3D(Permutations[BA + 1], fx - 1, fy, fz - 1)),
                                        Lerp(u, Grad3D(Permutations[AB + 1], fx, fy - 1, fz - 1),
                                                Grad3D(Permutations[BB + 1], fx - 1, fy - 1, fz - 1))));

            return res * F3;
        }

        void ArrayNoise1D(const float* values, const unsigned int length, float* out) const noexcept;

        void ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) const noexcept;

        void ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) const noexcept;

        void RangeNoise1D(const float* x_range, const unsigned int length, float* out) const noexcept;

        void RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept;

        void RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept;
};