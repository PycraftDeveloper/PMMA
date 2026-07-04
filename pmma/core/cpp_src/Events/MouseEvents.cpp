#include <GLFW/glfw3.h>

#include "PMMA_Core.hpp"

PMMA::Events::Mouse_Button_Left::Mouse_Button_Left() {
    PMMA::Core::MouseButtonEvent_Left_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_Left::~Mouse_Button_Left() {
    auto it = find(PMMA::Core::MouseButtonEvent_Left_Instances.begin(), PMMA::Core::MouseButtonEvent_Left_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_Left_Instances.end()) {
        PMMA::Core::MouseButtonEvent_Left_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_Right::Mouse_Button_Right() {
    PMMA::Core::MouseButtonEvent_Right_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_Right::~Mouse_Button_Right() {
    auto it = find(PMMA::Core::MouseButtonEvent_Right_Instances.begin(), PMMA::Core::MouseButtonEvent_Right_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_Right_Instances.end()) {
        PMMA::Core::MouseButtonEvent_Right_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_Middle::Mouse_Button_Middle() {
    PMMA::Core::MouseButtonEvent_Middle_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_Middle::~Mouse_Button_Middle() {
    auto it = find(PMMA::Core::MouseButtonEvent_Middle_Instances.begin(), PMMA::Core::MouseButtonEvent_Middle_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_Middle_Instances.end()) {
        PMMA::Core::MouseButtonEvent_Middle_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_0::Mouse_Button_0() {
    PMMA::Core::MouseButtonEvent_0_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_0::~Mouse_Button_0() {
    auto it = find(PMMA::Core::MouseButtonEvent_0_Instances.begin(), PMMA::Core::MouseButtonEvent_0_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_0_Instances.end()) {
        PMMA::Core::MouseButtonEvent_0_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_1::Mouse_Button_1() {
    PMMA::Core::MouseButtonEvent_1_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_1::~Mouse_Button_1() {
    auto it = find(PMMA::Core::MouseButtonEvent_1_Instances.begin(), PMMA::Core::MouseButtonEvent_1_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_1_Instances.end()) {
        PMMA::Core::MouseButtonEvent_1_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_2::Mouse_Button_2() {
    PMMA::Core::MouseButtonEvent_2_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_2::~Mouse_Button_2() {
    auto it = find(PMMA::Core::MouseButtonEvent_2_Instances.begin(), PMMA::Core::MouseButtonEvent_2_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_2_Instances.end()) {
        PMMA::Core::MouseButtonEvent_2_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_3::Mouse_Button_3() {
    PMMA::Core::MouseButtonEvent_3_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_3::~Mouse_Button_3() {
    auto it = find(PMMA::Core::MouseButtonEvent_3_Instances.begin(), PMMA::Core::MouseButtonEvent_3_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_3_Instances.end()) {
        PMMA::Core::MouseButtonEvent_3_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Button_4::Mouse_Button_4() {
    PMMA::Core::MouseButtonEvent_4_Instances.push_back(this);

    PMMA::Registry::MouseButtonEventInstanceCount++;
};

PMMA::Events::Mouse_Button_4::~Mouse_Button_4() {
    auto it = find(PMMA::Core::MouseButtonEvent_4_Instances.begin(), PMMA::Core::MouseButtonEvent_4_Instances.end(), this);
    if (it != PMMA::Core::MouseButtonEvent_4_Instances.end()) {
        PMMA::Core::MouseButtonEvent_4_Instances.erase(it);
    }

    PMMA::Registry::MouseButtonEventInstanceCount--;
};

PMMA::Events::Mouse_Position::Mouse_Position() {
    PMMA::Core::MousePositionEvent_Instances.push_back(this);

    PMMA::Registry::MousePositionEventInstanceCount++;
};

PMMA::Events::Mouse_Position::~Mouse_Position() {
    auto it = find(PMMA::Core::MousePositionEvent_Instances.begin(), PMMA::Core::MousePositionEvent_Instances.end(), this);
    if (it != PMMA::Core::MousePositionEvent_Instances.end()) {
        PMMA::Core::MousePositionEvent_Instances.erase(it);
    }

    PMMA::Registry::MousePositionEventInstanceCount--;
};

PMMA::Events::Mouse_EnterWindow::Mouse_EnterWindow() {
    PMMA::Core::MouseEnterWindowEvent_Instances.push_back(this);

    PMMA::Registry::MouseEnterWindowEventInstanceCount++;
};

PMMA::Events::Mouse_EnterWindow::~Mouse_EnterWindow() {
    auto it = find(PMMA::Core::MouseEnterWindowEvent_Instances.begin(), PMMA::Core::MouseEnterWindowEvent_Instances.end(), this);
    if (it != PMMA::Core::MouseEnterWindowEvent_Instances.end()) {
        PMMA::Core::MouseEnterWindowEvent_Instances.erase(it);
    }

    PMMA::Registry::MouseEnterWindowEventInstanceCount--;
};

PMMA::Events::Mouse_Scroll::Mouse_Scroll() {
    PMMA::Core::MouseScrollEventInstances.push_back(this);

    PMMA::Registry::MouseScrollEventInstanceCount++;
};

PMMA::Events::Mouse_Scroll::~Mouse_Scroll() {
    auto it = find(PMMA::Core::MouseScrollEventInstances.begin(), PMMA::Core::MouseScrollEventInstances.end(), this);
    if (it != PMMA::Core::MouseScrollEventInstances.end()) {
        PMMA::Core::MouseScrollEventInstances.erase(it);
    }

    PMMA::Registry::MouseScrollEventInstanceCount--;
};