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

#include "Rendering/RenderPipelineCore.hpp"
#include "NumberFormats.hpp"

class EXPORT CPP_Display {
    public:
        CPP_ColorFormat* WindowFillColor = nullptr;

    private:
        std::string Caption = "PMMA Display";
        std::string DefaultIconPath;

        GLFWmonitor* Monitor = nullptr;
        GLFWwindow* Window = nullptr;

        glm::mat4 OrthographicProjection;

        std::chrono::high_resolution_clock::time_point StartTime = std::chrono::high_resolution_clock::now();

        unsigned int Size[2] = {0, 0};

        float RefreshTime = 0.000001f;

        bool FullScreen;
        bool Resizable;
        bool NoFrame;
        bool Vsync;
        bool Centered;
        bool Maximized;
        bool OrthographicProjectionSet = false;

    public:
        CPP_Display();

        void PMMA_Update(GLFWwindow* Window);

        void Create(unsigned int* NewSize, std::string& NewCaption, std::string& NewIcon, bool NewFullScreen=true, bool NewResizable=false, bool NewNoFrame=false, bool NewVsync=true, bool NewCentered=true, bool NewMaximized=false, bool Transparent=false);

        inline unsigned int GetWidth() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            return Size[0];
        };

        inline unsigned int GetHeight() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            return Size[1];
        };

        inline void GetSize(unsigned int* out) {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            out[0] = Size[0];
            out[1] = Size[1];
        };

        GLFWmonitor* GetMonitorAtPoint(unsigned int* Point);

        GLFWmonitor* GetTargetMonitor(GLFWwindow* Window);

        GLFWmonitor* GetCurrentMonitor(GLFWwindow* Window);

        inline void SetRelativeWindowPosition(unsigned int* NewPosition) {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }

            glfwSetWindowPos(Window, NewPosition[0], NewPosition[1]);
        }

        inline void SetAbsoluteWindowPosition(unsigned int* NewPosition) {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }

            GLFWmonitor* PointMonitor = GetMonitorAtPoint(NewPosition);

            int Monitor_X_Position, Monitor_Y_Position;
            glfwGetMonitorPos(PointMonitor, &Monitor_X_Position, &Monitor_Y_Position);
            glfwSetWindowPos(Window, NewPosition[0] - Monitor_X_Position, NewPosition[1] - Monitor_Y_Position);
        }

        inline void CenterWindow() {
            if (Window == nullptr) {
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
                throw std::runtime_error("Display not created yet!");
            }

            glfwFocusWindow(Window);
        }

        inline void SetWindowMinimized(bool IsMinimized) {
            if (Window == nullptr) {
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
                throw std::runtime_error("Display not created yet!");
            }

            if (IsMaximized) {
                glfwMaximizeWindow(Window);
            }
            else {
                glfwRestoreWindow(Window);
            }
        }

        inline void SetCaption(std::string& new_caption) {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }

            glfwSetWindowTitle(Window, new_caption.c_str());
            Caption = new_caption;
        }

        inline std::string GetCaption() {
            return Caption;
        }

        inline void GetCenter_Pixels(unsigned int* out) {
            out[0] = (unsigned int)(Size[0] / 2);
            out[1] = (unsigned int)(Size[1] / 2);
        }

        inline void GetCenter_Pixels(unsigned int* ObjectSize, unsigned int* out) {
            out[0] = (unsigned int)((Size[0] - ObjectSize[0]) / 2);
            out[1] = (unsigned int)((Size[1] - ObjectSize[1]) / 2);
        }

        inline float GetAspectRatio() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            return (float)Size[0] / (float)Size[1];
        }

        void LimitRefreshRate(unsigned int RefreshRate, bool Minimized, bool FocusLoss, bool LowBattery);

        void ContinuousRefresh(
            unsigned int RefreshRate,
            bool Minimized,
            bool FocusLoss,
            bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery);

        void EventRefresh(
            unsigned int RefreshRate,
            unsigned int MaxRefreshRate,
            bool Minimized,
            bool FocusLoss,
            bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery);

        inline void TriggerEventRefresh() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            glfwPostEmptyEvent();
        }

        inline unsigned int GetFrameRate() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            return (unsigned int)(1 / RefreshTime);
        }

        inline float GetFrameTime() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            return RefreshTime;
        }

        inline glm::mat4 GetDisplayProjection() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }

            if (OrthographicProjectionSet) {
                return OrthographicProjection;
            }

            OrthographicProjection = glm::ortho(
                0.0f, static_cast<float>(Size[0]),        // Left to Right
                static_cast<float>(Size[1]), 0.0f,        // Top to Bottom (invert Y)
                -1.0f, 1.0f                               // Near and Far
            );
            OrthographicProjectionSet = true;
            return OrthographicProjection;
        };

        inline unsigned int CalculateRefreshRate(unsigned int RefreshRate, bool Minimized, bool FocusLoss, bool LowBattery) {
            unsigned int OriginalRefreshRate = RefreshRate;

            if (Minimized) {
                RefreshRate /= 5;
            }

            if (FocusLoss) {
                RefreshRate /= 2;
            }

            if (LowBattery) {
                RefreshRate /= 2;
            }

            if (Minimized) {
                RefreshRate = std::max(RefreshRate, 5u);
            } else {
                RefreshRate = std::max(RefreshRate, RefreshRate / 2);
            }

            if (RefreshRate > OriginalRefreshRate) {
                RefreshRate = OriginalRefreshRate;
            }

            return RefreshRate;
        }

        void SetIcon(string IconPath);

        ~CPP_Display();

        // WIPs

        void Get_2D_Surface(bool SetToBeUsed=true);

        void Get_3D_Surface(bool SetToBeUsed=true);

        void ToggleFullScreen();
};

#ifdef _MSC_VER
    #pragma warning(pop)
#endif