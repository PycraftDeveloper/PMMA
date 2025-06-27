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

float CPP_ControllerEvent::GetAxis_Decimal(int Axis) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->GetAxis_Decimal(Axis);
};

float CPP_ControllerEvent::GetAxis_Percentage(int Axis) {
    if (PMMA::ControllerManagerInstance == nullptr || PMMA::ControllerManagerInstance->Active == false) {
        return 0.0f;
    }
    return PMMA::ControllerEventInstances[ID]->GetAxis_Decimal(Axis);
};