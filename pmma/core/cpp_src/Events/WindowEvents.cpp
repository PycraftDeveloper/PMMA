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

    Control_KeyEventPtr = new CPP_KeyEvent_Control();
    Shift_KeyEventPtr = new CPP_KeyEvent_Shift();
    V_KeyEventPtr = new CPP_KeyEvent_V();
    Insert_KeyEventPtr = new CPP_KeyEvent_Insert();
    Delete_KeyEventPtr = new CPP_KeyEvent_Delete();
    Backspace_KeyEventPtr = new CPP_KeyEvent_Backspace();

    PMMA::TextEventInstanceCount++;
};

CPP_TextEvent::~CPP_TextEvent() {
    auto it = find(PMMA::TextEventInstances.begin(), PMMA::TextEventInstances.end(), this);
    if (it != PMMA::TextEventInstances.end()) {
        PMMA::TextEventInstances.erase(it);
    }

    Control_KeyEventPtr = nullptr;
    Shift_KeyEventPtr = nullptr;
    V_KeyEventPtr = nullptr;
    Insert_KeyEventPtr = nullptr;
    Delete_KeyEventPtr = nullptr;
    Backspace_KeyEventPtr = nullptr;

    PMMA::TextEventInstanceCount--;
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

void CPP_TextEvent::GenericUpdate(GLFWwindow* window) {
    if (!IsEnabled) {
        return;
    }

    if (Control_KeyEventPtr->GetPressed()) {
        if (V_KeyEventPtr->PollLongPressed() || V_KeyEventPtr->GetPressedToggle()) {
            const char* ClipboardData = glfwGetClipboardString(window);
            if (ClipboardData == nullptr) {
                return;
            }
            std::string NewTextContent = ClipboardData;
            Update(NewTextContent);
        }
    }

    if (Shift_KeyEventPtr->GetPressed()) {
        if (Insert_KeyEventPtr->PollLongPressed() || Insert_KeyEventPtr->GetPressedToggle()) {
            const char* ClipboardData = glfwGetClipboardString(window);
            if (ClipboardData == nullptr) {
                return;
            }
            std::string NewTextContent = ClipboardData;
            Update(NewTextContent);
        }
    }

    if (Backspace_KeyEventPtr->PollLongPressed() || Backspace_KeyEventPtr->GetPressedToggle()) {
        RemoveBack();
    }

    if (Delete_KeyEventPtr->PollLongPressed() || Delete_KeyEventPtr->GetPressedToggle()) {
        RemoveFront();
    }
};

CPP_DropEvent::CPP_DropEvent() {
    PMMA::DropEvent_Instances.push_back(this);

    PMMA::DropEventInstanceCount++;
};

CPP_DropEvent::~CPP_DropEvent() {
    auto it = find(PMMA::DropEvent_Instances.begin(), PMMA::DropEvent_Instances.end(), this);
    if (it != PMMA::DropEvent_Instances.end()) {
        PMMA::DropEvent_Instances.erase(it);
    }

    PMMA::DropEventInstanceCount--;
};