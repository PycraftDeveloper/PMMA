#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <vector>
#include <iostream>

#include <GLFW/glfw3.h>

#include "NumberConverter.hpp"

class EXPORT CPP_TextEvent {
    private:
        std::string Text = "";
        bool IsEnabled = true;

    public:
        CPP_TextEvent();

        ~CPP_TextEvent();

        inline void Update(std::string NewTextContent) {
            if (!IsEnabled) {
                return;
            }
            Text += NewTextContent;
        };

        void RemoveBack();

        void RemoveFront();

        inline std::string GetText() {
            return Text;
        };

        inline void SetEnabled(bool NewIsEnabled) {
            IsEnabled = NewIsEnabled;
        };

        inline bool GetEnabled() {
            return IsEnabled;
        };

        inline void ClearText() {
            Text = "";
        };
};

class EXPORT CPP_MousePositionEvent {
    public:
        void GetPosition(float* out);

        void GetDelta(float* out);

        void GetDeltaToggle(float* out);
};

class EXPORT CPP_MouseEnterWindowEvent {
    public:
        bool GetEntered();

        bool GetEnteredToggle();
};

class EXPORT CPP_MouseButton_Left_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_Right_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_Middle_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_0_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_1_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_2_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_3_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_4_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
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

class EXPORT CPP_ControllerEvent {
    private:
        std::string Name;
        std::string GUID;
        std::vector<CPP_BasicProportionConverter> AxesData;
        unsigned int ID;
        int AxisCount;
        bool Connected;

    public:
        CPP_ControllerEvent(unsigned int new_ID) {
            ID = new_ID;
            Connected = false;
            Name = "";
            GUID = "";
        };

        inline void UpdateConnection(bool new_Connected) {
            if (new_Connected) {
                Name = glfwGetJoystickName(ID);
                GUID = glfwGetJoystickGUID(ID);

                glfwGetJoystickAxes(ID, &AxisCount);
                for (int i = 0; i < AxisCount; i++) {
                    AxesData.emplace_back();
                }

                Update();
            } else {
                Name = "";
                GUID = "";
                AxesData.clear();
            }
            Connected = new_Connected;
        };

        inline void Update() {
            const float* axes = glfwGetJoystickAxes(ID, &AxisCount);
            for (int i = 0; i < AxisCount; i++) {
                AxesData[i].SetProportion_Decimal(axes[i]);
            }
        };

        inline bool GetConnected() {
            return Connected;
        };

        inline float GetAxis_Decimal(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxesData[AxisID].GetProportion_Decimal();
        };

        inline float GetAxis_Percentage(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxesData[AxisID].GetProportion_Percentage();
        };
};