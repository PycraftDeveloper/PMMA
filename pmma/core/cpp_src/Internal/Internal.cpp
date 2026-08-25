#include <cstdint>
#include <mutex>

#include "Internal/Core/PMMA_Core.hpp"

namespace PMMA::Internal {
uint32_t GetRandomSeed() {
    std::lock_guard<std::mutex> lock(PMMA::Core::Registry::SeedGeneratorLock);
    return PMMA::Core::Registry::SeedDistribution(PMMA::Core::Registry::RandomSeedGenerator);
}

std::optional<std::array<uint8_t, 3>> FindColor(std::string_view key) {
    auto it = std::find_if(
        PMMA::Constants::Colors::ColorMap.begin(), PMMA::Constants::Colors::ColorMap.end(),
        [key](const PMMA::Internal::ColorEntry &e) {
            return e.name == key;
        });

    if (it != PMMA::Constants::Colors::ColorMap.end())
        return it->value;

    return std::nullopt;
}
} // namespace PMMA::Internal