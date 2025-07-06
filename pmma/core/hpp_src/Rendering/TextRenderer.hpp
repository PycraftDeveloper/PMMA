#pragma once
#include "PMMA_Exports.hpp"

#include <string>

#include <glm/glm.hpp>

class EXPORT CPP_TextRenderer {
    public:
        std::string Text;
        std::string Font;

        glm::vec4 ForegroundColor;
        glm::vec4 BackgroundColor = glm::vec4(0, 0, 0, 0);

        glm::vec2 Position;

        unsigned int Size;

        CPP_TextRenderer();

        inline void SetText(std::string NewText) {
            Text = NewText;
        };

        inline void SetFont(std::string NewFont) {
            Font = NewFont;
        };

        inline void SetSize(unsigned int NewSize) {
            Size = NewSize;
        };

        inline void SetForegroundColor(float* NewColor) {
            ForegroundColor = glm::vec4(NewColor[0], NewColor[1], NewColor[2], NewColor[3]);
        };

        inline void SetBackgroundColor(float* NewColor) {
            BackgroundColor = glm::vec4(NewColor[0], NewColor[1], NewColor[2], NewColor[3]);
        };

        inline void SetPosition(unsigned int* NewPosition) {
            Position = glm::vec2(NewPosition[0], NewPosition[1]);
        };

        void Render();
};