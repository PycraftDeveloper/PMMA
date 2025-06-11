#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

class EXPORT CPP_InternalKeyEvent {
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

class EXPORT CPP_InternalKeyPadEvent {
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