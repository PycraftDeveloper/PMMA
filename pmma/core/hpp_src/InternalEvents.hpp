#pragma once
#include "PMMA_Exports.hpp"

#include <iostream>
#include <chrono>

class EXPORT CPP_InternalKeyEvent {
    private:
        std::chrono::high_resolution_clock::time_point LastEventTime;
        std::chrono::high_resolution_clock::time_point PreviousEventTime;
        float DoublePressDuration = 0.5f;
        float LongPressDuration = 1.0f;
        bool IsPressed = false;
        bool IsPressedToggle = false;
        bool IsLongPressValid = false;
        bool IsDoublePressed = false;
        bool PreviousState = false;

    public:
        inline void Update(bool NewIsPressed) {
            if (NewIsPressed == PreviousState) {
                return;
            }
            PreviousState = NewIsPressed;
            IsPressed = NewIsPressed;
            IsPressedToggle = NewIsPressed;
            if (IsPressed) {
                PreviousEventTime = LastEventTime;
                LastEventTime = std::chrono::high_resolution_clock::now();
                IsLongPressValid = true;

                std::chrono::duration<float> Duration = LastEventTime - PreviousEventTime;
                if (Duration.count() <= DoublePressDuration) {
                    IsDoublePressed = true;
                }
            } else {
                IsLongPressValid = false;
                IsDoublePressed = false;
            }
        };

        inline bool GetPressed() {
            return IsPressed;
        };

        inline void SetDoublePressDuration(float Duration) {
            DoublePressDuration = Duration;
        };

        inline bool GetPressedToggle() {
            if (IsPressedToggle) {
                IsPressedToggle = false;
                return true;
            }
            return false;
        };

        inline bool GetDoublePressed() {
            return IsDoublePressed;
        };

        inline void SetLongPressDuration(float Duration) {
            LongPressDuration = Duration;
        };

        inline bool GetLongPressed() {
            if (IsPressed && IsLongPressValid) {
                std::chrono::duration<float> Duration = std::chrono::high_resolution_clock::now() - LastEventTime;
                if (Duration.count() >= LongPressDuration) {
                    return true;
                }
            }
            return false;
        };
};

class EXPORT CPP_InternalKeyPadEvent : public CPP_InternalKeyEvent {
};