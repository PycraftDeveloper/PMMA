#include <GLFW/glfw3.h>
#include <STB/stb_image.h>
#include <bx/platform.h>
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

// For native window handles via GLFW
#if BX_PLATFORM_WINDOWS
    #define GLFW_EXPOSE_NATIVE_WIN32
    #include <GLFW/glfw3native.h>
#elif BX_PLATFORM_LINUX || BX_PLATFORM_BSD
    #define GLFW_EXPOSE_NATIVE_X11
    #define GLFW_EXPOSE_NATIVE_WAYLAND
    #include <GLFW/glfw3native.h>
#elif BX_PLATFORM_OSX
    #define GLFW_EXPOSE_NATIVE_COCOA
    #include <GLFW/glfw3native.h>
#endif

#include "PMMA_Core.hpp"

using namespace std;

void CPP_Display::PMMA_Update(GLFWwindow* Window) {
    if (PMMA_Core::KeyManagerInstance == nullptr) {
        if (PMMA_Registry::KeyboardEventInstanceCount > 0) {
            PMMA_Core::KeyManagerInstance = new CPP_InternalKeyEventManager();
            glfwSetKeyCallback(Window, CPP_InternalKeyEventManager::KeyCallback);
        }
    } else {
        if (PMMA_Registry::KeyboardEventInstanceCount <= 0) {
            glfwSetKeyCallback(Window, nullptr);
            delete PMMA_Core::KeyManagerInstance;
            PMMA_Core::KeyManagerInstance = nullptr;
            PMMA_Registry::KeyboardEventInstanceCount = 0;
        } else {
            PMMA_Core::KeyManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::TextManagerInstance == nullptr) {
        if (PMMA_Registry::TextEventInstanceCount > 0) {
            PMMA_Core::TextManagerInstance = new CPP_InternalTextEventManager();
            glfwSetCharCallback(Window, CPP_InternalTextEventManager::TextCallback);
        }
    } else {
        if (PMMA_Registry::TextEventInstanceCount <= 0) {
            glfwSetCharCallback(Window, nullptr);
            delete PMMA_Core::TextManagerInstance;
            PMMA_Core::TextManagerInstance = nullptr;
            PMMA_Registry::TextEventInstanceCount = 0;
        } else {
            PMMA_Core::TextManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::MousePositionManagerInstance == nullptr) {
        if (PMMA_Registry::MousePositionEventInstanceCount > 0) {
            PMMA_Core::MousePositionManagerInstance = new CPP_InternalMousePositionEventManager();
            glfwSetCursorPosCallback(Window, CPP_InternalMousePositionEventManager::CursorPositionCallback);
        }
    } else {
        if (PMMA_Registry::MousePositionEventInstanceCount <= 0) {
            glfwSetCursorPosCallback(Window, nullptr);
            delete PMMA_Core::MousePositionManagerInstance;
            PMMA_Core::MousePositionManagerInstance = nullptr;
            PMMA_Registry::MousePositionEventInstanceCount = 0;
        } else {
            PMMA_Core::MousePositionManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::MouseEnterWindowManagerInstance == nullptr) {
        if (PMMA_Registry::MouseEnterWindowEventInstanceCount > 0) {
            PMMA_Core::MouseEnterWindowManagerInstance = new CPP_InternalMouseEnterWindowEventManager();
            glfwSetCursorEnterCallback(Window, CPP_InternalMouseEnterWindowEventManager::CursorEnterCallback);
        }
    } else {
        if (PMMA_Registry::MouseEnterWindowEventInstanceCount <= 0) {
            glfwSetCursorEnterCallback(Window, nullptr);
            delete PMMA_Core::MouseEnterWindowManagerInstance;
            PMMA_Core::MouseEnterWindowManagerInstance = nullptr;
            PMMA_Registry::MouseEnterWindowEventInstanceCount = 0;
        } else {
            PMMA_Core::MouseEnterWindowManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::MouseButtonManagerInstance == nullptr) {
        if (PMMA_Registry::MouseButtonEventInstanceCount > 0) {
            PMMA_Core::MouseButtonManagerInstance = new CPP_InternalMouseButtonEventManager();
            glfwSetMouseButtonCallback(Window, CPP_InternalMouseButtonEventManager::MouseButtonCallback);
        }
    } else {
        if (PMMA_Registry::MouseButtonEventInstanceCount <= 0) {
            glfwSetMouseButtonCallback(Window, nullptr);
            delete PMMA_Core::MouseButtonManagerInstance;
            PMMA_Core::MouseButtonManagerInstance = nullptr;
            PMMA_Registry::MouseButtonEventInstanceCount = 0;
        } else {
            PMMA_Core::MouseButtonManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::MouseScrollManagerInstance == nullptr) {
        if (PMMA_Registry::MouseScrollEventInstanceCount > 0) {
            PMMA_Core::MouseScrollManagerInstance = new CPP_InternalMouseScrollEventManager();
            glfwSetScrollCallback(Window, CPP_InternalMouseScrollEventManager::ScrollCallback);
        }
    } else {
        if (PMMA_Registry::MouseScrollEventInstanceCount <= 0) {
            glfwSetScrollCallback(Window, nullptr);
            delete PMMA_Core::MouseScrollManagerInstance;
            PMMA_Core::MouseScrollManagerInstance = nullptr;
            PMMA_Registry::MouseScrollEventInstanceCount = 0;
        } else {
            PMMA_Core::MouseScrollManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::ControllerManagerInstance == nullptr) {
        if (PMMA_Registry::ControllerEventInstanceCount > 0) {
            PMMA_Core::ControllerManagerInstance = new CPP_InternalControllerEventManager();
            glfwSetJoystickCallback(CPP_InternalControllerEventManager::JoystickCallback);
        }
    } else {
        if (PMMA_Registry::ControllerEventInstanceCount <= 0) {
            glfwSetJoystickCallback(nullptr);
            delete PMMA_Core::ControllerManagerInstance;
            PMMA_Core::ControllerManagerInstance = nullptr;
            PMMA_Registry::ControllerEventInstanceCount = 0;
        } else {
            PMMA_Core::ControllerManagerInstance->Update(Window);
        }
    }

    if (PMMA_Core::DropManagerInstance == nullptr) {
        if (PMMA_Registry::DropEventInstanceCount > 0) {
            PMMA_Core::DropManagerInstance = new CPP_InternalDropEventManager();
            glfwSetDropCallback(Window, CPP_InternalDropEventManager::DropCallback);
        }
    } else {
        if (PMMA_Registry::DropEventInstanceCount <= 0) {
            glfwSetDropCallback(Window, nullptr);
            delete PMMA_Core::DropManagerInstance;
            PMMA_Core::DropManagerInstance = nullptr;
            PMMA_Registry::DropEventInstanceCount = 0;
        } else {
            PMMA_Core::DropManagerInstance->Update(Window);
        }
    }

    if (glfwWindowShouldClose(Window)) {
        PMMA_Registry::IsApplicationRunning = false;
    }

    if (!PMMA_Registry::UserSetEscapeKeyShouldCloseWindow) {
        PMMA_Registry::EscapeKeyShouldCloseWindow = FullScreen;
    }

    if (PMMA_Registry::EscapeKeyShouldCloseWindow && Escape_KeyEvent->GetPressed()) {
        PMMA_Registry::IsApplicationRunning = false;
    }

    if (PMMA_Registry::F11KeyShouldToggleFullScreen && F11_KeyEvent->GetPressed()) {
        ToggleFullScreen();
    }
}

CPP_Display::CPP_Display() {
    Logger = new CPP_Logger();

    if (PMMA_Core::DisplayInstance != nullptr) {
        Logger->InternalLogDebug(
            21,
            "A display instance already exists. The previous one will \
be destroyed, closing any windows the application has created. Continue \
use the current one instead, but consider properly garbage collecting \
the previous display object. We are looking to support multiple windows \
in future versions of PMMA, but it is not a priority.", false);
        delete PMMA_Core::DisplayInstance;
        PMMA_Core::DisplayInstance = nullptr;
    }
    PMMA_Core::DisplayInstance = this;

    WindowFillColor = new CPP_ColorFormat();

    if (!PMMA_Registry::GLFW_Initialized) {
        glfwInit();
        PMMA_Registry::GLFW_Initialized = true;
    }

    PMMA_Registry::GLFW_References++;

    DefaultIconPath = PMMA_Registry::PMMA_Location + PMMA_Registry::PathSeparator + "resources" + PMMA_Registry::PathSeparator + "Icon.png";

    F11_KeyEvent = new CPP_KeyEvent_F11();
    Escape_KeyEvent = new CPP_KeyEvent_Escape();
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

    unsigned int Point[2] = {
        (unsigned int)(Mouse_X_Position + Window_X_Position),
        (unsigned int)(Mouse_Y_Position + Window_Y_Position) };

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

void CPP_Display::Create(
        unsigned int* NewSize,
        std::string NewCaption,
        std::string NewIcon,
        bool NewFullScreen,
        bool NewResizable,
        bool NewNoFrame,
        bool NewVsync,
        bool NewCentered,
        bool NewMaximized,
        bool Transparent) {
    Caption = NewCaption;
    FullScreen = NewFullScreen;
    Resizable = NewResizable;
    NoFrame = NewNoFrame;
    Vsync = NewVsync;
    Centered = NewCentered;
    Maximized = NewMaximized;

    glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
    glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);
    GLFWwindow* TemporaryWindow = glfwCreateWindow(
        1,
        1,
        Caption.c_str(),
        NULL,
        NULL);
    if (!TemporaryWindow) {
        throw runtime_error("Failed to create GLFW window");

        PMMA_Registry::GLFW_References--;
        if (PMMA_Registry::GLFW_References <= 0) {
            PMMA_Registry::GLFW_Initialized = false;
            glfwTerminate();
        }
        return;
    }

    int TemporaryWindow_X_Position, TemporaryWindow_Y_Position;
    glfwGetWindowPos(
        TemporaryWindow,
        &TemporaryWindow_X_Position,
        &TemporaryWindow_Y_Position);

    GLFWmonitor* CurrentMonitor = GetCurrentMonitor(TemporaryWindow);
    int CurrentMonitor_X_Position, CurrentMonitor_Y_Position;
    glfwGetMonitorPos(
        CurrentMonitor,
        &CurrentMonitor_X_Position,
        &CurrentMonitor_Y_Position);

    unsigned int RelativeWindow_X_Position, RelativeWindow_Y_Position;
    RelativeWindow_X_Position = TemporaryWindow_X_Position - CurrentMonitor_X_Position;
    RelativeWindow_Y_Position = TemporaryWindow_Y_Position - CurrentMonitor_Y_Position;

    GLFWmonitor* TargetMonitor = GetTargetMonitor(TemporaryWindow);
    glfwDestroyWindow(TemporaryWindow);
    glfwWindowHint(GLFW_VISIBLE, GLFW_TRUE);

    int TargetMonitor_X_Position, TargetMonitor_Y_Position;
    glfwGetMonitorPos(
        TargetMonitor,
        &TargetMonitor_X_Position,
        &TargetMonitor_Y_Position);

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
        if (!WindowFillColor->GetSet()) {
            float fill_color[4] = {0, 0, 0, 0};
            WindowFillColor->Set_rgba(fill_color);
        }
        glfwWindowHint(GLFW_TRANSPARENT_FRAMEBUFFER, GLFW_TRUE);
        cout << "You have specified that this window should be transparent. \
Please note that this isn't guaranteed and relies on the Operating System, \
GPU/drivers and device settings to be set correctly in order to work." << endl;
    } else {
        if (!WindowFillColor->GetSet()) {
            float fill_color[4] = {0, 0, 0, 1};
            WindowFillColor->Set_rgba(fill_color);
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

    glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);

    if (FullScreen) {
        Window = glfwCreateWindow(
            Size[0],
            Size[1],
            Caption.c_str(),
            TargetMonitor,
            NULL);
    } else {
        Window = glfwCreateWindow(
            Size[0],
            Size[1],
            Caption.c_str(),
            NULL,
            NULL);

        if (Centered) {
            int Window_X_Offset = TargetMonitor_X_Position + (Monitor_Width - Size[0]) / 2;
            int Window_Y_Offset = TargetMonitor_Y_Position + (Monitor_Height - Size[1]) / 2;
        }
        Position[0] = Window_X_Offset;
        Position[1] = Window_Y_Offset;
        glfwSetWindowPos(Window, Window_X_Offset, Window_Y_Offset);
    }

    if (!Window) {
        throw runtime_error("Failed to create GLFW window");

        PMMA_Registry::GLFW_References--;
        if (PMMA_Registry::GLFW_References <= 0) {
            PMMA_Registry::GLFW_Initialized = false;
            glfwTerminate();
        }
        return;
    }

    bgfx::PlatformData pd{};
    pd.ndt          = nullptr;
    pd.nwh          = nullptr;
    pd.context      = nullptr;
    pd.backBuffer   = nullptr;
    pd.backBufferDS = nullptr;

    #if BX_PLATFORM_WINDOWS
        pd.nwh = glfwGetWin32Window(Window);
    #elif BX_PLATFORM_OSX
        pd.nwh = glfwGetCocoaWindow(Window);
    #elif BX_PLATFORM_LINUX || BX_PLATFORM_BSD
        if (glfwGetPlatform() == GLFW_PLATFORM_WAYLAND) {
            pd.ndt = glfwGetWaylandDisplay();
            pd.nwh = (void*)glfwGetWaylandWindow(Window);
        } else { // X11
            pd.ndt = glfwGetX11Display();
            pd.nwh = (void*)(uintptr_t)glfwGetX11Window(Window);
        }
    #endif

    //bgfx::setPlatformData(pd);

    bgfx::Init init;
    init.type = bgfx::RendererType::Count; // auto-detect renderer
    init.resolution.width  = Size[0];
    init.resolution.height = Size[1];
    init.resolution.reset  = Vsync ? BGFX_RESET_VSYNC : BGFX_RESET_NONE;
    init.platformData = pd;

    if (!bgfx::init(init)) {
        throw std::runtime_error("Failed to initialize BGFX");
    }

    bgfx::setViewClear(0, BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH, 0x000000ff, 1.0f, 0);
    bgfx::setViewRect(0, 0, 0, Size[0], Size[1]);

    if (!Vsync) {
        PMMA_Core::InternalLoggerInstance->InternalLogDebug(
            33,
            "You are not using vsync. We strongly recommend using \
vsync to limit the refresh rate of your window. Doing so will reduce \
visual tearing and improve frame pacing."
        );
    }

    if (NewIcon == "") {
        NewIcon = DefaultIconPath;
    }
    SetIcon(NewIcon);

    PMMA_Core::RenderPipelineCore = new CPP_RenderPipelineCore();
}

void CPP_Display::Clear() {
    if (Window == nullptr) {
        PMMA_Core::InternalLoggerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    unsigned int out_color[4];
    WindowFillColor->Get_RGBA(out_color);

    uint32_t clearColor =
    ( (uint8_t)(out_color[3]) << 24 ) | // A
    ( (uint8_t)(out_color[0]) << 16 ) | // R
    ( (uint8_t)(out_color[1]) <<  8 ) | // G
    ( (uint8_t)(out_color[2]) );        // B

    bgfx::setViewClear(
        0,  // view ID (use 0 for your main screen)
        BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH,
        clearColor,
        1.0f, // depth clear value
        0     // stencil clear value
    );

    PMMA_Core::RenderPipelineCore->Reset();

    if (PMMA_Core::AnimationManagerInstance != nullptr) {
        if (PMMA_Core::AnimationManagerInstance->Update()) { // returns true if no longer needed
            delete PMMA_Core::AnimationManagerInstance;
            PMMA_Core::AnimationManagerInstance = nullptr;
        }
    }
}

void CPP_Display::LimitRefreshRate(unsigned int RefreshRate) {
    RefreshRate = CPP_Display::CalculateRefreshRate(RefreshRate);

    float estimate = 0.001f;
    float average = 0.001f;
    unsigned int samples = 1;

    std::chrono::high_resolution_clock::time_point EndTime = chrono::high_resolution_clock::now();
    chrono::duration<float> FrameDuration = EndTime - StartTime;

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

unsigned int CPP_Display::CalculateRefreshRate(unsigned int RefreshRate) {
    bool Minimized = glfwGetWindowAttrib(Window, GLFW_ICONIFIED) == GLFW_TRUE;
    bool FocusLoss = glfwGetWindowAttrib(Window, GLFW_FOCUSED) == GLFW_FALSE;
    bool LowBattery = PMMA_Registry::IsPowerSavingModeEnabled;

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
        RefreshRate = max(RefreshRate, 5u);
    } else {
        RefreshRate = max(RefreshRate, RefreshRate / 2);
    }

    if (RefreshRate > OriginalRefreshRate) {
        RefreshRate = OriginalRefreshRate;
    }

    return RefreshRate;
}

void CPP_Display::ContinuousRefresh(
            unsigned int RefreshRate,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) {

    if (Window == nullptr) {
        PMMA_Core::InternalLoggerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    PMMA_Core::RenderPipelineCore->Render();

    bgfx::touch(0);   // Ensure view 0 is cleared
    bgfx::frame();
    glfwPollEvents();

    PMMA_Update(Window);

    if (RefreshRate > 0) {
        LimitRefreshRate(RefreshRate);
    }

    std::chrono::high_resolution_clock::time_point EndTime = chrono::high_resolution_clock::now();
    chrono::duration<float> FrameDuration = EndTime - StartTime;
    RefreshTime = chrono::duration<float>(EndTime - StartTime).count();

    StartTime = chrono::high_resolution_clock::now();
}

void CPP_Display::EventRefresh(
            unsigned int RefreshRate,
            unsigned int MaxRefreshRate,
            bool LowerRefreshRate_OnMinimize,
            bool LowerRefreshRate_OnFocusLoss,
            bool LowerRefreshRate_OnLowBattery) {

    if (Window == nullptr) {
        PMMA_Core::InternalLoggerInstance->InternalLogError(
            18,
            "You need to create a display before using this function. \
You can do this using `Display.create`."
        );
        throw runtime_error("Display not created yet!");
    }

    PMMA_Core::RenderPipelineCore->Render();

    bgfx::touch(0);   // Ensure view 0 is cleared
    bgfx::frame();

    MaxRefreshRate = CPP_Display::CalculateRefreshRate(
        MaxRefreshRate);

    if (RefreshRate == 0) {
        glfwWaitEvents();
    } else {
        glfwWaitEventsTimeout(1.0f / RefreshRate);
    }

    PMMA_Update(Window);

    if (MaxRefreshRate > 0) {
        LimitRefreshRate(MaxRefreshRate);
    }

    std::chrono::high_resolution_clock::time_point EndTime = chrono::high_resolution_clock::now();
    chrono::duration<float> FrameDuration = EndTime - StartTime;
    RefreshTime = chrono::duration<float>(EndTime - StartTime).count();

    StartTime = chrono::high_resolution_clock::now();
}

void CPP_Display::SetIcon(string IconPath) {
    if (IconPath == "") {
        IconPath = DefaultIconPath;
    }

    int width, height, channels;
    unsigned char* pixels = stbi_load(
        IconPath.c_str(),
        &width,
        &height,
        &channels,
        4);

    if (pixels) {
        GLFWimage icon;
        icon.width = width;
        icon.height = height;
        icon.pixels = pixels;

        glfwSetWindowIcon(Window, 1, &icon);
        stbi_image_free(pixels);  // Don’t forget to free the image
    } else {
        throw runtime_error("Failed to load icon: " + IconPath);
    }
}

void CPP_Display::ToggleFullScreen() {
    FullScreen = !FullScreen;

    unsigned int new_width, new_height;

    if (FullScreen) {
        GLFWmonitor* CurrentMonitor = GetCurrentMonitor(Window);
        int CurrentMonitor_X_Position, CurrentMonitor_Y_Position;
        int TemporaryWindow_X_Position, TemporaryWindow_Y_Position;
        glfwGetWindowPos(
            Window,
            &TemporaryWindow_X_Position,
            &TemporaryWindow_Y_Position);

        glfwGetMonitorPos(
            CurrentMonitor,
            &CurrentMonitor_X_Position,
            &CurrentMonitor_Y_Position);

        unsigned int RelativeWindow_X_Position, RelativeWindow_Y_Position;
        RelativeWindow_X_Position = TemporaryWindow_X_Position - CurrentMonitor_X_Position;
        RelativeWindow_Y_Position = TemporaryWindow_Y_Position - CurrentMonitor_Y_Position;

        GLFWmonitor* TargetMonitor = GetTargetMonitor(Window);

        glfwWindowHint(GLFW_VISIBLE, GLFW_TRUE);

        int TargetMonitor_X_Position, TargetMonitor_Y_Position;
        glfwGetMonitorPos(
            TargetMonitor,
            &TargetMonitor_X_Position,
            &TargetMonitor_Y_Position);

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
        Position[0] = Window_X_Offset;
        Position[1] = Window_Y_Offset;
        Size[0] = GetWidth();
        Size[1] = GetHeight();
        const GLFWvidmode* mode = glfwGetVideoMode(CurrentMonitor);
        glfwSetWindowMonitor(Window, CurrentMonitor, 0, 0, mode->width, mode->height, 0);
        new_width = mode->width;
        new_height = mode->height;
    } else {
        GLFWmonitor* CurrentMonitor = GetCurrentMonitor(Window);
        glfwSetWindowMonitor(Window, NULL, Position[0], Position[1], Size[0], Size[1], 0);
        new_width = Size[0];
        new_height = Size[1];
    }

    bgfx::setViewRect(0, 0, 0, uint16_t(new_width), uint16_t(new_height));
}

CPP_Display::~CPP_Display() {
    if (PMMA_Core::RenderPipelineCore != nullptr) {
        delete PMMA_Core::RenderPipelineCore;
        PMMA_Core::RenderPipelineCore = nullptr;
    }

    if (PMMA_Core::KeyManagerInstance != nullptr) {
        delete PMMA_Core::KeyManagerInstance;
        PMMA_Core::KeyManagerInstance = nullptr;
    }

    if (PMMA_Core::TextManagerInstance != nullptr) {
        delete PMMA_Core::TextManagerInstance;
        PMMA_Core::TextManagerInstance = nullptr;
    }

    if (PMMA_Core::MousePositionManagerInstance != nullptr) {
        delete PMMA_Core::MousePositionManagerInstance;
        PMMA_Core::MousePositionManagerInstance = nullptr;
    }

    if (PMMA_Core::MouseEnterWindowManagerInstance != nullptr) {
        delete PMMA_Core::MouseEnterWindowManagerInstance;
        PMMA_Core::MouseEnterWindowManagerInstance = nullptr;
    }

    if (PMMA_Core::MouseButtonManagerInstance != nullptr) {
        delete PMMA_Core::MouseButtonManagerInstance;
        PMMA_Core::MouseButtonManagerInstance = nullptr;
    }

    if (PMMA_Core::MouseScrollManagerInstance != nullptr) {
        delete PMMA_Core::MouseScrollManagerInstance;
        PMMA_Core::MouseScrollManagerInstance = nullptr;
    }

    if (PMMA_Core::ControllerManagerInstance != nullptr) {
        delete PMMA_Core::ControllerManagerInstance;
        PMMA_Core::ControllerManagerInstance = nullptr;
    }

    if (PMMA_Core::DropManagerInstance != nullptr) {
        delete PMMA_Core::DropManagerInstance;
        PMMA_Core::DropManagerInstance = nullptr;
    }

    glfwDestroyWindow(Window);
    Window = nullptr;

    PMMA_Registry::GLFW_References--;
    if (PMMA_Registry::GLFW_References <= 0) {
        PMMA_Registry::GLFW_Initialized = false;
        glfwTerminate();
    }

    PMMA_Core::DisplayInstance = nullptr;

    delete WindowFillColor;
    WindowFillColor = nullptr;

    delete F11_KeyEvent;
    F11_KeyEvent = nullptr;
    delete Escape_KeyEvent;
    Escape_KeyEvent = nullptr;

    delete Logger;
    Logger = nullptr;
}