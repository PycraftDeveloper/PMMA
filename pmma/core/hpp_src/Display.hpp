#pragma once
#ifdef _MSC_VER // disabled at bottom
#pragma warning(push)
#pragma warning(disable : 4251)
#endif

#include "Internal/Core/PMMA_Exports.hpp"

#include <array>
#include <chrono>
#include <optional>
#include <stdexcept>
#include <string>

#include <GLFW/glfw3.h>
#include <bgfx/bgfx.h>

namespace PMMA::Types {
class Color;
}

namespace PMMA::Internal::Rendering::Core2D {
class RenderPipelineManager;
}

namespace PMMA::Events {
class Key_Space;
class Key_Apostrophe;
class Key_Comma;
class Key_Minus;
class Key_Period;
class Key_Slash;
class Key_0;
class Key_1;
class Key_2;
class Key_3;
class Key_4;
class Key_5;
class Key_6;
class Key_7;
class Key_8;
class Key_9;
class Key_Semicolon;
class Key_Equal;
class Key_A;
class Key_B;
class Key_C;
class Key_D;
class Key_E;
class Key_F;
class Key_G;
class Key_H;
class Key_I;
class Key_J;
class Key_K;
class Key_L;
class Key_M;
class Key_N;
class Key_O;
class Key_P;
class Key_Q;
class Key_R;
class Key_S;
class Key_T;
class Key_U;
class Key_V;
class Key_W;
class Key_X;
class Key_Y;
class Key_Z;
class Key_Left_Bracket;
class Key_Backslash;
class Key_Right_Bracket;
class Key_Grave_Accent;
class Key_World_1;
class Key_World_2;
class Key_Escape;
class Key_Enter;
class Key_Tab;
class Key_Backspace;
class Key_Insert;
class Key_Delete;
class Key_Right;
class Key_Left;
class Key_Down;
class Key_Up;
class Key_Page_Up;
class Key_Page_Down;
class Key_Home;
class Key_End;
class Key_Caps_Lock;
class Key_Scroll_Lock;
class Key_Num_Lock;
class Key_Print_Screen;
class Key_Pause;
class Key_F1;
class Key_F2;
class Key_F3;
class Key_F4;
class Key_F5;
class Key_F6;
class Key_F7;
class Key_F8;
class Key_F9;
class Key_F10;
class Key_F11;
class Key_F12;
class Key_F13;
class Key_F14;
class Key_F15;
class Key_F16;
class Key_F17;
class Key_F18;
class Key_F19;
class Key_F20;
class Key_F21;
class Key_F22;
class Key_F23;
class Key_F24;
class Key_F25;
class Key_Left_Shift;
class Key_Left_Control;
class Key_Left_Alt;
class Key_Left_Super;
class Key_Right_Shift;
class Key_Right_Control;
class Key_Right_Alt;
class Key_Right_Super;
class Key_Shift;
class Key_Control;
class Key_Alt;
class Key_Super;
class Key_Menu;
class KeyPad_0;
class KeyPad_1;
class KeyPad_2;
class KeyPad_3;
class KeyPad_4;
class KeyPad_5;
class KeyPad_6;
class KeyPad_7;
class KeyPad_8;
class KeyPad_9;
class KeyPad_Decimal;
class KeyPad_Divide;
class KeyPad_Multiply;
class KeyPad_Subtract;
class KeyPad_Add;
class KeyPad_Enter;
class KeyPad_Equal;
class TextInput;
class Mouse_Position;
class Mouse_EnterWindow;
class Mouse_Button_Left;
class Mouse_Button_Right;
class Mouse_Button_Middle;
class Mouse_Button_0;
class Mouse_Button_1;
class Mouse_Button_2;
class Mouse_Button_3;
class Mouse_Button_4;
class Mouse_Scroll;
class Drop;
} // namespace PMMA::Events

namespace PMMA::Internal::Events {
class InternalKeyManager;
class InternalTextManager;
class InternalMousePositionManager;
class InternalMouseEnterWindowManager;
class InternalMouseButtonManager;
class InternalMouseScrollManager;
class InternalDropManager;
} // namespace PMMA::Internal::Events

namespace PMMA {
/**
 * A struct used to more easily customize the default arguments when creating a display.
 */
struct Display_Create_Kwargs {
    /**
     * The window title name.
     */
    std::string Caption = "PMMA Display";

    /**
     * This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.
     */
    std::string IconPath = "";

    /**
     * This is used to control if the window should be full screen or not. If the value is left as the default 'std::nullopt' PMMA will set the window to be automatically full screened when the window size is (0, 0).
     */
    std::optional<bool> OptionalFullScreen = std::nullopt;

    /**
     * This is used to control whether the window can be resized by the user. By default the end user cannot resize the window.
     */
    bool Resizable = false;

    /**
     * This is used to control whether the window has a border and title bar visible. Please note that when no title bar is visible it can be harder for the user to re-position the window. By default the window is set to have a frame.
     */
    bool NoFrame = false;

    /**
     * This is used to determine if the window refresh rate will be synchronized with the current monitor refresh rate. This is by default set to 'true' as this can improve application efficiency and reduce visual tearing.
     */
    bool Vsync = true;

    /**
     * This is used to set the window to be centered in the currently active window when created. The currently active window is typically the one the mouse cursor is in when the window is created. This defaults to 'true' ensuring the window is centered on screen. This does not prevent the window from being moved later on.
     */
    bool Centered = true;

    /**
     * This is used to determine if the window should be considered as
     * in a maximized state. The default value here is 'true'.
     */
    bool Maximized = false;
};

/**
 * A struct used to more easily customize the default arguments when refreshing a display.
 */
struct Display_Refresh_Kwargs {
    /**
     * The minimum refresh rate to dynamically adjust down to. If this value is 0, then the display will be updated only when nessasary (most efficient), this will not break window functionality.
     */
    unsigned int MinRefreshRate = 5;

    /**
     * The maximum refresh rate to dynamically adjust up to. There is no guarantee this value will be achieved - but the window should not refresh at a faster rate for extended period of times. If set to 'std::nullopt' the window refresh rate will be capped at either 60 when not using vsync, or allowed to run up to the vsync limit.
     */
    std::optional<unsigned int> MaxRefreshRate = std::nullopt;

    /**
     * This is used to completely disable any dynamic refresh rate behaviour and force the window to refresh as fast as possible. This is not recommended for most use-cases, but could be useful for performance testing.
     */
    bool LimitRefreshRate = true;

    /**
     * This is used to customize the dynamic refresh rate behaviour. If 'true' then when the window is minimized the refresh rate of the window will drop. If 'false' the refresh rate of the window will not change when the window is minimized.
     */
    bool LowerRefreshRate_OnMinimize = true;

    /**
     * This is used to customize the dynamic refresh rate behaviour. If 'true' then when the window is not in focus the refresh rate of the window will drop. If 'false' the refresh rate of the window will not change when the window is not in focus.
     */
    bool LowerRefreshRate_OnFocusLoss = true;

    /**
     * This is used to customize the dynamic refresh rate behaviour. If 'true' then when the device is in a ‘low power state’ the refresh rate of the window will drop. If 'false' the refresh rate of the window will not change when the device is in a ‘low power state’.
     */
    bool LowerRefreshRate_OnLowBattery = true;
};

/**
 * This class is responsible for managing the display window, including its creation, configuration, and properties. It provides methods to manipulate the window's state, such as minimizing, maximizing, and setting its position. Additionally, it offers functionality to retrieve information about the display, such as its size, aspect ratio, and frame rate.
 */
class EXPORT Display {
public:
    /**
     * Used to control the background color of the window.
     */
    PMMA::Types::Color *WindowFillColor = nullptr;
    PMMA::Events::Key_F11 *F11_KeyEvent;
    PMMA::Events::Key_Escape *Escape_KeyEvent;

    PMMA::Internal::Rendering::Core2D::RenderPipelineManager *RenderPipelineCore;

    unsigned char DisplayID = 0;

    bgfx::FrameBufferHandle DisplayFrameBufferHandle = BGFX_INVALID_HANDLE;

    std::vector<PMMA::Events::Key_Space *> KeyEvent_Space_Instances;
    std::vector<PMMA::Events::Key_Apostrophe *> KeyEvent_Apostrophe_Instances;
    std::vector<PMMA::Events::Key_Comma *> KeyEvent_Comma_Instances;
    std::vector<PMMA::Events::Key_Minus *> KeyEvent_Minus_Instances;
    std::vector<PMMA::Events::Key_Period *> KeyEvent_Period_Instances;
    std::vector<PMMA::Events::Key_Slash *> KeyEvent_Slash_Instances;
    std::vector<PMMA::Events::Key_0 *> KeyEvent_0_Instances;
    std::vector<PMMA::Events::Key_1 *> KeyEvent_1_Instances;
    std::vector<PMMA::Events::Key_2 *> KeyEvent_2_Instances;
    std::vector<PMMA::Events::Key_3 *> KeyEvent_3_Instances;
    std::vector<PMMA::Events::Key_4 *> KeyEvent_4_Instances;
    std::vector<PMMA::Events::Key_5 *> KeyEvent_5_Instances;
    std::vector<PMMA::Events::Key_6 *> KeyEvent_6_Instances;
    std::vector<PMMA::Events::Key_7 *> KeyEvent_7_Instances;
    std::vector<PMMA::Events::Key_8 *> KeyEvent_8_Instances;
    std::vector<PMMA::Events::Key_9 *> KeyEvent_9_Instances;
    std::vector<PMMA::Events::Key_Semicolon *> KeyEvent_Semicolon_Instances;
    std::vector<PMMA::Events::Key_Equal *> KeyEvent_Equal_Instances;
    std::vector<PMMA::Events::Key_A *> KeyEvent_A_Instances;
    std::vector<PMMA::Events::Key_B *> KeyEvent_B_Instances;
    std::vector<PMMA::Events::Key_C *> KeyEvent_C_Instances;
    std::vector<PMMA::Events::Key_D *> KeyEvent_D_Instances;
    std::vector<PMMA::Events::Key_E *> KeyEvent_E_Instances;
    std::vector<PMMA::Events::Key_F *> KeyEvent_F_Instances;
    std::vector<PMMA::Events::Key_G *> KeyEvent_G_Instances;
    std::vector<PMMA::Events::Key_H *> KeyEvent_H_Instances;
    std::vector<PMMA::Events::Key_I *> KeyEvent_I_Instances;
    std::vector<PMMA::Events::Key_J *> KeyEvent_J_Instances;
    std::vector<PMMA::Events::Key_K *> KeyEvent_K_Instances;
    std::vector<PMMA::Events::Key_L *> KeyEvent_L_Instances;
    std::vector<PMMA::Events::Key_M *> KeyEvent_M_Instances;
    std::vector<PMMA::Events::Key_N *> KeyEvent_N_Instances;
    std::vector<PMMA::Events::Key_O *> KeyEvent_O_Instances;
    std::vector<PMMA::Events::Key_P *> KeyEvent_P_Instances;
    std::vector<PMMA::Events::Key_Q *> KeyEvent_Q_Instances;
    std::vector<PMMA::Events::Key_R *> KeyEvent_R_Instances;
    std::vector<PMMA::Events::Key_S *> KeyEvent_S_Instances;
    std::vector<PMMA::Events::Key_T *> KeyEvent_T_Instances;
    std::vector<PMMA::Events::Key_U *> KeyEvent_U_Instances;
    std::vector<PMMA::Events::Key_V *> KeyEvent_V_Instances;
    std::vector<PMMA::Events::Key_W *> KeyEvent_W_Instances;
    std::vector<PMMA::Events::Key_X *> KeyEvent_X_Instances;
    std::vector<PMMA::Events::Key_Y *> KeyEvent_Y_Instances;
    std::vector<PMMA::Events::Key_Z *> KeyEvent_Z_Instances;
    std::vector<PMMA::Events::Key_Left_Bracket *> KeyEvent_Left_Bracket_Instances;
    std::vector<PMMA::Events::Key_Backslash *> KeyEvent_Backslash_Instances;
    std::vector<PMMA::Events::Key_Right_Bracket *> KeyEvent_Right_Bracket_Instances;
    std::vector<PMMA::Events::Key_Grave_Accent *> KeyEvent_Grave_Accent_Instances;
    std::vector<PMMA::Events::Key_World_1 *> KeyEvent_World_1_Instances;
    std::vector<PMMA::Events::Key_World_2 *> KeyEvent_World_2_Instances;
    std::vector<PMMA::Events::Key_Escape *> KeyEvent_Escape_Instances;
    std::vector<PMMA::Events::Key_Enter *> KeyEvent_Enter_Instances;
    std::vector<PMMA::Events::Key_Tab *> KeyEvent_Tab_Instances;
    std::vector<PMMA::Events::Key_Backspace *> KeyEvent_Backspace_Instances;
    std::vector<PMMA::Events::Key_Insert *> KeyEvent_Insert_Instances;
    std::vector<PMMA::Events::Key_Delete *> KeyEvent_Delete_Instances;
    std::vector<PMMA::Events::Key_Right *> KeyEvent_Right_Instances;
    std::vector<PMMA::Events::Key_Left *> KeyEvent_Left_Instances;
    std::vector<PMMA::Events::Key_Down *> KeyEvent_Down_Instances;
    std::vector<PMMA::Events::Key_Up *> KeyEvent_Up_Instances;
    std::vector<PMMA::Events::Key_Page_Up *> KeyEvent_Page_Up_Instances;
    std::vector<PMMA::Events::Key_Page_Down *> KeyEvent_Page_Down_Instances;
    std::vector<PMMA::Events::Key_Home *> KeyEvent_Home_Instances;
    std::vector<PMMA::Events::Key_End *> KeyEvent_End_Instances;
    std::vector<PMMA::Events::Key_Caps_Lock *> KeyEvent_Caps_Lock_Instances;
    std::vector<PMMA::Events::Key_Scroll_Lock *> KeyEvent_Scroll_Lock_Instances;
    std::vector<PMMA::Events::Key_Num_Lock *> KeyEvent_Num_Lock_Instances;
    std::vector<PMMA::Events::Key_Print_Screen *> KeyEvent_Print_Screen_Instances;
    std::vector<PMMA::Events::Key_Pause *> KeyEvent_Pause_Instances;
    std::vector<PMMA::Events::Key_F1 *> KeyEvent_F1_Instances;
    std::vector<PMMA::Events::Key_F2 *> KeyEvent_F2_Instances;
    std::vector<PMMA::Events::Key_F3 *> KeyEvent_F3_Instances;
    std::vector<PMMA::Events::Key_F4 *> KeyEvent_F4_Instances;
    std::vector<PMMA::Events::Key_F5 *> KeyEvent_F5_Instances;
    std::vector<PMMA::Events::Key_F6 *> KeyEvent_F6_Instances;
    std::vector<PMMA::Events::Key_F7 *> KeyEvent_F7_Instances;
    std::vector<PMMA::Events::Key_F8 *> KeyEvent_F8_Instances;
    std::vector<PMMA::Events::Key_F9 *> KeyEvent_F9_Instances;
    std::vector<PMMA::Events::Key_F10 *> KeyEvent_F10_Instances;
    std::vector<PMMA::Events::Key_F11 *> KeyEvent_F11_Instances;
    std::vector<PMMA::Events::Key_F12 *> KeyEvent_F12_Instances;
    std::vector<PMMA::Events::Key_F13 *> KeyEvent_F13_Instances;
    std::vector<PMMA::Events::Key_F14 *> KeyEvent_F14_Instances;
    std::vector<PMMA::Events::Key_F15 *> KeyEvent_F15_Instances;
    std::vector<PMMA::Events::Key_F16 *> KeyEvent_F16_Instances;
    std::vector<PMMA::Events::Key_F17 *> KeyEvent_F17_Instances;
    std::vector<PMMA::Events::Key_F18 *> KeyEvent_F18_Instances;
    std::vector<PMMA::Events::Key_F19 *> KeyEvent_F19_Instances;
    std::vector<PMMA::Events::Key_F20 *> KeyEvent_F20_Instances;
    std::vector<PMMA::Events::Key_F21 *> KeyEvent_F21_Instances;
    std::vector<PMMA::Events::Key_F22 *> KeyEvent_F22_Instances;
    std::vector<PMMA::Events::Key_F23 *> KeyEvent_F23_Instances;
    std::vector<PMMA::Events::Key_F24 *> KeyEvent_F24_Instances;
    std::vector<PMMA::Events::Key_F25 *> KeyEvent_F25_Instances;
    std::vector<PMMA::Events::Key_Left_Shift *> KeyEvent_Left_Shift_Instances;
    std::vector<PMMA::Events::Key_Left_Control *> KeyEvent_Left_Control_Instances;
    std::vector<PMMA::Events::Key_Left_Alt *> KeyEvent_Left_Alt_Instances;
    std::vector<PMMA::Events::Key_Left_Super *> KeyEvent_Left_Super_Instances;
    std::vector<PMMA::Events::Key_Right_Shift *> KeyEvent_Right_Shift_Instances;
    std::vector<PMMA::Events::Key_Right_Control *> KeyEvent_Right_Control_Instances;
    std::vector<PMMA::Events::Key_Right_Alt *> KeyEvent_Right_Alt_Instances;
    std::vector<PMMA::Events::Key_Right_Super *> KeyEvent_Right_Super_Instances;
    std::vector<PMMA::Events::Key_Shift *> KeyEvent_Shift_Instances;
    std::vector<PMMA::Events::Key_Control *> KeyEvent_Control_Instances;
    std::vector<PMMA::Events::Key_Alt *> KeyEvent_Alt_Instances;
    std::vector<PMMA::Events::Key_Super *> KeyEvent_Super_Instances;
    std::vector<PMMA::Events::Key_Menu *> KeyEvent_Menu_Instances;
    std::vector<PMMA::Events::KeyPad_0 *> KeyPadEvent_0_Instances;
    std::vector<PMMA::Events::KeyPad_1 *> KeyPadEvent_1_Instances;
    std::vector<PMMA::Events::KeyPad_2 *> KeyPadEvent_2_Instances;
    std::vector<PMMA::Events::KeyPad_3 *> KeyPadEvent_3_Instances;
    std::vector<PMMA::Events::KeyPad_4 *> KeyPadEvent_4_Instances;
    std::vector<PMMA::Events::KeyPad_5 *> KeyPadEvent_5_Instances;
    std::vector<PMMA::Events::KeyPad_6 *> KeyPadEvent_6_Instances;
    std::vector<PMMA::Events::KeyPad_7 *> KeyPadEvent_7_Instances;
    std::vector<PMMA::Events::KeyPad_8 *> KeyPadEvent_8_Instances;
    std::vector<PMMA::Events::KeyPad_9 *> KeyPadEvent_9_Instances;
    std::vector<PMMA::Events::KeyPad_Decimal *> KeyPadEvent_Decimal_Instances;
    std::vector<PMMA::Events::KeyPad_Divide *> KeyPadEvent_Divide_Instances;
    std::vector<PMMA::Events::KeyPad_Multiply *> KeyPadEvent_Multiply_Instances;
    std::vector<PMMA::Events::KeyPad_Subtract *> KeyPadEvent_Subtract_Instances;
    std::vector<PMMA::Events::KeyPad_Add *> KeyPadEvent_Add_Instances;
    std::vector<PMMA::Events::KeyPad_Enter *> KeyPadEvent_Enter_Instances;
    std::vector<PMMA::Events::KeyPad_Equal *> KeyPadEvent_Equal_Instances;

    std::vector<PMMA::Events::TextInput *> TextEventInstances;

    std::vector<PMMA::Events::Mouse_Position *> MousePositionEvent_Instances;
    std::vector<PMMA::Events::Mouse_EnterWindow *> MouseEnterWindowEvent_Instances;

    std::vector<PMMA::Events::Mouse_Button_Left *> MouseButtonEvent_Left_Instances;
    std::vector<PMMA::Events::Mouse_Button_Right *> MouseButtonEvent_Right_Instances;
    std::vector<PMMA::Events::Mouse_Button_Middle *> MouseButtonEvent_Middle_Instances;
    std::vector<PMMA::Events::Mouse_Button_0 *> MouseButtonEvent_0_Instances;
    std::vector<PMMA::Events::Mouse_Button_1 *> MouseButtonEvent_1_Instances;
    std::vector<PMMA::Events::Mouse_Button_2 *> MouseButtonEvent_2_Instances;
    std::vector<PMMA::Events::Mouse_Button_3 *> MouseButtonEvent_3_Instances;
    std::vector<PMMA::Events::Mouse_Button_4 *> MouseButtonEvent_4_Instances;

    std::vector<PMMA::Events::Mouse_Scroll *> MouseScrollEventInstances;

    std::vector<PMMA::Internal::Events::InternalController *> InternalControllerEventInstances;

    std::vector<PMMA::Events::Drop *> DropEvent_Instances;

    PMMA::Internal::Events::InternalKeyManager *KeyManagerInstance = nullptr;
    PMMA::Internal::Events::InternalTextManager *TextManagerInstance = nullptr;
    PMMA::Internal::Events::InternalMousePositionManager *MousePositionManagerInstance = nullptr;
    PMMA::Internal::Events::InternalMouseEnterWindowManager *MouseEnterWindowManagerInstance = nullptr;
    PMMA::Internal::Events::InternalMouseButtonManager *MouseButtonManagerInstance = nullptr;
    PMMA::Internal::Events::InternalMouseScrollManager *MouseScrollManagerInstance = nullptr;
    PMMA::Internal::Events::InternalDropManager *DropManagerInstance = nullptr;

private:
    std::string Caption = "PMMA Display";
    std::string DefaultIconPath;

    GLFWmonitor *Monitor = nullptr;
    GLFWwindow *Window = nullptr;

    float OrthographicProjection[16] = {0.0f};

    uint16_t PreviousDisplaySize[2];

    std::chrono::high_resolution_clock::time_point StartTime = std::chrono::high_resolution_clock::now();

    uint16_t Size[2] = {0, 0};
    unsigned int Position[2] = {0, 0};
    unsigned int CurrentMonitorRefreshRate = 0;
    uint16_t CurrentSize[2] = {0, 0};

    float RefreshTime = 0.000001f;

    bool FullScreen;
    bool Resizable;
    bool NoFrame;
    bool Vsync;
    bool Centered;
    bool Maximized;
    bool OrthographicProjectionSet = false;
    bool IsSecondaryDisplay = false;
    bool DisplayShouldClose = false;
    bool FirstFrame = true;

public:
    bool DisplaySizeChanged = true;

    Display();
    ~Display();

private:
    void PMMA_Update(GLFWwindow *Window);

public:
    /**
     * This method is used to create a window which will be the rendering target for PMMA. All 2D and 3D content will end up being rendered to this window.
     * \param NewSize The size of the window in pixels. If set to (0, 0) the window will be created at the current monitor's resolution and be automatically full-screen.
     * \param kwargs A dictionary of keyword arguments that can be used to configure the window. See the documentation for more information.
     * \note This method must be called before any rendering can occur.
     * \note Certain display settings can only be set at the time of window creation. If you need to change these settings, you will need to recreate the window. We are working on making this process easier.
     * \note Only one PMMA display can be created at a time. You can have multiple display instances but they will all share the same object behind the scenes. This is something we are looking to address in a future version of PMMA.
     */
    void Create(uint16_t *NewSize, Display_Create_Kwargs kwargs = {});

    /**
     * This method is used to get if the window is set to use vsync. Note that this does not check if vsync is supported in your setup, as this varies based on third party factors that we cannot check.
     * \returns bool - Returns `true` when vsync is used. Returns `false` when the window is not using vsync.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowUsingVsync();

    /**
     * This method gets the refresh rate of the current monitor video mode.
     * \returns unsigned int - The current monitor video mode refresh rate.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    unsigned int GetCurrentMonitorRefreshRate();

    /**
     * This method gets the current window width in pixels.
     * \returns unsigned int - The window width in pixels.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    uint16_t GetWidth();

    /**
     * This method gets the current window height in pixels.
     * \returns unsigned int - The window height in pixels.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    uint16_t GetHeight();

    /**
     * This method gets the current size of the window in pixels (width, height)
     * \param out The output size of the window in pixels.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void GetSize(uint16_t *out);

private:
    GLFWmonitor *GetMonitorAtPoint(unsigned int *Point);

    GLFWmonitor *GetTargetMonitor(GLFWwindow *Window);

    GLFWmonitor *GetCurrentMonitor(GLFWwindow *Window);

public:
    /**
     * This method is used to set the window to be positioned on-screen relative to the origin of the current monitor (the top left corner).
     * \param position The number of pixels to move the window to. This takes two values (x, y).
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetRelativeWindowPosition(unsigned int *NewPosition);

    /**
     * This method is used to set the window to be positioned on-screen relative to the windowing system's origin (typically the top left corner of the left-most monitor as arranged on your desktop).
     * \param position The number of pixels to move the window to. This takes two values (x, y).
     * \note Please be aware that some monitor layouts will have 'gaps' between each monitor due to their arrangement or resolution. Care should be taken to not place the window in this area as it will not be seen.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetAbsoluteWindowPosition(unsigned int *NewPosition);

    /**
     * This method is used to position the window centrally in the monitor the window was first created on.
     * \note We are working on a way to have this center the window to whichever monitor it is currently on.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void CenterWindow();

    /**
     * This method is used to clear all rendered graphics from the previous frame, and also used to apply the specified background color defined in `Display::WindowFillColor`.
     * \note This method must be called from the same thread that the window was created in.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void Clear();

    /**
     * This method is used to force the created window to be put into focus.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetWindowInFocus();

    /**
     * This method is used to minimize the created window (to the taskbar or equivalent on your operating system).
     * \param value When `true` the display will be minimized. When `false` the display will be returned to its original state (not maximized).
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetWindowMinimized(bool IsMinimized);

    /**
     * This method is used to maximize the created window to fill the current monitor, showing the title bar.
     * \param value When `true` the display will be maximized. When `false` the display will be returned to its original state (not minimized).
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetWindowMaximized(bool IsMaximized);

    /**
     * This method is used to get if the window is currently in focus.
     * \returns bool - Returns `true` when in focus. Returns `false` when not in focus.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowInFocus();

    /**
     * This method is used to get if the window is currently minimized.
     * \returns bool - Returns `true` when the window is minimized. Returns `false` when the window is not minimized.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowMinimized();

    /**
     * This method is used to get if the window is resizable.
     * \returns bool - Returns `true` when the window is able to be resized by the end user. Returns `false` when the window is not resizable by the end user.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowResizable();

    /**
     * This method is used to get if the window is currently visible on-screen.
     * \returns bool - Returns `true` when the window is visible. Returns `false` when the window is not visible.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowVisible();

    /**
     * This method is used to get if the window is set to be always on top.
     * \returns bool - Returns `true` when the window is always on top. Returns `false` when the window is not always on top.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowAlwaysOnTop();

    /**
     * This method is used get if the window is set to automatically minimize when it is no longer in focus. This is typically seen in game applications.
     * \returns bool - Returns `true` when the window is configured to automatically minimize when focus is lost. Returns `false` when the window is not configured to automatically minimize when focus is lost.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowAutoMinimize();

    /**
     * This method is used to get if the window is currently maximized.
     * \returns bool - Returns `true` when the window is maximized. Returns `false` when the window is not maximized.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    bool GetIsWindowMaximized();

    /**
     * This method is used to get the number of Multi-Sample Anti-Aliasing samples.
     * \returns unsigned int - The number of samples.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    unsigned int GetWindow_MSAA_Samples();

    /**
     * This method is used to pass a string to use as the display caption.
     * \param std::string - The window title name.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetCaption(std::string new_caption);

    /**
     * This method is used to get the window caption.
     * \returns std::string - The window caption as a string.
     */
    inline std::string GetCaption() {
        return Caption;
    }

    /**
     * This method is used to get the center point of the window.
     * \param unsigned int* The center point as a coordinate (x, y).
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void GetCenterPosition(uint16_t *out);

    /**
     * This method is used to get the horizontal center point of the window.
     * \returns The horizontal center position.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    uint16_t GetHorizontalCenterPosition();

    /**
     * This method is used to get the vertical center point of the window.
     * \returns The vertical center position.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    uint16_t GetVerticalCenterPosition();

    /**
     * This method is used to get the center point of the window.
     * \param ObjectSize: The size in the format (x, y) to offset the center position.
     * \param out: The output center point as a coordinate (x, y).\
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void GetCenterPosition(uint16_t *ObjectSize, uint16_t *out);

    /**
     * This method is used to get the horizontal center position.
     * \param ObjectSize: The horizontal size to offset the center position.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    uint16_t GetHorizontalCenterPosition(uint16_t ObjectSize);

    /**
     * This method is used to get the vertical center position.
     * \param ObjectSize: The vertical size to offset the center position.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    uint16_t GetVerticalCenterPosition(uint16_t ObjectSize);

    /**
     * This method is used to get the aspect ratio of the window.
     * \returns float - The window aspect ratio. For example: 2.667 would be returned for a window with aspect ration 16:9.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    float GetAspectRatio();

private:
    void LimitRefreshRate(unsigned int RefreshRate);

public:
    /**
     * This method is used to update the window to show all the content rendered since `Display.clear`. Additionally, it is used to limit the refresh rate of the window to avoid excessive resource usage.
     * When the window is created with `vsync=True` the refresh rate of the window will be forced to the monitor refresh rate. Otherwise, the refresh rate will be dynamically adjusted to save resources. This behaviour is customizable using the parameters below.
     * \param kwargs Used to customize the default refresh parameters.
     * \note If you set `min_refresh_rate` to 0, the display will be refreshed when the user interacts with it or when the rendered content on-screen changes. This created a highly-efficient behaviour seen in most desktop applications and is generally recommended.
     * \note This method must be called from the same thread that the window was created in.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void Refresh(Display_Refresh_Kwargs kwargs = {});

    /**
     * This method is used to force the window to refresh. This works even when `min_refresh_rate` is 0.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void TriggerEventRefresh();

    /**
     * This method is used to get the current frame rate of the window.
     * \returns unsigned int - The refresh rate of the window.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    unsigned int GetFrameRate();

    /**
     * This method is used to get the current frame time of the window.
     * \returns float - The time in seconds between the current and previous frame.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    float GetFrameTime();

    /**
     * This method is used to get the display's orthographic projection.
     * \param out The output projection matrix.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void GetOrthographicProjection(float *out);

private:
    unsigned int CalculateRefreshRate(unsigned int RefreshRate,
                                      bool LowerRefreshRate_OnMinimize,
                                      bool LowerRefreshRate_OnFocusLoss,
                                      bool LowerRefreshRate_OnLowBattery);

public:
    /**
     * This method is used to pass an image file path to the display to be used as an icon, which replaces the default icon.
     * \param icon_path This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void SetIcon(std::string IconPath);

    /**
     * This method is used to switch the window between full screen and windowed modes.
     * \warning A valid window must be created using `Display::Create` before calling this method.
     */
    void ToggleFullScreen();

    inline bool GetIsWindowCreated() {
        return Window != nullptr;
    }

    void SetAsActiveDisplay();

    inline bool GetIsSecondaryDisplay() {
        return IsSecondaryDisplay;
    }

    inline bool GetShouldClose() {
        return DisplayShouldClose;
    }

    bool GetIsActiveDisplay();
};
} // namespace PMMA

#ifdef _MSC_VER
#pragma warning(pop)
#endif