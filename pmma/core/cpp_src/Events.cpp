#include <string>
#include <algorithm>

#include "Events.hpp"

#include "PMMA_Core.hpp"

using namespace std;

size_t utf8_char_length(unsigned char c) {
    if ((c & 0x80) == 0x00) return 1;       // 0xxxxxxx
    else if ((c & 0xE0) == 0xC0) return 2;  // 110xxxxx
    else if ((c & 0xF0) == 0xE0) return 3;  // 1110xxxx
    else if ((c & 0xF8) == 0xF0) return 4;  // 11110xxx
    return 1; // fallback - invalid UTF-8, treat as 1 byte
};

void remove_utf8_char(string& text, size_t n) {
    size_t i = 0;  // byte index in the string
    size_t char_index = 0;  // character count

    while (i < text.size() && char_index < n) {
        size_t len = utf8_char_length(static_cast<unsigned char>(text[i]));
        i += len;
        char_index++;
    }

    if (i >= text.size()) {
        // N is out of range, do nothing
        return;
    }

    // Now i is the byte offset of the Nth character
    size_t len = utf8_char_length(static_cast<unsigned char>(text[i]));
    text.erase(i, len);
};

// Finds the start index of the last UTF-8 character
size_t get_last_utf8_char_index(const string& text) {
    if (text.empty()) return string::npos;

    size_t i = text.size() - 1;

    // Move backwards while the byte is a UTF-8 continuation byte (starts with '10')
    while (i > 0 && (static_cast<unsigned char>(text[i]) & 0xC0) == 0x80) {
        i--;
    }
    return i;
};

// Removes the last UTF-8 character from the string
void remove_last_utf8_char(string& text) {
    size_t start = get_last_utf8_char_index(text);
    if (start == string::npos) {
        // String is empty, nothing to remove
        return;
    }
    text.erase(start);
};

CPP_TextEvent::CPP_TextEvent() {
    PMMA::TextEventInstances.push_back(this);
};

CPP_TextEvent::~CPP_TextEvent() {
    auto it = find(PMMA::TextEventInstances.begin(), PMMA::TextEventInstances.end(), this);
    if (it != PMMA::TextEventInstances.end()) {
        PMMA::TextEventInstances.erase(it);
    }
};

void CPP_TextEvent::RemoveBack() {
    if (!IsEnabled) {
        return;
    }
    if (!Text.empty()) {
        remove_last_utf8_char(Text);
    }
};

void CPP_TextEvent::RemoveFront() {
    if (!IsEnabled) {
        return;
    }
    if (Text.size() > 0) {
        remove_utf8_char(Text, 0);
    }
};

void CPP_MousePositionEvent::GetPosition(float* out) {
    if (PMMA::MousePositionEvent_Instance == nullptr) {
        throw runtime_error("PMMA::MousePositionEvent_Instance is null");
    }
    PMMA::MousePositionEvent_Instance->GetPosition(out);
};

void CPP_MousePositionEvent::GetDelta(float* out) {
    if (PMMA::MousePositionEvent_Instance == nullptr) {
        throw runtime_error("PMMA::MousePositionEvent_Instance is null");
    }
    PMMA::MousePositionEvent_Instance->GetDelta(out);
};

void CPP_MousePositionEvent::GetDeltaToggle(float* out) {
    if (PMMA::MousePositionEvent_Instance == nullptr) {
        throw runtime_error("PMMA::MousePositionEvent_Instance is null");
    }
    PMMA::MousePositionEvent_Instance->GetDeltaToggle(out);
};

bool CPP_MouseEnterWindowEvent::GetEntered() {
    if (PMMA::MouseEnterWindowEvent_Instance == nullptr) {
        throw runtime_error("PMMA::MouseEnterWindowEvent_Instance is null");
    }
    return PMMA::MouseEnterWindowEvent_Instance->GetEntered();
};

bool CPP_MouseEnterWindowEvent::GetEnteredToggle() {
    if (PMMA::MouseEnterWindowEvent_Instance == nullptr) {
        throw runtime_error("PMMA::MouseEnterWindowEvent_Instance is null");
    }
    return PMMA::MouseEnterWindowEvent_Instance->GetEnteredToggle();
};

bool CPP_MouseButton_Left_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetPressed();
};

void CPP_MouseButton_Left_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    PMMA::MouseButtonEvent_Left_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_Left_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetPressedToggle();
};

bool CPP_MouseButton_Left_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetDoublePressed();
};

void CPP_MouseButton_Left_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    PMMA::MouseButtonEvent_Left_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_Left_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetLongPressed();
};

bool CPP_MouseButton_Left_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->PollLongPressed();
};

void CPP_MouseButton_Left_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    PMMA::MouseButtonEvent_Left_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_Left_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_Left_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetLongPressDuration();
};

float CPP_MouseButton_Left_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_Left_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Left_Instance is null");
    }
    return PMMA::MouseButtonEvent_Left_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_Right_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetPressed();
};

void CPP_MouseButton_Right_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    PMMA::MouseButtonEvent_Right_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_Right_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetPressedToggle();
};

bool CPP_MouseButton_Right_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetDoublePressed();
};

void CPP_MouseButton_Right_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    PMMA::MouseButtonEvent_Right_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_Right_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetLongPressed();
};

bool CPP_MouseButton_Right_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->PollLongPressed();
};

void CPP_MouseButton_Right_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    PMMA::MouseButtonEvent_Right_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_Right_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_Right_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetLongPressDuration();
};

float CPP_MouseButton_Right_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_Right_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Right_Instance is null");
    }
    return PMMA::MouseButtonEvent_Right_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_Middle_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetPressed();
};

void CPP_MouseButton_Middle_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    PMMA::MouseButtonEvent_Middle_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_Middle_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetPressedToggle();
};

bool CPP_MouseButton_Middle_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetDoublePressed();
};

void CPP_MouseButton_Middle_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    PMMA::MouseButtonEvent_Middle_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_Middle_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetLongPressed();
};

bool CPP_MouseButton_Middle_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->PollLongPressed();
};

void CPP_MouseButton_Middle_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    PMMA::MouseButtonEvent_Middle_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_Middle_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_Middle_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetLongPressDuration();
};

float CPP_MouseButton_Middle_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_Middle_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_Middle_Instance is null");
    }
    return PMMA::MouseButtonEvent_Middle_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_0_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetPressed();
};

void CPP_MouseButton_0_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    PMMA::MouseButtonEvent_0_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_0_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetPressedToggle();
};

bool CPP_MouseButton_0_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetDoublePressed();
};

void CPP_MouseButton_0_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    PMMA::MouseButtonEvent_0_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_0_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetLongPressed();
};

bool CPP_MouseButton_0_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->PollLongPressed();
};

void CPP_MouseButton_0_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    PMMA::MouseButtonEvent_0_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_0_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_0_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetLongPressDuration();
};

float CPP_MouseButton_0_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_0_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_0_Instance is null");
    }
    return PMMA::MouseButtonEvent_0_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_1_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetPressed();
};

void CPP_MouseButton_1_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    PMMA::MouseButtonEvent_1_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_1_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetPressedToggle();
};

bool CPP_MouseButton_1_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetDoublePressed();
};

void CPP_MouseButton_1_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    PMMA::MouseButtonEvent_1_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_1_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetLongPressed();
};

bool CPP_MouseButton_1_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->PollLongPressed();
};

void CPP_MouseButton_1_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    PMMA::MouseButtonEvent_1_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_1_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_1_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetLongPressDuration();
};

float CPP_MouseButton_1_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_1_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_1_Instance is null");
    }
    return PMMA::MouseButtonEvent_1_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_2_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetPressed();
};

void CPP_MouseButton_2_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    PMMA::MouseButtonEvent_2_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_2_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetPressedToggle();
};

bool CPP_MouseButton_2_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetDoublePressed();
};

void CPP_MouseButton_2_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    PMMA::MouseButtonEvent_2_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_2_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetLongPressed();
};

bool CPP_MouseButton_2_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->PollLongPressed();
};

void CPP_MouseButton_2_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    PMMA::MouseButtonEvent_2_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_2_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_2_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetLongPressDuration();
};

float CPP_MouseButton_2_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_2_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_2_Instance is null");
    }
    return PMMA::MouseButtonEvent_2_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_3_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetPressed();
};

void CPP_MouseButton_3_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    PMMA::MouseButtonEvent_3_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_3_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetPressedToggle();
};

bool CPP_MouseButton_3_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetDoublePressed();
};

void CPP_MouseButton_3_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    PMMA::MouseButtonEvent_3_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_3_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetLongPressed();
};

bool CPP_MouseButton_3_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->PollLongPressed();
};

void CPP_MouseButton_3_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    PMMA::MouseButtonEvent_3_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_3_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_3_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetLongPressDuration();
};

float CPP_MouseButton_3_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_3_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_3_Instance is null");
    }
    return PMMA::MouseButtonEvent_3_Instance->GetDoublePressDuration();
};

bool CPP_MouseButton_4_Event::GetPressed() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetPressed();
};

void CPP_MouseButton_4_Event::SetDoublePressDuration(float duration) {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    PMMA::MouseButtonEvent_4_Instance->SetDoublePressDuration(duration);
};

bool CPP_MouseButton_4_Event::GetPressedToggle() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetPressedToggle();
};

bool CPP_MouseButton_4_Event::GetDoublePressed() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetDoublePressed();
};

void CPP_MouseButton_4_Event::SetLongPressDuration(float duration) {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    PMMA::MouseButtonEvent_4_Instance->SetLongPressDuration(duration);
};

bool CPP_MouseButton_4_Event::GetLongPressed() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetLongPressed();
};

bool CPP_MouseButton_4_Event::PollLongPressed() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->PollLongPressed();
};

void CPP_MouseButton_4_Event::SetRepeatPressDuration(float Duration) {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    PMMA::MouseButtonEvent_4_Instance->SetRepeatPressDuration(Duration);
};

float CPP_MouseButton_4_Event::GetRepeatPressDuration() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetRepeatPressDuration();
};

float CPP_MouseButton_4_Event::GetLongPressDuration() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetLongPressDuration();
};

float CPP_MouseButton_4_Event::GetDoublePressDuration() {
    if (PMMA::MouseButtonEvent_4_Instance == nullptr) {
        throw runtime_error("MouseButtonEvent_4_Instance is null");
    }
    return PMMA::MouseButtonEvent_4_Instance->GetDoublePressDuration();
};

CPP_MouseScrollEvent::CPP_MouseScrollEvent() {
    PMMA::MouseScrollEventInstances.push_back(this);
};

CPP_MouseScrollEvent::~CPP_MouseScrollEvent() {
    auto it = find(PMMA::MouseScrollEventInstances.begin(), PMMA::MouseScrollEventInstances.end(), this);
    if (it != PMMA::MouseScrollEventInstances.end()) {
        PMMA::MouseScrollEventInstances.erase(it);
    }
};