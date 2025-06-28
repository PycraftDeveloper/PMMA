#define GLAD_GL_IMPLEMENTATION
#include <glad/gl.h>

#include <vector>

#include "PMMA_Core.hpp"

#include "KeyEvents.hpp"
#include "MouseEvents.hpp"
#include "WindowEvents.hpp"
#include "ControllerEvents.hpp"

using namespace std;

namespace PMMA {
    CPP_Display* DisplayInstance = nullptr;

    vector<CPP_KeyEvent_Space*> KeyEvent_Space_Instances;
    vector<CPP_KeyEvent_Apostrophe*> KeyEvent_Apostrophe_Instances;
    vector<CPP_KeyEvent_Comma*> KeyEvent_Comma_Instances;
    vector<CPP_KeyEvent_Minus*> KeyEvent_Minus_Instances;
    vector<CPP_KeyEvent_Period*> KeyEvent_Period_Instances;
    vector<CPP_KeyEvent_Slash*> KeyEvent_Slash_Instances;
    vector<CPP_KeyEvent_0*> KeyEvent_0_Instances;
    vector<CPP_KeyEvent_1*> KeyEvent_1_Instances;
    vector<CPP_KeyEvent_2*> KeyEvent_2_Instances;
    vector<CPP_KeyEvent_3*> KeyEvent_3_Instances;
    vector<CPP_KeyEvent_4*> KeyEvent_4_Instances;
    vector<CPP_KeyEvent_5*> KeyEvent_5_Instances;
    vector<CPP_KeyEvent_6*> KeyEvent_6_Instances;
    vector<CPP_KeyEvent_7*> KeyEvent_7_Instances;
    vector<CPP_KeyEvent_8*> KeyEvent_8_Instances;
    vector<CPP_KeyEvent_9*> KeyEvent_9_Instances;
    vector<CPP_KeyEvent_Semicolon*> KeyEvent_Semicolon_Instances;
    vector<CPP_KeyEvent_Equal*> KeyEvent_Equal_Instances;
    vector<CPP_KeyEvent_A*> KeyEvent_A_Instances;
    vector<CPP_KeyEvent_B*> KeyEvent_B_Instances;
    vector<CPP_KeyEvent_C*> KeyEvent_C_Instances;
    vector<CPP_KeyEvent_D*> KeyEvent_D_Instances;
    vector<CPP_KeyEvent_E*> KeyEvent_E_Instances;
    vector<CPP_KeyEvent_F*> KeyEvent_F_Instances;
    vector<CPP_KeyEvent_G*> KeyEvent_G_Instances;
    vector<CPP_KeyEvent_H*> KeyEvent_H_Instances;
    vector<CPP_KeyEvent_I*> KeyEvent_I_Instances;
    vector<CPP_KeyEvent_J*> KeyEvent_J_Instances;
    vector<CPP_KeyEvent_K*> KeyEvent_K_Instances;
    vector<CPP_KeyEvent_L*> KeyEvent_L_Instances;
    vector<CPP_KeyEvent_M*> KeyEvent_M_Instances;
    vector<CPP_KeyEvent_N*> KeyEvent_N_Instances;
    vector<CPP_KeyEvent_O*> KeyEvent_O_Instances;
    vector<CPP_KeyEvent_P*> KeyEvent_P_Instances;
    vector<CPP_KeyEvent_Q*> KeyEvent_Q_Instances;
    vector<CPP_KeyEvent_R*> KeyEvent_R_Instances;
    vector<CPP_KeyEvent_S*> KeyEvent_S_Instances;
    vector<CPP_KeyEvent_T*> KeyEvent_T_Instances;
    vector<CPP_KeyEvent_U*> KeyEvent_U_Instances;
    vector<CPP_KeyEvent_V*> KeyEvent_V_Instances;
    vector<CPP_KeyEvent_W*> KeyEvent_W_Instances;
    vector<CPP_KeyEvent_X*> KeyEvent_X_Instances;
    vector<CPP_KeyEvent_Y*> KeyEvent_Y_Instances;
    vector<CPP_KeyEvent_Z*> KeyEvent_Z_Instances;
    vector<CPP_KeyEvent_Left_Bracket*> KeyEvent_Left_Bracket_Instances;
    vector<CPP_KeyEvent_Backslash*> KeyEvent_Backslash_Instances;
    vector<CPP_KeyEvent_Right_Bracket*> KeyEvent_Right_Bracket_Instances;
    vector<CPP_KeyEvent_Grave_Accent*> KeyEvent_Grave_Accent_Instances;
    vector<CPP_KeyEvent_World_1*> KeyEvent_World_1_Instances;
    vector<CPP_KeyEvent_World_2*> KeyEvent_World_2_Instances;
    vector<CPP_KeyEvent_Escape*> KeyEvent_Escape_Instances;
    vector<CPP_KeyEvent_Enter*> KeyEvent_Enter_Instances;
    vector<CPP_KeyEvent_Tab*> KeyEvent_Tab_Instances;
    vector<CPP_KeyEvent_Backspace*> KeyEvent_Backspace_Instances;
    vector<CPP_KeyEvent_Insert*> KeyEvent_Insert_Instances;
    vector<CPP_KeyEvent_Delete*> KeyEvent_Delete_Instances;
    vector<CPP_KeyEvent_Right*> KeyEvent_Right_Instances;
    vector<CPP_KeyEvent_Left*> KeyEvent_Left_Instances;
    vector<CPP_KeyEvent_Down*> KeyEvent_Down_Instances;
    vector<CPP_KeyEvent_Up*> KeyEvent_Up_Instances;
    vector<CPP_KeyEvent_Page_Up*> KeyEvent_Page_Up_Instances;
    vector<CPP_KeyEvent_Page_Down*> KeyEvent_Page_Down_Instances;
    vector<CPP_KeyEvent_Home*> KeyEvent_Home_Instances;
    vector<CPP_KeyEvent_End*> KeyEvent_End_Instances;
    vector<CPP_KeyEvent_Caps_Lock*> KeyEvent_Caps_Lock_Instances;
    vector<CPP_KeyEvent_Scroll_Lock*> KeyEvent_Scroll_Lock_Instances;
    vector<CPP_KeyEvent_Num_Lock*> KeyEvent_Num_Lock_Instances;
    vector<CPP_KeyEvent_Print_Screen*> KeyEvent_Print_Screen_Instances;
    vector<CPP_KeyEvent_Pause*> KeyEvent_Pause_Instances;
    vector<CPP_KeyEvent_F1*> KeyEvent_F1_Instances;
    vector<CPP_KeyEvent_F2*> KeyEvent_F2_Instances;
    vector<CPP_KeyEvent_F3*> KeyEvent_F3_Instances;
    vector<CPP_KeyEvent_F4*> KeyEvent_F4_Instances;
    vector<CPP_KeyEvent_F5*> KeyEvent_F5_Instances;
    vector<CPP_KeyEvent_F6*> KeyEvent_F6_Instances;
    vector<CPP_KeyEvent_F7*> KeyEvent_F7_Instances;
    vector<CPP_KeyEvent_F8*> KeyEvent_F8_Instances;
    vector<CPP_KeyEvent_F9*> KeyEvent_F9_Instances;
    vector<CPP_KeyEvent_F10*> KeyEvent_F10_Instances;
    vector<CPP_KeyEvent_F11*> KeyEvent_F11_Instances;
    vector<CPP_KeyEvent_F12*> KeyEvent_F12_Instances;
    vector<CPP_KeyEvent_F13*> KeyEvent_F13_Instances;
    vector<CPP_KeyEvent_F14*> KeyEvent_F14_Instances;
    vector<CPP_KeyEvent_F15*> KeyEvent_F15_Instances;
    vector<CPP_KeyEvent_F16*> KeyEvent_F16_Instances;
    vector<CPP_KeyEvent_F17*> KeyEvent_F17_Instances;
    vector<CPP_KeyEvent_F18*> KeyEvent_F18_Instances;
    vector<CPP_KeyEvent_F19*> KeyEvent_F19_Instances;
    vector<CPP_KeyEvent_F20*> KeyEvent_F20_Instances;
    vector<CPP_KeyEvent_F21*> KeyEvent_F21_Instances;
    vector<CPP_KeyEvent_F22*> KeyEvent_F22_Instances;
    vector<CPP_KeyEvent_F23*> KeyEvent_F23_Instances;
    vector<CPP_KeyEvent_F24*> KeyEvent_F24_Instances;
    vector<CPP_KeyEvent_F25*> KeyEvent_F25_Instances;
    vector<CPP_KeyEvent_Left_Shift*> KeyEvent_Left_Shift_Instances;
    vector<CPP_KeyEvent_Left_Control*> KeyEvent_Left_Control_Instances;
    vector<CPP_KeyEvent_Left_Alt*> KeyEvent_Left_Alt_Instances;
    vector<CPP_KeyEvent_Left_Super*> KeyEvent_Left_Super_Instances;
    vector<CPP_KeyEvent_Right_Shift*> KeyEvent_Right_Shift_Instances;
    vector<CPP_KeyEvent_Right_Control*> KeyEvent_Right_Control_Instances;
    vector<CPP_KeyEvent_Right_Alt*> KeyEvent_Right_Alt_Instances;
    vector<CPP_KeyEvent_Right_Super*> KeyEvent_Right_Super_Instances;
    vector<CPP_KeyEvent_Shift*> KeyEvent_Shift_Instances;
    vector<CPP_KeyEvent_Control*> KeyEvent_Control_Instances;
    vector<CPP_KeyEvent_Alt*> KeyEvent_Alt_Instances;
    vector<CPP_KeyEvent_Super*> KeyEvent_Super_Instances;
    vector<CPP_KeyEvent_Menu*> KeyEvent_Menu_Instances;
    vector<CPP_KeyPadEvent_0*> KeyPadEvent_0_Instances;
    vector<CPP_KeyPadEvent_1*> KeyPadEvent_1_Instances;
    vector<CPP_KeyPadEvent_2*> KeyPadEvent_2_Instances;
    vector<CPP_KeyPadEvent_3*> KeyPadEvent_3_Instances;
    vector<CPP_KeyPadEvent_4*> KeyPadEvent_4_Instances;
    vector<CPP_KeyPadEvent_5*> KeyPadEvent_5_Instances;
    vector<CPP_KeyPadEvent_6*> KeyPadEvent_6_Instances;
    vector<CPP_KeyPadEvent_7*> KeyPadEvent_7_Instances;
    vector<CPP_KeyPadEvent_8*> KeyPadEvent_8_Instances;
    vector<CPP_KeyPadEvent_9*> KeyPadEvent_9_Instances;
    vector<CPP_KeyPadEvent_Decimal*> KeyPadEvent_Decimal_Instances;
    vector<CPP_KeyPadEvent_Divide*> KeyPadEvent_Divide_Instances;
    vector<CPP_KeyPadEvent_Multiply*> KeyPadEvent_Multiply_Instances;
    vector<CPP_KeyPadEvent_Subtract*> KeyPadEvent_Subtract_Instances;
    vector<CPP_KeyPadEvent_Add*> KeyPadEvent_Add_Instances;
    vector<CPP_KeyPadEvent_Enter*> KeyPadEvent_Enter_Instances;
    vector<CPP_KeyPadEvent_Equal*> KeyPadEvent_Equal_Instances;

    vector<CPP_TextEvent*> TextEventInstances;

    vector<CPP_MousePositionEvent*> MousePositionEvent_Instances;
    vector<CPP_MouseEnterWindowEvent*> MouseEnterWindowEvent_Instances;

    vector<CPP_MouseButtonEvent_Left*> MouseButtonEvent_Left_Instances;
    vector<CPP_MouseButtonEvent_Right*> MouseButtonEvent_Right_Instances;
    vector<CPP_MouseButtonEvent_Middle*> MouseButtonEvent_Middle_Instances;
    vector<CPP_MouseButtonEvent_0*> MouseButtonEvent_0_Instances;
    vector<CPP_MouseButtonEvent_1*> MouseButtonEvent_1_Instances;
    vector<CPP_MouseButtonEvent_2*> MouseButtonEvent_2_Instances;
    vector<CPP_MouseButtonEvent_3*> MouseButtonEvent_3_Instances;
    vector<CPP_MouseButtonEvent_4*> MouseButtonEvent_4_Instances;

    vector<CPP_MouseScrollEvent*> MouseScrollEventInstances;

    vector<CPP_InternalControllerEvent*> ControllerEventInstances;

    vector<CPP_DropEvent*> DropEvent_Instances;

    CPP_InternalKeyEventManager* KeyManagerInstance = nullptr;
    CPP_InternalTextEventManager* TextManagerInstance = nullptr;
    CPP_InternalMousePositionEventManager* MousePositionManagerInstance = nullptr;
    CPP_InternalMouseEnterWindowEventManager* MouseEnterWindowManagerInstance = nullptr;
    CPP_InternalMouseButtonEventManager* MouseButtonManagerInstance = nullptr;
    CPP_InternalMouseScrollEventManager* MouseScrollManagerInstance = nullptr;
    CPP_InternalControllerEventManager* ControllerManagerInstance = nullptr;
    CPP_InternalDropEventManager* DropManagerInstance = nullptr;

    string PMMA_Location = "";
    string PathSeparator = "";

    bool GLFW_Initialized = false;

    int GLFW_References = 0;

    unsigned int KeyboardEventInstanceCount = 0;
    unsigned int TextEventInstanceCount = 0; //
    unsigned int MousePositionEventInstanceCount = 0; //
    unsigned int MouseEnterWindowEventInstanceCount = 0; //
    unsigned int MouseButtonEventInstanceCount = 0; //
    unsigned int MouseScrollEventInstanceCount = 0; //
    unsigned int ControllerEventInstanceCount = 0; //
    unsigned int DropEventInstanceCount = 0; //
}