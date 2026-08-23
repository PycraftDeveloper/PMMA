#define PMMA_ALLOW_UMBRELLA_HEADER
#include "PMMA_Core.hpp"

size_t utf8_char_length(unsigned char c) {
    if ((c & 0x80) == 0x00)
        return 1; // 0xxxxxxx
    else if ((c & 0xE0) == 0xC0)
        return 2; // 110xxxxx
    else if ((c & 0xF0) == 0xE0)
        return 3; // 1110xxxx
    else if ((c & 0xF8) == 0xF0)
        return 4; // 11110xxx
    return 1;     // fallback - invalid UTF-8, treat as 1 byte
};

void remove_utf8_char(std::string &text, size_t n) {
    size_t i = 0;          // byte index in the string
    size_t char_index = 0; // character count

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
size_t get_last_utf8_char_index(const std::string &text) {
    if (text.empty())
        return std::string::npos;

    size_t i = text.size() - 1;

    // Move backwards while the byte is a UTF-8 continuation byte (starts with '10')
    while (i > 0 && (static_cast<unsigned char>(text[i]) & 0xC0) == 0x80) {
        i--;
    }
    return i;
};

// Removes the last UTF-8 character from the string
void remove_last_utf8_char(std::string &text) {
    size_t start = get_last_utf8_char_index(text);
    if (start == std::string::npos) {
        // String is empty, nothing to remove
        return;
    }
    text.erase(start);
};

PMMA::Events::TextInput::TextInput() {
    PMMA::Core::ActiveDisplayInstance->TextEventInstances.push_back(this);

    Control_KeyEventPtr = new PMMA::Events::Key_Control();
    Shift_KeyEventPtr = new PMMA::Events::Key_Shift();
    V_KeyEventPtr = new PMMA::Events::Key_V();
    Insert_KeyEventPtr = new PMMA::Events::Key_Insert();
    Delete_KeyEventPtr = new PMMA::Events::Key_Delete();
    Backspace_KeyEventPtr = new PMMA::Events::Key_Backspace();

    PMMA::Registry::TextEventInstanceCount++;
};

PMMA::Events::TextInput::~TextInput() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->TextEventInstances.begin(), PMMA::Core::ActiveDisplayInstance->TextEventInstances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->TextEventInstances.end()) {
        PMMA::Core::ActiveDisplayInstance->TextEventInstances.erase(it);
    }

    Control_KeyEventPtr = nullptr;
    Shift_KeyEventPtr = nullptr;
    V_KeyEventPtr = nullptr;
    Insert_KeyEventPtr = nullptr;
    Delete_KeyEventPtr = nullptr;
    Backspace_KeyEventPtr = nullptr;

    PMMA::Registry::TextEventInstanceCount--;
};

void PMMA::Events::TextInput::RemoveBack() {
    if (!IsEnabled) {
        return;
    }
    if (!TextBuffer.empty()) {
        remove_last_utf8_char(TextBuffer);
    }
};

void PMMA::Events::TextInput::RemoveFront() {
    if (!IsEnabled) {
        return;
    }
    if (TextBuffer.size() > 0) {
        remove_utf8_char(TextBuffer, 0);
    }
};

void PMMA::Events::TextInput::GenericUpdate(GLFWwindow *window) {
    if (!IsEnabled) {
        return;
    }

    if (Control_KeyEventPtr->GetPressed()) {
        if (V_KeyEventPtr->PollLongPressed() || V_KeyEventPtr->GetPressedToggle()) {
            const char *ClipboardData = glfwGetClipboardString(window);
            if (ClipboardData == nullptr) {
                return;
            }
            std::string NewTextContent = ClipboardData;
            Update(NewTextContent);
        }
    }

    if (Shift_KeyEventPtr->GetPressed()) {
        if (Insert_KeyEventPtr->PollLongPressed() || Insert_KeyEventPtr->GetPressedToggle()) {
            const char *ClipboardData = glfwGetClipboardString(window);
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

PMMA::Events::Drop::Drop() {
    PMMA::Core::ActiveDisplayInstance->DropEvent_Instances.push_back(this);

    PMMA::Registry::DropEventInstanceCount++;
};

PMMA::Events::Drop::~Drop() {
    auto it = find(PMMA::Core::ActiveDisplayInstance->DropEvent_Instances.begin(), PMMA::Core::ActiveDisplayInstance->DropEvent_Instances.end(), this);
    if (it != PMMA::Core::ActiveDisplayInstance->DropEvent_Instances.end()) {
        PMMA::Core::ActiveDisplayInstance->DropEvent_Instances.erase(it);
    }

    PMMA::Registry::DropEventInstanceCount--;
};