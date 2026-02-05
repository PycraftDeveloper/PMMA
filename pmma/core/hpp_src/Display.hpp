#pragma once
#ifdef _MSC_VER // disabled at bottom
    #pragma warning(push)
    #pragma warning(disable: 4251)
#endif

#include "PMMA_Exports.hpp"

#include <string>
#include <stdexcept>
#include <chrono>
#include <array>
#include <optional>

#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

#include "Events/WindowEvents.hpp"
#include "Events/KeyEvents.hpp"
#include "Internal/Management/CoreRenderPipelineManager.hpp"
#include "CoreTypes.hpp"
#include "Logger.hpp"

/**
 * A struct used to more easily customize the default arguments when creating a display.
 */
struct CPP_Display_Create_Kwargs {
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
struct CPP_Display_Refresh_Kwargs {
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
class EXPORT CPP_Display {
    public:
        /**
         * Used to control the background color of the window.
         */
        CPP_Color* WindowFillColor = nullptr;
        CPP_KeyEvent_F11* F11_KeyEvent;
        CPP_KeyEvent_Escape* Escape_KeyEvent;

    private:
        CPP_Logger* Logger;

        std::string Caption = "PMMA Display";
        std::string DefaultIconPath;

        GLFWmonitor* Monitor = nullptr;
        GLFWwindow* Window = nullptr;

        float OrthographicProjection[16] = {0.0f};

        unsigned int PreviousDisplaySize[2];

        std::chrono::high_resolution_clock::time_point StartTime = std::chrono::high_resolution_clock::now();

        unsigned int Size[2] = {0, 0};
        unsigned int Position[2] = {0, 0};
        unsigned int CurrentMonitorRefreshRate = 0;
        int CurrentSize[2] = {0, 0};

        float RefreshTime = 0.000001f;

        bool FullScreen;
        bool Resizable;
        bool NoFrame;
        bool Vsync;
        bool Centered;
        bool Maximized;
        bool OrthographicProjectionSet = false;

    public:
        bool DisplaySizeChanged = true;

        CPP_Display();
        ~CPP_Display();

    private:
        void PMMA_Update(GLFWwindow* Window);

        public:
        /**
         * This method is used to create a window which will be the rendering target for PMMA. All 2D and 3D content will end up being rendered to this window.
         * \param NewSize The size of the window in pixels. If set to (0, 0) the window will be created at the current monitor's resolution and be automatically full-screen.
         * \param kwargs A dictionary of keyword arguments that can be used to configure the window. See the documentation for more information.
         * \note This method must be called before any rendering can occur.
         * \note Certain display settings can only be set at the time of window creation. If you need to change these settings, you will need to recreate the window. We are working on making this process easier.
         * \note Only one PMMA display can be created at a time. You can have multiple display instances but they will all share the same object behind the scenes. This is something we are looking to address in a future version of PMMA.
         */
        void Create(unsigned int* NewSize, CPP_Display_Create_Kwargs kwargs = {});

        /**
         * This method is used to get if the window is set to use vsync. Note that this does not check if vsync is supported in your setup, as this varies based on third party factors that we cannot check.
         * \returns bool - Returns `true` when vsync is used. Returns `false` when the window is not using vsync.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowUsingVsync() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return Vsync;
        }

        /**
         * This method gets the refresh rate of the current monitor video mode.
         * \returns unsigned int - The current monitor video mode refresh rate.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline unsigned int GetCurrentMonitorRefreshRate() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            GLFWmonitor* CurrentMonitor = GetCurrentMonitor(Window);
            const GLFWvidmode* Mode = glfwGetVideoMode(CurrentMonitor);
            CurrentMonitorRefreshRate = Mode->refreshRate;
            return CurrentMonitorRefreshRate;
        }

        /**
         * This method gets the current window width in pixels.
         * \returns unsigned int - The window width in pixels.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline unsigned int GetWidth() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }
            return CurrentSize[0];
        };

        /**
         * This method gets the current window height in pixels.
         * \returns unsigned int - The window height in pixels.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline unsigned int GetHeight() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return CurrentSize[1];
        };

        /**
         * This method gets the current size of the window in pixels (width, height)
         * \param out The output size of the window in pixels.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void GetSize(int* out) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            out[0] = CurrentSize[0];
            out[1] = CurrentSize[1];
        };

    private:
        GLFWmonitor* GetMonitorAtPoint(unsigned int* Point);

        GLFWmonitor* GetTargetMonitor(GLFWwindow* Window);

        GLFWmonitor* GetCurrentMonitor(GLFWwindow* Window);

    public:
        /**
         * This method is used to set the window to be positioned on-screen relative to the origin of the current monitor (the top left corner).
         * \param position The number of pixels to move the window to. This takes two values (x, y).
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void SetRelativeWindowPosition(unsigned int* NewPosition) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            glfwSetWindowPos(Window, NewPosition[0], NewPosition[1]);
        }

        /**
         * This method is used to set the window to be positioned on-screen relative to the windowing system's origin (typically the top left corner of the left-most monitor as arranged on your desktop).
         * \param position The number of pixels to move the window to. This takes two values (x, y).
         * \note Please be aware that some monitor layouts will have 'gaps' between each monitor due to their arrangement or resolution. Care should be taken to not place the window in this area as it will not be seen.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void SetAbsoluteWindowPosition(unsigned int* NewPosition) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            GLFWmonitor* PointMonitor = GetMonitorAtPoint(NewPosition);

            int Monitor_X_Position, Monitor_Y_Position;
            glfwGetMonitorPos(PointMonitor, &Monitor_X_Position, &Monitor_Y_Position);
            glfwSetWindowPos(Window, NewPosition[0] - Monitor_X_Position, NewPosition[1] - Monitor_Y_Position);
        }

        /**
         * This method is used to position the window centrally in the monitor the window was first created on.
         * \note We are working on a way to have this center the window to whichever monitor it is currently on.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void CenterWindow() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            GLFWmonitor* CurrentMonitor = GetCurrentMonitor(Window);

            int Monitor_Width, Monitor_Height;
            const GLFWvidmode* Mode = glfwGetVideoMode(CurrentMonitor);
            Monitor_Width = Mode->width;
            Monitor_Height = Mode->height;

            int Window_X_Offset = (Monitor_Width - Size[0]) / 2;
            int Window_Y_Offset = (Monitor_Height - Size[1]) / 2;

            glfwSetWindowPos(Window, Window_X_Offset, Window_Y_Offset);
        }

        /**
         * This method is used to clear all rendered graphics from the previous frame, and also used to apply the specified background color defined in `CPP_Display::WindowFillColor`.
         * \note This method must be called from the same thread that the window was created in.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        void Clear();

        /**
         * This method is used to force the created window to be put into focus.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void SetWindowInFocus() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            glfwFocusWindow(Window);
        }

        /**
         * This method is used to minimize the created window (to the taskbar or equivalent on your operating system).
         * \param value When `true` the display will be minimized. When `false` the display will be returned to its original state (not maximized).
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void SetWindowMinimized(bool IsMinimized) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            if (IsMinimized) {
                glfwIconifyWindow(Window);
            }
            else {
                glfwRestoreWindow(Window);
            }
        }

        /**
         * This method is used to maximize the created window to fill the current monitor, showing the title bar.
         * \param value When `true` the display will be maximized. When `false` the display will be returned to its original state (not minimized).
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void SetWindowMaximized(bool IsMaximized) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            if (IsMaximized) {
                glfwMaximizeWindow(Window);
            }
            else {
                glfwRestoreWindow(Window);
            }
        }

        /**
         * This method is used to get if the window is currently in focus.
         * \returns bool - Returns `true` when in focus. Returns `false` when not in focus.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowInFocus() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_FOCUSED) == GLFW_TRUE;
        }

        /**
         * This method is used to get if the window is currently minimized.
         * \returns bool - Returns `true` when the window is minimized. Returns `false` when the window is not minimized.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowMinimized() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_ICONIFIED) == GLFW_TRUE;
        }

        /**
         * This method is used to get if the window is resizable.
         * \returns bool - Returns `true` when the window is able to be resized by the end user. Returns `false` when the window is not resizable by the end user.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowResizable() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_RESIZABLE) == GLFW_TRUE;
        }

        /**
         * This method is used to get if the window is currently visible on-screen.
         * \returns bool - Returns `true` when the window is visible. Returns `false` when the window is not visible.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowVisible() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_VISIBLE) == GLFW_TRUE;
        }

        /**
         * This method is used to get if the window is set to be always on top.
         * \returns bool - Returns `true` when the window is always on top. Returns `false` when the window is not always on top.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowAlwaysOnTop() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_FLOATING) == GLFW_TRUE;
        }

        /**
         * This method is used get if the window is set to automatically minimize when it is no longer in focus. This is typically seen in game applications.
         * \returns bool - Returns `true` when the window is configured to automatically minimize when focus is lost. Returns `false` when the window is not configured to automatically minimize when focus is lost.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowAutoMinimize() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_AUTO_ICONIFY) == GLFW_TRUE;
        }

        /**
         * This method is used to get if the window is currently maximized.
         * \returns bool - Returns `true` when the window is maximized. Returns `false` when the window is not maximized.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline bool GetIsWindowMaximized() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_MAXIMIZED) == GLFW_TRUE;
        }

        /**
         * This method is used to get the number of Multi-Sample Anti-Aliasing samples.
         * \returns unsigned int - The number of samples.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline unsigned int GetWindow_MSAA_Samples() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            return glfwGetWindowAttrib(Window, GLFW_SAMPLES);
        }

        /**
         * This method is used to pass a string to use as the display caption.
         * \param std::string - The window title name.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void SetCaption(std::string new_caption) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            glfwSetWindowTitle(Window, new_caption.c_str());
            Caption = new_caption;
        }

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
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void GetCenterPosition(unsigned int* out) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            out[0] = (unsigned int)(Size[0] / 2);
            out[1] = (unsigned int)(Size[1] / 2);
        }

        /**
         * This method is used to get the center point of the window.
         * \param ObjectSize: The size in the format (x, y) to offset the center position.
         * \param out: The output center point as a coordinate (x, y).\
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void GetCenterPosition(unsigned int* ObjectSize, unsigned int* out) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            out[0] = (unsigned int)((Size[0] - ObjectSize[0]) / 2);
            out[1] = (unsigned int)((Size[1] - ObjectSize[1]) / 2);
        }

        /**
         * This method is used to get the aspect ratio of the window.
         * \returns float - The window aspect ratio. For example: 2.667 would be returned for a window with aspect ration 16:9.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline float GetAspectRatio() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }
            int Size[2];
            GetSize(Size);
            return (float)Size[0] / (float)Size[1];
        }

    private:
        void LimitRefreshRate(unsigned int RefreshRate);

    public:
        /**
         * This method is used to update the window to show all the content rendered since `Display.clear`. Additionally, it is used to limit the refresh rate of the window to avoid excessive resource usage.
         * When the window is created with `vsync=True` the refresh rate of the window will be forced to the monitor refresh rate. Otherwise, the refresh rate will be dynamically adjusted to save resources. This behaviour is customizable using the parameters below.
         * \param kwargs Used to customize the default refresh parameters.
         * \note If you set `min_refresh_rate` to 0, the display will be refreshed when the user interacts with it or when the rendered content on-screen changes. This created a highly-efficient behaviour seen in most desktop applications and is generally recommended.
         * \note This method must be called from the same thread that the window was created in.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
        */
        void Refresh(CPP_Display_Refresh_Kwargs kwargs = {});

        /**
         * This method is used to force the window to refresh. This works even when `min_refresh_rate` is 0.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void TriggerEventRefresh() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }
            glfwPostEmptyEvent();
        }

        /**
         * This method is used to get the current frame rate of the window.
         * \returns unsigned int - The refresh rate of the window.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline unsigned int GetFrameRate() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }
            return (unsigned int)(1 / RefreshTime);
        }

        /**
         * This method is used to get the current frame time of the window.
         * \returns float - The time in seconds between the current and previous frame.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline float GetFrameTime() {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }
            return RefreshTime;
        }

        /**
         * This method is used to get the display's orthographic projection.
         * \param out The output projection matrix.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        inline void GetOrthographicProjection(float* out) {
            if (Window == nullptr) {
                Logger->InternalLogError(
                    18,
                    "You need to create a display using `Display.create` \
before you can call this function.");
                throw std::runtime_error("Display not created yet!");
            }

            if (OrthographicProjectionSet) {
                out[0] = OrthographicProjection[0];
                out[1] = OrthographicProjection[1];
                out[2] = OrthographicProjection[2];
                out[3] = OrthographicProjection[3];
                out[4] = OrthographicProjection[4];
                out[5] = OrthographicProjection[5];
                out[6] = OrthographicProjection[6];
                out[7] = OrthographicProjection[7];
                out[8] = OrthographicProjection[8];
                out[9] = OrthographicProjection[9];
                out[10] = OrthographicProjection[10];
                out[11] = OrthographicProjection[11];
                out[12] = OrthographicProjection[12];
                out[13] = OrthographicProjection[13];
                out[14] = OrthographicProjection[14];
                out[15] = OrthographicProjection[15];
                return;
            }

            int Size[2];
            GetSize(Size);

            OrthographicProjection[0] = 2.0f / Size[0];
            OrthographicProjection[5] = -2.0f / Size[1];
            OrthographicProjection[10] = -1.0f;
            OrthographicProjection[12] = -1.0f;
            OrthographicProjection[13] = 1.0f;
            OrthographicProjection[15] = 1.0f;

            OrthographicProjectionSet = true;
        };

    private:
        unsigned int CalculateRefreshRate(unsigned int RefreshRate,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery);

    public:
        /**
         * This method is used to pass an image file path to the display to be used as an icon, which replaces the default icon.
         * \param icon_path This is used to set the window icon. You should enter a valid file path here. If left as the default empty string, the default PMMA display icon is used.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        void SetIcon(std::string IconPath);

        /**
         * This method is used to switch the window between full screen and windowed modes.
         * \warning A valid window must be created using `CPP_Display::Create` before calling this method.
         */
        void ToggleFullScreen();

        inline bool IsWindowCreated() {
            return Window != nullptr;
        }
};

#ifdef _MSC_VER
    #pragma warning(pop)
#endif