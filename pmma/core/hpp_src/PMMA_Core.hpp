#pragma once
#include "PMMA_Exports.hpp"

#include <vector>

#include "Display.hpp"
#include "NumberConverter.hpp"

#include "InternalEvents.hpp"
#include "Events.hpp"

namespace PMMA {
    EXPORT extern CPP_Display* DisplayInstance;

    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Space_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Apostrophe_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Comma_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Minus_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Period_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Slash_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_0_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_1_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_2_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_3_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_4_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_5_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_6_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_7_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_8_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_9_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Semicolon_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Equal_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_A_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_B_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_C_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_D_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_E_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_G_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_H_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_I_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_J_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_K_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_L_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_M_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_N_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_O_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_P_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Q_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_R_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_S_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_T_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_U_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_V_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_W_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_X_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Y_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Z_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Left_Bracket_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Backslash_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Right_Bracket_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Grave_Accent_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_World_1_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_World_2_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Escape_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Enter_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Tab_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Backspace_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Insert_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Delete_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Right_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Left_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Down_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Up_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Page_Up_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Page_Down_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Home_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_End_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Caps_Lock_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Scroll_Lock_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Num_Lock_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Print_Screen_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Pause_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F1_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F2_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F3_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F4_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F5_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F6_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F7_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F8_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F9_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F10_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F11_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F12_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F13_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F14_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F15_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F16_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F17_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F18_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F19_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F20_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F21_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F22_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F23_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F24_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_F25_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_0_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_1_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_2_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_3_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_4_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_5_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_6_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_7_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_8_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_9_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Decimal_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Divide_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Multiply_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Subtract_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Add_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Enter_Instance;
    EXPORT extern CPP_InternalKeyPadEvent* KeyPadEvent_Equal_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Left_Shift_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Left_Control_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Left_Alt_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Left_Super_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Right_Shift_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Right_Control_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Right_Alt_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Right_Super_Instance;
    EXPORT extern CPP_InternalKeyEvent* KeyEvent_Menu_Instance;

    EXPORT extern std::vector<CPP_TextEvent*> TextEventInstances;

    EXPORT extern CPP_InternalMousePositionEvent* MousePositionEvent_Instance;
    EXPORT extern CPP_InternalMouseEnterWindowEvent* MouseEnterWindowEvent_Instance;

    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_Left_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_Right_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_Middle_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_0_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_1_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_2_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_3_Instance;
    EXPORT extern CPP_InternalMouseButtonEvent* MouseButtonEvent_4_Instance;

    EXPORT extern std::vector<CPP_MouseScrollEvent*> MouseScrollEventInstances;

    EXPORT extern std::vector<CPP_ControllerEvent*> ControllerEventInstances;

    EXPORT extern bool GLFW_Initialized;

    EXPORT extern int GLFW_References;
}

#include "AdvancedMathematics.hpp"
#include "InternalEventsManager.hpp"
#include "FractalBrownianMotion.hpp"
#include "PerlinNoise.hpp"