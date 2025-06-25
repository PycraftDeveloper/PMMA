#pragma once
#include "PMMA_Exports.hpp"

#include <GLFW/glfw3.h>

#include "Events.hpp"

class EXPORT CPP_EventsManager {
private:
    CPP_KeyEvent_Left_Shift* Left_Shift_Instance = nullptr;
    CPP_KeyEvent_Right_Shift* Right_Shift_Instance = nullptr;
    CPP_KeyEvent_Left_Control* Left_Control_Instance = nullptr;
    CPP_KeyEvent_Right_Control* Right_Control_Instance = nullptr;
    CPP_KeyEvent_Left_Alt* Left_Alt_Instance = nullptr;
    CPP_KeyEvent_Right_Alt* Right_Alt_Instance = nullptr;
    CPP_KeyEvent_Left_Super* Left_Super_Instance = nullptr;
    CPP_KeyEvent_Right_Super* Right_Super_Instance = nullptr;

public:
    CPP_EventsManager(GLFWwindow* Window);
    ~CPP_EventsManager();

    static void KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods);
    static void TextCallback(GLFWwindow* window, unsigned int codepoint);
    static void CursorPositionCallback(GLFWwindow* window, double xpos, double ypos);
    static void CursorEnterCallback(GLFWwindow* window, int entered);
    static void MouseButtonCallback(GLFWwindow* window, int button, int action, int mods);
    static void ScrollCallback(GLFWwindow* window, double xoffset, double yoffset);
    static void JoystickCallback(int jid, int event);
    static void DropCallback(GLFWwindow* window, int count, const char** paths);
    void GenericUpdate(GLFWwindow* window);
};