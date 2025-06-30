#include <iostream>
#include <string>
#include <stdexcept>
#include <chrono>
#include <thread>

#include <glad/gl.h>
#include <GLFW/glfw3.h>

#include "Display.hpp"
#include "NumberConverter.hpp"
#include "RenderPipelineCore.hpp"

#include "PMMA_Core.hpp"

using namespace std;

void CPP_Display::PMMA_Update(GLFWwindow* Window) {
    if (PMMA::KeyManagerInstance == nullptr) {
        if (PMMA::KeyboardEventInstanceCount > 0) {
            PMMA::KeyManagerInstance = new CPP_InternalKeyEventManager();
            glfwSetKeyCallback(Window, CPP_InternalKeyEventManager::KeyCallback);
        }
    } else {
        if (PMMA::KeyboardEventInstanceCount <= 0) {
            glfwSetKeyCallback(Window, nullptr);
            delete PMMA::KeyManagerInstance;
            PMMA::KeyManagerInstance = nullptr;
            PMMA::KeyboardEventInstanceCount = 0;
        } else {
            PMMA::KeyManagerInstance->Update(Window);
        }
    }

    if (PMMA::TextManagerInstance == nullptr) {
        if (PMMA::TextEventInstanceCount > 0) {
            PMMA::TextManagerInstance = new CPP_InternalTextEventManager();
            glfwSetCharCallback(Window, CPP_InternalTextEventManager::TextCallback);
        }
    } else {
        if (PMMA::TextEventInstanceCount <= 0) {
            glfwSetCharCallback(Window, nullptr);
            delete PMMA::TextManagerInstance;
            PMMA::TextManagerInstance = nullptr;
            PMMA::TextEventInstanceCount = 0;
        } else {
            PMMA::TextManagerInstance->Update(Window);
        }
    }

    if (PMMA::MousePositionManagerInstance == nullptr) {
        if (PMMA::MousePositionEventInstanceCount > 0) {
            PMMA::MousePositionManagerInstance = new CPP_InternalMousePositionEventManager();
            glfwSetCursorPosCallback(Window, CPP_InternalMousePositionEventManager::CursorPositionCallback);
        }
    } else {
        if (PMMA::MousePositionEventInstanceCount <= 0) {
            glfwSetCursorPosCallback(Window, nullptr);
            delete PMMA::MousePositionManagerInstance;
            PMMA::MousePositionManagerInstance = nullptr;
            PMMA::MousePositionEventInstanceCount = 0;
        } else {
            PMMA::MousePositionManagerInstance->Update(Window);
        }
    }

    if (PMMA::MouseEnterWindowManagerInstance == nullptr) {
        if (PMMA::MouseEnterWindowEventInstanceCount > 0) {
            PMMA::MouseEnterWindowManagerInstance = new CPP_InternalMouseEnterWindowEventManager();
            glfwSetCursorEnterCallback(Window, CPP_InternalMouseEnterWindowEventManager::CursorEnterCallback);
        }
    } else {
        if (PMMA::MouseEnterWindowEventInstanceCount <= 0) {
            glfwSetCursorEnterCallback(Window, nullptr);
            delete PMMA::MouseEnterWindowManagerInstance;
            PMMA::MouseEnterWindowManagerInstance = nullptr;
            PMMA::MouseEnterWindowEventInstanceCount = 0;
        } else {
            PMMA::MouseEnterWindowManagerInstance->Update(Window);
        }
    }

    if (PMMA::MouseButtonManagerInstance == nullptr) {
        if (PMMA::MouseButtonEventInstanceCount > 0) {
            PMMA::MouseButtonManagerInstance = new CPP_InternalMouseButtonEventManager();
            glfwSetMouseButtonCallback(Window, CPP_InternalMouseButtonEventManager::MouseButtonCallback);
        }
    } else {
        if (PMMA::MouseButtonEventInstanceCount <= 0) {
            glfwSetMouseButtonCallback(Window, nullptr);
            delete PMMA::MouseButtonManagerInstance;
            PMMA::MouseButtonManagerInstance = nullptr;
            PMMA::MouseButtonEventInstanceCount = 0;
        } else {
            PMMA::MouseButtonManagerInstance->Update(Window);
        }
    }

    if (PMMA::MouseScrollManagerInstance == nullptr) {
        if (PMMA::MouseScrollEventInstanceCount > 0) {
            PMMA::MouseScrollManagerInstance = new CPP_InternalMouseScrollEventManager();
            glfwSetScrollCallback(Window, CPP_InternalMouseScrollEventManager::ScrollCallback);
        }
    } else {
        if (PMMA::MouseScrollEventInstanceCount <= 0) {
            glfwSetScrollCallback(Window, nullptr);
            delete PMMA::MouseScrollManagerInstance;
            PMMA::MouseScrollManagerInstance = nullptr;
            PMMA::MouseScrollEventInstanceCount = 0;
        } else {
            PMMA::MouseScrollManagerInstance->Update(Window);
        }
    }

    if (PMMA::ControllerManagerInstance == nullptr) {
        if (PMMA::ControllerEventInstanceCount > 0) {
            PMMA::ControllerManagerInstance = new CPP_InternalControllerEventManager();
            glfwSetJoystickCallback(CPP_InternalControllerEventManager::JoystickCallback);
        }
    } else {
        if (PMMA::ControllerEventInstanceCount <= 0) {
            glfwSetJoystickCallback(nullptr);
            delete PMMA::ControllerManagerInstance;
            PMMA::ControllerManagerInstance = nullptr;
            PMMA::ControllerEventInstanceCount = 0;
        } else {
            PMMA::ControllerManagerInstance->Update(Window);
        }
    }

    if (PMMA::DropManagerInstance == nullptr) {
        if (PMMA::DropEventInstanceCount > 0) {
            PMMA::DropManagerInstance = new CPP_InternalDropEventManager();
            glfwSetDropCallback(Window, CPP_InternalDropEventManager::DropCallback);
        }
    } else {
        if (PMMA::DropEventInstanceCount <= 0) {
            glfwSetDropCallback(Window, nullptr);
            delete PMMA::DropManagerInstance;
            PMMA::DropManagerInstance = nullptr;
            PMMA::DropEventInstanceCount = 0;
        } else {
            PMMA::DropManagerInstance->Update(Window);
        }
    }
}

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

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);

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

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);

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

    int version = gladLoadGL(glfwGetProcAddress);
    cout << "OpenGL version: " << GLAD_VERSION_MAJOR(version) << "." << GLAD_VERSION_MINOR(version) << endl;

    if (Vsync) {
        glfwSwapInterval(1);
    } else {
        glfwSwapInterval(0);
        cout << "You are not using vsync. We strongly recommend using \
vsync to limit the refresh rate of your window. Doing so will reduce \
visual tearing and improve frame pacing." << endl;
    }


    PMMA::RenderPipelineCore = new CPP_RenderPipelineCore();
}

void CPP_Display::Clear(float* in_color) {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    WindowFillColor->SetColor_rgba(in_color);
    glClearColor(in_color[0], in_color[1], in_color[2], in_color[3]);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    PMMA::RenderPipelineCore->Clear();
}

void CPP_Display::Clear() {
    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    float out_color[4];
    WindowFillColor->GetColor_rgba(out_color);
    glClearColor(out_color[0], out_color[1], out_color[2], out_color[3]);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    PMMA::RenderPipelineCore->Clear();
}

void CPP_Display::LimitRefreshRate(unsigned int RefreshRate, bool Minimized, bool FocusLoss, bool LowBattery) {
    if (Vsync) {
        return;
    }

    RefreshRate = CPP_Display::CalculateRefreshRate(RefreshRate, Minimized, FocusLoss, LowBattery);

    float estimate = 0.001f;
    float average = 0.001f;
    unsigned int samples = 1;

    std::chrono::high_resolution_clock::time_point EndTime = chrono::high_resolution_clock::now();
    chrono::duration<float> FrameDuration = EndTime - StartTime;
    RefreshTime = chrono::duration<float>(EndTime - StartTime).count();

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

    StartTime = chrono::high_resolution_clock::now();
}

void CPP_Display::ContinuousRefresh(
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

    PMMA::RenderPipelineCore->Render();

    glfwSwapBuffers(Window);
    glfwPollEvents();

    PMMA_Update(Window);

    if (RefreshRate > 0) {
        LimitRefreshRate(RefreshRate, Minimized, FocusLoss, LowBattery);
    }
}

void CPP_Display::EventRefresh(
            unsigned int RefreshRate,
            unsigned int MaxRefreshRate,
            bool Minimized,
            bool FocusLoss,
            bool LowBattery,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) {

    if (Window == nullptr) {
        throw runtime_error("Display not created yet!");
    }

    PMMA::RenderPipelineCore->Render();

    glfwSwapBuffers(Window);

    MaxRefreshRate = CPP_Display::CalculateRefreshRate(MaxRefreshRate, Minimized, FocusLoss, LowBattery);

    if (RefreshRate == 0) {
        glfwWaitEvents();
    } else {
        glfwWaitEventsTimeout(1.0f / RefreshRate);
    }

    PMMA_Update(Window);

    if (MaxRefreshRate > 0) {
        LimitRefreshRate(MaxRefreshRate, Minimized, FocusLoss, LowBattery);
    }
}

CPP_Display::~CPP_Display() {
    if (PMMA::RenderPipelineCore != nullptr) {
        delete PMMA::RenderPipelineCore;
        PMMA::RenderPipelineCore = nullptr;
    }

    if (PMMA::KeyManagerInstance != nullptr) {
        delete PMMA::KeyManagerInstance;
        PMMA::KeyManagerInstance = nullptr;
    }

    if (PMMA::TextManagerInstance != nullptr) {
        delete PMMA::TextManagerInstance;
        PMMA::TextManagerInstance = nullptr;
    }

    if (PMMA::MousePositionManagerInstance != nullptr) {
        delete PMMA::MousePositionManagerInstance;
        PMMA::MousePositionManagerInstance = nullptr;
    }

    if (PMMA::MouseEnterWindowManagerInstance != nullptr) {
        delete PMMA::MouseEnterWindowManagerInstance;
        PMMA::MouseEnterWindowManagerInstance = nullptr;
    }

    if (PMMA::MouseButtonManagerInstance != nullptr) {
        delete PMMA::MouseButtonManagerInstance;
        PMMA::MouseButtonManagerInstance = nullptr;
    }

    if (PMMA::MouseScrollManagerInstance != nullptr) {
        delete PMMA::MouseScrollManagerInstance;
        PMMA::MouseScrollManagerInstance = nullptr;
    }

    if (PMMA::ControllerManagerInstance != nullptr) {
        delete PMMA::ControllerManagerInstance;
        PMMA::ControllerManagerInstance = nullptr;
    }

    if (PMMA::DropManagerInstance != nullptr) {
        delete PMMA::DropManagerInstance;
        PMMA::DropManagerInstance = nullptr;
    }

    glfwDestroyWindow(Window);
    Window = nullptr;

    PMMA::GLFW_References--;
    if (PMMA::GLFW_References <= 0) {
        PMMA::GLFW_Initialized = false;
        glfwTerminate();
    }

    PMMA::DisplayInstance = nullptr;
}