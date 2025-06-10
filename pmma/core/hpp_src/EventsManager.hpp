#pragma once
#include "PMMA_Exports.hpp"

#include <GLFW/glfw3.h>

namespace EventsManager {
    EXPORT void KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods);

    EXPORT void TextCallback(GLFWwindow* window, unsigned int codepoint);

    EXPORT void CursorPositionCallback(GLFWwindow* window, double xpos, double ypos);

    EXPORT void CursorEnterCallback(GLFWwindow* window, int entered);

    EXPORT void MousePositionCallback(GLFWwindow* window, int button, int action, int mods);

    EXPORT void MouseButtonCallback(GLFWwindow* window, int button, int action, int mods);

    EXPORT void ScrollCallback(GLFWwindow* window, double xoffset, double yoffset);

    EXPORT void JoystickCallback(int jid, int event);

    EXPORT void DropCallback(GLFWwindow* window, int count, const char** paths);
}