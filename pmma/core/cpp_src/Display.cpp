#include <iostream>
#include <string>
#include <stdexcept>

#include <GLFW/glfw3.h>

#include "Display.hpp"

#include "Registry.hpp"
#include "Components.hpp"

using namespace std;

CPP_Display::CPP_Display() {
    if (CPP_Components::display != nullptr) {
        CPP_Components::display->~CPP_Display();
    }
    CPP_Components::display = this;
}

GLFWmonitor* CPP_Display::GetTargetMonitor(GLFWwindow* window) {
    int Window_X_Position, Window_Y_Position;
    glfwGetWindowPos(window, &Window_X_Position, &Window_Y_Position);

    double Mouse_X_Position, Mouse_Y_Position;
    glfwGetCursorPos(window, &Mouse_X_Position, &Mouse_Y_Position);

    int AbsoluteMouse_X_Position = (int)Mouse_X_Position + Window_X_Position;
    int AbsoluteMouse_Y_Position = (int)Mouse_Y_Position + Window_Y_Position;
    int count;

    GLFWmonitor** monitors = glfwGetMonitors(&count);

    for (int i = 0; i < count; i++) {
        int mx, my;
        glfwGetMonitorPos(monitors[i], &mx, &my);
        const GLFWvidmode* mode = glfwGetVideoMode(monitors[i]);

        if (AbsoluteMouse_X_Position >= mx && AbsoluteMouse_X_Position < mx + mode->width &&
            AbsoluteMouse_Y_Position >= my && AbsoluteMouse_Y_Position < my + mode->height) {
            // Found the monitor where the mouse cursor is
            return monitors[i];
        }
    }

    // Fallback
    return glfwGetPrimaryMonitor();
}

GLFWmonitor* CPP_Display::GetCurrentMonitor(GLFWwindow* window) {
    int Window_X_Position, Window_Y_Position;
    glfwGetWindowPos(window, &Window_X_Position, &Window_Y_Position);

    int count;
    GLFWmonitor** monitors = glfwGetMonitors(&count);

    for (int i = 0; i < count; i++) {
        int mx, my;
        glfwGetMonitorPos(monitors[i], &mx, &my);
        const GLFWvidmode* mode = glfwGetVideoMode(monitors[i]);

        if (Window_X_Position >= mx && Window_X_Position < mx + mode->width &&
            Window_Y_Position >= my && Window_Y_Position < my + mode->height) {
            // Found the monitor where the window is
            return monitors[i];
        }
    }

    // Fallback
    return glfwGetPrimaryMonitor();
}

void CPP_Display::Create(unsigned int* NewSize, std::string& NewCaption, std::string& NewIcon, bool NewFullScreen, bool NewResizable, bool NewNoFrame, bool NewVsync, bool NewCentered, bool NewMaximized) {
    if (!CPP_Registry::Is_GLFW_Initialized) {
        glfwInit();
        CPP_Registry::Is_GLFW_Initialized = true;
    }
    CPP_Registry::GLFW_References++;

    Caption = NewCaption;
    FullScreen = NewFullScreen;
    Resizable = NewResizable;
    NoFrame = NewNoFrame;
    Vsync = NewVsync;
    Icon = NewIcon;
    Centered = NewCentered;
    Maximized = NewMaximized;

    glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
    GLFWwindow* TemporaryWindow = glfwCreateWindow(1, 1, Caption.c_str(), NULL, NULL);
    if (!TemporaryWindow) {
        throw runtime_error("Failed to create GLFW window");

        CPP_Registry::GLFW_References--;
        if (CPP_Registry::GLFW_References <= 0) {
            glfwTerminate();
            CPP_Registry::Is_GLFW_Initialized = false;
        }
    return;
    }

    int TemporaryWindow_X_Position, TemporaryWindow_Y_Position;
    glfwGetWindowPos(TemporaryWindow, &TemporaryWindow_X_Position, &TemporaryWindow_Y_Position);

    GLFWmonitor* CurrentMonitor = GetCurrentMonitor(TemporaryWindow);
    int CurrentMonitor_X_Position, CurrentMonitor_Y_Position;
    glfwGetMonitorPos(CurrentMonitor, &CurrentMonitor_X_Position, &CurrentMonitor_Y_Position);

    int RelativeWindow_X_Position, RelativeWindow_Y_Position;
    RelativeWindow_X_Position = TemporaryWindow_X_Position - CurrentMonitor_X_Position;
    RelativeWindow_Y_Position = TemporaryWindow_Y_Position - CurrentMonitor_Y_Position;

    GLFWmonitor* TargetMonitor = GetTargetMonitor(TemporaryWindow);
    glfwDestroyWindow(TemporaryWindow);
    glfwWindowHint(GLFW_VISIBLE, GLFW_TRUE);

    int TargetMonitor_X_Position, TargetMonitor_Y_Position;
    glfwGetMonitorPos(TargetMonitor, &TargetMonitor_X_Position, &TargetMonitor_Y_Position);

    const GLFWvidmode* Mode = glfwGetVideoMode(TargetMonitor);
    int Monitor_Width = Mode->width;
    int Monitor_Height = Mode->height;

    if (RelativeWindow_X_Position > Monitor_Width - Size[0]) {
        RelativeWindow_X_Position = Monitor_Width - Size[0];
    }
    if (RelativeWindow_Y_Position > Monitor_Height - Size[1]) {
        RelativeWindow_Y_Position = Monitor_Height - Size[1];
    }
    if (RelativeWindow_X_Position < 0) {
        RelativeWindow_X_Position = 0;
    }
    if (RelativeWindow_Y_Position < 0) {
        RelativeWindow_Y_Position = 0;
    }

    int Window_X_Offset = TargetMonitor_X_Position + RelativeWindow_X_Position;
    int Window_Y_Offset = TargetMonitor_Y_Position + RelativeWindow_Y_Position;

    if (NewSize[0] > 0) {
        Size[0] = NewSize[0];
    } else {
        Size[0] = Monitor_Width;
    }

    if (NewSize[1] > 0) {
        Size[1] = NewSize[1];
    } else {
        Size[1] = Monitor_Height;
    }

    if (FullScreen) {
        Window = glfwCreateWindow(Size[0], Size[1], Caption.c_str(), TargetMonitor, NULL);
    } else {
        Window = glfwCreateWindow(Size[0], Size[1], Caption.c_str(), NULL, NULL);

        if (Centered) {
            int Window_X_Offset = TargetMonitor_X_Position + (Monitor_Width - Size[0]) / 2;
            int Window_Y_Offset = TargetMonitor_Y_Position + (Monitor_Height - Size[1]) / 2;
        }
        glfwSetWindowPos(Window, Window_X_Offset, Window_Y_Offset);
    }

    if (!Window) {
        throw runtime_error("Failed to create GLFW window");

        CPP_Registry::GLFW_References--;
        if (CPP_Registry::GLFW_References <= 0) {
            glfwTerminate();
            CPP_Registry::Is_GLFW_Initialized = false;
        }
        return;
    }

    glfwMakeContextCurrent(Window);
}

void CPP_Display::SetWindowInFocus() {
    if (Window == nullptr) {
        throw std::runtime_error("Display not created yet!");
    }

    glfwFocusWindow(Window);
}

void CPP_Display::SetWindowMinimized(bool IsMinimized) {
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

void CPP_Display::SetWindowMaximized(bool IsMaximized) {
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

CPP_Display::~CPP_Display() {
    glfwDestroyWindow(Window);
    Window = nullptr;

    CPP_Registry::GLFW_References--;
    if (CPP_Registry::GLFW_References <= 0) {
        glfwTerminate();
        CPP_Registry::Is_GLFW_Initialized = false;
    }

    CPP_Components::display = nullptr;
}