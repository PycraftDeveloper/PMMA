#pragma once

#include <array>

using namespace std;

class CPP_PerlinNoise {
    private:
        array<uint8_t, 512> Permutations;

        static const float F2;
        static const float F3;

        static inline float CPP_Fade(float t) noexcept {
            return t * t * t * (t * (t * 6 - 15) + 10);
        }

        static inline float CPP_Lerp(float t, float a, float b) noexcept {
            return a + t * (b - a);
        }

        static inline float CPP_Grad1D(int hash, float x) noexcept {
            return (hash & 1) ? x : -x;
        }

        static inline float CPP_Grad2D(int hash, float x, float y) noexcept {
            const int r = hash & 3;
            if (r == 0) return x + y;
            if (r == 1) return -x + y;
            if (r == 2) return x - y;
            return -x - y;
        }

        static inline float CPP_Grad3D(int hash, float x, float y, float z) noexcept {
            const float u = (hash < 8) ? x : y;
            const float v = (hash < 4) ? y : ((hash == 12 || hash == 14) ? x : z);
            return ((hash & 1) ? -u : u) + ((hash & 2) ? -v : v);
        }

        static inline int CPP_FastFloor(float x) noexcept {
            int xi = static_cast<int>(x);
            return (x < xi) ? xi - 1 : xi;
        }

    public:
        CPP_PerlinNoise(const uint32_t seed);

        inline float CPP_Noise1D(const float x) const noexcept {
            int CX = CPP_FastFloor(x);
            int X = CX & 255;
            float fx = x - CX;
            float u = CPP_Fade(fx);

            int A = Permutations[X];
            int B = Permutations[X + 1];

            float res = CPP_Lerp(u, CPP_Grad1D(Permutations[A], fx), CPP_Grad1D(Permutations[B], fx - 1));

            return res;
        }

        inline float CPP_Noise2D(const float x, const float y) const noexcept {
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

        inline float CPP_Noise3D(const float x, const float y, const float z) const noexcept {
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

        void CPP_ArrayNoise1D(const float* values, const unsigned int length, float* out) const noexcept;

        void CPP_ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) const noexcept;

        void CPP_ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) const noexcept;

        void CPP_RangeNoise1D(const float* x_range, const unsigned int length, float* out) const noexcept;

        void CPP_RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept;

        void CPP_RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept;
};