#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include "Internal/Events/EventsManager.hpp"
#include "Internal/Events/InternalEvents.hpp"

namespace PMMA::Events {
class EXPORT Mouse_Position {
private:
    float position[2] = {0, 0};
    float previous_position[2] = {0, 0};
    float delta[2] = {0, 0};
    float toggle_delta[2] = {0, 0};
    bool Enabled = true;

public:
    Mouse_Position();
    ~Mouse_Position();

    inline void Update(float x_value, float y_value) {
        if (!Enabled) {
            return;
        }
        delta[0] = x_value - position[0];
        delta[1] = y_value - position[1];
        toggle_delta[0] = delta[0];
        toggle_delta[1] = delta[1];
        previous_position[0] = position[0];
        previous_position[1] = position[1];
        position[0] = x_value;
        position[1] = y_value;
    };

    inline void GetPosition(float *out) {
        out[0] = position[0];
        out[1] = position[1];
    };

    inline void GetDelta(float *out) {
        out[0] = delta[0];
        out[1] = delta[1];
    };

    inline void GetDeltaToggle(float *out) {
        out[0] = toggle_delta[0];
        out[1] = toggle_delta[1];
        toggle_delta[0] = 0;
        toggle_delta[1] = 0;
    };

    inline bool GetEnabled() {
        return Enabled;
    };

    inline void SetEnabled(bool NewIsEnabled) {
        Enabled = NewIsEnabled;
    };
};

class EXPORT Mouse_EnterWindow {
private:
    bool IsEntered = false;
    bool IsEnteredToggle = false;
    bool Enabled = true;

public:
    Mouse_EnterWindow();
    ~Mouse_EnterWindow();

    inline void Update(bool NewIsEntered) {
        if (!Enabled) {
            return;
        }
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

    inline bool GetEnabled() {
        return Enabled;
    };

    inline void SetEnabled(bool NewIsEnabled) {
        Enabled = NewIsEnabled;
    };
};

class EXPORT Mouse_Button_Left : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_Left();
    ~Mouse_Button_Left();
};

class EXPORT Mouse_Button_Right : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_Right();
    ~Mouse_Button_Right();
};

class EXPORT Mouse_Button_Middle : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_Middle();
    ~Mouse_Button_Middle();
};

class EXPORT Mouse_Button_0 : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_0();
    ~Mouse_Button_0();
};

class EXPORT Mouse_Button_1 : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_1();
    ~Mouse_Button_1();
};

class EXPORT Mouse_Button_2 : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_2();
    ~Mouse_Button_2();
};

class EXPORT Mouse_Button_3 : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_3();
    ~Mouse_Button_3();
};

class EXPORT Mouse_Button_4 : public PMMA::Internal::Events::ButtonPressed {
public:
    Mouse_Button_4();
    ~Mouse_Button_4();
};

class EXPORT Mouse_Scroll {
private:
    float Position[2] = {0, 0};
    float Delta[2] = {0, 0};
    float DeltaToggle[2] = {0, 0};
    bool IsEnabled = true;

public:
    Mouse_Scroll();

    ~Mouse_Scroll();

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

    inline void GetPosition(float *out) {
        out[0] = Position[0];
        out[1] = Position[1];
    };

    inline void GetDelta(float *out) {
        out[0] = Delta[0];
        out[1] = Delta[1];
    };

    inline void GetDeltaToggle(float *out) {
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
} // namespace PMMA::Events