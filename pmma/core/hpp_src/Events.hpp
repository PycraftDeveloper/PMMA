#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>

#include "PMMA_Core.hpp"

class EXPORT CPP_SpaceKeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            return PMMA::KeyEvent_Space_Instance->GetPressed();
        };
};