#pragma once
#include "PMMA_Exports.hpp"

#include <vector>
#include <string>

#include "General.hpp"

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/RenderPipelineManager.hpp"
#include "Rendering/RenderPipelineCore.hpp"

#include "Display.hpp"
#include "NumberConverter.hpp"

#include "Events/KeyEvents.hpp"
#include "Events/KeyPadEvents.hpp"
#include "Events/MouseEvents.hpp"
#include "Events/WindowEvents.hpp"
#include "Events/ControllerEvents.hpp"

#include "Events/InternalEventsManager.hpp"

/*
Notes:
    > Internal events MUST have a default 'safe value' to return before the event manager is initialized.
*/

namespace PMMA {
    EXPORT extern CPP_Display* DisplayInstance;

    EXPORT extern CPP_RenderPipelineCore* RenderPipelineCore;

    EXPORT extern std::vector<CPP_KeyEvent_Space*> KeyEvent_Space_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Apostrophe*> KeyEvent_Apostrophe_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Comma*> KeyEvent_Comma_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Minus*> KeyEvent_Minus_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Period*> KeyEvent_Period_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Slash*> KeyEvent_Slash_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_0*> KeyEvent_0_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_1*> KeyEvent_1_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_2*> KeyEvent_2_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_3*> KeyEvent_3_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_4*> KeyEvent_4_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_5*> KeyEvent_5_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_6*> KeyEvent_6_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_7*> KeyEvent_7_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_8*> KeyEvent_8_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_9*> KeyEvent_9_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Semicolon*> KeyEvent_Semicolon_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Equal*> KeyEvent_Equal_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_A*> KeyEvent_A_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_B*> KeyEvent_B_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_C*> KeyEvent_C_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_D*> KeyEvent_D_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_E*> KeyEvent_E_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F*> KeyEvent_F_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_G*> KeyEvent_G_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_H*> KeyEvent_H_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_I*> KeyEvent_I_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_J*> KeyEvent_J_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_K*> KeyEvent_K_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_L*> KeyEvent_L_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_M*> KeyEvent_M_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_N*> KeyEvent_N_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_O*> KeyEvent_O_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_P*> KeyEvent_P_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Q*> KeyEvent_Q_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_R*> KeyEvent_R_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_S*> KeyEvent_S_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_T*> KeyEvent_T_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_U*> KeyEvent_U_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_V*> KeyEvent_V_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_W*> KeyEvent_W_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_X*> KeyEvent_X_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Y*> KeyEvent_Y_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Z*> KeyEvent_Z_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Left_Bracket*> KeyEvent_Left_Bracket_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Backslash*> KeyEvent_Backslash_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Right_Bracket*> KeyEvent_Right_Bracket_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Grave_Accent*> KeyEvent_Grave_Accent_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_World_1*> KeyEvent_World_1_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_World_2*> KeyEvent_World_2_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Escape*> KeyEvent_Escape_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Enter*> KeyEvent_Enter_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Tab*> KeyEvent_Tab_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Backspace*> KeyEvent_Backspace_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Insert*> KeyEvent_Insert_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Delete*> KeyEvent_Delete_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Right*> KeyEvent_Right_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Left*> KeyEvent_Left_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Down*> KeyEvent_Down_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Up*> KeyEvent_Up_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Page_Up*> KeyEvent_Page_Up_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Page_Down*> KeyEvent_Page_Down_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Home*> KeyEvent_Home_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_End*> KeyEvent_End_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Caps_Lock*> KeyEvent_Caps_Lock_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Scroll_Lock*> KeyEvent_Scroll_Lock_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Num_Lock*> KeyEvent_Num_Lock_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Print_Screen*> KeyEvent_Print_Screen_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Pause*> KeyEvent_Pause_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F1*> KeyEvent_F1_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F2*> KeyEvent_F2_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F3*> KeyEvent_F3_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F4*> KeyEvent_F4_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F5*> KeyEvent_F5_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F6*> KeyEvent_F6_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F7*> KeyEvent_F7_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F8*> KeyEvent_F8_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F9*> KeyEvent_F9_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F10*> KeyEvent_F10_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F11*> KeyEvent_F11_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F12*> KeyEvent_F12_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F13*> KeyEvent_F13_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F14*> KeyEvent_F14_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F15*> KeyEvent_F15_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F16*> KeyEvent_F16_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F17*> KeyEvent_F17_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F18*> KeyEvent_F18_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F19*> KeyEvent_F19_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F20*> KeyEvent_F20_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F21*> KeyEvent_F21_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F22*> KeyEvent_F22_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F23*> KeyEvent_F23_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F24*> KeyEvent_F24_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_F25*> KeyEvent_F25_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Left_Shift*> KeyEvent_Left_Shift_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Left_Control*> KeyEvent_Left_Control_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Left_Alt*> KeyEvent_Left_Alt_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Left_Super*> KeyEvent_Left_Super_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Right_Shift*> KeyEvent_Right_Shift_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Right_Control*> KeyEvent_Right_Control_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Right_Alt*> KeyEvent_Right_Alt_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Right_Super*> KeyEvent_Right_Super_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Shift*> KeyEvent_Shift_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Control*> KeyEvent_Control_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Alt*> KeyEvent_Alt_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Super*> KeyEvent_Super_Instances;
    EXPORT extern std::vector<CPP_KeyEvent_Menu*> KeyEvent_Menu_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_0*> KeyPadEvent_0_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_1*> KeyPadEvent_1_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_2*> KeyPadEvent_2_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_3*> KeyPadEvent_3_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_4*> KeyPadEvent_4_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_5*> KeyPadEvent_5_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_6*> KeyPadEvent_6_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_7*> KeyPadEvent_7_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_8*> KeyPadEvent_8_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_9*> KeyPadEvent_9_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Decimal*> KeyPadEvent_Decimal_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Divide*> KeyPadEvent_Divide_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Multiply*> KeyPadEvent_Multiply_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Subtract*> KeyPadEvent_Subtract_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Add*> KeyPadEvent_Add_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Enter*> KeyPadEvent_Enter_Instances;
    EXPORT extern std::vector<CPP_KeyPadEvent_Equal*> KeyPadEvent_Equal_Instances;

    EXPORT extern std::vector<CPP_TextEvent*> TextEventInstances;

    EXPORT extern std::vector<CPP_MousePositionEvent*> MousePositionEvent_Instances;
    EXPORT extern std::vector<CPP_MouseEnterWindowEvent*> MouseEnterWindowEvent_Instances;

    EXPORT extern std::vector<CPP_MouseButtonEvent_Left*> MouseButtonEvent_Left_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_Right*> MouseButtonEvent_Right_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_Middle*> MouseButtonEvent_Middle_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_0*> MouseButtonEvent_0_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_1*> MouseButtonEvent_1_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_2*> MouseButtonEvent_2_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_3*> MouseButtonEvent_3_Instances;
    EXPORT extern std::vector<CPP_MouseButtonEvent_4*> MouseButtonEvent_4_Instances;

    EXPORT extern std::vector<CPP_MouseScrollEvent*> MouseScrollEventInstances;

    EXPORT extern std::vector<CPP_InternalControllerEvent*> InternalControllerEventInstances;
    EXPORT extern std::vector<CPP_ControllerEvent*> ControllerEvent_Instances;

    EXPORT extern std::vector<CPP_DropEvent*> DropEvent_Instances;

    EXPORT extern CPP_InternalKeyEventManager* KeyManagerInstance;
    EXPORT extern CPP_InternalTextEventManager* TextManagerInstance;
    EXPORT extern CPP_InternalMousePositionEventManager* MousePositionManagerInstance;
    EXPORT extern CPP_InternalMouseEnterWindowEventManager* MouseEnterWindowManagerInstance;
    EXPORT extern CPP_InternalMouseButtonEventManager* MouseButtonManagerInstance;
    EXPORT extern CPP_InternalMouseScrollEventManager* MouseScrollManagerInstance;
    EXPORT extern CPP_InternalControllerEventManager* ControllerManagerInstance;
    EXPORT extern CPP_InternalDropEventManager* DropManagerInstance;

    EXPORT extern std::string PMMA_Location;
    EXPORT extern std::string PathSeparator;

    EXPORT extern unsigned int KeyboardEventInstanceCount;
    EXPORT extern unsigned int TextEventInstanceCount;
    EXPORT extern unsigned int MousePositionEventInstanceCount;
    EXPORT extern unsigned int MouseEnterWindowEventInstanceCount;
    EXPORT extern unsigned int MouseButtonEventInstanceCount;
    EXPORT extern unsigned int MouseScrollEventInstanceCount;
    EXPORT extern unsigned int ControllerEventInstanceCount;
    EXPORT extern unsigned int DropEventInstanceCount;

    EXPORT extern bool GLFW_Initialized;

    EXPORT extern int GLFW_References;
}

#include "AdvancedMathematics.hpp"
#include "FractalBrownianMotion.hpp"
#include "PerlinNoise.hpp"
#include "OpenGL.hpp"
#include "Rendering/TextRenderer.hpp"