#pragma once

#include <GLFW/glfw3.h>

#include "Events/KeyEvents.hpp"

class CPP_InternalKeyEventManager {
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
        bool Active;

        CPP_InternalKeyEventManager();
        ~CPP_InternalKeyEventManager();

        void Update(GLFWwindow* Window);

        static void KeyCallback(GLFWwindow* window, int key, int scancode, int action, int mods);
};

class CPP_InternalTextEventManager {
    public:
        bool Active;

        CPP_InternalTextEventManager();
        ~CPP_InternalTextEventManager();

        void Update(GLFWwindow* Window);

        static void TextCallback(GLFWwindow* window, unsigned int codepoint);
};

class CPP_InternalMousePositionEventManager {
    public:
        bool Active;

        CPP_InternalMousePositionEventManager();
        ~CPP_InternalMousePositionEventManager();

        void Update(GLFWwindow* Window);

        static void CursorPositionCallback(GLFWwindow* window, double xpos, double ypos);
};

class CPP_InternalMouseEnterWindowEventManager {
    public:
        bool Active;

        CPP_InternalMouseEnterWindowEventManager();
        ~CPP_InternalMouseEnterWindowEventManager();

        void Update(GLFWwindow* Window);

        static void CursorEnterCallback(GLFWwindow* window, int entered);
};

class CPP_InternalMouseButtonEventManager {
    public:
        bool Active;

        CPP_InternalMouseButtonEventManager();
        ~CPP_InternalMouseButtonEventManager();

        void Update(GLFWwindow* Window);

        static void MouseButtonCallback(GLFWwindow* window, int button, int action, int mods);
};

class CPP_InternalMouseScrollEventManager {
    public:
        bool Active;

        CPP_InternalMouseScrollEventManager();
        ~CPP_InternalMouseScrollEventManager();

        void Update(GLFWwindow* Window);

        static void ScrollCallback(GLFWwindow* window, double xoffset, double yoffset);
};

class CPP_InternalControllerEventManager {
    public:
        bool Active;

        CPP_InternalControllerEventManager();
        ~CPP_InternalControllerEventManager();

        void Update(GLFWwindow* Window);

        static void JoystickCallback(int jid, int event);
};

class CPP_InternalDropEventManager {
    public:
        bool Active;

        CPP_InternalDropEventManager();
        ~CPP_InternalDropEventManager();

        void Update(GLFWwindow* Window);

        static void DropCallback(GLFWwindow* window, int count, const char** paths);
};