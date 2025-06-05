#pragma once

#include <string>
#include <stdexcept>

#include <GLFW/glfw3.h>

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

        GLFWmonitor* Monitor = nullptr;
        GLFWwindow* Window = nullptr;

    public:
        CPP_Display();

        void Create(unsigned int* NewSize, std::string& NewCaption, std::string& NewIcon, bool NewFullScreen=true, bool NewResizable=false, bool NewNoFrame=false, bool NewVsync=true, bool NewCentered=true, bool NewMaximized=false);

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

        // WIPs

        void SetRelativeWindowPosition(unsigned int* Position);

        void SetAbsoluteWindowPosition(unsigned int* Position);

        void CenterWindow();

        void Clear(); // Need to make number converters for this.

        void SetWindowInFocus();

        void SetWindowMinimized(bool IsMinimized);

        void SetWindowMaximized(bool IsMaximized);

        void Get_2D_Surface(bool SetToBeUsed=true);

        void Get_3D_Surface(bool SetToBeUsed=true);

        void SetCaption(std::string& new_caption);

        std::string GetCaption();

        void SetIcon();

        void ToggleFullScreen();

        inline float GetAspectRatio() {
            if (Window == nullptr) {
                throw std::runtime_error("Display not created yet!");
            }
            return (float)Size[0] / (float)Size[1];
        }

        void Refresh(
            unsigned int RefreshRate,
            bool LowerRefreshRate_OnMinimize=true,
            bool LowerRefreshRate_OnFocusLoss=true,
            bool LowerRefreshRate_OnLowBattery=true);

        inline unsigned int GetFrameRate();

        inline float GetFrameTime();

        inline void GetCenter_Pixels(unsigned int* out) {
            out[0] = (unsigned int)(Size[0] / 2);
            out[1] = (unsigned int)(Size[1] / 2);
        }

        inline void GetCenter_Pixels(unsigned int* ObjectSize, unsigned int* out) {
            out[0] = (unsigned int)((Size[0] - ObjectSize[0]) / 2);
            out[1] = (unsigned int)((Size[1] - ObjectSize[1]) / 2);
        }

        void GetDisplayProjection();

        ~CPP_Display();
};