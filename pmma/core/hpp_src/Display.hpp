#pragma once

#include <string>
#include <stdexcept>
#include <chrono>
#include <array>

#include <GLFW/glfw3.h>

#include "PMMA_Core.hpp"

class CPP_ColorConverter;

class CPP_Display {
    private:
        unsigned int Size[2] = {0, 0};
        std::string Caption = "PMMA Display";
        bool FullScreen;
        bool Resizable;
        bool NoFrame;
        bool Vsync;
        std::string Icon;
        bool Centered;
        bool Maximized;
        float RefreshTime = 0.000001f;
        std::chrono::high_resolution_clock::time_point StartTime = std::chrono::high_resolution_clock::now();

        GLFWmonitor* Monitor = nullptr;
        GLFWwindow* Window = nullptr;

        CPP_ColorConverter* WindowFillColor = nullptr;

    public:
        CPP_Display(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude);

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

        void SetRelativeWindowPosition(unsigned int* Position);

        void SetAbsoluteWindowPosition(unsigned int* Position);

        void CenterWindow();

        void Clear();

        void SetWindowInFocus();

        void SetWindowMinimized(bool IsMinimized);

        void SetWindowMaximized(bool IsMaximized);

        void SetCaption(std::string& new_caption);

        std::string GetCaption();

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

        void Refresh(
            unsigned int RefreshRate,
            bool Minimized,
            bool FocusLoss,
            bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery);

        void Refresh();

        ~CPP_Display();

        // WIPs

        inline unsigned int GetFrameRate();

        inline float GetFrameTime();

        void GetDisplayProjection();

        void Get_2D_Surface(bool SetToBeUsed=true);

        void Get_3D_Surface(bool SetToBeUsed=true);

        void SetIcon();

        void ToggleFullScreen();
};