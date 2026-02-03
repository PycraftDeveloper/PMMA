#pragma once
#include "PMMA_Exports.hpp"

#include <string>
#include <filesystem>

#include <glm/glm.hpp>

class EXPORT CPP_TextRenderer {
    public:
        CPP_DisplayCoordinate* Position;
        CPP_Color* ForegroundColor;
        CPP_Color* BackgroundColor;
        CPP_Logger* Logger;

        std::string Text = "";
        std::string Font;

        uint64_t ID;

        unsigned int Size;

        bool SizeSet = false;
        bool UseInLineFormatting = true;
        bool GlyphsPrepared = false;
        bool Changed = true;

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

        inline void SetUseInLineFormatting(bool NewUseInLineFormatting) {
            if (NewUseInLineFormatting != UseInLineFormatting) {
                Changed = true;
                GlyphsPrepared = false;
            }

            UseInLineFormatting = NewUseInLineFormatting;
        };

        inline bool GetUseInLineFormatting() {
            return UseInLineFormatting;
        };

        inline void SetText(std::string NewText) {
            if (NewText != Text) {
                Changed = true;
            }

            Text = NewText;
            GlyphsPrepared = false;
        };

        inline void SetFont(std::string NewFont) {
            if (!std::filesystem::exists(NewFont)) {
                if (Logger == nullptr) {
                    Logger = new CPP_Logger();
                }
                Logger->InternalLogError(
                    51,
                    "The specified font file does not exist: '" + NewFont + "'.");
                throw std::runtime_error("Font file does not exist!");
            }

            if (NewFont != Font) {
                Changed = true;
                GlyphsPrepared = false;
            }

            Font = NewFont;
        };

        inline void SetSize(unsigned int NewSize) {
            if (NewSize != Size) {
                Changed = true;
                GlyphsPrepared = false;
            }

            Size = NewSize;
            SizeSet = true;
        };

        void Render();
};