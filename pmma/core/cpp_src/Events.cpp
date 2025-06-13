#include <string>

#include "Events.hpp"

#include "PMMA_Core.hpp"

using namespace std;

size_t utf8_char_length(unsigned char c) {
    if ((c & 0x80) == 0x00) return 1;       // 0xxxxxxx
    else if ((c & 0xE0) == 0xC0) return 2;  // 110xxxxx
    else if ((c & 0xF0) == 0xE0) return 3;  // 1110xxxx
    else if ((c & 0xF8) == 0xF0) return 4;  // 11110xxx
    return 1; // fallback - invalid UTF-8, treat as 1 byte
}

void remove_utf8_char(std::string& text, size_t n) {
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
}

// Finds the start index of the last UTF-8 character
size_t get_last_utf8_char_index(const std::string& text) {
    if (text.empty()) return std::string::npos;

    size_t i = text.size() - 1;

    // Move backwards while the byte is a UTF-8 continuation byte (starts with '10')
    while (i > 0 && (static_cast<unsigned char>(text[i]) & 0xC0) == 0x80) {
        i--;
    }
    return i;
}

// Removes the last UTF-8 character from the string
void remove_last_utf8_char(std::string& text) {
    size_t start = get_last_utf8_char_index(text);
    if (start == std::string::npos) {
        // String is empty, nothing to remove
        return;
    }
    text.erase(start);
}

CPP_TextEvent::CPP_TextEvent() {
    PMMA::InternalTextEventInstances.push_back(this);
};

CPP_TextEvent::~CPP_TextEvent() {
    auto it = std::find(PMMA::InternalTextEventInstances.begin(), PMMA::InternalTextEventInstances.end(), this);
    if (it != PMMA::InternalTextEventInstances.end()) {
        PMMA::InternalTextEventInstances.erase(it);
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

void CPP_MouseEvent::GetPosition(float* out) {
    if (PMMA::MouseEvent_Instance == nullptr) {
        throw std::runtime_error("PMMA::MouseEvent_Instance is null");
    }
    PMMA::MouseEvent_Instance->GetPosition(out);
};

void CPP_MouseEvent::GetDelta(float* out) {
    if (PMMA::MouseEvent_Instance == nullptr) {
        throw std::runtime_error("PMMA::MouseEvent_Instance is null");
    }
    PMMA::MouseEvent_Instance->GetDelta(out);
};

void CPP_MouseEvent::GetDeltaToggle(float* out) {
    if (PMMA::MouseEvent_Instance == nullptr) {
        throw std::runtime_error("PMMA::MouseEvent_Instance is null");
    }
    PMMA::MouseEvent_Instance->GetDeltaToggle(out);
};