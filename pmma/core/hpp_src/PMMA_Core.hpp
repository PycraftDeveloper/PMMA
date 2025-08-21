#pragma once

#include <vector>
#include <string>
#include <cstdint>
#include <cmath>
#include <iostream>
#include <stdexcept>
#include <chrono>
#include <thread>
#include <fstream>
#include <sstream>
#include <array>
#include <algorithm>
#include <map>

#include "General.hpp"
#include "InternalManagement.hpp"

#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"
#include "Rendering/Shapes2D/PixelShape.hpp"
#include "Rendering/Shapes2D/PolygonShape.hpp"
#include "Rendering/Shapes2D/LineShape.hpp"
#include "Rendering/Shapes2D/ArcShape.hpp"
#include "Rendering/Shapes2D/EllipseShape.hpp"

#include "Rendering/Shape2DRenderPipelineManager.hpp"
#include "Rendering/TextRendererPipelineManager.hpp"
#include "Rendering/RenderPipelineCore.hpp"

#include "Display.hpp"
#include "NumberConverter.hpp"
#include "NumberFormats.hpp"

#include "Events/KeyEvents.hpp"
#include "Events/KeyPadEvents.hpp"
#include "Events/MouseEvents.hpp"
#include "Events/WindowEvents.hpp"
#include "Events/ControllerEvents.hpp"

#include "Events/InternalEventsManager.hpp"

#include "AdvancedMathematics.hpp"
#include "FractalBrownianMotion.hpp"
#include "PerlinNoise.hpp"
#include "OpenGL.hpp"

#include "Utility/FontUtils.hpp"
#include "Utility/CPU_FeatureSetUtils.hpp"

#include "Passport.hpp"
#include "Logger.hpp"
#include "InternalLogger.hpp"

#include "Animation/AnimationManager.hpp"
#include "Animation/Types/LinearAnimation.hpp"
#include "Animation/Types/RadialAnimation.hpp"

/*
Notes:
    > Internal events MUST have a default 'safe value' to return before the event manager is initialized.
*/

namespace PMMA_Core {
    extern CPP_Display* DisplayInstance;

    extern CPP_RenderPipelineCore* RenderPipelineCore;

    extern std::vector<CPP_KeyEvent_Space*> KeyEvent_Space_Instances;
    extern std::vector<CPP_KeyEvent_Apostrophe*> KeyEvent_Apostrophe_Instances;
    extern std::vector<CPP_KeyEvent_Comma*> KeyEvent_Comma_Instances;
    extern std::vector<CPP_KeyEvent_Minus*> KeyEvent_Minus_Instances;
    extern std::vector<CPP_KeyEvent_Period*> KeyEvent_Period_Instances;
    extern std::vector<CPP_KeyEvent_Slash*> KeyEvent_Slash_Instances;
    extern std::vector<CPP_KeyEvent_0*> KeyEvent_0_Instances;
    extern std::vector<CPP_KeyEvent_1*> KeyEvent_1_Instances;
    extern std::vector<CPP_KeyEvent_2*> KeyEvent_2_Instances;
    extern std::vector<CPP_KeyEvent_3*> KeyEvent_3_Instances;
    extern std::vector<CPP_KeyEvent_4*> KeyEvent_4_Instances;
    extern std::vector<CPP_KeyEvent_5*> KeyEvent_5_Instances;
    extern std::vector<CPP_KeyEvent_6*> KeyEvent_6_Instances;
    extern std::vector<CPP_KeyEvent_7*> KeyEvent_7_Instances;
    extern std::vector<CPP_KeyEvent_8*> KeyEvent_8_Instances;
    extern std::vector<CPP_KeyEvent_9*> KeyEvent_9_Instances;
    extern std::vector<CPP_KeyEvent_Semicolon*> KeyEvent_Semicolon_Instances;
    extern std::vector<CPP_KeyEvent_Equal*> KeyEvent_Equal_Instances;
    extern std::vector<CPP_KeyEvent_A*> KeyEvent_A_Instances;
    extern std::vector<CPP_KeyEvent_B*> KeyEvent_B_Instances;
    extern std::vector<CPP_KeyEvent_C*> KeyEvent_C_Instances;
    extern std::vector<CPP_KeyEvent_D*> KeyEvent_D_Instances;
    extern std::vector<CPP_KeyEvent_E*> KeyEvent_E_Instances;
    extern std::vector<CPP_KeyEvent_F*> KeyEvent_F_Instances;
    extern std::vector<CPP_KeyEvent_G*> KeyEvent_G_Instances;
    extern std::vector<CPP_KeyEvent_H*> KeyEvent_H_Instances;
    extern std::vector<CPP_KeyEvent_I*> KeyEvent_I_Instances;
    extern std::vector<CPP_KeyEvent_J*> KeyEvent_J_Instances;
    extern std::vector<CPP_KeyEvent_K*> KeyEvent_K_Instances;
    extern std::vector<CPP_KeyEvent_L*> KeyEvent_L_Instances;
    extern std::vector<CPP_KeyEvent_M*> KeyEvent_M_Instances;
    extern std::vector<CPP_KeyEvent_N*> KeyEvent_N_Instances;
    extern std::vector<CPP_KeyEvent_O*> KeyEvent_O_Instances;
    extern std::vector<CPP_KeyEvent_P*> KeyEvent_P_Instances;
    extern std::vector<CPP_KeyEvent_Q*> KeyEvent_Q_Instances;
    extern std::vector<CPP_KeyEvent_R*> KeyEvent_R_Instances;
    extern std::vector<CPP_KeyEvent_S*> KeyEvent_S_Instances;
    extern std::vector<CPP_KeyEvent_T*> KeyEvent_T_Instances;
    extern std::vector<CPP_KeyEvent_U*> KeyEvent_U_Instances;
    extern std::vector<CPP_KeyEvent_V*> KeyEvent_V_Instances;
    extern std::vector<CPP_KeyEvent_W*> KeyEvent_W_Instances;
    extern std::vector<CPP_KeyEvent_X*> KeyEvent_X_Instances;
    extern std::vector<CPP_KeyEvent_Y*> KeyEvent_Y_Instances;
    extern std::vector<CPP_KeyEvent_Z*> KeyEvent_Z_Instances;
    extern std::vector<CPP_KeyEvent_Left_Bracket*> KeyEvent_Left_Bracket_Instances;
    extern std::vector<CPP_KeyEvent_Backslash*> KeyEvent_Backslash_Instances;
    extern std::vector<CPP_KeyEvent_Right_Bracket*> KeyEvent_Right_Bracket_Instances;
    extern std::vector<CPP_KeyEvent_Grave_Accent*> KeyEvent_Grave_Accent_Instances;
    extern std::vector<CPP_KeyEvent_World_1*> KeyEvent_World_1_Instances;
    extern std::vector<CPP_KeyEvent_World_2*> KeyEvent_World_2_Instances;
    extern std::vector<CPP_KeyEvent_Escape*> KeyEvent_Escape_Instances;
    extern std::vector<CPP_KeyEvent_Enter*> KeyEvent_Enter_Instances;
    extern std::vector<CPP_KeyEvent_Tab*> KeyEvent_Tab_Instances;
    extern std::vector<CPP_KeyEvent_Backspace*> KeyEvent_Backspace_Instances;
    extern std::vector<CPP_KeyEvent_Insert*> KeyEvent_Insert_Instances;
    extern std::vector<CPP_KeyEvent_Delete*> KeyEvent_Delete_Instances;
    extern std::vector<CPP_KeyEvent_Right*> KeyEvent_Right_Instances;
    extern std::vector<CPP_KeyEvent_Left*> KeyEvent_Left_Instances;
    extern std::vector<CPP_KeyEvent_Down*> KeyEvent_Down_Instances;
    extern std::vector<CPP_KeyEvent_Up*> KeyEvent_Up_Instances;
    extern std::vector<CPP_KeyEvent_Page_Up*> KeyEvent_Page_Up_Instances;
    extern std::vector<CPP_KeyEvent_Page_Down*> KeyEvent_Page_Down_Instances;
    extern std::vector<CPP_KeyEvent_Home*> KeyEvent_Home_Instances;
    extern std::vector<CPP_KeyEvent_End*> KeyEvent_End_Instances;
    extern std::vector<CPP_KeyEvent_Caps_Lock*> KeyEvent_Caps_Lock_Instances;
    extern std::vector<CPP_KeyEvent_Scroll_Lock*> KeyEvent_Scroll_Lock_Instances;
    extern std::vector<CPP_KeyEvent_Num_Lock*> KeyEvent_Num_Lock_Instances;
    extern std::vector<CPP_KeyEvent_Print_Screen*> KeyEvent_Print_Screen_Instances;
    extern std::vector<CPP_KeyEvent_Pause*> KeyEvent_Pause_Instances;
    extern std::vector<CPP_KeyEvent_F1*> KeyEvent_F1_Instances;
    extern std::vector<CPP_KeyEvent_F2*> KeyEvent_F2_Instances;
    extern std::vector<CPP_KeyEvent_F3*> KeyEvent_F3_Instances;
    extern std::vector<CPP_KeyEvent_F4*> KeyEvent_F4_Instances;
    extern std::vector<CPP_KeyEvent_F5*> KeyEvent_F5_Instances;
    extern std::vector<CPP_KeyEvent_F6*> KeyEvent_F6_Instances;
    extern std::vector<CPP_KeyEvent_F7*> KeyEvent_F7_Instances;
    extern std::vector<CPP_KeyEvent_F8*> KeyEvent_F8_Instances;
    extern std::vector<CPP_KeyEvent_F9*> KeyEvent_F9_Instances;
    extern std::vector<CPP_KeyEvent_F10*> KeyEvent_F10_Instances;
    extern std::vector<CPP_KeyEvent_F11*> KeyEvent_F11_Instances;
    extern std::vector<CPP_KeyEvent_F12*> KeyEvent_F12_Instances;
    extern std::vector<CPP_KeyEvent_F13*> KeyEvent_F13_Instances;
    extern std::vector<CPP_KeyEvent_F14*> KeyEvent_F14_Instances;
    extern std::vector<CPP_KeyEvent_F15*> KeyEvent_F15_Instances;
    extern std::vector<CPP_KeyEvent_F16*> KeyEvent_F16_Instances;
    extern std::vector<CPP_KeyEvent_F17*> KeyEvent_F17_Instances;
    extern std::vector<CPP_KeyEvent_F18*> KeyEvent_F18_Instances;
    extern std::vector<CPP_KeyEvent_F19*> KeyEvent_F19_Instances;
    extern std::vector<CPP_KeyEvent_F20*> KeyEvent_F20_Instances;
    extern std::vector<CPP_KeyEvent_F21*> KeyEvent_F21_Instances;
    extern std::vector<CPP_KeyEvent_F22*> KeyEvent_F22_Instances;
    extern std::vector<CPP_KeyEvent_F23*> KeyEvent_F23_Instances;
    extern std::vector<CPP_KeyEvent_F24*> KeyEvent_F24_Instances;
    extern std::vector<CPP_KeyEvent_F25*> KeyEvent_F25_Instances;
    extern std::vector<CPP_KeyEvent_Left_Shift*> KeyEvent_Left_Shift_Instances;
    extern std::vector<CPP_KeyEvent_Left_Control*> KeyEvent_Left_Control_Instances;
    extern std::vector<CPP_KeyEvent_Left_Alt*> KeyEvent_Left_Alt_Instances;
    extern std::vector<CPP_KeyEvent_Left_Super*> KeyEvent_Left_Super_Instances;
    extern std::vector<CPP_KeyEvent_Right_Shift*> KeyEvent_Right_Shift_Instances;
    extern std::vector<CPP_KeyEvent_Right_Control*> KeyEvent_Right_Control_Instances;
    extern std::vector<CPP_KeyEvent_Right_Alt*> KeyEvent_Right_Alt_Instances;
    extern std::vector<CPP_KeyEvent_Right_Super*> KeyEvent_Right_Super_Instances;
    extern std::vector<CPP_KeyEvent_Shift*> KeyEvent_Shift_Instances;
    extern std::vector<CPP_KeyEvent_Control*> KeyEvent_Control_Instances;
    extern std::vector<CPP_KeyEvent_Alt*> KeyEvent_Alt_Instances;
    extern std::vector<CPP_KeyEvent_Super*> KeyEvent_Super_Instances;
    extern std::vector<CPP_KeyEvent_Menu*> KeyEvent_Menu_Instances;
    extern std::vector<CPP_KeyPadEvent_0*> KeyPadEvent_0_Instances;
    extern std::vector<CPP_KeyPadEvent_1*> KeyPadEvent_1_Instances;
    extern std::vector<CPP_KeyPadEvent_2*> KeyPadEvent_2_Instances;
    extern std::vector<CPP_KeyPadEvent_3*> KeyPadEvent_3_Instances;
    extern std::vector<CPP_KeyPadEvent_4*> KeyPadEvent_4_Instances;
    extern std::vector<CPP_KeyPadEvent_5*> KeyPadEvent_5_Instances;
    extern std::vector<CPP_KeyPadEvent_6*> KeyPadEvent_6_Instances;
    extern std::vector<CPP_KeyPadEvent_7*> KeyPadEvent_7_Instances;
    extern std::vector<CPP_KeyPadEvent_8*> KeyPadEvent_8_Instances;
    extern std::vector<CPP_KeyPadEvent_9*> KeyPadEvent_9_Instances;
    extern std::vector<CPP_KeyPadEvent_Decimal*> KeyPadEvent_Decimal_Instances;
    extern std::vector<CPP_KeyPadEvent_Divide*> KeyPadEvent_Divide_Instances;
    extern std::vector<CPP_KeyPadEvent_Multiply*> KeyPadEvent_Multiply_Instances;
    extern std::vector<CPP_KeyPadEvent_Subtract*> KeyPadEvent_Subtract_Instances;
    extern std::vector<CPP_KeyPadEvent_Add*> KeyPadEvent_Add_Instances;
    extern std::vector<CPP_KeyPadEvent_Enter*> KeyPadEvent_Enter_Instances;
    extern std::vector<CPP_KeyPadEvent_Equal*> KeyPadEvent_Equal_Instances;

    extern std::vector<CPP_TextEvent*> TextEventInstances;

    extern std::vector<CPP_MousePositionEvent*> MousePositionEvent_Instances;
    extern std::vector<CPP_MouseEnterWindowEvent*> MouseEnterWindowEvent_Instances;

    extern std::vector<CPP_MouseButtonEvent_Left*> MouseButtonEvent_Left_Instances;
    extern std::vector<CPP_MouseButtonEvent_Right*> MouseButtonEvent_Right_Instances;
    extern std::vector<CPP_MouseButtonEvent_Middle*> MouseButtonEvent_Middle_Instances;
    extern std::vector<CPP_MouseButtonEvent_0*> MouseButtonEvent_0_Instances;
    extern std::vector<CPP_MouseButtonEvent_1*> MouseButtonEvent_1_Instances;
    extern std::vector<CPP_MouseButtonEvent_2*> MouseButtonEvent_2_Instances;
    extern std::vector<CPP_MouseButtonEvent_3*> MouseButtonEvent_3_Instances;
    extern std::vector<CPP_MouseButtonEvent_4*> MouseButtonEvent_4_Instances;

    extern std::vector<CPP_MouseScrollEvent*> MouseScrollEventInstances;

    extern std::vector<CPP_InternalControllerEvent*> InternalControllerEventInstances;
    extern std::vector<CPP_ControllerEvent*> ControllerEvent_Instances;

    extern std::vector<CPP_DropEvent*> DropEvent_Instances;

    extern CPP_InternalKeyEventManager* KeyManagerInstance;
    extern CPP_InternalTextEventManager* TextManagerInstance;
    extern CPP_InternalMousePositionEventManager* MousePositionManagerInstance;
    extern CPP_InternalMouseEnterWindowEventManager* MouseEnterWindowManagerInstance;
    extern CPP_InternalMouseButtonEventManager* MouseButtonManagerInstance;
    extern CPP_InternalMouseScrollEventManager* MouseScrollManagerInstance;
    extern CPP_InternalControllerEventManager* ControllerManagerInstance;
    extern CPP_InternalDropEventManager* DropManagerInstance;

    extern CPP_Passport* PassportInstance;
    extern CPP_InternalLogger* InternalLoggerInstance;

    extern PowerSavingManager PowerSavingManagerInstance;

    extern CPP_AnimationManager* AnimationManagerInstance;
}

namespace PMMA_Registry {
    extern std::string PMMA_Location;
    extern std::string PathSeparator;
    extern std::string Current_PMMA_Version;
    extern std::string Latest_PMMA_Version;
    extern std::string Locale;

    extern std::chrono::high_resolution_clock::time_point StartupTime;

    extern uint64_t ClassObject_ID_System;

    extern unsigned int KeyboardEventInstanceCount;
    extern unsigned int TextEventInstanceCount;
    extern unsigned int MousePositionEventInstanceCount;
    extern unsigned int MouseEnterWindowEventInstanceCount;
    extern unsigned int MouseButtonEventInstanceCount;
    extern unsigned int MouseScrollEventInstanceCount;
    extern unsigned int ControllerEventInstanceCount;
    extern unsigned int DropEventInstanceCount;

    extern float CurrentShapeQuality;

    extern int GLFW_References;

    extern bool GLFW_Initialized;
    extern bool CPU_Supports_AVX2;
    extern bool CPU_Supports_AVX512;
    extern bool IsPowerSavingModeEnabled;
    extern bool IsDebuggingModeEnabled;
    extern bool IsApplicationRunning;
    extern bool EscapeKeyShouldCloseWindow;
    extern bool UserSetEscapeKeyShouldCloseWindow;
    extern bool F11KeyShouldToggleFullScreen;
    extern bool UserDefinedShapeQuality;
}

EXPORT void PMMA_Initialize();

EXPORT void PMMA_Uninitialize();