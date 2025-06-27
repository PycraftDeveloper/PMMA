#pragma once
#include "PMMA_Exports.hpp"

#include "EventsCore.hpp"

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

class EXPORT CPP_MousePositionEvent {
    public:
        CPP_MousePositionEvent();
        ~CPP_MousePositionEvent();

        void GetPosition(float* out);

        void GetDelta(float* out);

        void GetDeltaToggle(float* out);
};

class EXPORT CPP_MouseEnterWindowEvent {
    public:
        CPP_MouseEnterWindowEvent();
        ~CPP_MouseEnterWindowEvent();

        bool GetEntered();

        bool GetEnteredToggle();
};

class EXPORT CPP_MouseButtonEvent_Left : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_Left();
        ~CPP_MouseButtonEvent_Left();

};

class EXPORT CPP_MouseButtonEvent_Right : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_Right();
        ~CPP_MouseButtonEvent_Right();

};

class EXPORT CPP_MouseButtonEvent_Middle : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_Middle();
        ~CPP_MouseButtonEvent_Middle();

};

class EXPORT CPP_MouseButtonEvent_0 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_0();
        ~CPP_MouseButtonEvent_0();

};

class EXPORT CPP_MouseButtonEvent_1 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_1();
        ~CPP_MouseButtonEvent_1();

};

class EXPORT CPP_MouseButtonEvent_2 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_2();
        ~CPP_MouseButtonEvent_2();

};

class EXPORT CPP_MouseButtonEvent_3 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_3();
        ~CPP_MouseButtonEvent_3();

};

class EXPORT CPP_MouseButtonEvent_4 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_4();
        ~CPP_MouseButtonEvent_4();

};

class EXPORT CPP_MouseScrollEvent {
    private:
        float Position[2] = {0, 0};
        float Delta[2] = {0, 0};
        float DeltaToggle[2] = {0, 0};
        bool IsEnabled = true;

    public:
        CPP_MouseScrollEvent();

        ~CPP_MouseScrollEvent();

        inline void Update(float delta_x, float delta_y) {
            if (!IsEnabled) {
                return;
            }
            Delta[0] = delta_x;
            Delta[1] = delta_y;
            DeltaToggle[0] += delta_x;
            DeltaToggle[1] += delta_y;
            Position[0] += delta_x;
            Position[1] += delta_y;
        };

        inline void GetPosition(float* out) {
            out[0] = Position[0];
            out[1] = Position[1];
        };

        inline void GetDelta(float* out) {
            out[0] = Delta[0];
            out[1] = Delta[1];
        };

        inline void GetDeltaToggle(float* out) {
            out[0] = DeltaToggle[0];
            out[1] = DeltaToggle[1];
            DeltaToggle[0] = 0;
            DeltaToggle[1] = 0;
        };

        inline float GetHorizontalPosition() {
            return Position[0];
        };

        inline float GetVerticalPosition() {
            return Position[1];
        };

        inline float GetHorizontalDelta() {
            return Delta[0];
        };

        inline float GetVerticalDelta() {
            return Delta[1];
        };

        inline float GetHorizontalDeltaToggle() {
            float out = DeltaToggle[0];
            DeltaToggle[0] = 0;
            return out;
        };

        inline float GetVerticalDeltaToggle() {
            float out = DeltaToggle[1];
            DeltaToggle[1] = 0;
            return out;
        };

        inline void ClearPosition() {
            Position[0] = 0;
            Position[1] = 0;
        };

        inline bool GetEnabled() {
            return IsEnabled;
        };

        inline void SetEnabled(bool NewIsEnabled) {
            IsEnabled = NewIsEnabled;
        };
};