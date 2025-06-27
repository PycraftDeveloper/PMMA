#include <string>
#include <algorithm>

#include <GLFW/glfw3.h>

#include "MouseEvents.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_MouseButtonEvent_Left::CPP_MouseButtonEvent_Left() {
    PMMA::MouseButtonEvent_Left_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_Left::~CPP_MouseButtonEvent_Left() {
    auto it = find(PMMA::MouseButtonEvent_Left_Instances.begin(), PMMA::MouseButtonEvent_Left_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_Left_Instances.end()) {
        PMMA::MouseButtonEvent_Left_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_Right::CPP_MouseButtonEvent_Right() {
    PMMA::MouseButtonEvent_Right_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_Right::~CPP_MouseButtonEvent_Right() {
    auto it = find(PMMA::MouseButtonEvent_Right_Instances.begin(), PMMA::MouseButtonEvent_Right_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_Right_Instances.end()) {
        PMMA::MouseButtonEvent_Right_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_Middle::CPP_MouseButtonEvent_Middle() {
    PMMA::MouseButtonEvent_Middle_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_Middle::~CPP_MouseButtonEvent_Middle() {
    auto it = find(PMMA::MouseButtonEvent_Middle_Instances.begin(), PMMA::MouseButtonEvent_Middle_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_Middle_Instances.end()) {
        PMMA::MouseButtonEvent_Middle_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_0::CPP_MouseButtonEvent_0() {
    PMMA::MouseButtonEvent_0_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_0::~CPP_MouseButtonEvent_0() {
    auto it = find(PMMA::MouseButtonEvent_0_Instances.begin(), PMMA::MouseButtonEvent_0_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_0_Instances.end()) {
        PMMA::MouseButtonEvent_0_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_1::CPP_MouseButtonEvent_1() {
    PMMA::MouseButtonEvent_1_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_1::~CPP_MouseButtonEvent_1() {
    auto it = find(PMMA::MouseButtonEvent_1_Instances.begin(), PMMA::MouseButtonEvent_1_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_1_Instances.end()) {
        PMMA::MouseButtonEvent_1_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_2::CPP_MouseButtonEvent_2() {
    PMMA::MouseButtonEvent_2_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_2::~CPP_MouseButtonEvent_2() {
    auto it = find(PMMA::MouseButtonEvent_2_Instances.begin(), PMMA::MouseButtonEvent_2_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_2_Instances.end()) {
        PMMA::MouseButtonEvent_2_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_3::CPP_MouseButtonEvent_3() {
    PMMA::MouseButtonEvent_3_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_3::~CPP_MouseButtonEvent_3() {
    auto it = find(PMMA::MouseButtonEvent_3_Instances.begin(), PMMA::MouseButtonEvent_3_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_3_Instances.end()) {
        PMMA::MouseButtonEvent_3_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_4::CPP_MouseButtonEvent_4() {
    PMMA::MouseButtonEvent_4_Instances.push_back(this);

    PMMA::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_4::~CPP_MouseButtonEvent_4() {
    auto it = find(PMMA::MouseButtonEvent_4_Instances.begin(), PMMA::MouseButtonEvent_4_Instances.end(), this);
    if (it != PMMA::MouseButtonEvent_4_Instances.end()) {
        PMMA::MouseButtonEvent_4_Instances.erase(it);
    }

    PMMA::MouseButtonEventInstanceCount--;
};

CPP_MousePositionEvent::CPP_MousePositionEvent() {
    PMMA::MousePositionEventInstanceCount++;
};

CPP_MousePositionEvent::~CPP_MousePositionEvent() {
    PMMA::MousePositionEventInstanceCount--;
};

void CPP_MousePositionEvent::GetPosition(float* out) {
    if (PMMA::MousePositionManagerInstance == nullptr || PMMA::MousePositionManagerInstance->Active == false) {
        float defaultPosition[2] = {0.0f, 0.0f};
        out[0] = defaultPosition[0];
        out[1] = defaultPosition[1];
    }
    PMMA::MousePositionEvent_Instance->GetPosition(out);
};

void CPP_MousePositionEvent::GetDelta(float* out) {
    if (PMMA::MousePositionManagerInstance == nullptr || PMMA::MousePositionManagerInstance->Active == false) {
        float defaultDelta[2] = {0.0f, 0.0f};
        out[0] = defaultDelta[0];
        out[1] = defaultDelta[1];
    }
    PMMA::MousePositionEvent_Instance->GetDelta(out);
};

void CPP_MousePositionEvent::GetDeltaToggle(float* out) {
    if (PMMA::MousePositionManagerInstance == nullptr || PMMA::MousePositionManagerInstance->Active == false) {
        float defaultToggleDelta[2] = {0.0f, 0.0f};
        out[0] = defaultToggleDelta[0];
        out[1] = defaultToggleDelta[1];
    }
    PMMA::MousePositionEvent_Instance->GetDeltaToggle(out);
};

CPP_MouseEnterWindowEvent::CPP_MouseEnterWindowEvent() {
    PMMA::MouseEnterWindowEventInstanceCount++;
};

CPP_MouseEnterWindowEvent::~CPP_MouseEnterWindowEvent() {
    PMMA::MouseEnterWindowEventInstanceCount--;
};

bool CPP_MouseEnterWindowEvent::GetEntered() {
    if (PMMA::MouseEnterWindowManagerInstance == nullptr || PMMA::MouseEnterWindowManagerInstance->Active == false) {
        return false;
    }
    return PMMA::MouseEnterWindowEvent_Instance->GetEntered();
};

bool CPP_MouseEnterWindowEvent::GetEnteredToggle() {
    if (PMMA::MouseEnterWindowManagerInstance == nullptr || PMMA::MouseEnterWindowManagerInstance->Active == false) {
        return false;
    }
    return PMMA::MouseEnterWindowEvent_Instance->GetEnteredToggle();
};

CPP_MouseScrollEvent::CPP_MouseScrollEvent() {
    PMMA::MouseScrollEventInstances.push_back(this);

    PMMA::MouseScrollEventInstanceCount++;
};

CPP_MouseScrollEvent::~CPP_MouseScrollEvent() {
    auto it = find(PMMA::MouseScrollEventInstances.begin(), PMMA::MouseScrollEventInstances.end(), this);
    if (it != PMMA::MouseScrollEventInstances.end()) {
        PMMA::MouseScrollEventInstances.erase(it);
    }

    PMMA::MouseScrollEventInstanceCount--;
};