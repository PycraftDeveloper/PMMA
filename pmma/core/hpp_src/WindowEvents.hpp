#pragma once
#include "PMMA_Exports.hpp"

#include <string>
#include <vector>

class EXPORT CPP_DropEvent {
    private:
        std::vector<std::string> FilePaths;
        unsigned int FilePathCount = 0;
        bool IsEnabled = true;

    public:
        CPP_DropEvent();
        ~CPP_DropEvent();

        inline void Update(std::vector<std::string> NewFilePaths, unsigned int NewCount) {
            if (!IsEnabled) {
                return;
            }
            FilePaths = NewFilePaths;
            FilePathCount = NewCount;
        };

        inline const char** GetFilePaths() {
            const char** paths = new const char*[FilePathCount];
            for (unsigned int i = 0; i < FilePathCount; i++) {
                paths[i] = FilePaths[i].c_str();
            }
            return paths;
        };

        inline unsigned int GetNumberOfFilePaths() {
            return FilePathCount;
        };

        inline void ClearFilePaths() {
            FilePaths.clear();
            FilePathCount = 0;
        };

        inline bool GetEnabled() {
            return IsEnabled;
        };

        inline void SetEnabled(bool NewIsEnabled) {
            IsEnabled = NewIsEnabled;
        };
};