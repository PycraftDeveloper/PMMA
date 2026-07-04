#pragma once

#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

#include "Animation/LinearAnimation.hpp"
#include "Animation/RadialAnimation.hpp"

#include "Events/ControllerEvents.hpp"
#include "Events/KeyEvents.hpp"
#include "Events/KeyPadEvents.hpp"
#include "Events/MouseEvents.hpp"
#include "Events/WindowEvents.hpp"

#include "Graphics/Shader.hpp"

#include "Internal/AnimationManager.hpp"
#include "Internal/InternalManager.hpp"
#include "Internal/LoggingManager.hpp"

#include "Internal/Events/EventsManager.hpp"

#include "Internal/Rendering/Core2D/RenderPipelineManager.hpp"

#include "Internal/Utility/CPU_FeatureSetUtils.hpp"
#include "Internal/Utility/FontUtils.hpp"

#include "Rendering/Shapes2D/ArcShape.hpp"
#include "Rendering/Shapes2D/EllipseShape.hpp"
#include "Rendering/Shapes2D/LineShape.hpp"
#include "Rendering/Shapes2D/PixelShape.hpp"
#include "Rendering/Shapes2D/PolygonShape.hpp"
#include "Rendering/Shapes2D/RadialPolygonShape.hpp"
#include "Rendering/Shapes2D/RectangleShape.hpp"

#include "Rendering/TextRenderer.hpp"

#include "Constants.hpp"
#include "Display.hpp"
#include "FractalBrownianMotion.hpp"
#include "General.hpp"
#include "Logger.hpp"
#include "Maths.hpp"
#include "Passport.hpp"
#include "PerlinNoise.hpp"
#include "Random.hpp"
#include "Types.hpp"

/*
Notes:
    > Internal events MUST have a default 'safe value' to return before the event manager is initialized.
*/

namespace PMMA::Core {
extern PMMA::Display *ActiveDisplayInstance;
extern PMMA::Display *MasterDisplayInstance;

extern std::vector<PMMA::Events::Key_Space *> KeyEvent_Space_Instances;
extern std::vector<PMMA::Events::Key_Apostrophe *> KeyEvent_Apostrophe_Instances;
extern std::vector<PMMA::Events::Key_Comma *> KeyEvent_Comma_Instances;
extern std::vector<PMMA::Events::Key_Minus *> KeyEvent_Minus_Instances;
extern std::vector<PMMA::Events::Key_Period *> KeyEvent_Period_Instances;
extern std::vector<PMMA::Events::Key_Slash *> KeyEvent_Slash_Instances;
extern std::vector<PMMA::Events::Key_0 *> KeyEvent_0_Instances;
extern std::vector<PMMA::Events::Key_1 *> KeyEvent_1_Instances;
extern std::vector<PMMA::Events::Key_2 *> KeyEvent_2_Instances;
extern std::vector<PMMA::Events::Key_3 *> KeyEvent_3_Instances;
extern std::vector<PMMA::Events::Key_4 *> KeyEvent_4_Instances;
extern std::vector<PMMA::Events::Key_5 *> KeyEvent_5_Instances;
extern std::vector<PMMA::Events::Key_6 *> KeyEvent_6_Instances;
extern std::vector<PMMA::Events::Key_7 *> KeyEvent_7_Instances;
extern std::vector<PMMA::Events::Key_8 *> KeyEvent_8_Instances;
extern std::vector<PMMA::Events::Key_9 *> KeyEvent_9_Instances;
extern std::vector<PMMA::Events::Key_Semicolon *> KeyEvent_Semicolon_Instances;
extern std::vector<PMMA::Events::Key_Equal *> KeyEvent_Equal_Instances;
extern std::vector<PMMA::Events::Key_A *> KeyEvent_A_Instances;
extern std::vector<PMMA::Events::Key_B *> KeyEvent_B_Instances;
extern std::vector<PMMA::Events::Key_C *> KeyEvent_C_Instances;
extern std::vector<PMMA::Events::Key_D *> KeyEvent_D_Instances;
extern std::vector<PMMA::Events::Key_E *> KeyEvent_E_Instances;
extern std::vector<PMMA::Events::Key_F *> KeyEvent_F_Instances;
extern std::vector<PMMA::Events::Key_G *> KeyEvent_G_Instances;
extern std::vector<PMMA::Events::Key_H *> KeyEvent_H_Instances;
extern std::vector<PMMA::Events::Key_I *> KeyEvent_I_Instances;
extern std::vector<PMMA::Events::Key_J *> KeyEvent_J_Instances;
extern std::vector<PMMA::Events::Key_K *> KeyEvent_K_Instances;
extern std::vector<PMMA::Events::Key_L *> KeyEvent_L_Instances;
extern std::vector<PMMA::Events::Key_M *> KeyEvent_M_Instances;
extern std::vector<PMMA::Events::Key_N *> KeyEvent_N_Instances;
extern std::vector<PMMA::Events::Key_O *> KeyEvent_O_Instances;
extern std::vector<PMMA::Events::Key_P *> KeyEvent_P_Instances;
extern std::vector<PMMA::Events::Key_Q *> KeyEvent_Q_Instances;
extern std::vector<PMMA::Events::Key_R *> KeyEvent_R_Instances;
extern std::vector<PMMA::Events::Key_S *> KeyEvent_S_Instances;
extern std::vector<PMMA::Events::Key_T *> KeyEvent_T_Instances;
extern std::vector<PMMA::Events::Key_U *> KeyEvent_U_Instances;
extern std::vector<PMMA::Events::Key_V *> KeyEvent_V_Instances;
extern std::vector<PMMA::Events::Key_W *> KeyEvent_W_Instances;
extern std::vector<PMMA::Events::Key_X *> KeyEvent_X_Instances;
extern std::vector<PMMA::Events::Key_Y *> KeyEvent_Y_Instances;
extern std::vector<PMMA::Events::Key_Z *> KeyEvent_Z_Instances;
extern std::vector<PMMA::Events::Key_Left_Bracket *> KeyEvent_Left_Bracket_Instances;
extern std::vector<PMMA::Events::Key_Backslash *> KeyEvent_Backslash_Instances;
extern std::vector<PMMA::Events::Key_Right_Bracket *> KeyEvent_Right_Bracket_Instances;
extern std::vector<PMMA::Events::Key_Grave_Accent *> KeyEvent_Grave_Accent_Instances;
extern std::vector<PMMA::Events::Key_World_1 *> KeyEvent_World_1_Instances;
extern std::vector<PMMA::Events::Key_World_2 *> KeyEvent_World_2_Instances;
extern std::vector<PMMA::Events::Key_Escape *> KeyEvent_Escape_Instances;
extern std::vector<PMMA::Events::Key_Enter *> KeyEvent_Enter_Instances;
extern std::vector<PMMA::Events::Key_Tab *> KeyEvent_Tab_Instances;
extern std::vector<PMMA::Events::Key_Backspace *> KeyEvent_Backspace_Instances;
extern std::vector<PMMA::Events::Key_Insert *> KeyEvent_Insert_Instances;
extern std::vector<PMMA::Events::Key_Delete *> KeyEvent_Delete_Instances;
extern std::vector<PMMA::Events::Key_Right *> KeyEvent_Right_Instances;
extern std::vector<PMMA::Events::Key_Left *> KeyEvent_Left_Instances;
extern std::vector<PMMA::Events::Key_Down *> KeyEvent_Down_Instances;
extern std::vector<PMMA::Events::Key_Up *> KeyEvent_Up_Instances;
extern std::vector<PMMA::Events::Key_Page_Up *> KeyEvent_Page_Up_Instances;
extern std::vector<PMMA::Events::Key_Page_Down *> KeyEvent_Page_Down_Instances;
extern std::vector<PMMA::Events::Key_Home *> KeyEvent_Home_Instances;
extern std::vector<PMMA::Events::Key_End *> KeyEvent_End_Instances;
extern std::vector<PMMA::Events::Key_Caps_Lock *> KeyEvent_Caps_Lock_Instances;
extern std::vector<PMMA::Events::Key_Scroll_Lock *> KeyEvent_Scroll_Lock_Instances;
extern std::vector<PMMA::Events::Key_Num_Lock *> KeyEvent_Num_Lock_Instances;
extern std::vector<PMMA::Events::Key_Print_Screen *> KeyEvent_Print_Screen_Instances;
extern std::vector<PMMA::Events::Key_Pause *> KeyEvent_Pause_Instances;
extern std::vector<PMMA::Events::Key_F1 *> KeyEvent_F1_Instances;
extern std::vector<PMMA::Events::Key_F2 *> KeyEvent_F2_Instances;
extern std::vector<PMMA::Events::Key_F3 *> KeyEvent_F3_Instances;
extern std::vector<PMMA::Events::Key_F4 *> KeyEvent_F4_Instances;
extern std::vector<PMMA::Events::Key_F5 *> KeyEvent_F5_Instances;
extern std::vector<PMMA::Events::Key_F6 *> KeyEvent_F6_Instances;
extern std::vector<PMMA::Events::Key_F7 *> KeyEvent_F7_Instances;
extern std::vector<PMMA::Events::Key_F8 *> KeyEvent_F8_Instances;
extern std::vector<PMMA::Events::Key_F9 *> KeyEvent_F9_Instances;
extern std::vector<PMMA::Events::Key_F10 *> KeyEvent_F10_Instances;
extern std::vector<PMMA::Events::Key_F11 *> KeyEvent_F11_Instances;
extern std::vector<PMMA::Events::Key_F12 *> KeyEvent_F12_Instances;
extern std::vector<PMMA::Events::Key_F13 *> KeyEvent_F13_Instances;
extern std::vector<PMMA::Events::Key_F14 *> KeyEvent_F14_Instances;
extern std::vector<PMMA::Events::Key_F15 *> KeyEvent_F15_Instances;
extern std::vector<PMMA::Events::Key_F16 *> KeyEvent_F16_Instances;
extern std::vector<PMMA::Events::Key_F17 *> KeyEvent_F17_Instances;
extern std::vector<PMMA::Events::Key_F18 *> KeyEvent_F18_Instances;
extern std::vector<PMMA::Events::Key_F19 *> KeyEvent_F19_Instances;
extern std::vector<PMMA::Events::Key_F20 *> KeyEvent_F20_Instances;
extern std::vector<PMMA::Events::Key_F21 *> KeyEvent_F21_Instances;
extern std::vector<PMMA::Events::Key_F22 *> KeyEvent_F22_Instances;
extern std::vector<PMMA::Events::Key_F23 *> KeyEvent_F23_Instances;
extern std::vector<PMMA::Events::Key_F24 *> KeyEvent_F24_Instances;
extern std::vector<PMMA::Events::Key_F25 *> KeyEvent_F25_Instances;
extern std::vector<PMMA::Events::Key_Left_Shift *> KeyEvent_Left_Shift_Instances;
extern std::vector<PMMA::Events::Key_Left_Control *> KeyEvent_Left_Control_Instances;
extern std::vector<PMMA::Events::Key_Left_Alt *> KeyEvent_Left_Alt_Instances;
extern std::vector<PMMA::Events::Key_Left_Super *> KeyEvent_Left_Super_Instances;
extern std::vector<PMMA::Events::Key_Right_Shift *> KeyEvent_Right_Shift_Instances;
extern std::vector<PMMA::Events::Key_Right_Control *> KeyEvent_Right_Control_Instances;
extern std::vector<PMMA::Events::Key_Right_Alt *> KeyEvent_Right_Alt_Instances;
extern std::vector<PMMA::Events::Key_Right_Super *> KeyEvent_Right_Super_Instances;
extern std::vector<PMMA::Events::Key_Shift *> KeyEvent_Shift_Instances;
extern std::vector<PMMA::Events::Key_Control *> KeyEvent_Control_Instances;
extern std::vector<PMMA::Events::Key_Alt *> KeyEvent_Alt_Instances;
extern std::vector<PMMA::Events::Key_Super *> KeyEvent_Super_Instances;
extern std::vector<PMMA::Events::Key_Menu *> KeyEvent_Menu_Instances;
extern std::vector<PMMA::Events::KeyPad_0 *> KeyPadEvent_0_Instances;
extern std::vector<PMMA::Events::KeyPad_1 *> KeyPadEvent_1_Instances;
extern std::vector<PMMA::Events::KeyPad_2 *> KeyPadEvent_2_Instances;
extern std::vector<PMMA::Events::KeyPad_3 *> KeyPadEvent_3_Instances;
extern std::vector<PMMA::Events::KeyPad_4 *> KeyPadEvent_4_Instances;
extern std::vector<PMMA::Events::KeyPad_5 *> KeyPadEvent_5_Instances;
extern std::vector<PMMA::Events::KeyPad_6 *> KeyPadEvent_6_Instances;
extern std::vector<PMMA::Events::KeyPad_7 *> KeyPadEvent_7_Instances;
extern std::vector<PMMA::Events::KeyPad_8 *> KeyPadEvent_8_Instances;
extern std::vector<PMMA::Events::KeyPad_9 *> KeyPadEvent_9_Instances;
extern std::vector<PMMA::Events::KeyPad_Decimal *> KeyPadEvent_Decimal_Instances;
extern std::vector<PMMA::Events::KeyPad_Divide *> KeyPadEvent_Divide_Instances;
extern std::vector<PMMA::Events::KeyPad_Multiply *> KeyPadEvent_Multiply_Instances;
extern std::vector<PMMA::Events::KeyPad_Subtract *> KeyPadEvent_Subtract_Instances;
extern std::vector<PMMA::Events::KeyPad_Add *> KeyPadEvent_Add_Instances;
extern std::vector<PMMA::Events::KeyPad_Enter *> KeyPadEvent_Enter_Instances;
extern std::vector<PMMA::Events::KeyPad_Equal *> KeyPadEvent_Equal_Instances;

extern std::vector<CPP_TextEvent *> TextEventInstances;

extern std::vector<PMMA::Events::Mouse_Position *> MousePositionEvent_Instances;
extern std::vector<PMMA::Events::Mouse_EnterWindow *> MouseEnterWindowEvent_Instances;

extern std::vector<PMMA::Events::Mouse_Button_Left *> MouseButtonEvent_Left_Instances;
extern std::vector<PMMA::Events::Mouse_Button_Right *> MouseButtonEvent_Right_Instances;
extern std::vector<PMMA::Events::Mouse_Button_Middle *> MouseButtonEvent_Middle_Instances;
extern std::vector<PMMA::Events::MouseButton_0 *> MouseButtonEvent_0_Instances;
extern std::vector<PMMA::Events::MouseButton_1 *> MouseButtonEvent_1_Instances;
extern std::vector<PMMA::Events::MouseButton_2 *> MouseButtonEvent_2_Instances;
extern std::vector<PMMA::Events::MouseButton_3 *> MouseButtonEvent_3_Instances;
extern std::vector<PMMA::Events::MouseButton_4 *> MouseButtonEvent_4_Instances;

extern std::vector<PMMA::Events::Mouse_Scroll *> MouseScrollEventInstances;

extern std::vector<PMMA::Internal::Events::InternalController *> InternalControllerEventInstances;
extern std::vector<PMMA::Events::Controller *> ControllerEvent_Instances;

extern std::vector<CPP_DropEvent *> DropEvent_Instances;

extern PMMA::Internal::Events::InternalKeyManager *KeyManagerInstance;
extern PMMA::Internal::Events::InternalTextManager *TextManagerInstance;
extern PMMA::Internal::Events::InternalMousePositionManager *MousePositionManagerInstance;
extern PMMA::Internal::Events::InternalMouseEnterWindowManager *MouseEnterWindowManagerInstance;
extern PMMA::Internal::Events::InternalMouseButtonManager *MouseButtonManagerInstance;
extern PMMA::Internal::Events::InternalMouseScrollManager *MouseScrollManagerInstance;
extern PMMA::Internal::Events::InternalControllerManager *ControllerManagerInstance;
extern PMMA::Internal::Events::InternalDropManager *DropManagerInstance;

extern CPP_Passport *PassportInstance;
extern CPP_LoggingManager *LoggingManagerInstance;

extern PowerSavingManager PowerSavingManagerInstance;

extern CPP_AnimationManager *AnimationManagerInstance;

extern CPP_FastRandom *RandomGenerator;
} // namespace PMMA::Core

namespace PMMA::Registry {
extern std::vector<unsigned char> SecondaryDisplayIDs;
extern std::string PMMA_Location;
extern std::string PathSeparator;
extern std::string Current_PMMA_Version;
extern std::string Latest_PMMA_Version;
extern std::string Locale;

extern std::mutex SeedGeneratorLock;
extern std::mt19937 RandomSeedGenerator;
extern std::uniform_int_distribution<uint32_t> SeedDistribution;

extern std::chrono::high_resolution_clock::time_point StartupTime;

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
} // namespace PMMA::Registry

EXPORT void PMMA_Initialize(std::string location);

EXPORT void PMMA_Uninitialize();

uint32_t GetRandomSeed();