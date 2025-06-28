#include "ControllerEvents.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_ControllerEvent::CPP_ControllerEvent(unsigned int NewID) {
    PMMA::ControllerEventInstanceCount++;
    ID = NewID;
};

CPP_ControllerEvent::~CPP_ControllerEvent() {
    PMMA::ControllerEventInstanceCount--;
};

bool CPP_ControllerEvent::GetConnected() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->GetConnected();
};

bool CPP_ControllerEvent::GetActive() {
    return !(PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false);
};

float CPP_ControllerEvent::GetRawAxis_Decimal(int Axis) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawAxis_Decimal(Axis);
};

float CPP_ControllerEvent::GetRawAxis_Percentage(int Axis) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawAxis_Decimal(Axis);
};

int CPP_ControllerEvent::GetRawAxisCount() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawAxisCount();
};

int CPP_ControllerEvent::GetRawButtonCount() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawButtonCount();
};

int CPP_ControllerEvent::GetRawHatCount() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawHatCount();
};

bool CPP_ControllerEvent::GetRawButtonPressed(int ButtonID) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawButtonPressed(ButtonID);
};

std::string CPP_ControllerEvent::GetRawHatState(int HatID) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return CPP_Constants::HAT_NOT_PRESSED;
    }
    return PMMA::ControllerEventInstances[ID]->GetRawHatState(HatID);
};

std::string CPP_ControllerEvent::GetRawName() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::ControllerEventInstances[ID]->GetRawName();
};

std::string CPP_ControllerEvent::GetGamePadName() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::ControllerEventInstances[ID]->GetGamePadName();
};

std::string CPP_ControllerEvent::GetGUID() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return "";
    }
    return PMMA::ControllerEventInstances[ID]->GetGUID();
};

bool CPP_ControllerEvent::Get_GamePad_A_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_A_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_A_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_A_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_A_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_A_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_A_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_A_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_A_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_A_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_A_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_A_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_A_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_A_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_A_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_A_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_B_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_B_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_B_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_B_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_B_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_B_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_B_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_B_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_B_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_B_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_B_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_B_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_B_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_B_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_B_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_B_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_X_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_X_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_X_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_X_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_X_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_X_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_X_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_X_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_X_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_X_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_X_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_X_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_X_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_X_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_X_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_X_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Y_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Y_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Y_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Y_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Y_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Y_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Y_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Y_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Y_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Y_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Y_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Y_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Y_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Y_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Y_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Y_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Left_Bumper_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Left_Bumper_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Left_Bumper_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Left_Bumper_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Left_Bumper_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Left_Bumper_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Left_Bumper_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Left_Bumper_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Left_Bumper_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Bumper_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Right_Bumper_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Right_Bumper_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Right_Bumper_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Right_Bumper_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Right_Bumper_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Right_Bumper_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Right_Bumper_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Right_Bumper_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Right_Bumper_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Bumper_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Back_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Back_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Back_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Back_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Back_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Back_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Back_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Back_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Back_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Back_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Back_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Back_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Back_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Back_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Back_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Back_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Start_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Start_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Start_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Start_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Start_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Start_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Start_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Start_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Start_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Start_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Start_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Start_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Start_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Start_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Start_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Start_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Guide_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Guide_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Guide_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Guide_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Guide_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Guide_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Guide_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Guide_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Guide_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Guide_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Guide_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Guide_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Guide_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Guide_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Guide_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Guide_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Left_Thumb_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Left_Thumb_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Left_Thumb_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Left_Thumb_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Left_Thumb_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Left_Thumb_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Left_Thumb_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Left_Thumb_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Left_Thumb_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Left_Thumb_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_Right_Thumb_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Right_Thumb_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_Right_Thumb_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Right_Thumb_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_Right_Thumb_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_Right_Thumb_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_Right_Thumb_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_Right_Thumb_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_Right_Thumb_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_Right_Thumb_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Up_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Up_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Up_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Up_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_DPad_Up_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_DPad_Up_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Up_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Up_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Up_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Up_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Right_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Right_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Right_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Right_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_DPad_Right_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_DPad_Right_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Right_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Right_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Right_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Right_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Down_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Down_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Down_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Down_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_DPad_Down_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_DPad_Down_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Down_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Down_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Down_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Down_Button_DoublePressDuration();
};


bool CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_Pressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_Pressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Left_Button_DoublePressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Left_Button_DoublePressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_PressedToggle() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_PressedToggle();
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_DoublePressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_DoublePressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Left_Button_LongPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Left_Button_LongPressDuration(Duration);
};

bool CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_LongPressed();
};

bool CPP_ControllerEvent::Poll_GamePad_DPad_Left_Button_LongPressed() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return false;
    }
    return PMMA::ControllerEventInstances[ID]->Poll_GamePad_DPad_Left_Button_LongPressed();
};

void CPP_ControllerEvent::Set_GamePad_DPad_Left_Button_RepeatPressDuration(float Duration) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return;
    }
    PMMA::ControllerEventInstances[ID]->Set_GamePad_DPad_Left_Button_RepeatPressDuration(Duration);
};

float CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_RepeatPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_RepeatPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_LongPressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_LongPressDuration();
};

float CPP_ControllerEvent::Get_GamePad_DPad_Left_Button_DoublePressDuration() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_GamePad_DPad_Left_Button_DoublePressDuration();
};

float CPP_ControllerEvent::Get_Right_Stick_X_Axis_Percentage() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Right_Stick_X_Axis_Percentage();
};

float CPP_ControllerEvent::Get_Right_Stick_Y_Axis_Percentage() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Right_Stick_Y_Axis_Percentage();
};


float CPP_ControllerEvent::Get_Right_Stick_X_Axis_Decimal() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Right_Stick_X_Axis_Decimal();
};

float CPP_ControllerEvent::Get_Right_Stick_Y_Axis_Decimal() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Right_Stick_Y_Axis_Decimal();
};


float CPP_ControllerEvent::Get_Left_Stick_X_Axis_Percentage() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Left_Stick_X_Axis_Percentage();
};

float CPP_ControllerEvent::Get_Left_Stick_Y_Axis_Percentage() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Left_Stick_Y_Axis_Percentage();
};


float CPP_ControllerEvent::Get_Left_Stick_X_Axis_Decimal() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Left_Stick_X_Axis_Decimal();
};

float CPP_ControllerEvent::Get_Left_Stick_Y_Axis_Decimal() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Left_Stick_Y_Axis_Decimal();
};


float CPP_ControllerEvent::Get_Right_Trigger_Axis_Percentage() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Right_Trigger_Axis_Percentage();
};

float CPP_ControllerEvent::Get_Left_Trigger_Axis_Percentage() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Left_Trigger_Axis_Percentage();
};


float CPP_ControllerEvent::Get_Right_Trigger_Axis_Decimal() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Right_Trigger_Axis_Decimal();
};

float CPP_ControllerEvent::Get_Left_Trigger_Axis_Decimal() {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->Get_Left_Trigger_Axis_Decimal();
};
