#pragma once
#include "PMMA_Exports.hpp"

#include <string>

#include <glm/glm.hpp>

class EXPORT CPP_TextRenderer {
    public:
        std::string Text;
        std::string Font;

        CPP_ColorFormat* ForegroundColor;
        CPP_ColorFormat* BackgroundColor;

        glm::vec2 Position;
        uint64_t ID;

        unsigned int Size;

        CPP_TextRenderer();

        ~CPP_TextRenderer() {
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
        };

        inline void SetSize(unsigned int NewSize) {
            Size = NewSize;
        };

        inline void SetPosition(unsigned int* NewPosition) {
            Position = glm::vec2(NewPosition[0], NewPosition[1]);
        };

        void Render();
};