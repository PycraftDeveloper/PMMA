#pragma once

#include <iostream>
#include <random>
#include <cstdint>
#include <chrono>

class CPP_FastRandom {
    private:
        uint64_t s[2];  // state

        inline uint64_t rotl(const uint64_t x, int k) {
            return (x << k) | (x >> (64 - k));
        }

        uint64_t next64() {
            const uint64_t s0 = s[0];
            uint64_t s1 = s[1];
            const uint64_t result = s0 + s1;

            s1 ^= s0;
            s[0] = rotl(s0, 55) ^ s1 ^ (s1 << 14);
            s[1] = rotl(s1, 36);

            return result;
        }

        // SplitMix64 for seeding
        static uint64_t splitmix64(uint64_t &x) {
            uint64_t z = (x += 0x9e3779b97f4a7c15ULL);
            z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
            z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
            return z ^ (z >> 31);
        }

    public:
        CPP_FastRandom() {
            SetSeed();
        }

        CPP_FastRandom(uint64_t seed) {
            SetSeed(seed);
        }

        inline void SetSeed(uint64_t seed) {
            s[0] = splitmix64(seed);
            s[1] = splitmix64(seed);
        }

        void SetSeed();

        inline uint32_t Next() {
            return static_cast<uint32_t>(next64() >> 32);
        }

        inline float NextUniform() {
            return (next64() >> 40) * (1.0f / (1ULL << 24));
        }

        // Fast integer in [0, max]
        inline uint32_t Next(uint32_t max) {
            return Next() % max;
        }

        // Float in [0, max], truncated to integer precision
        inline float Next(float max) {
            return static_cast<float>(Next(static_cast<uint32_t>(max + 1)));
        }

        inline float Next(int max) {
            return static_cast<float>(Next(static_cast<uint32_t>(max + 1)));
        }
};