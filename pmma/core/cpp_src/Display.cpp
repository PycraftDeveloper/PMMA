#include <iostream>
#include <string>
#include <stdexcept>
#include <chrono>
#include <thread>
#include <array>

#include <GLFW/glfw3.h>

#include "Display.hpp"
#include "NumberConverter.hpp"
#include "InternalEventsManager.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_Display::CPP_Display(uint32_t new_seed, uint32_t new_octaves, float new_frequency, float new_amplitude) {
    if (PMMA::DisplayInstance != nullptr) {
        delete PMMA::DisplayInstance;
        PMMA::DisplayInstance = nullptr;
    }
    PMMA::DisplayInstance = this;

    WindowFillColor = new CPP_ColorConverter(new_seed, new_octaves, new_frequency, new_amplitude);

    if (!PMMA::GLFW_Initialized) {
        glfwInit();
        PMMA::GLFW_Initialized = true;
    }

    PMMA::GLFW_References++;
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

void CPP_Display::Create(unsigned int* NewSize, std::string& NewCaption, std::string& NewIcon, bool NewFullScreen, bool NewResizable, bool NewNoFrame, bool NewVsync, bool NewCentered, bool NewMaximized, bool Transparent) {
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

        PMMA::GLFW_References--;
        if (PMMA::GLFW_References <= 0) {
            PMMA::GLFW_Initialized = false;
            glfwTerminate();
        }
        return;
    }

    int TemporaryWindow_X_Position, TemporaryWindow_Y_Position;
    glfwGetWindowPos(TemporaryWindow, &TemporaryWindow_X_Position, &TemporaryWindow_Y_Position);

    GLFWmonitor* CurrentMonitor = GetCurrentMonitor(TemporaryWindow);
    int CurrentMonitor_X_Position, CurrentMonitor_Y_Position;
    glfwGetMonitorPos(CurrentMonitor, &CurrentMonitor_X_Position, &CurrentMonitor_Y_Position);

    unsigned int RelativeWindow_X_Position, RelativeWindow_Y_Position;
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

    if (Transparent) {
        if (!WindowFillColor->GetColorIsSet()) {
            WindowFillColor->SetColor_rgba(new float[4] {0, 0, 0, 0});
        }
        glfwWindowHint(GLFW_TRANSPARENT_FRAMEBUFFER, GLFW_TRUE);
        cout << "You have specified that this window should be transparent. \
Please note that this isn't guaranteed and relies on the Operating System, \
GPU/drivers and device settings to be set correctly in order to work." << endl;
    } else {
        if (!WindowFillColor->GetColorIsSet()) {
            WindowFillColor->SetColor_rgba(new float[4] {0, 0, 0, 1});
        }
        glfwWindowHint(GLFW_TRANSPARENT_FRAMEBUFFER, GLFW_FALSE);
    }

    if (Resizable) {
        glfwWindowHint(GLFW_RESIZABLE, GLFW_TRUE);
    } else {
        glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
    }

    if (NoFrame) {
        glfwWindowHint(GLFW_DECORATED, GLFW_FALSE);
    } else {
        glfwWindowHint(GLFW_DECORATED, GLFW_TRUE);
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

        PMMA::GLFW_References--;
        if (PMMA::GLFW_References <= 0) {
            PMMA::GLFW_Initialized = false;
            glfwTerminate();
        }
        return;
    }

    glfwMakeContextCurrent(Window);

    if (Vsync) {
        glfwSwapInterval(1);
    } else {
        glfwSwapInterval(0);
        cout << "You are not using vsync. We strongly recommend using \
vsync to limit the refresh rate of your window. Doing so will reduce \
visual tearing and improve frame pacing." << endl;
    }

    EventsManagerInstance = new CPP_EventsManager(Window);
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

void CPP_Display::CenterWindow() {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
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

void CPP_Display::Clear(float* in_color) {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    WindowFillColor->SetColor_rgba(in_color);
    glClearColor(in_color[0], in_color[1], in_color[2], in_color[3]);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

void CPP_Display::Clear() {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    float out_color[4];
    WindowFillColor->GetColor_rgba(out_color);
    glClearColor(out_color[0], out_color[1], out_color[2], out_color[3]);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

void CPP_Display::SetCaption(string& new_caption) {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glfwSetWindowTitle(Window, new_caption.c_str());
    Caption = new_caption;
}

string CPP_Display::GetCaption() {
    return Caption;
}

void CPP_Display::Refresh(
            unsigned int RefreshRate,
            bool Minimized,
            bool FocusLoss,
            bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) {

    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glfwSwapBuffers(Window);
    glfwPollEvents();

    EventsManagerInstance->GenericUpdate(Window);

    float estimate = 0.001f;
    float average = 0.001f;
    unsigned int samples = 1;

    std::chrono::high_resolution_clock::time_point EndTime = chrono::high_resolution_clock::now();
    chrono::duration<float> FrameDuration = EndTime - StartTime;
    RefreshTime = chrono::duration<float>(EndTime - StartTime).count();

    if (!Vsync || Minimized || FocusLoss || LowBattery) {
        float TargetFrameTime = 1.0f / static_cast<float>(RefreshRate);
        float SleepTime = TargetFrameTime - FrameDuration.count();

        while (SleepTime > average) {
            std::chrono::high_resolution_clock::time_point s = chrono::high_resolution_clock::now();
            std::this_thread::sleep_for(std::chrono::milliseconds(1));
            std::chrono::high_resolution_clock::time_point e = chrono::high_resolution_clock::now();
            estimate = chrono::duration<float>(e - s).count();
            average = (average * samples + estimate) / (samples + 1);
            samples += 1;
            SleepTime -= average;
        }

        std::chrono::high_resolution_clock::time_point s = chrono::high_resolution_clock::now();
        while (chrono::duration<float>(chrono::high_resolution_clock::now() - s).count() < SleepTime) {
        }
    }

    StartTime = chrono::high_resolution_clock::now();
}

void CPP_Display::Refresh() {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    glfwSwapBuffers(Window);
    glfwPollEvents();

    EventsManagerInstance->GenericUpdate(Window);
}

CPP_Display::~CPP_Display() {
    delete EventsManagerInstance;
    EventsManagerInstance = nullptr;

    glfwDestroyWindow(Window);
    Window = nullptr;

    PMMA::GLFW_References--;
    if (PMMA::GLFW_References <= 0) {
        PMMA::GLFW_Initialized = false;
        glfwTerminate();
    }

    PMMA::DisplayInstance = nullptr;
}