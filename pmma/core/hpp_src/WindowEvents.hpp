#pragma once
#include "PMMA_Exports.hpp"

class EXPORT CPP_InternalDropEvent {
    private:
        std::string FilePath;
        bool IsEnabled = true;

    public:
        inline void Update(std::string NewFilePath) {
            if (!IsEnabled) {
                return;
            }
            FilePath = NewFilePath;
        };

        inline std::string GetFilePath() {
            return FilePath;
        };

        inline void ClearFilePath() {
            FilePath = "";
        };

        inline bool GetEnabled() {
            return IsEnabled;
        };

        inline void SetEnabled(bool NewIsEnabled) {
            IsEnabled = NewIsEnabled;
        };
};

class EXPORT CPP_DropEvent {
    public:
        CPP_DropEvent();
        ~CPP_DropEvent();

        std::string GetFilePath();

        void ClearFilePath();

        bool GetEnabled();

        void SetEnabled(bool NewIsEnabled);
};