#include <string>
#include <algorithm>

#include <GLFW/glfw3.h>

#include "Events/MouseEvents.hpp"

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
    PMMA::MousePositionEvent_Instances.push_back(this);

    PMMA::MousePositionEventInstanceCount++;
};

CPP_MousePositionEvent::~CPP_MousePositionEvent() {
    auto it = find(PMMA::MousePositionEvent_Instances.begin(), PMMA::MousePositionEvent_Instances.end(), this);
    if (it != PMMA::MousePositionEvent_Instances.end()) {
        PMMA::MousePositionEvent_Instances.erase(it);
    }

    PMMA::MousePositionEventInstanceCount--;
};

CPP_MouseEnterWindowEvent::CPP_MouseEnterWindowEvent() {
    PMMA::MouseEnterWindowEvent_Instances.push_back(this);

    PMMA::MouseEnterWindowEventInstanceCount++;
};

CPP_MouseEnterWindowEvent::~CPP_MouseEnterWindowEvent() {
    auto it = find(PMMA::MouseEnterWindowEvent_Instances.begin(), PMMA::MouseEnterWindowEvent_Instances.end(), this);
    if (it != PMMA::MouseEnterWindowEvent_Instances.end()) {
        PMMA::MouseEnterWindowEvent_Instances.erase(it);
    }

    PMMA::MouseEnterWindowEventInstanceCount--;
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