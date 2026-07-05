#include <cstdint>
#include <mutex>

#include "PMMA_Core.hpp"

namespace PMMA::Internal {
uint32_t GetRandomSeed() {
    std::lock_guard<std::mutex> lock(PMMA::Registry::SeedGeneratorLock);
    return PMMA::Registry::SeedDistribution(PMMA::Registry::RandomSeedGenerator);
}
} // namespace PMMA::Internal