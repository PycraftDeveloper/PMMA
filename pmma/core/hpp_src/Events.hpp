#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>

class EXPORT CPP_TextEvent {
    private:
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

class EXPORT CPP_MouseButton_Left_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_Right_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_Middle_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_0_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_1_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_2_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_3_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};

class EXPORT CPP_MouseButton_4_Event {
    public:
        bool GetPressed();

        void SetDoublePressDuration(float duration);

        bool GetPressedToggle();

        bool GetDoublePressed();

        void SetLongPressDuration(float duration);

        bool GetLongPressed();

        bool PollLongPressed();

        void SetRepeatPressDuration(float Duration);

        float GetRepeatPressDuration();

        float GetLongPressDuration();

        float GetDoublePressDuration();
};