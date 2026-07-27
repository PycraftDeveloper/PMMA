#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

#include <GLFW/glfw3.h>

#include "Constants.hpp"
#include "Logger.hpp"
#include "Types.hpp"

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
    PMMA::Logger *Logger;

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
    InternalController(unsigned int new_ID) {
        GamePad_A_Button = new ButtonPressed();
        GamePad_B_Button = new ButtonPressed();
        GamePad_X_Button = new ButtonPressed();
        GamePad_Y_Button = new ButtonPressed();
        GamePad_Left_Bumper_Button = new ButtonPressed();
        GamePad_Right_Bumper_Button = new ButtonPressed();
        GamePad_Back_Button = new ButtonPressed();
        GamePad_Start_Button = new ButtonPressed();
        GamePad_Guide_Button = new ButtonPressed();
        GamePad_Left_Thumb_Button = new ButtonPressed();
        GamePad_Right_Thumb_Button = new ButtonPressed();
        GamePad_DPad_Up_Button = new ButtonPressed();
        GamePad_DPad_Right_Button = new ButtonPressed();
        GamePad_DPad_Down_Button = new ButtonPressed();
        GamePad_DPad_Left_Button = new ButtonPressed();

        GamePad_Left_Trigger = new PMMA::Types::Proportion();
        GamePad_Right_Trigger = new PMMA::Types::Proportion();
        GamePad_Left_Stick_X = new PMMA::Types::Proportion();
        GamePad_Left_Stick_Y = new PMMA::Types::Proportion();
        GamePad_Right_Stick_X = new PMMA::Types::Proportion();
        GamePad_Right_Stick_Y = new PMMA::Types::Proportion();

        ID = new_ID;
        Connected = false;
        IsGamePad = false;
        UpdateRawData = false;
        GamePadName = "";
        RawName = "";
        GUID = "";

        Logger = new PMMA::Logger();
    };

    ~InternalController() {
        delete GamePad_A_Button;
        delete GamePad_B_Button;
        delete GamePad_X_Button;
        delete GamePad_Y_Button;
        delete GamePad_Left_Bumper_Button;
        delete GamePad_Right_Bumper_Button;
        delete GamePad_Back_Button;
        delete GamePad_Start_Button;
        delete GamePad_Guide_Button;
        delete GamePad_Left_Thumb_Button;
        delete GamePad_Right_Thumb_Button;
        delete GamePad_DPad_Up_Button;
        delete GamePad_DPad_Right_Button;
        delete GamePad_DPad_Down_Button;
        delete GamePad_DPad_Left_Button;

        delete GamePad_Left_Trigger;
        delete GamePad_Right_Trigger;
        delete GamePad_Left_Stick_X;
        delete GamePad_Left_Stick_Y;
        delete GamePad_Right_Stick_X;
        delete GamePad_Right_Stick_Y;

        delete Logger;

        GamePad_A_Button = nullptr;
        GamePad_B_Button = nullptr;
        GamePad_X_Button = nullptr;
        GamePad_Y_Button = nullptr;
        GamePad_Left_Bumper_Button = nullptr;
        GamePad_Right_Bumper_Button = nullptr;
        GamePad_Back_Button = nullptr;
        GamePad_Start_Button = nullptr;
        GamePad_Guide_Button = nullptr;
        GamePad_Left_Thumb_Button = nullptr;
        GamePad_Right_Thumb_Button = nullptr;
        GamePad_DPad_Up_Button = nullptr;
        GamePad_DPad_Right_Button = nullptr;
        GamePad_DPad_Down_Button = nullptr;
        GamePad_DPad_Left_Button = nullptr;

        GamePad_Left_Trigger = nullptr;
        GamePad_Right_Trigger = nullptr;
        GamePad_Left_Stick_X = nullptr;
        GamePad_Left_Stick_Y = nullptr;
        GamePad_Right_Stick_X = nullptr;
        GamePad_Right_Stick_Y = nullptr;

        Logger = nullptr;

        RawAxesData.clear();
        RawButtonData.clear();
        RawHatStateData.clear();
    }

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

    inline void Update() {
        if (UpdateRawData) {
            const float *axes = glfwGetJoystickAxes(ID, &RawAxisCount);
            for (int i = 0; i < RawAxisCount; i++) {
                RawAxesData[i].SetDecimal(axes[i]);
            }

            const unsigned char *buttons = glfwGetJoystickButtons(ID, &RawButtonCount);
            for (int i = 0; i < RawButtonCount; i++) {
                RawButtonData[i] = (buttons[i] == GLFW_PRESS);
            }

            const unsigned char *hats = glfwGetJoystickHats(ID, &RawHatCount);
            for (int i = 0; i < RawHatCount; i++) {
                switch (hats[i]) {
                case GLFW_HAT_CENTERED:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::NOT_PRESSED);
                    break;
                case GLFW_HAT_UP:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_UP);
                    break;
                case GLFW_HAT_RIGHT:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_RIGHT);
                    break;
                case GLFW_HAT_DOWN:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_DOWN);
                    break;
                case GLFW_HAT_LEFT:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_LEFT);
                    break;
                case GLFW_HAT_RIGHT | GLFW_HAT_UP:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_UP_RIGHT);
                    break;
                case GLFW_HAT_RIGHT | GLFW_HAT_DOWN:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_DOWN_RIGHT);
                    break;
                case GLFW_HAT_LEFT | GLFW_HAT_DOWN:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_DOWN_LEFT);
                    break;
                case GLFW_HAT_LEFT | GLFW_HAT_UP:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::PRESSED_UP_LEFT);
                    break;
                default:
                    RawHatStateData[i] = (PMMA::Constants::HatStates::NOT_PRESSED);
                };
            }
        }

        if (IsGamePad) {
            GLFWgamepadstate state;

            if (glfwGetGamepadState(ID, &state)) {
                GamePad_A_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_A] == GLFW_PRESS);
                GamePad_B_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_B] == GLFW_PRESS);
                GamePad_X_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_X] == GLFW_PRESS);
                GamePad_Y_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_Y] == GLFW_PRESS);
                GamePad_Left_Bumper_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_LEFT_BUMPER] == GLFW_PRESS);
                GamePad_Right_Bumper_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER] == GLFW_PRESS);
                GamePad_Back_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_BACK] == GLFW_PRESS);
                GamePad_Start_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_START] == GLFW_PRESS);
                GamePad_Guide_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_GUIDE] == GLFW_PRESS);
                GamePad_Left_Thumb_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_LEFT_THUMB] == GLFW_PRESS);
                GamePad_Right_Thumb_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_RIGHT_THUMB] == GLFW_PRESS);
                GamePad_DPad_Up_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_UP] == GLFW_PRESS);
                GamePad_DPad_Right_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_RIGHT] == GLFW_PRESS);
                GamePad_DPad_Down_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_DOWN] == GLFW_PRESS);
                GamePad_DPad_Left_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_LEFT] == GLFW_PRESS);

                GamePad_Left_Trigger->SetDecimal(state.axes[GLFW_GAMEPAD_AXIS_LEFT_TRIGGER]);
                GamePad_Right_Trigger->SetDecimal(state.axes[GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER]);
                GamePad_Left_Stick_X->SetDecimal(state.axes[GLFW_GAMEPAD_AXIS_LEFT_X]);
                GamePad_Left_Stick_Y->SetDecimal(state.axes[GLFW_GAMEPAD_AXIS_LEFT_Y]);
                GamePad_Right_Stick_X->SetDecimal(state.axes[GLFW_GAMEPAD_AXIS_RIGHT_X]);
                GamePad_Right_Stick_Y->SetDecimal(state.axes[GLFW_GAMEPAD_AXIS_RIGHT_Y]);
            }
        }
    };

    inline std::string GetRawName() {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return RawName;
    };

    inline std::string GetGamePadName() {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return GamePadName;
    };

    inline std::string GetGUID() {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return GUID;
    };

    inline bool GetConnected() {
        return Connected;
    };

    inline int GetRawAxisCount() {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return RawAxisCount;
    };

    inline int GetRawButtonCount() {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return RawButtonCount;
    };

    inline int GetRawHatCount() {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return RawHatCount;
    };

    inline float GetRawAxis_Decimal(int AxisID) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }

        Logger->InternalLogDebug(
            20,
            "This function uses raw controller data - we recommend \
you instead use the pre-mapped controller axis for improved compatibility \
with other controller models (as they might have a different axis associated with \
the specified axis ID). If the controller isn't expected to change, or PMMA \
does not include a pre-mapped API for the target axis then this is the recommended \
way to get the axis data.");
        UpdateRawData = true;
        return RawAxesData[AxisID].GetDecimal();
    };

    inline float GetRawAxis_Percentage(int AxisID) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        Logger->InternalLogDebug(
            20,
            "This function uses raw controller data - we recommend \
you instead use the pre-mapped controller axis for improved compatibility \
with other controller models (as they might have a different axis associated with \
the specified axis ID). If the controller isn't expected to change, or PMMA \
does not include a pre-mapped API for the target axis then this is the recommended \
way to get the axis data.");
        UpdateRawData = true;
        return RawAxesData[AxisID].GetPercentage();
    };

    inline bool GetRawButtonPressed(int ButtonID) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        Logger->InternalLogDebug(
            20,
            "This function uses raw controller data - we recommend \
you instead use the pre-mapped controller buttons for improved compatibility \
with other controller models (as they might have a different button associated with \
the specified button ID). If the controller isn't expected to change, or PMMA \
does not include a pre-mapped API for the target button then this is the recommended \
way to get the button data.");
        UpdateRawData = true;
        return RawButtonData[ButtonID];
    };

    inline std::string GetRawHatState(int HatID) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        Logger->InternalLogDebug(
            20,
            "This function uses raw controller data - we recommend \
you instead use the pre-mapped controller hat buttons for improved compatibility \
with other controller models (as they might have a different hat button associated with \
the specified hat button ID). If the controller isn't expected to change, or PMMA \
does not include a pre-mapped API for the target hat button then this is the recommended \
way to get the hat button data.");
        UpdateRawData = true;
        return std::string(RawHatStateData[HatID]);
    };

    inline float AxisDeadZoneConverter_Percentage(float DeadZone, float value) { // DeadZone as percentage, value as percentage
        if (abs(value) <= DeadZone) {
            return 0.0f;
        }

        if (value >= 0) {
            return std::max(0.0f, ((value - DeadZone) / (100 - DeadZone)) * 100);
        }
        return std::min(0.0f, ((value - DeadZone) / (100 + DeadZone)) * 100);
    }

    inline float AxisDeadZoneConverter_Decimal(float DeadZone, float value) { // DeadZone as percentage
        return AxisDeadZoneConverter_Percentage(DeadZone, value * 100) / 100;
    }

    inline float Get_Left_Trigger_Axis_Percentage(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Trigger->GetPercentage());
    }

    inline float Get_Right_Trigger_Axis_Percentage(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Trigger->GetPercentage());
    }

    inline float Get_Left_Trigger_Axis_Decimal(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Trigger->GetDecimal());
    }

    inline float Get_Right_Trigger_Axis_Decimal(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Trigger->GetDecimal());
    }

    inline float Get_Right_Stick_X_Axis_Percentage(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_X->GetPercentage());
    }

    inline float Get_Right_Stick_Y_Axis_Percentage(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_Y->GetPercentage());
    }

    inline float Get_Right_Stick_X_Axis_Decimal(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Stick_X->GetDecimal());
    }

    inline float Get_Right_Stick_Y_Axis_Decimal(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Stick_Y->GetDecimal());
    }

    inline float Get_Left_Stick_X_Axis_Percentage(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_X->GetPercentage());
    }

    inline float Get_Left_Stick_Y_Axis_Percentage(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_Y->GetPercentage());
    }

    inline float Get_Left_Stick_X_Axis_Decimal(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_X->GetDecimal());
    }

    inline float Get_Left_Stick_Y_Axis_Decimal(float DeadZone) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_Y->GetDecimal());
    }

    inline void Get_Left_Stick_Position_Decimal(float DeadZone, float *out) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        out[0] = AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_X->GetDecimal());
        out[1] = AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_Y->GetDecimal());
    }

    inline void Get_Right_Stick_Position_Decimal(float DeadZone, float *out) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        out[0] = GamePad_Right_Stick_X->GetDecimal();
        out[1] = GamePad_Right_Stick_Y->GetDecimal();
    }

    inline void Get_Left_Stick_Position_Percentage(float DeadZone, float *out) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        out[0] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_X->GetPercentage());
        out[1] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_Y->GetPercentage());
    }

    inline void Get_Right_Stick_Position_Percentage(float DeadZone, float *out) {
        if (!Connected) {
            Logger->InternalLogWarn(
                19,
                "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
            throw std::runtime_error("Controller is not connected");
        }
        out[0] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_X->GetPercentage());
        out[1] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_Y->GetPercentage());
    }
};
} // namespace PMMA::Internal::Events