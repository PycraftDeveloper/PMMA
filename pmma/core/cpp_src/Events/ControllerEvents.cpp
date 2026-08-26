
#include "Internal/Core/PMMA_Core.hpp"
#include "Internal/Core/PMMA_Registry.hpp"

#include "Internal/Events/EventsManager.hpp"

#include "Events/ControllerEvents.hpp"

PMMA::Events::Controller::Controller(unsigned int NewID) {
    PMMA::Core::ControllerEvent_Instances.push_back(this);

    PMMA::Core::Registry::ControllerEventInstanceCount++;
    ID = NewID;

    PMMA::Core::LoggingManagerInstance->InternalLogDebug(
        8,
        "Please note that when specifying the ID of the controller you \
wish to use it is not guaranteed to remain at that ID when the application \
is restarted. In testing this issue was only present when connecting/disconnecting \
controllers. We instead recommend querying each controller ID and seeing which \
ones are connected instead of relying on the ID to persist for improved \
application reliability.");
};

PMMA::Events::Controller::~Controller() {
    auto it = find(PMMA::Core::ControllerEvent_Instances.begin(), PMMA::Core::ControllerEvent_Instances.end(), this);
    if (it != PMMA::Core::ControllerEvent_Instances.end()) {
        PMMA::Core::ControllerEvent_Instances.erase(it);
    }

    A_Button = nullptr;
    B_Button = nullptr;
    X_Button = nullptr;
    Y_Button = nullptr;
    Left_Bumper_Button = nullptr;
    Right_Bumper_Button = nullptr;
    Back_Button = nullptr;
    Start_Button = nullptr;
    Guide_Button = nullptr;
    Left_Thumb_Button = nullptr;
    Right_Thumb_Button = nullptr;
    DPad_Up_Button = nullptr;
    DPad_Down_Button = nullptr;
    DPad_Left_Button = nullptr;
    DPad_Right_Button = nullptr;

    PMMA::Core::Registry::ControllerEventInstanceCount--;
};

void PMMA::Events::Controller::Update() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return;
    }
    A_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_A_Button;
    B_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_B_Button;
    X_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_X_Button;
    Y_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Y_Button;
    Left_Bumper_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Left_Bumper_Button;
    Right_Bumper_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Right_Bumper_Button;
    Back_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Back_Button;
    Start_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Start_Button;
    Guide_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Guide_Button;
    Left_Thumb_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Left_Thumb_Button;
    Right_Thumb_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_Right_Thumb_Button;
    DPad_Up_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_DPad_Up_Button;
    DPad_Down_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_DPad_Down_Button;
    DPad_Left_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_DPad_Left_Button;
    DPad_Right_Button = PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GamePad_DPad_Right_Button;
};

bool PMMA::Events::Controller::GetConnected() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetConnected();
};

bool PMMA::Events::Controller::GetActive() {
    return !(PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false);
};

float PMMA::Events::Controller::GetRawAxis_Decimal(int Axis) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawAxis_Decimal(Axis);
};

float PMMA::Events::Controller::GetRawAxis_Percentage(int Axis) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawAxis_Decimal(Axis);
};

int PMMA::Events::Controller::GetRawAxisCount() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawAxisCount();
};

int PMMA::Events::Controller::GetRawButtonCount() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawButtonCount();
};

int PMMA::Events::Controller::GetRawHatCount() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawHatCount();
};

bool PMMA::Events::Controller::GetRawButtonPressed(int ButtonID) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawButtonPressed(ButtonID);
};

std::string PMMA::Events::Controller::GetRawHatState(int HatID) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return std::string(PMMA::Constants::HatStates::NOT_PRESSED);
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawHatState(HatID);
};

std::string PMMA::Events::Controller::GetRawName() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetRawName();
};

std::string PMMA::Events::Controller::GetGamePadName() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetGamePadName();
};

std::string PMMA::Events::Controller::GetGUID() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->GetGUID();
};

float PMMA::Events::Controller::Get_Right_Stick_X_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Stick_X_Axis_Percentage(DeadZone);
};

float PMMA::Events::Controller::Get_Right_Stick_Y_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Stick_Y_Axis_Percentage(DeadZone);
};

float PMMA::Events::Controller::Get_Right_Stick_X_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Stick_X_Axis_Decimal(DeadZone);
};

float PMMA::Events::Controller::Get_Right_Stick_Y_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Stick_Y_Axis_Decimal(DeadZone);
};

float PMMA::Events::Controller::Get_Left_Stick_X_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Stick_X_Axis_Percentage(DeadZone);
};

float PMMA::Events::Controller::Get_Left_Stick_Y_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Stick_Y_Axis_Percentage(DeadZone);
};

float PMMA::Events::Controller::Get_Left_Stick_X_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Stick_X_Axis_Decimal(DeadZone);
};

float PMMA::Events::Controller::Get_Left_Stick_Y_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Stick_Y_Axis_Decimal(DeadZone);
};

float PMMA::Events::Controller::Get_Right_Trigger_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Trigger_Axis_Percentage(DeadZone);
};

float PMMA::Events::Controller::Get_Left_Trigger_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Trigger_Axis_Percentage(DeadZone);
};

float PMMA::Events::Controller::Get_Right_Trigger_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Trigger_Axis_Decimal(DeadZone);
};

float PMMA::Events::Controller::Get_Left_Trigger_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Trigger_Axis_Decimal(DeadZone);
};

void PMMA::Events::Controller::Get_Left_Stick_Position_Percentage(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Stick_Position_Percentage(DeadZone, out);
};

void PMMA::Events::Controller::Get_Right_Stick_Position_Percentage(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Stick_Position_Percentage(DeadZone, out);
};

void PMMA::Events::Controller::Get_Left_Stick_Position_Decimal(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Left_Stick_Position_Decimal(DeadZone, out);
};

void PMMA::Events::Controller::Get_Right_Stick_Position_Decimal(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::ActiveDisplayInstance->InternalControllerEventInstances[ID]->Get_Right_Stick_Position_Decimal(DeadZone, out);
};