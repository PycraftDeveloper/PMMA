#pragma once
#include "PMMA_Exports.hpp"

#include <iostream>
#include <chrono>
#include <vector>

class EXPORT CPP_InternalKeyEvent {
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

class EXPORT CPP_InternalKeyPadEvent : public CPP_InternalKeyEvent {
};

class EXPORT CPP_InternalMousePositionEvent {
    private:
        float position[2] = {0, 0};
        float previous_position[2] = {0, 0};
        float delta[2] = {0, 0};
        float toggle_delta[2] = {0, 0};

    public:
        inline void Update(float x_value, float y_value) {
            delta[0] = x_value - position[0];
            delta[1] = y_value - position[1];
            toggle_delta[0] = delta[0];
            toggle_delta[1] = delta[1];
            previous_position[0] = position[0];
            previous_position[1] = position[1];
            position[0] = x_value;
            position[1] = y_value;
        };

        inline void GetPosition(float* out) {
            out[0] = position[0];
            out[1] = position[1];
        };

        inline void GetDelta(float* out) {
            out[0] = delta[0];
            out[1] = delta[1];
        };

        inline void GetDeltaToggle(float* out) {
            out[0] = toggle_delta[0];
            out[1] = toggle_delta[1];
            toggle_delta[0] = 0;
            toggle_delta[1] = 0;
        };
};

class EXPORT CPP_InternalMouseEnterWindowEvent {
    private:
        bool IsEntered = false;
        bool IsEnteredToggle = false;

    public:
        inline void Update(bool NewIsEntered) {
            if (NewIsEntered != IsEntered) {
                IsEnteredToggle = NewIsEntered;
            }
            IsEntered = NewIsEntered;
        };

        inline bool GetEntered() {
            return IsEntered;
        };

        inline bool GetEnteredToggle() {
            if (IsEnteredToggle) {
                IsEnteredToggle = false;
                return true;
            }
            return false;
        };
};

class EXPORT CPP_InternalMouseButtonEvent : public CPP_InternalKeyEvent {
};