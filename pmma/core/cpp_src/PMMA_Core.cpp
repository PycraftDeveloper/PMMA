#include "Display.hpp"
#include "NumberConverter.hpp"
#include "EventsManager.hpp"
#include "PMMA_Core.hpp"

static CPP_Display* DisplayInstance = nullptr;
static bool GLFW_Initialized = false;
static int GLFW_References = 0;
static CPP_ColorConverter* WindowFillColor = nullptr;
static int WindowFillColorReferences = 0;

EXPORT CPP_Display* GetDisplayInstance() {
    return DisplayInstance;
}

EXPORT void SetDisplayInstance(CPP_Display* new_instance) {
    DisplayInstance = new_instance;
}

EXPORT CPP_ColorConverter* GetWindowFillColor() {
    return WindowFillColor;
}

EXPORT void SetWindowFillColor(CPP_ColorConverter* new_instance) {
    WindowFillColor = new_instance;
}

EXPORT bool Get_GLFW_Initialized() {
    return GLFW_Initialized;
}

EXPORT void Set_GLFW_Initialized(bool value) {
    GLFW_Initialized = value;
}

EXPORT int Get_GLFW_References() {
    return GLFW_References;
}

EXPORT void Set_GLFW_References(int value) {
    GLFW_References = value;
}

EXPORT int GetWindowFillColorReferences() {
    return WindowFillColorReferences;
}

EXPORT void SetWindowFillColorReferences(int value) {
    WindowFillColorReferences = value;
}