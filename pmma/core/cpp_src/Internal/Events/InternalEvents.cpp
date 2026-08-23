#include "Internal/Events/InternalEvents.hpp"

#include "Types.hpp"

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

PMMA::Internal::Events::InternalController::InternalController(unsigned int new_ID) {
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
};

PMMA::Internal::Events::InternalController::~InternalController() {
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

    RawAxesData.clear();
    RawButtonData.clear();
    RawHatStateData.clear();
}

void PMMA::Internal::Events::InternalController::Update() {
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

std::string PMMA::Internal::Events::InternalController::GetRawName() {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return RawName;
};

std::string PMMA::Internal::Events::InternalController::GetGamePadName() {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return GamePadName;
};

std::string PMMA::Internal::Events::InternalController::GetGUID() {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return GUID;
};

int PMMA::Internal::Events::InternalController::GetRawAxisCount() {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return RawAxisCount;
};

int PMMA::Internal::Events::InternalController::GetRawButtonCount() {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return RawButtonCount;
};

int PMMA::Internal::Events::InternalController::GetRawHatCount() {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return RawHatCount;
};

float PMMA::Internal::Events::InternalController::GetRawAxis_Decimal(int AxisID) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }

    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
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

float PMMA::Internal::Events::InternalController::GetRawAxis_Percentage(int AxisID) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
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

bool PMMA::Internal::Events::InternalController::GetRawButtonPressed(int ButtonID) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
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

std::string PMMA::Internal::Events::InternalController::GetRawHatState(int HatID) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
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

float PMMA::Internal::Events::InternalController::Get_Left_Trigger_Axis_Percentage(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Trigger->GetPercentage());
}

float PMMA::Internal::Events::InternalController::Get_Right_Trigger_Axis_Percentage(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Trigger->GetPercentage());
}

float PMMA::Internal::Events::InternalController::Get_Left_Trigger_Axis_Decimal(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Trigger->GetDecimal());
}

float PMMA::Internal::Events::InternalController::Get_Right_Trigger_Axis_Decimal(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Trigger->GetDecimal());
}

float PMMA::Internal::Events::InternalController::Get_Right_Stick_X_Axis_Percentage(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_X->GetPercentage());
}

float PMMA::Internal::Events::InternalController::Get_Right_Stick_Y_Axis_Percentage(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_Y->GetPercentage());
}

float PMMA::Internal::Events::InternalController::Get_Right_Stick_X_Axis_Decimal(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Stick_X->GetDecimal());
}

float PMMA::Internal::Events::InternalController::Get_Right_Stick_Y_Axis_Decimal(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Stick_Y->GetDecimal());
}

float PMMA::Internal::Events::InternalController::Get_Left_Stick_X_Axis_Percentage(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_X->GetPercentage());
}

float PMMA::Internal::Events::InternalController::Get_Left_Stick_Y_Axis_Percentage(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_Y->GetPercentage());
}

float PMMA::Internal::Events::InternalController::Get_Left_Stick_X_Axis_Decimal(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_X->GetDecimal());
}

float PMMA::Internal::Events::InternalController::Get_Left_Stick_Y_Axis_Decimal(float DeadZone) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_Y->GetDecimal());
}

void PMMA::Internal::Events::InternalController::Get_Left_Stick_Position_Decimal(float DeadZone, float *out) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    out[0] = AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_X->GetDecimal());
    out[1] = AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_Y->GetDecimal());
}

void PMMA::Internal::Events::InternalController::Get_Right_Stick_Position_Decimal(float DeadZone, float *out) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    out[0] = GamePad_Right_Stick_X->GetDecimal();
    out[1] = GamePad_Right_Stick_Y->GetDecimal();
}

void PMMA::Internal::Events::InternalController::Get_Left_Stick_Position_Percentage(float DeadZone, float *out) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    out[0] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_X->GetPercentage());
    out[1] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_Y->GetPercentage());
}

void PMMA::Internal::Events::InternalController::Get_Right_Stick_Position_Percentage(float DeadZone, float *out) {
    if (!Connected) {
        PMMA::Core::LoggingManagerInstance->InternalLogWarn(
            19,
            "The controller with ID: " + std::to_string(ID) + " \
is not currently connected. Please ensure this is the ID you are expecting \
and that the controller is connected before calling this function.");
        throw std::runtime_error("Controller is not connected");
    }
    out[0] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_X->GetPercentage());
    out[1] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_Y->GetPercentage());
}