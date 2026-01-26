#include "Random.hpp"

#include <random>

#include "PMMA_Core.hpp"

void CPP_FastRandom::SetSeed() {
    uint64_t seed = static_cast<uint64_t>(GetRandomSeed());
    s[0] = splitmix64(seed);
    s[1] = splitmix64(seed);
}