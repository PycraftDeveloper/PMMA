#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>

#include "PMMA_Core.hpp"

class EXPORT CPP_SpaceKeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::SpaceKeyEventInstance == nullptr) {
                throw std::runtime_error("SpaceKeyEventInstance is null");
            }
            return PMMA::SpaceKeyEventInstance->GetPressed();
        };
};