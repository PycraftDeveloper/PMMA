#pragma once

#include <cpr/cpr.h>
#include <iostream>
#include <string>

namespace PMMA::Internal {
class NetworkingManager {
public:
    std::string QueryLatest_PMMA_Version();
};
} // namespace PMMA::Internal