#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <vector>
#include <iostream>
#include <chrono>

#include <GLFW/glfw3.h>

#include "NumberConverter.hpp"

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

class EXPORT CPP_KeyEvent_Space : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Space();
        ~CPP_KeyEvent_Space();
};

class EXPORT CPP_KeyEvent_Apostrophe : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Apostrophe();
        ~CPP_KeyEvent_Apostrophe();
};

class EXPORT CPP_KeyEvent_Comma : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Comma();
        ~CPP_KeyEvent_Comma();
};

class EXPORT CPP_KeyEvent_Minus : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Minus();
        ~CPP_KeyEvent_Minus();
};

class EXPORT CPP_KeyEvent_Period : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Period();
        ~CPP_KeyEvent_Period();
};

class EXPORT CPP_KeyEvent_Slash : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Slash();
        ~CPP_KeyEvent_Slash();
};

class EXPORT CPP_KeyEvent_0 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_0();
        ~CPP_KeyEvent_0();
};

class EXPORT CPP_KeyEvent_1 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_1();
        ~CPP_KeyEvent_1();
};

class EXPORT CPP_KeyEvent_2 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_2();
        ~CPP_KeyEvent_2();
};

class EXPORT CPP_KeyEvent_3 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_3();
        ~CPP_KeyEvent_3();
};

class EXPORT CPP_KeyEvent_4 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_4();
        ~CPP_KeyEvent_4();
};

class EXPORT CPP_KeyEvent_5 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_5();
        ~CPP_KeyEvent_5();
};

class EXPORT CPP_KeyEvent_6 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_6();
        ~CPP_KeyEvent_6();
};

class EXPORT CPP_KeyEvent_7 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_7();
        ~CPP_KeyEvent_7();
};

class EXPORT CPP_KeyEvent_8 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_8();
        ~CPP_KeyEvent_8();
};

class EXPORT CPP_KeyEvent_9 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_9();
        ~CPP_KeyEvent_9();
};

class EXPORT CPP_KeyEvent_Semicolon : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Semicolon();
        ~CPP_KeyEvent_Semicolon();
};

class EXPORT CPP_KeyEvent_Equal : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Equal();
        ~CPP_KeyEvent_Equal();
};

class EXPORT CPP_KeyEvent_A : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_A();
        ~CPP_KeyEvent_A();
};

class EXPORT CPP_KeyEvent_B : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_B();
        ~CPP_KeyEvent_B();
};

class EXPORT CPP_KeyEvent_C : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_C();
        ~CPP_KeyEvent_C();
};

class EXPORT CPP_KeyEvent_D : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_D();
        ~CPP_KeyEvent_D();
};

class EXPORT CPP_KeyEvent_E : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_E();
        ~CPP_KeyEvent_E();
};

class EXPORT CPP_KeyEvent_F : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F();
        ~CPP_KeyEvent_F();
};

class EXPORT CPP_KeyEvent_G : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_G();
        ~CPP_KeyEvent_G();
};

class EXPORT CPP_KeyEvent_H : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_H();
        ~CPP_KeyEvent_H();
};

class EXPORT CPP_KeyEvent_I : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_I();
        ~CPP_KeyEvent_I();
};

class EXPORT CPP_KeyEvent_J : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_J();
        ~CPP_KeyEvent_J();
};

class EXPORT CPP_KeyEvent_K : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_K();
        ~CPP_KeyEvent_K();
};

class EXPORT CPP_KeyEvent_L : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_L();
        ~CPP_KeyEvent_L();
};

class EXPORT CPP_KeyEvent_M : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_M();
        ~CPP_KeyEvent_M();
};

class EXPORT CPP_KeyEvent_N : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_N();
        ~CPP_KeyEvent_N();
};

class EXPORT CPP_KeyEvent_O : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_O();
        ~CPP_KeyEvent_O();
};

class EXPORT CPP_KeyEvent_P : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_P();
        ~CPP_KeyEvent_P();
};

class EXPORT CPP_KeyEvent_Q : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Q();
        ~CPP_KeyEvent_Q();
};

class EXPORT CPP_KeyEvent_R : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_R();
        ~CPP_KeyEvent_R();
};

class EXPORT CPP_KeyEvent_S : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_S();
        ~CPP_KeyEvent_S();
};

class EXPORT CPP_KeyEvent_T : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_T();
        ~CPP_KeyEvent_T();
};

class EXPORT CPP_KeyEvent_U : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_U();
        ~CPP_KeyEvent_U();
};

class EXPORT CPP_KeyEvent_V : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_V();
        ~CPP_KeyEvent_V();
};

class EXPORT CPP_KeyEvent_W : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_W();
        ~CPP_KeyEvent_W();
};

class EXPORT CPP_KeyEvent_X : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_X();
        ~CPP_KeyEvent_X();
};

class EXPORT CPP_KeyEvent_Y : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Y();
        ~CPP_KeyEvent_Y();
};

class EXPORT CPP_KeyEvent_Z : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Z();
        ~CPP_KeyEvent_Z();
};

class EXPORT CPP_KeyEvent_Left_Bracket : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Left_Bracket();
        ~CPP_KeyEvent_Left_Bracket();
};

class EXPORT CPP_KeyEvent_Backslash : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Backslash();
        ~CPP_KeyEvent_Backslash();
};

class EXPORT CPP_KeyEvent_Right_Bracket : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Right_Bracket();
        ~CPP_KeyEvent_Right_Bracket();
};

class EXPORT CPP_KeyEvent_Grave_Accent : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Grave_Accent();
        ~CPP_KeyEvent_Grave_Accent();
};

class EXPORT CPP_KeyEvent_World_1 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_World_1();
        ~CPP_KeyEvent_World_1();
};

class EXPORT CPP_KeyEvent_World_2 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_World_2();
        ~CPP_KeyEvent_World_2();
};

class EXPORT CPP_KeyEvent_Escape : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Escape();
        ~CPP_KeyEvent_Escape();
};

class EXPORT CPP_KeyEvent_Enter : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Enter();
        ~CPP_KeyEvent_Enter();
};

class EXPORT CPP_KeyEvent_Tab : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Tab();
        ~CPP_KeyEvent_Tab();
};

class EXPORT CPP_KeyEvent_Backspace : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Backspace();
        ~CPP_KeyEvent_Backspace();
};

class EXPORT CPP_KeyEvent_Insert : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Insert();
        ~CPP_KeyEvent_Insert();
};

class EXPORT CPP_KeyEvent_Delete : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Delete();
        ~CPP_KeyEvent_Delete();
};

class EXPORT CPP_KeyEvent_Right : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Right();
        ~CPP_KeyEvent_Right();
};

class EXPORT CPP_KeyEvent_Left : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Left();
        ~CPP_KeyEvent_Left();
};

class EXPORT CPP_KeyEvent_Down : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Down();
        ~CPP_KeyEvent_Down();
};

class EXPORT CPP_KeyEvent_Up : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Up();
        ~CPP_KeyEvent_Up();
};

class EXPORT CPP_KeyEvent_Page_Up : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Page_Up();
        ~CPP_KeyEvent_Page_Up();
};

class EXPORT CPP_KeyEvent_Page_Down : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Page_Down();
        ~CPP_KeyEvent_Page_Down();
};

class EXPORT CPP_KeyEvent_Home : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Home();
        ~CPP_KeyEvent_Home();
};

class EXPORT CPP_KeyEvent_End : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_End();
        ~CPP_KeyEvent_End();
};

class EXPORT CPP_KeyEvent_Caps_Lock : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Caps_Lock();
        ~CPP_KeyEvent_Caps_Lock();
};

class EXPORT CPP_KeyEvent_Scroll_Lock : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Scroll_Lock();
        ~CPP_KeyEvent_Scroll_Lock();
};

class EXPORT CPP_KeyEvent_Num_Lock : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Num_Lock();
        ~CPP_KeyEvent_Num_Lock();
};

class EXPORT CPP_KeyEvent_Print_Screen : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Print_Screen();
        ~CPP_KeyEvent_Print_Screen();
};

class EXPORT CPP_KeyEvent_Pause : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Pause();
        ~CPP_KeyEvent_Pause();
};

class EXPORT CPP_KeyEvent_F1 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F1();
        ~CPP_KeyEvent_F1();
};

class EXPORT CPP_KeyEvent_F2 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F2();
        ~CPP_KeyEvent_F2();
};

class EXPORT CPP_KeyEvent_F3 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F3();
        ~CPP_KeyEvent_F3();
};

class EXPORT CPP_KeyEvent_F4 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F4();
        ~CPP_KeyEvent_F4();
};

class EXPORT CPP_KeyEvent_F5 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F5();
        ~CPP_KeyEvent_F5();
};

class EXPORT CPP_KeyEvent_F6 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F6();
        ~CPP_KeyEvent_F6();
};

class EXPORT CPP_KeyEvent_F7 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F7();
        ~CPP_KeyEvent_F7();
};

class EXPORT CPP_KeyEvent_F8 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F8();
        ~CPP_KeyEvent_F8();
};

class EXPORT CPP_KeyEvent_F9 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F9();
        ~CPP_KeyEvent_F9();
};

class EXPORT CPP_KeyEvent_F10 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F10();
        ~CPP_KeyEvent_F10();
};

class EXPORT CPP_KeyEvent_F11 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F11();
        ~CPP_KeyEvent_F11();
};

class EXPORT CPP_KeyEvent_F12 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F12();
        ~CPP_KeyEvent_F12();
};

class EXPORT CPP_KeyEvent_F13 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F13();
        ~CPP_KeyEvent_F13();
};

class EXPORT CPP_KeyEvent_F14 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F14();
        ~CPP_KeyEvent_F14();
};

class EXPORT CPP_KeyEvent_F15 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F15();
        ~CPP_KeyEvent_F15();
};

class EXPORT CPP_KeyEvent_F16 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F16();
        ~CPP_KeyEvent_F16();
};

class EXPORT CPP_KeyEvent_F17 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F17();
        ~CPP_KeyEvent_F17();
};

class EXPORT CPP_KeyEvent_F18 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F18();
        ~CPP_KeyEvent_F18();
};

class EXPORT CPP_KeyEvent_F19 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F19();
        ~CPP_KeyEvent_F19();
};

class EXPORT CPP_KeyEvent_F20 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F20();
        ~CPP_KeyEvent_F20();
};

class EXPORT CPP_KeyEvent_F21 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F21();
        ~CPP_KeyEvent_F21();
};

class EXPORT CPP_KeyEvent_F22 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F22();
        ~CPP_KeyEvent_F22();
};

class EXPORT CPP_KeyEvent_F23 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F23();
        ~CPP_KeyEvent_F23();
};

class EXPORT CPP_KeyEvent_F24 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F24();
        ~CPP_KeyEvent_F24();
};

class EXPORT CPP_KeyEvent_F25 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_F25();
        ~CPP_KeyEvent_F25();
};

class EXPORT CPP_KeyEvent_Left_Shift : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Left_Shift();
        ~CPP_KeyEvent_Left_Shift();
};

class EXPORT CPP_KeyEvent_Left_Control : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Left_Control();
        ~CPP_KeyEvent_Left_Control();
};

class EXPORT CPP_KeyEvent_Left_Alt : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Left_Alt();
        ~CPP_KeyEvent_Left_Alt();
};

class EXPORT CPP_KeyEvent_Left_Super : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Left_Super();
        ~CPP_KeyEvent_Left_Super();
};

class EXPORT CPP_KeyEvent_Right_Shift : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Right_Shift();
        ~CPP_KeyEvent_Right_Shift();
};

class EXPORT CPP_KeyEvent_Right_Control : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Right_Control();
        ~CPP_KeyEvent_Right_Control();
};

class EXPORT CPP_KeyEvent_Right_Alt : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Right_Alt();
        ~CPP_KeyEvent_Right_Alt();
};

class EXPORT CPP_KeyEvent_Right_Super : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Right_Super();
        ~CPP_KeyEvent_Right_Super();
};

class EXPORT CPP_KeyEvent_Shift : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Shift();
        ~CPP_KeyEvent_Shift();
};

class EXPORT CPP_KeyEvent_Control : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Control();
        ~CPP_KeyEvent_Control();
};

class EXPORT CPP_KeyEvent_Alt : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Alt();
        ~CPP_KeyEvent_Alt();
};

class EXPORT CPP_KeyEvent_Super : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Super();
        ~CPP_KeyEvent_Super();
};

class EXPORT CPP_KeyEvent_Menu : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyEvent_Menu();
        ~CPP_KeyEvent_Menu();
};

class EXPORT CPP_KeyPadEvent_0 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_0();
        ~CPP_KeyPadEvent_0();
};

class EXPORT CPP_KeyPadEvent_1 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_1();
        ~CPP_KeyPadEvent_1();
};

class EXPORT CPP_KeyPadEvent_2 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_2();
        ~CPP_KeyPadEvent_2();
};

class EXPORT CPP_KeyPadEvent_3 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_3();
        ~CPP_KeyPadEvent_3();
};

class EXPORT CPP_KeyPadEvent_4 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_4();
        ~CPP_KeyPadEvent_4();
};

class EXPORT CPP_KeyPadEvent_5 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_5();
        ~CPP_KeyPadEvent_5();
};

class EXPORT CPP_KeyPadEvent_6 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_6();
        ~CPP_KeyPadEvent_6();
};

class EXPORT CPP_KeyPadEvent_7 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_7();
        ~CPP_KeyPadEvent_7();
};

class EXPORT CPP_KeyPadEvent_8 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_8();
        ~CPP_KeyPadEvent_8();
};

class EXPORT CPP_KeyPadEvent_9 : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_9();
        ~CPP_KeyPadEvent_9();
};

class EXPORT CPP_KeyPadEvent_Decimal : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Decimal();
        ~CPP_KeyPadEvent_Decimal();
};

class EXPORT CPP_KeyPadEvent_Divide : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Divide();
        ~CPP_KeyPadEvent_Divide();
};

class EXPORT CPP_KeyPadEvent_Multiply : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Multiply();
        ~CPP_KeyPadEvent_Multiply();
};

class EXPORT CPP_KeyPadEvent_Subtract : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Subtract();
        ~CPP_KeyPadEvent_Subtract();
};

class EXPORT CPP_KeyPadEvent_Add : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Add();
        ~CPP_KeyPadEvent_Add();
};

class EXPORT CPP_KeyPadEvent_Enter : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Enter();
        ~CPP_KeyPadEvent_Enter();
};

class EXPORT CPP_KeyPadEvent_Equal : public CPP_ButtonPressedEvent {
    public:
        CPP_KeyPadEvent_Equal();
        ~CPP_KeyPadEvent_Equal();
};

class EXPORT CPP_InternalMousePositionEvent {
    private:
        float position[2] = {0, 0};
        float previous_position[2] = {0, 0};
        float delta[2] = {0, 0};
        float toggle_delta[2] = {0, 0};

    public:
        inline void Update(float x_value, float y_value) {
            delta[0] = x_value - position[0];
            delta[1] = y_value - position[1];
            toggle_delta[0] = delta[0];
            toggle_delta[1] = delta[1];
            previous_position[0] = position[0];
            previous_position[1] = position[1];
            position[0] = x_value;
            position[1] = y_value;
        };

        inline void GetPosition(float* out) {
            out[0] = position[0];
            out[1] = position[1];
        };

        inline void GetDelta(float* out) {
            out[0] = delta[0];
            out[1] = delta[1];
        };

        inline void GetDeltaToggle(float* out) {
            out[0] = toggle_delta[0];
            out[1] = toggle_delta[1];
            toggle_delta[0] = 0;
            toggle_delta[1] = 0;
        };
};

class EXPORT CPP_InternalMouseEnterWindowEvent {
    private:
        bool IsEntered = false;
        bool IsEnteredToggle = false;

    public:
        inline void Update(bool NewIsEntered) {
            if (NewIsEntered != IsEntered) {
                IsEnteredToggle = NewIsEntered;
            }
            IsEntered = NewIsEntered;
        };

        inline bool GetEntered() {
            return IsEntered;
        };

        inline bool GetEnteredToggle() {
            if (IsEnteredToggle) {
                IsEnteredToggle = false;
                return true;
            }
            return false;
        };
};

class EXPORT CPP_MousePositionEvent {
    public:
        void GetPosition(float* out);

        void GetDelta(float* out);

        void GetDeltaToggle(float* out);
};

class EXPORT CPP_MouseEnterWindowEvent {
    public:
        bool GetEntered();

        bool GetEnteredToggle();
};

class EXPORT CPP_MouseButtonEvent_Left : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_Left();
        ~CPP_MouseButtonEvent_Left();

};

class EXPORT CPP_MouseButtonEvent_Right : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_Right();
        ~CPP_MouseButtonEvent_Right();

};

class EXPORT CPP_MouseButtonEvent_Middle : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_Middle();
        ~CPP_MouseButtonEvent_Middle();

};

class EXPORT CPP_MouseButtonEvent_0 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_0();
        ~CPP_MouseButtonEvent_0();

};

class EXPORT CPP_MouseButtonEvent_1 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_1();
        ~CPP_MouseButtonEvent_1();

};

class EXPORT CPP_MouseButtonEvent_2 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_2();
        ~CPP_MouseButtonEvent_2();

};

class EXPORT CPP_MouseButtonEvent_3 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_3();
        ~CPP_MouseButtonEvent_3();

};

class EXPORT CPP_MouseButtonEvent_4 : public CPP_ButtonPressedEvent {
    public:
        CPP_MouseButtonEvent_4();
        ~CPP_MouseButtonEvent_4();

};

class EXPORT CPP_TextEvent {
    private:
        CPP_KeyEvent_Control* Control_KeyEventPtr = nullptr;
        CPP_KeyEvent_Shift* Shift_KeyEventPtr = nullptr;
        CPP_KeyEvent_V* V_KeyEventPtr = nullptr;
        CPP_KeyEvent_Insert* Insert_KeyEventPtr = nullptr;
        CPP_KeyEvent_Delete* Delete_KeyEventPtr = nullptr;
        CPP_KeyEvent_Backspace* Backspace_KeyEventPtr = nullptr;
        std::string Text = "";
        bool IsEnabled = true;

    public:
        CPP_TextEvent();

        ~CPP_TextEvent();

        inline void Update(std::string NewTextContent) {
            if (!IsEnabled) {
                return;
            }
            Text += NewTextContent;
        };

        void GenericUpdate(GLFWwindow* window);

        void RemoveBack();

        void RemoveFront();

        inline std::string GetText() {
            return Text;
        };

        inline void SetEnabled(bool NewIsEnabled) {
            IsEnabled = NewIsEnabled;
        };

        inline bool GetEnabled() {
            return IsEnabled;
        };

        inline void ClearText() {
            Text = "";
        };

        inline void Set_ControlKey_DoublePressDuration(float NewDuration) {
            Control_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_ControlKey_LongPressDuration(float NewDuration) {
            Control_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_ControlKey_RepeatPressDuration(float NewDuration) {
            Control_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_ShiftKey_DoublePressDuration(float NewDuration) {
            Shift_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_ShiftKey_LongPressDuration(float NewDuration) {
            Shift_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_ShiftKey_RepeatPressDuration(float NewDuration) {
            Shift_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_VKey_DoublePressDuration(float NewDuration) {
            V_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_VKey_LongPressDuration(float NewDuration) {
            V_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_VKey_RepeatPressDuration(float NewDuration) {
            V_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_InsertKey_DoublePressDuration(float NewDuration) {
            Insert_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_InsertKey_LongPressDuration(float NewDuration) {
            Insert_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_InsertKey_RepeatPressDuration(float NewDuration) {
            Insert_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_DeleteKey_DoublePressDuration(float NewDuration) {
            Delete_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_DeleteKey_LongPressDuration(float NewDuration) {
            Delete_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_DeleteKey_RepeatPressDuration(float NewDuration) {
            Delete_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_BackspaceKey_DoublePressDuration(float NewDuration) {
            Backspace_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_BackspaceKey_LongPressDuration(float NewDuration) {
            Backspace_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_BackspaceKey_RepeatPressDuration(float NewDuration) {
            Backspace_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };
};

class EXPORT CPP_MouseScrollEvent {
    private:
        float Position[2] = {0, 0};
        float Delta[2] = {0, 0};
        float DeltaToggle[2] = {0, 0};
        bool IsEnabled = true;

    public:
        CPP_MouseScrollEvent();

        ~CPP_MouseScrollEvent();

        inline void Update(float delta_x, float delta_y) {
            if (!IsEnabled) {
                return;
            }
            Delta[0] = delta_x;
            Delta[1] = delta_y;
            DeltaToggle[0] += delta_x;
            DeltaToggle[1] += delta_y;
            Position[0] += delta_x;
            Position[1] += delta_y;
        };

        inline void GetPosition(float* out) {
            out[0] = Position[0];
            out[1] = Position[1];
        };

        inline void GetDelta(float* out) {
            out[0] = Delta[0];
            out[1] = Delta[1];
        };

        inline void GetDeltaToggle(float* out) {
            out[0] = DeltaToggle[0];
            out[1] = DeltaToggle[1];
            DeltaToggle[0] = 0;
            DeltaToggle[1] = 0;
        };

        inline float GetHorizontalPosition() {
            return Position[0];
        };

        inline float GetVerticalPosition() {
            return Position[1];
        };

        inline float GetHorizontalDelta() {
            return Delta[0];
        };

        inline float GetVerticalDelta() {
            return Delta[1];
        };

        inline float GetHorizontalDeltaToggle() {
            float out = DeltaToggle[0];
            DeltaToggle[0] = 0;
            return out;
        };

        inline float GetVerticalDeltaToggle() {
            float out = DeltaToggle[1];
            DeltaToggle[1] = 0;
            return out;
        };

        inline void ClearPosition() {
            Position[0] = 0;
            Position[1] = 0;
        };

        inline bool GetEnabled() {
            return IsEnabled;
        };

        inline void SetEnabled(bool NewIsEnabled) {
            IsEnabled = NewIsEnabled;
        };
};

class EXPORT CPP_ControllerEvent {
    private:
        std::string Name;
        std::string GUID;
        std::vector<CPP_BasicProportionConverter> AxesData;
        unsigned int ID;
        int AxisCount;
        bool Connected;

    public:
        CPP_ControllerEvent(unsigned int new_ID) {
            ID = new_ID;
            Connected = false;
            Name = "";
            GUID = "";
        };

        inline void UpdateConnection(bool new_Connected) {
            if (new_Connected) {
                Name = glfwGetJoystickName(ID);
                GUID = glfwGetJoystickGUID(ID);

                glfwGetJoystickAxes(ID, &AxisCount);
                for (int i = 0; i < AxisCount; i++) {
                    AxesData.emplace_back();
                }

                Update();
            } else {
                Name = "";
                GUID = "";
                AxesData.clear();
            }
            Connected = new_Connected;
        };

        inline void Update() {
            const float* axes = glfwGetJoystickAxes(ID, &AxisCount);
            for (int i = 0; i < AxisCount; i++) {
                AxesData[i].SetProportion_Decimal(axes[i]);
            }
        };

        inline bool GetConnected() {
            return Connected;
        };

        inline float GetAxis_Decimal(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxesData[AxisID].GetProportion_Decimal();
        };

        inline float GetAxis_Percentage(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxesData[AxisID].GetProportion_Percentage();
        };
};