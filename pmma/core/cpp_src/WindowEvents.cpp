#include <stdexcept>

#include "WindowEvents.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_DropEvent::CPP_DropEvent() {
    PMMA::DropEventInstanceCount++;
};

CPP_DropEvent::~CPP_DropEvent() {
    PMMA::DropEventInstanceCount--;
};

string CPP_DropEvent::GetFilePath() {
    if (PMMA::DropManagerInstance == nullptr || PMMA::DropManagerInstance->Active == false) {
        return "";
    }
    return PMMA::DropEvent_Instance->GetFilePath();
};

void CPP_DropEvent::ClearFilePath() {
    if (PMMA::DropManagerInstance == nullptr || PMMA::DropManagerInstance->Active == false) {
        return;
    }
    PMMA::DropEvent_Instance->ClearFilePath();
};

bool CPP_DropEvent::GetEnabled() {
    if (PMMA::DropManagerInstance == nullptr || PMMA::DropManagerInstance->Active == false) {
        return false;
    }
    return PMMA::DropEvent_Instance->GetEnabled();
}

void CPP_DropEvent::SetEnabled(bool enabled) {
    if (PMMA::DropManagerInstance == nullptr || PMMA::DropManagerInstance->Active == false) {
        return;
    }
    PMMA::DropEvent_Instance->SetEnabled(enabled);
};