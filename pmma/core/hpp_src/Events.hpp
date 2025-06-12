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