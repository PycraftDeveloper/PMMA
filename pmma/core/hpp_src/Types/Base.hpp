#pragma once

#include <cstdint>
#include <optional>

namespace PMMA::Types {
struct Configure_Kwargs {
    std::optional<uint32_t> seed = std::nullopt;
    uint32_t octaves = 2;
    float frequency = 0.75f;
    float amplitude = 1.0f;
};
} // namespace PMMA::Types