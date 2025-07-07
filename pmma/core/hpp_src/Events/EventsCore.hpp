#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

class EXPORT CPP_ButtonPressedEvent {
    private:
        std::chrono::high_resolution_clock::time_point LastEventTime;
        std::chrono::high_resolution_clock::time_point PreviousEventTime;
        std::chrono::high_resolution_clock::time_point LongPressPollTime;
        float DoublePressDuration = 0.5f;
        float LongPressDuration = 1.0f;
        float RepeatPressDuration = 0.25f;
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
                LongPressPollTime = LastEventTime;
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

        inline bool PollLongPressed() {
            bool LongPressed = GetLongPressed();
            if (LongPressed) {
                std::chrono::duration<float> Duration = std::chrono::high_resolution_clock::now() - LongPressPollTime;
                if (Duration.count() >= RepeatPressDuration) {
                    LongPressPollTime = std::chrono::high_resolution_clock::now();
                    return true;
                }
                return false;
            }
            return false;
        };

        inline void SetRepeatPressDuration(float Duration) {
            RepeatPressDuration = Duration;
        };

        inline float GetRepeatPressDuration() {
            return RepeatPressDuration;
        };

        inline float GetLongPressDuration() {
            return LongPressDuration;
        };

        inline float GetDoublePressDuration() {
            return DoublePressDuration;
        };
};