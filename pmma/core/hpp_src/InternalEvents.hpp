#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

class EXPORT CPP_InternalSpaceKeyEvent {
    private:
        std::chrono::high_resolution_clock::time_point LastEventTime;
        float DoublePressDuration;
        bool IsPressed;
        bool IsDoublePressed;

    public:
        inline void Update(bool NewIsPressed) {
            IsPressed = NewIsPressed;
        };

        inline bool GetPressed() {
            return IsPressed;
        };
};