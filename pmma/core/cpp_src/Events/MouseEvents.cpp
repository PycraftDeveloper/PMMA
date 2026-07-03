#include <GLFW/glfw3.h>

#include "PMMA_Core.hpp"

CPP_MouseButtonEvent_Left::CPP_MouseButtonEvent_Left() {
    PMMA::Core::MouseButtonEvent_Left_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_Left::~CPP_MouseButtonEvent_Left() {
    auto it = find(PMMA::Core::MouseButtonEvent_Left_Instances.begin(), PMMA::Core::MouseButtonEvent_Left_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_Left_Instances.end()) {
        PMMA::Core::MouseButtonEvent_Left_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_Right::CPP_MouseButtonEvent_Right() {
    PMMA::Core::MouseButtonEvent_Right_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_Right::~CPP_MouseButtonEvent_Right() {
    auto it = find(PMMA::Core::MouseButtonEvent_Right_Instances.begin(), PMMA::Core::MouseButtonEvent_Right_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_Right_Instances.end()) {
        PMMA::Core::MouseButtonEvent_Right_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_Middle::CPP_MouseButtonEvent_Middle() {
    PMMA::Core::MouseButtonEvent_Middle_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_Middle::~CPP_MouseButtonEvent_Middle() {
    auto it = find(PMMA::Core::MouseButtonEvent_Middle_Instances.begin(), PMMA::Core::MouseButtonEvent_Middle_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_Middle_Instances.end()) {
        PMMA::Core::MouseButtonEvent_Middle_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_0::CPP_MouseButtonEvent_0() {
    PMMA::Core::MouseButtonEvent_0_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_0::~CPP_MouseButtonEvent_0() {
    auto it = find(PMMA::Core::MouseButtonEvent_0_Instances.begin(), PMMA::Core::MouseButtonEvent_0_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_0_Instances.end()) {
        PMMA::Core::MouseButtonEvent_0_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_1::CPP_MouseButtonEvent_1() {
    PMMA::Core::MouseButtonEvent_1_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_1::~CPP_MouseButtonEvent_1() {
    auto it = find(PMMA::Core::MouseButtonEvent_1_Instances.begin(), PMMA::Core::MouseButtonEvent_1_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_1_Instances.end()) {
        PMMA::Core::MouseButtonEvent_1_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_2::CPP_MouseButtonEvent_2() {
    PMMA::Core::MouseButtonEvent_2_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_2::~CPP_MouseButtonEvent_2() {
    auto it = find(PMMA::Core::MouseButtonEvent_2_Instances.begin(), PMMA::Core::MouseButtonEvent_2_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_2_Instances.end()) {
        PMMA::Core::MouseButtonEvent_2_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_3::CPP_MouseButtonEvent_3() {
    PMMA::Core::MouseButtonEvent_3_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_3::~CPP_MouseButtonEvent_3() {
    auto it = find(PMMA::Core::MouseButtonEvent_3_Instances.begin(), PMMA::Core::MouseButtonEvent_3_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_3_Instances.end()) {
        PMMA::Core::MouseButtonEvent_3_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MouseButtonEvent_4::CPP_MouseButtonEvent_4() {
    PMMA::Core::MouseButtonEvent_4_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

CPP_MouseButtonEvent_4::~CPP_MouseButtonEvent_4() {
    auto it = find(PMMA::Core::MouseButtonEvent_4_Instances.begin(), PMMA::Core::MouseButtonEvent_4_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_4_Instances.end()) {
        PMMA::Core::MouseButtonEvent_4_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

CPP_MousePositionEvent::CPP_MousePositionEvent() {
    PMMA::Core::MousePositionEvent_Instances.push_back(this);

    PMMA::Registry::MousePositionEventInstanceCount++;
};

CPP_MousePositionEvent::~CPP_MousePositionEvent() {
    auto it = find(PMMA::Core::MousePositionEvent_Instances.begin(), PMMA::Core::MousePositionEvent_Instances.end(), this);
    if (it != PMMA::Core::MousePositionEvent_Instances.end()) {
        PMMA::Core::MousePositionEvent_Instances.erase(it);
    }

    PMMA::Registry::MousePositionEventInstanceCount--;
};

CPP_MouseEnterWindowEvent::CPP_MouseEnterWindowEvent() {
    PMMA::Core::MouseEnterWindowEvent_Instances.push_back(this);

    PMMA::Registry::MouseEnterWindowEventInstanceCount++;
};

CPP_MouseEnterWindowEvent::~CPP_MouseEnterWindowEvent() {
    auto it = find(PMMA::Core::MouseEnterWindowEvent_Instances.begin(), PMMA::Core::MouseEnterWindowEvent_Instances.end(), this);
    if (it != PMMA::Core::MouseEnterWindowEvent_Instances.end()) {
        PMMA::Core::MouseEnterWindowEvent_Instances.erase(it);
    }

    PMMA::Registry::MouseEnterWindowEventInstanceCount--;
};

CPP_MouseScrollEvent::CPP_MouseScrollEvent() {
    PMMA::Core::MouseScrollEventInstances.push_back(this);

    PMMA::Registry::MouseScrollEventInstanceCount++;
};

CPP_MouseScrollEvent::~CPP_MouseScrollEvent() {
    auto it = find(PMMA::Core::MouseScrollEventInstances.begin(), PMMA::Core::MouseScrollEventInstances.end(), this);
    if (it != PMMA::Core::MouseScrollEventInstances.end()) {
        PMMA::Core::MouseScrollEventInstances.erase(it);
    }

    PMMA::Registry::MouseScrollEventInstanceCount--;
};