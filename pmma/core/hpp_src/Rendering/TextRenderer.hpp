#pragma once
#include "PMMA_Exports.hpp"

#include <string>

#include <glm/glm.hpp>

class EXPORT CPP_TextRenderer {
    public:
        CPP_DisplayCoordinateFormat* Position;
        CPP_ColorFormat* ForegroundColor;
        CPP_ColorFormat* BackgroundColor;
        CPP_Logger* Logger;

        std::string Text = "";
        std::string Font;

        uint64_t ID;

        unsigned int Size;

        bool FontSet = false;
        bool SizeSet = false;

        CPP_TextRenderer();

        ~CPP_TextRenderer() {
            if (Logger != nullptr) {
                delete Logger;
                Logger = nullptr;
            }

            delete Position;
            Position = nullptr;

            delete ForegroundColor;
            ForegroundColor = nullptr;

            delete BackgroundColor;
            BackgroundColor = nullptr;
        };

        inline void SetText(std::string NewText) {
            Text = NewText;
        };

        inline void SetFont(std::string NewFont) {
            Font = NewFont;
            FontSet = true;
        };

        inline void SetSize(unsigned int NewSize) {
            Size = NewSize;
            SizeSet = true;
        };

        void Render();
};