#include <iostream>
#include <string>
#include <stdexcept>

#include <GLFW/glfw3.h>

#include "Display.hpp"
#include "PMMA_Core.hpp"

using namespace std;

CPP_Display::CPP_Display() {
    CPP_Display* ExistingDisplay;

    ExistingDisplay = GetDisplayInstance();
    if (ExistingDisplay != nullptr) {
        delete ExistingDisplay;
        ExistingDisplay = nullptr;
    }
    SetDisplayInstance(this);
}

GLFWmonitor* CPP_Display::GetMonitorAtPoint(unsigned int* Point) {
    int count;

    GLFWmonitor** monitors = glfwGetMonitors(&count);

    for (int i = 0; i < count; i++) {
        int mx, my;
        glfwGetMonitorPos(monitors[i], &mx, &my);

        unsigned int Monitor_X_Position = (unsigned int)mx;
        unsigned int Monitor_Y_Position = (unsigned int)my;

        const GLFWvidmode* mode = glfwGetVideoMode(monitors[i]);

        if (Point[0] >= Monitor_X_Position && Point[0] < Monitor_X_Position + mode->width &&
            Point[1] >= Monitor_Y_Position && Point[1] < Monitor_Y_Position + mode->height) {
            // Found the monitor where the mouse cursor is
            return monitors[i];
        }
    }

    // Fallback
    return glfwGetPrimaryMonitor();
}

GLFWmonitor* CPP_Display::GetTargetMonitor(GLFWwindow* window) {
    int Window_X_Position, Window_Y_Position;
    glfwGetWindowPos(window, &Window_X_Position, &Window_Y_Position);

    double Mouse_X_Position, Mouse_Y_Position;
    glfwGetCursorPos(window, &Mouse_X_Position, &Mouse_Y_Position);

    unsigned int Point[2] = { (unsigned int)(Mouse_X_Position + Window_X_Position), (unsigned int)(Mouse_Y_Position + Window_Y_Position) };

    return GetMonitorAtPoint(Point);
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
    if (!Get_GLFW_Initialized()) {
        glfwInit();
        Set_GLFW_Initialized(true);
    }

    Set_GLFW_References(Get_GLFW_References() + 1);

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

        int GLFW_References = Get_GLFW_References();
        GLFW_References--;
        Set_GLFW_References(GLFW_References);
        if (GLFW_References <= 0) {
            glfwTerminate();
            Set_GLFW_Initialized(false);
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

        int GLFW_References = Get_GLFW_References();
        GLFW_References--;
        Set_GLFW_References(GLFW_References);
        if (GLFW_References <= 0) {
            glfwTerminate();
            Set_GLFW_Initialized(false);
        }
        return;
    }

    glfwMakeContextCurrent(Window);
}

void CPP_Display::SetWindowInFocus() {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glfwFocusWindow(Window);
}

void CPP_Display::SetWindowMinimized(bool IsMinimized) {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
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
        throw runtime_error("Display not created yet!");
    }

    if (IsMaximized) {
        glfwMaximizeWindow(Window);
    }
    else {
        glfwRestoreWindow(Window);
    }
}

void CPP_Display::SetRelativeWindowPosition(unsigned int* NewPosition) {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glfwSetWindowPos(Window, NewPosition[0], NewPosition[1]);
}

void CPP_Display::SetAbsoluteWindowPosition(unsigned int* NewPosition) {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    GLFWmonitor* PointMonitor = GetMonitorAtPoint(NewPosition);

    int Monitor_X_Position, Monitor_Y_Position;
    glfwGetMonitorPos(PointMonitor, &Monitor_X_Position, &Monitor_Y_Position);
    glfwSetWindowPos(Window, NewPosition[0] - Monitor_X_Position, NewPosition[1] - Monitor_Y_Position);
}

CPP_Display::~CPP_Display() {
    glfwDestroyWindow(Window);
    Window = nullptr;

    int GLFW_References = Get_GLFW_References();
    GLFW_References--;
    Set_GLFW_References(GLFW_References);
    if (GLFW_References <= 0) {
        glfwTerminate();
        Set_GLFW_Initialized(false);
    }

    SetDisplayInstance(nullptr);
}