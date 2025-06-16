#include <vector>

#include "PMMA_Core.hpp"

using namespace std;

namespace PMMA {
    CPP_Display* DisplayInstance = nullptr;

    CPP_InternalKeyEvent* KeyEvent_Space_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Apostrophe_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Comma_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Minus_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Period_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Slash_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_0_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_1_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_2_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_3_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_4_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_5_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_6_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_7_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_8_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_9_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Semicolon_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Equal_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_A_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_B_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_C_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_D_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_E_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_G_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_H_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_I_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_J_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_K_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_L_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_M_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_N_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_O_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_P_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Q_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_R_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_S_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_T_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_U_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_V_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_W_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_X_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Y_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Z_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Left_Bracket_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Backslash_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Right_Bracket_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Grave_Accent_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_World_1_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_World_2_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Escape_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Enter_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Tab_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Backspace_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Insert_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Delete_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Right_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Left_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Down_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Up_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Page_Up_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Page_Down_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Home_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_End_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Caps_Lock_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Scroll_Lock_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Num_Lock_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Print_Screen_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Pause_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F1_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F2_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F3_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F4_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F5_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F6_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F7_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F8_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F9_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F10_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F11_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F12_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F13_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F14_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F15_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F16_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F17_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F18_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F19_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F20_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F21_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F22_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F23_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F24_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_F25_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_0_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_1_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_2_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_3_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_4_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_5_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_6_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_7_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_8_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_9_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Decimal_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Divide_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Multiply_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Subtract_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Add_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Enter_Instance = nullptr;
    CPP_InternalKeyPadEvent* KeyPadEvent_Equal_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Left_Shift_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Left_Control_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Left_Alt_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Left_Super_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Right_Shift_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Right_Control_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Right_Alt_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Right_Super_Instance = nullptr;
    CPP_InternalKeyEvent* KeyEvent_Menu_Instance = nullptr;

    vector<CPP_TextEvent*> TextEventInstances;

    CPP_InternalMousePositionEvent* MousePositionEvent_Instance = nullptr;
    CPP_InternalMouseEnterWindowEvent* MouseEnterWindowEvent_Instance = nullptr;

    CPP_InternalMouseButtonEvent* MouseButtonEvent_Left_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_Right_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_Middle_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_0_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_1_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_2_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_3_Instance = nullptr;
    CPP_InternalMouseButtonEvent* MouseButtonEvent_4_Instance = nullptr;

    vector<CPP_MouseScrollEvent*> MouseScrollEventInstances;

    vector<CPP_ControllerEvent*> ControllerEventInstances;

    bool GLFW_Initialized = false;

    int GLFW_References = 0;
}