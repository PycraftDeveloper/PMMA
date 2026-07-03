#include "PMMA_Core.hpp"

CPP_ControllerEvent::CPP_ControllerEvent(unsigned int NewID) {
    PMMA::Core::ControllerEvent_Instances.push_back(this);

    PMMA::Registry::ControllerEventInstanceCount++;
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

CPP_ControllerEvent::~CPP_ControllerEvent() {
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

    PMMA::Registry::ControllerEventInstanceCount--;
};

void CPP_ControllerEvent::Update() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return;
    }
    A_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_A_Button;
    B_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_B_Button;
    X_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_X_Button;
    Y_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Y_Button;
    Left_Bumper_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Left_Bumper_Button;
    Right_Bumper_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Right_Bumper_Button;
    Back_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Back_Button;
    Start_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Start_Button;
    Guide_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Guide_Button;
    Left_Thumb_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Left_Thumb_Button;
    Right_Thumb_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_Right_Thumb_Button;
    DPad_Up_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_DPad_Up_Button;
    DPad_Down_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_DPad_Down_Button;
    DPad_Left_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_DPad_Left_Button;
    DPad_Right_Button = PMMA::Core::InternalControllerEventInstances[ID]->GamePad_DPad_Right_Button;
};

bool CPP_ControllerEvent::GetConnected() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetConnected();
};

bool CPP_ControllerEvent::GetActive() {
    return !(PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false);
};

float CPP_ControllerEvent::GetRawAxis_Decimal(int Axis) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawAxis_Decimal(Axis);
};

float CPP_ControllerEvent::GetRawAxis_Percentage(int Axis) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawAxis_Decimal(Axis);
};

int CPP_ControllerEvent::GetRawAxisCount() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawAxisCount();
};

int CPP_ControllerEvent::GetRawButtonCount() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawButtonCount();
};

int CPP_ControllerEvent::GetRawHatCount() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawHatCount();
};

bool CPP_ControllerEvent::GetRawButtonPressed(int ButtonID) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawButtonPressed(ButtonID);
};

std::string CPP_ControllerEvent::GetRawHatState(int HatID) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return std::string(CPP_Constants::HatStates::NOT_PRESSED);
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawHatState(HatID);
};

std::string CPP_ControllerEvent::GetRawName() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetRawName();
};

std::string CPP_ControllerEvent::GetGamePadName() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetGamePadName();
};

std::string CPP_ControllerEvent::GetGUID() {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->GetGUID();
};

float CPP_ControllerEvent::Get_Right_Stick_X_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Stick_X_Axis_Percentage(DeadZone);
};

float CPP_ControllerEvent::Get_Right_Stick_Y_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Stick_Y_Axis_Percentage(DeadZone);
};

float CPP_ControllerEvent::Get_Right_Stick_X_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Stick_X_Axis_Decimal(DeadZone);
};

float CPP_ControllerEvent::Get_Right_Stick_Y_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Stick_Y_Axis_Decimal(DeadZone);
};

float CPP_ControllerEvent::Get_Left_Stick_X_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Stick_X_Axis_Percentage(DeadZone);
};

float CPP_ControllerEvent::Get_Left_Stick_Y_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Stick_Y_Axis_Percentage(DeadZone);
};

float CPP_ControllerEvent::Get_Left_Stick_X_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Stick_X_Axis_Decimal(DeadZone);
};

float CPP_ControllerEvent::Get_Left_Stick_Y_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Stick_Y_Axis_Decimal(DeadZone);
};

float CPP_ControllerEvent::Get_Right_Trigger_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Trigger_Axis_Percentage(DeadZone);
};

float CPP_ControllerEvent::Get_Left_Trigger_Axis_Percentage(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Trigger_Axis_Percentage(DeadZone);
};

float CPP_ControllerEvent::Get_Right_Trigger_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Trigger_Axis_Decimal(DeadZone);
};

float CPP_ControllerEvent::Get_Left_Trigger_Axis_Decimal(float DeadZone) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Trigger_Axis_Decimal(DeadZone);
};

void CPP_ControllerEvent::Get_Left_Stick_Position_Percentage(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Stick_Position_Percentage(DeadZone, out);
};

void CPP_ControllerEvent::Get_Right_Stick_Position_Percentage(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Stick_Position_Percentage(DeadZone, out);
};

void CPP_ControllerEvent::Get_Left_Stick_Position_Decimal(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::InternalControllerEventInstances[ID]->Get_Left_Stick_Position_Decimal(DeadZone, out);
};

void CPP_ControllerEvent::Get_Right_Stick_Position_Decimal(float DeadZone, float *out) {
    if (PMMA::Core::ControllerManagerInstance == nullptr || PMMA::Core::ControllerManagerInstance->Active == false) {
        out[0] = 0.0f;
        out[1] = 0.0f;
        return;
    }
    PMMA::Core::InternalControllerEventInstances[ID]->Get_Right_Stick_Position_Decimal(DeadZone, out);
};