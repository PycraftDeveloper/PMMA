#include <GLFW/glfw3.h>

#include "PMMA_Core.hpp"

PMMA::Events::Mouse_Button_Left::Mouse_Button_Left() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Left_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_Left::~Mouse_Button_Left() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Left_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Left_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Left_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Left_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_Right::Mouse_Button_Right() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Right_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_Right::~Mouse_Button_Right() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Right_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Right_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Right_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Right_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_Middle::Mouse_Button_Middle() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Middle_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_Middle::~Mouse_Button_Middle() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Middle_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Middle_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Middle_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_Middle_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_0::Mouse_Button_0() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_0_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_0::~Mouse_Button_0() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_0_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_0_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_0_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_0_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_1::Mouse_Button_1() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_1_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_1::~Mouse_Button_1() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_1_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_1_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_1_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_1_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_2::Mouse_Button_2() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_2_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_2::~Mouse_Button_2() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_2_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_2_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_2_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_2_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_3::Mouse_Button_3() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_3_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_3::~Mouse_Button_3() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_3_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_3_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_3_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_3_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_4::Mouse_Button_4() {
    PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_4_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_4::~Mouse_Button_4() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_4_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_4_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_4_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseButtonEvent_4_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Position::Mouse_Position() {
    PMMA::Core::ActiveDisplayInstance->MousePositionEvent_Instances.push_back(this);

    PMMA::Registry::MousePositionEventInstanceCount++;
};

PMMA::Events::Mouse_Position::~Mouse_Position() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MousePositionEvent_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MousePositionEvent_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MousePositionEvent_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MousePositionEvent_Instances.erase(it);
    }

    PMMA::Registry::MousePositionEventInstanceCount--;
};

PMMA::Events::Mouse_EnterWindow::Mouse_EnterWindow() {
    PMMA::Core::ActiveDisplayInstance->MouseEnterWindowEvent_Instances.push_back(this);

    PMMA::Registry::MouseEnterWindowEventInstanceCount++;
};

PMMA::Events::Mouse_EnterWindow::~Mouse_EnterWindow() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseEnterWindowEvent_Instances.begin(), PMMA::Core::ActiveDisplayInstance->MouseEnterWindowEvent_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseEnterWindowEvent_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseEnterWindowEvent_Instances.erase(it);
    }

    PMMA::Registry::MouseEnterWindowEventInstanceCount--;
};

PMMA::Events::Mouse_Scroll::Mouse_Scroll() {
    PMMA::Core::ActiveDisplayInstance->MouseScrollEventInstances.push_back(this);

    PMMA::Registry::MouseScrollEventInstanceCount++;
};

PMMA::Events::Mouse_Scroll::~Mouse_Scroll() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->MouseScrollEventInstances.begin(), PMMA::Core::ActiveDisplayInstance->MouseScrollEventInstances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->MouseScrollEventInstances.end()) {
        PMMA::Core::ActiveDisplayInstance->MouseScrollEventInstances.erase(it);
    }

    PMMA::Registry::MouseScrollEventInstanceCount--;
};