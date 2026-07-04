#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

namespace PMMA::Events {
class Key_Left_Shift;
class Key_Right_Shift;
class Key_Left_Control;
class Key_Right_Control;
class Key_Left_Alt;
class Key_Right_Alt;
class Key_Left_Super;
class Key_Right_Super;
} // namespace PMMA::Events

namespace PMMA::Internal::Events {
class InternalKeyManager {
private:
    PMMA::Events::Key_Left_Shift *Left_Shift_Instance = nullptr;
    PMMA::Events::Key_Right_Shift *Right_Shift_Instance = nullptr;
    PMMA::Events::Key_Left_Control *Left_Control_Instance = nullptr;
    PMMA::Events::Key_Right_Control *Right_Control_Instance = nullptr;
    PMMA::Events::Key_Left_Alt *Left_Alt_Instance = nullptr;
    PMMA::Events::Key_Right_Alt *Right_Alt_Instance = nullptr;
    PMMA::Events::Key_Left_Super *Left_Super_Instance = nullptr;
    PMMA::Events::Key_Right_Super *Right_Super_Instance = nullptr;

public:
    bool Active;

    InternalKeyManager();
    ~InternalKeyManager();

    void Update(GLFWwindow *Window);

    static void KeyCallback(GLFWwindow *window, int key, int scancode, int action, int mods);
};

class InternalTextManager {
public:
    bool Active;

    InternalTextManager();
    ~InternalTextManager();

    void Update(GLFWwindow *Window);

    static void TextCallback(GLFWwindow *window, unsigned int codepoint);
};

class InternalMousePositionManager {
public:
    bool Active;

    InternalMousePositionManager();
    ~InternalMousePositionManager();

    void Update(GLFWwindow *Window);

    static void CursorPositionCallback(GLFWwindow *window, double xpos, double ypos);
};

class InternalMouseEnterWindowManager {
public:
    bool Active;

    InternalMouseEnterWindowManager();
    ~InternalMouseEnterWindowManager();

    void Update(GLFWwindow *Window);

    static void CursorEnterCallback(GLFWwindow *window, int entered);
};

class InternalMouseButtonManager {
public:
    bool Active;

    InternalMouseButtonManager();
    ~InternalMouseButtonManager();

    void Update(GLFWwindow *Window);

    static void MouseButtonCallback(GLFWwindow *window, int button, int action, int mods);
};

class InternalMouseScrollManager {
public:
    bool Active;

    InternalMouseScrollManager();
    ~InternalMouseScrollManager();

    void Update(GLFWwindow *Window);

    static void ScrollCallback(GLFWwindow *window, double xoffset, double yoffset);
};

class InternalControllerManager {
public:
    bool Active;

    InternalControllerManager();
    ~InternalControllerManager();

    void Update(GLFWwindow *Window);

    static void JoystickCallback(int jid, int event);
};

class InternalDropManager {
public:
    bool Active;

    InternalDropManager();
    ~InternalDropManager();

    void Update(GLFWwindow *Window);

    static void DropCallback(GLFWwindow *window, int count, const char **paths);
};
} // namespace PMMA::Internal::Events