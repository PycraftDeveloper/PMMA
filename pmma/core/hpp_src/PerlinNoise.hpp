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

        float CPP_Noise1D(const float x) const noexcept;

        float CPP_Noise2D(const float x, const float y) const noexcept;

        float CPP_Noise3D(const float x, const float y, const float z) const noexcept;

        void CPP_ArrayNoise1D(const float* values, const unsigned int length, float* out) const noexcept;

        void CPP_ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) const noexcept;

        void CPP_ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) const noexcept;

        void CPP_RangeNoise1D(const float* x_range, const unsigned int length, float* out) const noexcept;

        void CPP_RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) const noexcept;

        void CPP_RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) const noexcept;
};