#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <chrono>

#include <GLFW/glfw3.h>

#include "Constants.hpp"

namespace PMMA::Types {
class Proportion;
}

namespace PMMA::Internal::Events {
class EXPORT ButtonPressed {
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

class InternalController {
public:
    ButtonPressed *GamePad_A_Button = nullptr;
    ButtonPressed *GamePad_B_Button = nullptr;
    ButtonPressed *GamePad_X_Button = nullptr;
    ButtonPressed *GamePad_Y_Button = nullptr;
    ButtonPressed *GamePad_Left_Bumper_Button = nullptr;
    ButtonPressed *GamePad_Right_Bumper_Button = nullptr;
    ButtonPressed *GamePad_Back_Button = nullptr;
    ButtonPressed *GamePad_Start_Button = nullptr;
    ButtonPressed *GamePad_Guide_Button = nullptr;
    ButtonPressed *GamePad_Left_Thumb_Button = nullptr;
    ButtonPressed *GamePad_Right_Thumb_Button = nullptr;
    ButtonPressed *GamePad_DPad_Up_Button = nullptr;
    ButtonPressed *GamePad_DPad_Right_Button = nullptr;
    ButtonPressed *GamePad_DPad_Down_Button = nullptr;
    ButtonPressed *GamePad_DPad_Left_Button = nullptr;

private:
    PMMA::Types::Proportion *GamePad_Left_Trigger = nullptr;
    PMMA::Types::Proportion *GamePad_Right_Trigger = nullptr;
    PMMA::Types::Proportion *GamePad_Left_Stick_X = nullptr;
    PMMA::Types::Proportion *GamePad_Left_Stick_Y = nullptr;
    PMMA::Types::Proportion *GamePad_Right_Stick_X = nullptr;
    PMMA::Types::Proportion *GamePad_Right_Stick_Y = nullptr;

    std::vector<PMMA::Types::Proportion> RawAxesData;
    std::vector<bool> RawButtonData;
    std::vector<std::string_view> RawHatStateData;
    std::string RawName;
    std::string GamePadName;
    std::string GUID;

    unsigned int ID;
    int RawAxisCount;
    int RawButtonCount;
    int RawHatCount;
    bool Connected;
    bool IsGamePad;
    bool UpdateRawData;

public:
    InternalController(unsigned int new_ID);

    ~InternalController();

    inline void UpdateConnection(bool new_Connected) {
        if (new_Connected) {
            RawName = glfwGetJoystickName(ID);
            GUID = glfwGetJoystickGUID(ID);

            IsGamePad = glfwJoystickIsGamepad(ID);

            if (IsGamePad) {
                GamePadName = glfwGetGamepadName(ID);
            }

            glfwGetJoystickAxes(ID, &RawAxisCount);
            for (int i = 0; i < RawAxisCount; i++) {
                RawAxesData.emplace_back();
            }

            glfwGetJoystickButtons(ID, &RawButtonCount);
            for (int i = 0; i < RawButtonCount; i++) {
                RawButtonData.push_back(false);
            }

            glfwGetJoystickHats(ID, &RawHatCount);
            for (int i = 0; i < RawHatCount; i++) {
                RawHatStateData.push_back(PMMA::Constants::HatStates::NOT_PRESSED);
            }

            Update();

        } else {
            RawName = "";
            GUID = "";
            GamePadName = "";
            RawAxesData.clear();
            RawButtonData.clear();
            RawHatStateData.clear();
        }
        Connected = new_Connected;
    };

    void Update();

    std::string GetRawName();

    std::string GetGamePadName();

    std::string GetGUID();

    inline bool GetConnected() {
        return Connected;
    };

    int GetRawAxisCount();

    int GetRawButtonCount();

    int GetRawHatCount();

    float GetRawAxis_Decimal(int AxisID);

    float GetRawAxis_Percentage(int AxisID);

    bool GetRawButtonPressed(int ButtonID);

    std::string GetRawHatState(int HatID);

    float Get_Left_Trigger_Axis_Percentage(float DeadZone);

    float Get_Right_Trigger_Axis_Percentage(float DeadZone);

    float Get_Left_Trigger_Axis_Decimal(float DeadZone);

    float Get_Right_Trigger_Axis_Decimal(float DeadZone);

    float Get_Right_Stick_X_Axis_Percentage(float DeadZone);

    float Get_Right_Stick_Y_Axis_Percentage(float DeadZone);

    float Get_Right_Stick_X_Axis_Decimal(float DeadZone);

    float Get_Right_Stick_Y_Axis_Decimal(float DeadZone);

    float Get_Left_Stick_X_Axis_Percentage(float DeadZone);

    float Get_Left_Stick_Y_Axis_Percentage(float DeadZone);

    float Get_Left_Stick_X_Axis_Decimal(float DeadZone);

    float Get_Left_Stick_Y_Axis_Decimal(float DeadZone);

    void Get_Left_Stick_Position_Decimal(float DeadZone, float *out);

    void Get_Right_Stick_Position_Decimal(float DeadZone, float *out);

    void Get_Left_Stick_Position_Percentage(float DeadZone, float *out);

    void Get_Right_Stick_Position_Percentage(float DeadZone, float *out);
};
} // namespace PMMA::Internal::Events