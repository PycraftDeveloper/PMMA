#include <iostream>
#include <string>

#include <GLFW/glfw3.h>

#include "InternalEventsManager.hpp"

#include "InternalEvents.hpp"
#include "PMMA_Core.hpp"

using namespace std;

inline string encode_utf8(unsigned int codepoint) {
    string out;
    if (codepoint <= 0x7F) {
        out += static_cast<char>(codepoint);
    } else if (codepoint <= 0x7FF) {
        out += static_cast<char>(0xC0 | ((codepoint >> 6) & 0x1F));
        out += static_cast<char>(0x80 | (codepoint & 0x3F));
    } else if (codepoint <= 0xFFFF) {
        out += static_cast<char>(0xE0 | ((codepoint >> 12) & 0x0F));
        out += static_cast<char>(0x80 | ((codepoint >> 6) & 0x3F));
        out += static_cast<char>(0x80 | (codepoint & 0x3F));
    } else if (codepoint <= 0x10FFFF) {
        out += static_cast<char>(0xF0 | ((codepoint >> 18) & 0x07));
        out += static_cast<char>(0x80 | ((codepoint >> 12) & 0x3F));
        out += static_cast<char>(0x80 | ((codepoint >> 6) & 0x3F));
        out += static_cast<char>(0x80 | (codepoint & 0x3F));
    }
    return out;
}

CPP_EventsManager::CPP_EventsManager(GLFWwindow* Window) {
    PMMA::KeyEvent_Space_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Apostrophe_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Comma_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Minus_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Period_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Slash_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_0_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_1_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_2_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_3_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_4_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_5_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_6_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_7_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_8_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_9_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Semicolon_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Equal_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_A_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_B_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_C_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_D_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_E_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_G_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_H_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_I_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_J_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_K_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_L_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_M_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_N_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_O_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_P_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Q_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_R_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_S_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_T_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_U_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_V_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_W_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_X_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Y_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Z_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Left_Bracket_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Backslash_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Right_Bracket_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Grave_Accent_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_World_1_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_World_2_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Escape_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Enter_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Tab_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Backspace_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Insert_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Delete_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Right_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Left_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Down_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Up_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Page_Up_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Page_Down_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Home_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_End_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Caps_Lock_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Scroll_Lock_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Num_Lock_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Print_Screen_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Pause_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F1_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F2_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F3_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F4_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F5_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F6_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F7_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F8_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F9_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F10_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F11_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F12_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F13_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F14_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F15_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F16_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F17_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F18_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F19_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F20_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F21_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F22_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F23_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F24_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_F25_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyPadEvent_0_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_1_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_2_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_3_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_4_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_5_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_6_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_7_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_8_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_9_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Decimal_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Divide_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Multiply_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Subtract_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Add_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Enter_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyPadEvent_Equal_Instance = new CPP_InternalKeyPadEvent();
    PMMA::KeyEvent_Left_Shift_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Left_Control_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Left_Alt_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Left_Super_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Right_Shift_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Right_Control_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Right_Alt_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Right_Super_Instance = new CPP_InternalKeyEvent();
    PMMA::KeyEvent_Menu_Instance = new CPP_InternalKeyEvent();

    PMMA::MousePositionEvent_Instance = new CPP_InternalMousePositionEvent();
    PMMA::MouseEnterWindowEvent_Instance = new CPP_InternalMouseEnterWindowEvent();

    PMMA::MouseButtonEvent_Left_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_Right_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_Middle_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_0_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_1_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_2_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_3_Instance = new CPP_InternalMouseButtonEvent();
    PMMA::MouseButtonEvent_4_Instance = new CPP_InternalMouseButtonEvent();

    for (unsigned int i = 0; i < 16; i++) {
        PMMA::ControllerEventInstances.emplace_back(new CPP_ControllerEvent(i));
        PMMA::ControllerEventInstances[i]->UpdateConnection(glfwJoystickPresent(i) == GLFW_TRUE);
    }

    glfwSetKeyCallback(Window, CPP_EventsManager::KeyCallback);
    glfwSetCharCallback(Window, CPP_EventsManager::TextCallback);
    glfwSetCursorPosCallback(Window, CPP_EventsManager::CursorPositionCallback);
    glfwSetCursorEnterCallback(Window, CPP_EventsManager::CursorEnterCallback);
    glfwSetMouseButtonCallback(Window, CPP_EventsManager::MouseButtonCallback);
    glfwSetScrollCallback(Window, CPP_EventsManager::ScrollCallback);
    glfwSetJoystickCallback(CPP_EventsManager::JoystickCallback);
    glfwSetDropCallback(Window, CPP_EventsManager::DropCallback);
}

CPP_EventsManager::~CPP_EventsManager() {
    delete PMMA::KeyEvent_Space_Instance;
    delete PMMA::KeyEvent_Apostrophe_Instance;
    delete PMMA::KeyEvent_Comma_Instance;
    delete PMMA::KeyEvent_Minus_Instance;
    delete PMMA::KeyEvent_Period_Instance;
    delete PMMA::KeyEvent_Slash_Instance;
    delete PMMA::KeyEvent_0_Instance;
    delete PMMA::KeyEvent_1_Instance;
    delete PMMA::KeyEvent_2_Instance;
    delete PMMA::KeyEvent_3_Instance;
    delete PMMA::KeyEvent_4_Instance;
    delete PMMA::KeyEvent_5_Instance;
    delete PMMA::KeyEvent_6_Instance;
    delete PMMA::KeyEvent_7_Instance;
    delete PMMA::KeyEvent_8_Instance;
    delete PMMA::KeyEvent_9_Instance;
    delete PMMA::KeyEvent_Semicolon_Instance;
    delete PMMA::KeyEvent_Equal_Instance;
    delete PMMA::KeyEvent_A_Instance;
    delete PMMA::KeyEvent_B_Instance;
    delete PMMA::KeyEvent_C_Instance;
    delete PMMA::KeyEvent_D_Instance;
    delete PMMA::KeyEvent_E_Instance;
    delete PMMA::KeyEvent_F_Instance;
    delete PMMA::KeyEvent_G_Instance;
    delete PMMA::KeyEvent_H_Instance;
    delete PMMA::KeyEvent_I_Instance;
    delete PMMA::KeyEvent_J_Instance;
    delete PMMA::KeyEvent_K_Instance;
    delete PMMA::KeyEvent_L_Instance;
    delete PMMA::KeyEvent_M_Instance;
    delete PMMA::KeyEvent_N_Instance;
    delete PMMA::KeyEvent_O_Instance;
    delete PMMA::KeyEvent_P_Instance;
    delete PMMA::KeyEvent_Q_Instance;
    delete PMMA::KeyEvent_R_Instance;
    delete PMMA::KeyEvent_S_Instance;
    delete PMMA::KeyEvent_T_Instance;
    delete PMMA::KeyEvent_U_Instance;
    delete PMMA::KeyEvent_V_Instance;
    delete PMMA::KeyEvent_W_Instance;
    delete PMMA::KeyEvent_X_Instance;
    delete PMMA::KeyEvent_Y_Instance;
    delete PMMA::KeyEvent_Z_Instance;
    delete PMMA::KeyEvent_Left_Bracket_Instance;
    delete PMMA::KeyEvent_Backslash_Instance;
    delete PMMA::KeyEvent_Right_Bracket_Instance;
    delete PMMA::KeyEvent_Grave_Accent_Instance;
    delete PMMA::KeyEvent_World_1_Instance;
    delete PMMA::KeyEvent_World_2_Instance;
    delete PMMA::KeyEvent_Escape_Instance;
    delete PMMA::KeyEvent_Enter_Instance;
    delete PMMA::KeyEvent_Tab_Instance;
    delete PMMA::KeyEvent_Backspace_Instance;
    delete PMMA::KeyEvent_Insert_Instance;
    delete PMMA::KeyEvent_Delete_Instance;
    delete PMMA::KeyEvent_Right_Instance;
    delete PMMA::KeyEvent_Left_Instance;
    delete PMMA::KeyEvent_Down_Instance;
    delete PMMA::KeyEvent_Up_Instance;
    delete PMMA::KeyEvent_Page_Up_Instance;
    delete PMMA::KeyEvent_Page_Down_Instance;
    delete PMMA::KeyEvent_Home_Instance;
    delete PMMA::KeyEvent_End_Instance;
    delete PMMA::KeyEvent_Caps_Lock_Instance;
    delete PMMA::KeyEvent_Scroll_Lock_Instance;
    delete PMMA::KeyEvent_Num_Lock_Instance;
    delete PMMA::KeyEvent_Print_Screen_Instance;
    delete PMMA::KeyEvent_Pause_Instance;
    delete PMMA::KeyEvent_F1_Instance;
    delete PMMA::KeyEvent_F2_Instance;
    delete PMMA::KeyEvent_F3_Instance;
    delete PMMA::KeyEvent_F4_Instance;
    delete PMMA::KeyEvent_F5_Instance;
    delete PMMA::KeyEvent_F6_Instance;
    delete PMMA::KeyEvent_F7_Instance;
    delete PMMA::KeyEvent_F8_Instance;
    delete PMMA::KeyEvent_F9_Instance;
    delete PMMA::KeyEvent_F10_Instance;
    delete PMMA::KeyEvent_F11_Instance;
    delete PMMA::KeyEvent_F12_Instance;
    delete PMMA::KeyEvent_F13_Instance;
    delete PMMA::KeyEvent_F14_Instance;
    delete PMMA::KeyEvent_F15_Instance;
    delete PMMA::KeyEvent_F16_Instance;
    delete PMMA::KeyEvent_F17_Instance;
    delete PMMA::KeyEvent_F18_Instance;
    delete PMMA::KeyEvent_F19_Instance;
    delete PMMA::KeyEvent_F20_Instance;
    delete PMMA::KeyEvent_F21_Instance;
    delete PMMA::KeyEvent_F22_Instance;
    delete PMMA::KeyEvent_F23_Instance;
    delete PMMA::KeyEvent_F24_Instance;
    delete PMMA::KeyEvent_F25_Instance;
    delete PMMA::KeyPadEvent_0_Instance;
    delete PMMA::KeyPadEvent_1_Instance;
    delete PMMA::KeyPadEvent_2_Instance;
    delete PMMA::KeyPadEvent_3_Instance;
    delete PMMA::KeyPadEvent_4_Instance;
    delete PMMA::KeyPadEvent_5_Instance;
    delete PMMA::KeyPadEvent_6_Instance;
    delete PMMA::KeyPadEvent_7_Instance;
    delete PMMA::KeyPadEvent_8_Instance;
    delete PMMA::KeyPadEvent_9_Instance;
    delete PMMA::KeyPadEvent_Decimal_Instance;
    delete PMMA::KeyPadEvent_Divide_Instance;
    delete PMMA::KeyPadEvent_Multiply_Instance;
    delete PMMA::KeyPadEvent_Subtract_Instance;
    delete PMMA::KeyPadEvent_Add_Instance;
    delete PMMA::KeyPadEvent_Enter_Instance;
    delete PMMA::KeyPadEvent_Equal_Instance;
    delete PMMA::KeyEvent_Left_Shift_Instance;
    delete PMMA::KeyEvent_Left_Control_Instance;
    delete PMMA::KeyEvent_Left_Alt_Instance;
    delete PMMA::KeyEvent_Left_Super_Instance;
    delete PMMA::KeyEvent_Right_Shift_Instance;
    delete PMMA::KeyEvent_Right_Control_Instance;
    delete PMMA::KeyEvent_Right_Alt_Instance;
    delete PMMA::KeyEvent_Right_Super_Instance;
    delete PMMA::KeyEvent_Menu_Instance;

    delete PMMA::MousePositionEvent_Instance;
    delete PMMA::MouseEnterWindowEvent_Instance;

    delete PMMA::MouseButtonEvent_Left_Instance;
    delete PMMA::MouseButtonEvent_Right_Instance;
    delete PMMA::MouseButtonEvent_Middle_Instance;
    delete PMMA::MouseButtonEvent_0_Instance;
    delete PMMA::MouseButtonEvent_1_Instance;
    delete PMMA::MouseButtonEvent_2_Instance;
    delete PMMA::MouseButtonEvent_3_Instance;
    delete PMMA::MouseButtonEvent_4_Instance;

    for (unsigned int i = 0; i < 16; i++) {
        delete PMMA::ControllerEventInstances[i];
    }

    PMMA::KeyEvent_Space_Instance = nullptr;
    PMMA::KeyEvent_Apostrophe_Instance = nullptr;
    PMMA::KeyEvent_Comma_Instance = nullptr;
    PMMA::KeyEvent_Minus_Instance = nullptr;
    PMMA::KeyEvent_Period_Instance = nullptr;
    PMMA::KeyEvent_Slash_Instance = nullptr;
    PMMA::KeyEvent_0_Instance = nullptr;
    PMMA::KeyEvent_1_Instance = nullptr;
    PMMA::KeyEvent_2_Instance = nullptr;
    PMMA::KeyEvent_3_Instance = nullptr;
    PMMA::KeyEvent_4_Instance = nullptr;
    PMMA::KeyEvent_5_Instance = nullptr;
    PMMA::KeyEvent_6_Instance = nullptr;
    PMMA::KeyEvent_7_Instance = nullptr;
    PMMA::KeyEvent_8_Instance = nullptr;
    PMMA::KeyEvent_9_Instance = nullptr;
    PMMA::KeyEvent_Semicolon_Instance = nullptr;
    PMMA::KeyEvent_Equal_Instance = nullptr;
    PMMA::KeyEvent_A_Instance = nullptr;
    PMMA::KeyEvent_B_Instance = nullptr;
    PMMA::KeyEvent_C_Instance = nullptr;
    PMMA::KeyEvent_D_Instance = nullptr;
    PMMA::KeyEvent_E_Instance = nullptr;
    PMMA::KeyEvent_F_Instance = nullptr;
    PMMA::KeyEvent_G_Instance = nullptr;
    PMMA::KeyEvent_H_Instance = nullptr;
    PMMA::KeyEvent_I_Instance = nullptr;
    PMMA::KeyEvent_J_Instance = nullptr;
    PMMA::KeyEvent_K_Instance = nullptr;
    PMMA::KeyEvent_L_Instance = nullptr;
    PMMA::KeyEvent_M_Instance = nullptr;
    PMMA::KeyEvent_N_Instance = nullptr;
    PMMA::KeyEvent_O_Instance = nullptr;
    PMMA::KeyEvent_P_Instance = nullptr;
    PMMA::KeyEvent_Q_Instance = nullptr;
    PMMA::KeyEvent_R_Instance = nullptr;
    PMMA::KeyEvent_S_Instance = nullptr;
    PMMA::KeyEvent_T_Instance = nullptr;
    PMMA::KeyEvent_U_Instance = nullptr;
    PMMA::KeyEvent_V_Instance = nullptr;
    PMMA::KeyEvent_W_Instance = nullptr;
    PMMA::KeyEvent_X_Instance = nullptr;
    PMMA::KeyEvent_Y_Instance = nullptr;
    PMMA::KeyEvent_Z_Instance = nullptr;
    PMMA::KeyEvent_Left_Bracket_Instance = nullptr;
    PMMA::KeyEvent_Backslash_Instance = nullptr;
    PMMA::KeyEvent_Right_Bracket_Instance = nullptr;
    PMMA::KeyEvent_Grave_Accent_Instance = nullptr;
    PMMA::KeyEvent_World_1_Instance = nullptr;
    PMMA::KeyEvent_World_2_Instance = nullptr;
    PMMA::KeyEvent_Escape_Instance = nullptr;
    PMMA::KeyEvent_Enter_Instance = nullptr;
    PMMA::KeyEvent_Tab_Instance = nullptr;
    PMMA::KeyEvent_Backspace_Instance = nullptr;
    PMMA::KeyEvent_Insert_Instance = nullptr;
    PMMA::KeyEvent_Delete_Instance = nullptr;
    PMMA::KeyEvent_Right_Instance = nullptr;
    PMMA::KeyEvent_Left_Instance = nullptr;
    PMMA::KeyEvent_Down_Instance = nullptr;
    PMMA::KeyEvent_Up_Instance = nullptr;
    PMMA::KeyEvent_Page_Up_Instance = nullptr;
    PMMA::KeyEvent_Page_Down_Instance = nullptr;
    PMMA::KeyEvent_Home_Instance = nullptr;
    PMMA::KeyEvent_End_Instance = nullptr;
    PMMA::KeyEvent_Caps_Lock_Instance = nullptr;
    PMMA::KeyEvent_Scroll_Lock_Instance = nullptr;
    PMMA::KeyEvent_Num_Lock_Instance = nullptr;
    PMMA::KeyEvent_Print_Screen_Instance = nullptr;
    PMMA::KeyEvent_Pause_Instance = nullptr;
    PMMA::KeyEvent_F1_Instance = nullptr;
    PMMA::KeyEvent_F2_Instance = nullptr;
    PMMA::KeyEvent_F3_Instance = nullptr;
    PMMA::KeyEvent_F4_Instance = nullptr;
    PMMA::KeyEvent_F5_Instance = nullptr;
    PMMA::KeyEvent_F6_Instance = nullptr;
    PMMA::KeyEvent_F7_Instance = nullptr;
    PMMA::KeyEvent_F8_Instance = nullptr;
    PMMA::KeyEvent_F9_Instance = nullptr;
    PMMA::KeyEvent_F10_Instance = nullptr;
    PMMA::KeyEvent_F11_Instance = nullptr;
    PMMA::KeyEvent_F12_Instance = nullptr;
    PMMA::KeyEvent_F13_Instance = nullptr;
    PMMA::KeyEvent_F14_Instance = nullptr;
    PMMA::KeyEvent_F15_Instance = nullptr;
    PMMA::KeyEvent_F16_Instance = nullptr;
    PMMA::KeyEvent_F17_Instance = nullptr;
    PMMA::KeyEvent_F18_Instance = nullptr;
    PMMA::KeyEvent_F19_Instance = nullptr;
    PMMA::KeyEvent_F20_Instance = nullptr;
    PMMA::KeyEvent_F21_Instance = nullptr;
    PMMA::KeyEvent_F22_Instance = nullptr;
    PMMA::KeyEvent_F23_Instance = nullptr;
    PMMA::KeyEvent_F24_Instance = nullptr;
    PMMA::KeyEvent_F25_Instance = nullptr;
    PMMA::KeyPadEvent_0_Instance = nullptr;
    PMMA::KeyPadEvent_1_Instance = nullptr;
    PMMA::KeyPadEvent_2_Instance = nullptr;
    PMMA::KeyPadEvent_3_Instance = nullptr;
    PMMA::KeyPadEvent_4_Instance = nullptr;
    PMMA::KeyPadEvent_5_Instance = nullptr;
    PMMA::KeyPadEvent_6_Instance = nullptr;
    PMMA::KeyPadEvent_7_Instance = nullptr;
    PMMA::KeyPadEvent_8_Instance = nullptr;
    PMMA::KeyPadEvent_9_Instance = nullptr;
    PMMA::KeyPadEvent_Decimal_Instance = nullptr;
    PMMA::KeyPadEvent_Divide_Instance = nullptr;
    PMMA::KeyPadEvent_Multiply_Instance = nullptr;
    PMMA::KeyPadEvent_Subtract_Instance = nullptr;
    PMMA::KeyPadEvent_Add_Instance = nullptr;
    PMMA::KeyPadEvent_Enter_Instance = nullptr;
    PMMA::KeyPadEvent_Equal_Instance = nullptr;
    PMMA::KeyEvent_Left_Shift_Instance = nullptr;
    PMMA::KeyEvent_Left_Control_Instance = nullptr;
    PMMA::KeyEvent_Left_Alt_Instance = nullptr;
    PMMA::KeyEvent_Left_Super_Instance = nullptr;
    PMMA::KeyEvent_Right_Shift_Instance = nullptr;
    PMMA::KeyEvent_Right_Control_Instance = nullptr;
    PMMA::KeyEvent_Right_Alt_Instance = nullptr;
    PMMA::KeyEvent_Right_Super_Instance = nullptr;
    PMMA::KeyEvent_Menu_Instance = nullptr;

    PMMA::MousePositionEvent_Instance = nullptr;
    PMMA::MouseEnterWindowEvent_Instance = nullptr;

    PMMA::MouseButtonEvent_Left_Instance = nullptr;
    PMMA::MouseButtonEvent_Right_Instance = nullptr;
    PMMA::MouseButtonEvent_Middle_Instance = nullptr;
    PMMA::MouseButtonEvent_0_Instance = nullptr;
    PMMA::MouseButtonEvent_1_Instance = nullptr;
    PMMA::MouseButtonEvent_2_Instance = nullptr;
    PMMA::MouseButtonEvent_3_Instance = nullptr;
    PMMA::MouseButtonEvent_4_Instance = nullptr;

    PMMA::ControllerEventInstances.clear();
}

void CPP_EventsManager::KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    if (key == GLFW_KEY_SPACE) {
        PMMA::KeyEvent_Space_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_APOSTROPHE) {
        PMMA::KeyEvent_Apostrophe_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_COMMA) {
        PMMA::KeyEvent_Comma_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_MINUS) {
        PMMA::KeyEvent_Minus_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_PERIOD) {
        PMMA::KeyEvent_Period_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_SLASH) {
        PMMA::KeyEvent_Slash_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_0) {
        PMMA::KeyEvent_0_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_1) {
        PMMA::KeyEvent_1_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_2) {
        PMMA::KeyEvent_2_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_3) {
        PMMA::KeyEvent_3_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_4) {
        PMMA::KeyEvent_4_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_5) {
        PMMA::KeyEvent_5_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_6) {
        PMMA::KeyEvent_6_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_7) {
        PMMA::KeyEvent_7_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_8) {
        PMMA::KeyEvent_8_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_9) {
        PMMA::KeyEvent_9_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_SEMICOLON) {
        PMMA::KeyEvent_Semicolon_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_EQUAL) {
        PMMA::KeyEvent_Equal_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_A) {
        PMMA::KeyEvent_A_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_B) {
        PMMA::KeyEvent_B_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_C) {
        PMMA::KeyEvent_C_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_D) {
        PMMA::KeyEvent_D_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_E) {
        PMMA::KeyEvent_E_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F) {
        PMMA::KeyEvent_F_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_G) {
        PMMA::KeyEvent_G_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_H) {
        PMMA::KeyEvent_H_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_I) {
        PMMA::KeyEvent_I_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_J) {
        PMMA::KeyEvent_J_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_K) {
        PMMA::KeyEvent_K_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_L) {
        PMMA::KeyEvent_L_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_M) {
        PMMA::KeyEvent_M_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_N) {
        PMMA::KeyEvent_N_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_O) {
        PMMA::KeyEvent_O_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_P) {
        PMMA::KeyEvent_P_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_Q) {
        PMMA::KeyEvent_Q_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_R) {
        PMMA::KeyEvent_R_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_S) {
        PMMA::KeyEvent_S_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_T) {
        PMMA::KeyEvent_T_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_U) {
        PMMA::KeyEvent_U_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_V) {
        PMMA::KeyEvent_V_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_W) {
        PMMA::KeyEvent_W_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_X) {
        PMMA::KeyEvent_X_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_Y) {
        PMMA::KeyEvent_Y_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_Z) {
        PMMA::KeyEvent_Z_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_LEFT_BRACKET) {
        PMMA::KeyEvent_Left_Bracket_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_BACKSLASH) {
        PMMA::KeyEvent_Backslash_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_RIGHT_BRACKET) {
        PMMA::KeyEvent_Right_Bracket_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_GRAVE_ACCENT) {
        PMMA::KeyEvent_Grave_Accent_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_WORLD_1) {
        PMMA::KeyEvent_World_1_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_WORLD_2) {
        PMMA::KeyEvent_World_2_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_ESCAPE) {
        PMMA::KeyEvent_Escape_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_ENTER) {
        PMMA::KeyEvent_Enter_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_TAB) {
        PMMA::KeyEvent_Tab_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_BACKSPACE) {
        PMMA::KeyEvent_Backspace_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_INSERT) {
        PMMA::KeyEvent_Insert_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_DELETE) {
        PMMA::KeyEvent_Delete_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_RIGHT) {
        PMMA::KeyEvent_Right_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_LEFT) {
        PMMA::KeyEvent_Left_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_DOWN) {
        PMMA::KeyEvent_Down_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_UP) {
        PMMA::KeyEvent_Up_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_PAGE_UP) {
        PMMA::KeyEvent_Page_Up_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_PAGE_DOWN) {
        PMMA::KeyEvent_Page_Down_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_HOME) {
        PMMA::KeyEvent_Home_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_END) {
        PMMA::KeyEvent_End_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_CAPS_LOCK) {
        PMMA::KeyEvent_Caps_Lock_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_SCROLL_LOCK) {
        PMMA::KeyEvent_Scroll_Lock_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_NUM_LOCK) {
        PMMA::KeyEvent_Num_Lock_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_PRINT_SCREEN) {
        PMMA::KeyEvent_Print_Screen_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_PAUSE) {
        PMMA::KeyEvent_Pause_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F1) {
        PMMA::KeyEvent_F1_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F2) {
        PMMA::KeyEvent_F2_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F3) {
        PMMA::KeyEvent_F3_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F4) {
        PMMA::KeyEvent_F4_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F5) {
        PMMA::KeyEvent_F5_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F6) {
        PMMA::KeyEvent_F6_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F7) {
        PMMA::KeyEvent_F7_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F8) {
        PMMA::KeyEvent_F8_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F9) {
        PMMA::KeyEvent_F9_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F10) {
        PMMA::KeyEvent_F10_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F11) {
        PMMA::KeyEvent_F11_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F12) {
        PMMA::KeyEvent_F12_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F13) {
        PMMA::KeyEvent_F13_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F14) {
        PMMA::KeyEvent_F14_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F15) {
        PMMA::KeyEvent_F15_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F16) {
        PMMA::KeyEvent_F16_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F17) {
        PMMA::KeyEvent_F17_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F18) {
        PMMA::KeyEvent_F18_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F19) {
        PMMA::KeyEvent_F19_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F20) {
        PMMA::KeyEvent_F20_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F21) {
        PMMA::KeyEvent_F21_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F22) {
        PMMA::KeyEvent_F22_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F23) {
        PMMA::KeyEvent_F23_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F24) {
        PMMA::KeyEvent_F24_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_F25) {
        PMMA::KeyEvent_F25_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_0) {
        PMMA::KeyPadEvent_0_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_1) {
        PMMA::KeyPadEvent_1_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_2) {
        PMMA::KeyPadEvent_2_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_3) {
        PMMA::KeyPadEvent_3_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_4) {
        PMMA::KeyPadEvent_4_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_5) {
        PMMA::KeyPadEvent_5_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_6) {
        PMMA::KeyPadEvent_6_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_7) {
        PMMA::KeyPadEvent_7_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_8) {
        PMMA::KeyPadEvent_8_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_9) {
        PMMA::KeyPadEvent_9_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_DECIMAL) {
        PMMA::KeyPadEvent_Decimal_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_DIVIDE) {
        PMMA::KeyPadEvent_Divide_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_MULTIPLY) {
        PMMA::KeyPadEvent_Multiply_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_SUBTRACT) {
        PMMA::KeyPadEvent_Subtract_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_ADD) {
        PMMA::KeyPadEvent_Add_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_ENTER) {
        PMMA::KeyPadEvent_Enter_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_KP_EQUAL) {
        PMMA::KeyPadEvent_Equal_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_LEFT_SHIFT) {
        PMMA::KeyEvent_Left_Shift_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_LEFT_CONTROL) {
        PMMA::KeyEvent_Left_Control_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_LEFT_ALT) {
        PMMA::KeyEvent_Left_Alt_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_LEFT_SUPER) {
        PMMA::KeyEvent_Left_Super_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_RIGHT_SHIFT) {
        PMMA::KeyEvent_Right_Shift_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_RIGHT_CONTROL) {
        PMMA::KeyEvent_Right_Control_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_RIGHT_ALT) {
        PMMA::KeyEvent_Right_Alt_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_RIGHT_SUPER) {
        PMMA::KeyEvent_Right_Super_Instance->Update(action!=GLFW_RELEASE);
    } else if (key == GLFW_KEY_MENU) {
        PMMA::KeyEvent_Menu_Instance->Update(action!=GLFW_RELEASE);
    } else {
        cout << "Unknown key: " << key << endl;
    }
}

void CPP_EventsManager::TextCallback(GLFWwindow* window, unsigned int codepoint) {
    string NewTextContent = encode_utf8(codepoint);
    for (int i = 0; i < PMMA::TextEventInstances.size(); i++) {
        PMMA::TextEventInstances[i]->Update(NewTextContent);
    }
}

void CPP_EventsManager::CursorPositionCallback(GLFWwindow* window, double xpos, double ypos) {
    PMMA::MousePositionEvent_Instance->Update(xpos, ypos);
}

void CPP_EventsManager::CursorEnterCallback(GLFWwindow* window, int entered) {
    PMMA::MouseEnterWindowEvent_Instance->Update(entered);
}

void CPP_EventsManager::MouseButtonCallback(GLFWwindow* window, int button, int action, int mods) {
    if (button == GLFW_MOUSE_BUTTON_LEFT) {
        PMMA::MouseButtonEvent_Left_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_RIGHT) {
        PMMA::MouseButtonEvent_Right_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_MIDDLE) {
        PMMA::MouseButtonEvent_Middle_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_4) {
        PMMA::MouseButtonEvent_0_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_5) {
        PMMA::MouseButtonEvent_1_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_6) {
        PMMA::MouseButtonEvent_2_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_7) {
        PMMA::MouseButtonEvent_3_Instance->Update(action!=GLFW_RELEASE);
    } else if (button == GLFW_MOUSE_BUTTON_8) {
        PMMA::MouseButtonEvent_4_Instance->Update(action!=GLFW_RELEASE);
    } else {
        cout << "Unknown mouse button: " << button << endl;
    }
}

void CPP_EventsManager::ScrollCallback(GLFWwindow* window, double xoffset, double yoffset) {
    for (int i = 0; i < PMMA::MouseScrollEventInstances.size(); i++) {
        PMMA::MouseScrollEventInstances[i]->Update(xoffset, yoffset);
    }
}

void CPP_EventsManager::JoystickCallback(int jid, int event) {
    PMMA::ControllerEventInstances[jid]->UpdateConnection(event==GLFW_CONNECTED);
}

void CPP_EventsManager::DropCallback(GLFWwindow* window, int count, const char** paths) {

}

void CPP_EventsManager::GenericUpdate(GLFWwindow* window) {
    vector<CPP_TextEvent*> EnabledTextEvents;
    for (int i = 0; i < PMMA::TextEventInstances.size(); i++) {
        if (PMMA::TextEventInstances[i]->GetEnabled()) {
            EnabledTextEvents.push_back(PMMA::TextEventInstances[i]);
        }
    }

    if (EnabledTextEvents.size() > 0) {
        if (PMMA::KeyEvent_Left_Control_Instance->GetPressed() || PMMA::KeyEvent_Right_Control_Instance->GetPressed()) {
            if (PMMA::KeyEvent_V_Instance->PollLongPressed() || PMMA::KeyEvent_V_Instance->GetPressedToggle()) {
                const char* ClipboardData = glfwGetClipboardString(window);
                if (ClipboardData == nullptr) {
                    return;
                }
                std::string NewTextContent = ClipboardData;
                for (int i = 0; i < EnabledTextEvents.size(); i++) {
                    EnabledTextEvents[i]->Update(NewTextContent);
                }
            }
        }

        if (PMMA::KeyEvent_Left_Shift_Instance->GetPressed() || PMMA::KeyEvent_Right_Shift_Instance->GetPressed()) {
            if (PMMA::KeyEvent_Insert_Instance->PollLongPressed() || PMMA::KeyEvent_Insert_Instance->GetPressedToggle()) {
                const char* ClipboardData = glfwGetClipboardString(window);
                if (ClipboardData == nullptr) {
                    return;
                }
                std::string NewTextContent = ClipboardData;
                for (int i = 0; i < EnabledTextEvents.size(); i++) {
                    EnabledTextEvents[i]->Update(NewTextContent);
                }
            }
        }

        if (PMMA::KeyEvent_Backspace_Instance->PollLongPressed() ||
                PMMA::KeyEvent_Backspace_Instance->GetPressedToggle()) {
            for (int i = 0; i < EnabledTextEvents.size(); i++) {
                EnabledTextEvents[i]->RemoveBack();
            }
        }

        if (PMMA::KeyEvent_Delete_Instance->PollLongPressed() ||
                PMMA::KeyEvent_Delete_Instance->GetPressedToggle()) {
            for (int i = 0; i < EnabledTextEvents.size(); i++) {
                EnabledTextEvents[i]->RemoveFront();
            }
        }
    }

    vector<CPP_ControllerEvent*> ConnectedControllers;
    for (int i = 0; i < PMMA::ControllerEventInstances.size(); i++) {
        if (PMMA::ControllerEventInstances[i]->GetConnected()) {
            ConnectedControllers.push_back(PMMA::ControllerEventInstances[i]);
        }
    }

    if (ConnectedControllers.size() > 0) {
        for (int i = 0; i < ConnectedControllers.size(); i++) {
            ConnectedControllers[i]->Update();
        }
    }
}