#pragma once

#include <GLFW/glfw3.h>

namespace EventsManager {
    void KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods);

    void TextCallback(GLFWwindow* window, unsigned int codepoint);

    void CursorPositionCallback(GLFWwindow* window, double xpos, double ypos);

    void CursorEnterCallback(GLFWwindow* window, int entered);

    void MousePositionCallback(GLFWwindow* window, int button, int action, int mods);

    void MouseButtonCallback(GLFWwindow* window, int button, int action, int mods);

    void ScrollCallback(GLFWwindow* window, double xoffset, double yoffset);

    void JoystickCallback(int jid, int event);

    void DropCallback(GLFWwindow* window, int count, const char** paths);
}