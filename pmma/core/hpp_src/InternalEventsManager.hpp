#pragma once
#include "PMMA_Exports.hpp"

#include <GLFW/glfw3.h>

class EXPORT CPP_EventsManager {
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
    static void GenericUpdate(GLFWwindow* window);
};