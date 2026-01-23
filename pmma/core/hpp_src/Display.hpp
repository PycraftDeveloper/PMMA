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

#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

#include "Events/WindowEvents.hpp"
#include "Events/KeyEvents.hpp"
#include "Internal/Management/CoreRenderPipelineManager.hpp"
#include "NumberFormats.hpp"
#include "Logger.hpp"

class EXPORT CPP_Display {
    public:
        CPP_ColorFormat* WindowFillColor = nullptr;
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

        void PMMA_Update(GLFWwindow* Window);

        void Create(
            unsigned int* NewSize,
            std::string NewCaption,
            std::string NewIcon,
            bool NewFullScreen=true,
            bool NewResizable=false,
            bool NewNoFrame=false,
            bool NewVsync=true,
            bool NewCentered=true,
            bool NewMaximized=false);

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

        GLFWmonitor* GetMonitorAtPoint(unsigned int* Point);

        GLFWmonitor* GetTargetMonitor(GLFWwindow* Window);

        GLFWmonitor* GetCurrentMonitor(GLFWwindow* Window);

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

        void Clear();

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

        inline std::string GetCaption() {
            return Caption;
        }

        inline void GetCenterPosition(unsigned int* out) {
            out[0] = (unsigned int)(Size[0] / 2);
            out[1] = (unsigned int)(Size[1] / 2);
        }

        inline void GetCenterPosition(unsigned int* ObjectSize, unsigned int* out) {
            out[0] = (unsigned int)((Size[0] - ObjectSize[0]) / 2);
            out[1] = (unsigned int)((Size[1] - ObjectSize[1]) / 2);
        }

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

        void LimitRefreshRate(unsigned int RefreshRate);

        void Refresh(
            unsigned int MinRefreshRate,
            unsigned int MaxRefreshRate,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery);

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

        inline void GetDisplayProjection(float* out) {
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

        unsigned int CalculateRefreshRate(unsigned int RefreshRate);

        void SetIcon(string IconPath);

        void ToggleFullScreen();

        inline bool IsWindowCreated() {
            return Window != nullptr;
        }

        // WIPs

        void Get_2D_Surface(bool SetToBeUsed=true);

        void Get_3D_Surface(bool SetToBeUsed=true);
};

#ifdef _MSC_VER
    #pragma warning(pop)
#endif