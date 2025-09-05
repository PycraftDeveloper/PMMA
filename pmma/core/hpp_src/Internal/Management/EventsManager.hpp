#pragma once
#include "PMMA_Exports.hpp"

#include <chrono>

#include <GLFW/glfw3.h>

class CPP_KeyEvent_Left_Shift;
class CPP_KeyEvent_Right_Shift;
class CPP_KeyEvent_Left_Control;
class CPP_KeyEvent_Right_Control;
class CPP_KeyEvent_Left_Alt;
class CPP_KeyEvent_Right_Alt;
class CPP_KeyEvent_Left_Super;
class CPP_KeyEvent_Right_Super;

class EXPORT CPP_ButtonPressedEvent {
    private:
        std::chrono::high_resolution_clock::time_point LastEventTime;
        std::chrono::high_resolution_clock::time_point PreviousEventTime;
        std::chrono::high_resolution_clock::time_point LongPressPollTime;
        float DoublePressDuration = 0.5f;
        float LongPressDuration = 1.0f;
        float RepeatPressDuration = 0.25f;
        bool IsPressed = false;
        bool IsPressedToggle = false;
        bool IsLongPressValid = false;
        bool IsDoublePressed = false;
        bool PreviousState = false;

    public:
        inline void Update(bool NewIsPressed) {
            if (NewIsPressed == PreviousState) {
                return;
            }
            PreviousState = NewIsPressed;
            IsPressed = NewIsPressed;
            IsPressedToggle = NewIsPressed;
            if (IsPressed) {
                PreviousEventTime = LastEventTime;
                LastEventTime = std::chrono::high_resolution_clock::now();
                LongPressPollTime = LastEventTime;
                IsLongPressValid = true;

                std::chrono::duration<float> Duration = LastEventTime - PreviousEventTime;
                if (Duration.count() <= DoublePressDuration) {
                    IsDoublePressed = true;
                }
            } else {
                IsLongPressValid = false;
                IsDoublePressed = false;
            }
        };

        inline bool GetPressed() {
            return IsPressed;
        };

        inline void SetDoublePressDuration(float Duration) {
            DoublePressDuration = Duration;
        };

        inline bool GetPressedToggle() {
            if (IsPressedToggle) {
                IsPressedToggle = false;
                return true;
            }
            return false;
        };

        inline bool GetDoublePressed() {
            return IsDoublePressed;
        };

        inline void SetLongPressDuration(float Duration) {
            LongPressDuration = Duration;
        };

        inline bool GetLongPressed() {
            if (IsPressed && IsLongPressValid) {
                std::chrono::duration<float> Duration = std::chrono::high_resolution_clock::now() - LastEventTime;
                if (Duration.count() >= LongPressDuration) {
                    return true;
                }
            }
            return false;
        };

        inline bool PollLongPressed() {
            bool LongPressed = GetLongPressed();
            if (LongPressed) {
                std::chrono::duration<float> Duration = std::chrono::high_resolution_clock::now() - LongPressPollTime;
                if (Duration.count() >= RepeatPressDuration) {
                    LongPressPollTime = std::chrono::high_resolution_clock::now();
                    return true;
                }
                return false;
            }
            return false;
        };

        inline void SetRepeatPressDuration(float Duration) {
            RepeatPressDuration = Duration;
        };

        inline float GetRepeatPressDuration() {
            return RepeatPressDuration;
        };

        inline float GetLongPressDuration() {
            return LongPressDuration;
        };

        inline float GetDoublePressDuration() {
            return DoublePressDuration;
        };
};

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