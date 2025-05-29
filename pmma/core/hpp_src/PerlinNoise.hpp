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
            if (r == 3) return -x - y;
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
        CPP_PerlinNoise(uint32_t seed = 0);

        float CPP_Noise1D(float x) const noexcept;

        float CPP_Noise2D(float x, float y) const noexcept;

        float CPP_Noise3D(float x, float y, float z) const noexcept;
};