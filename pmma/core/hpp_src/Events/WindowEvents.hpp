#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <string>
#include <vector>

#include <GLFW/glfw3.h>

namespace PMMA::Events {
class Key_Control;
class Key_Shift;
class Key_V;
class Key_Insert;
class Key_Delete;
class Key_Backspace;
} // namespace PMMA::Events

namespace PMMA::Events {
class EXPORT Drop {
private:
    std::vector<std::string> FilePaths;
    unsigned int FilePathCount = 0;
    bool IsEnabled = true;

public:
    Drop();
    ~Drop();

    inline void Update(std::vector<std::string> NewFilePaths, unsigned int NewCount) {
        if (!IsEnabled) {
            return;
        }
        FilePaths = NewFilePaths;
        FilePathCount = NewCount;
    };

    inline const char **GetFilePaths() {
        const char **paths = new const char *[FilePathCount];
        for (unsigned int i = 0; i < FilePathCount; i++) {
            paths[i] = FilePaths[i].c_str();
        }
        return paths;
    };

    inline const char **GetFilePathsToggle() {
        const char **paths = new const char *[FilePathCount];
        for (unsigned int i = 0; i < FilePathCount; i++) {
            paths[i] = FilePaths[i].c_str();
        }
        FilePaths.clear();
        FilePathCount = 0;
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

class EXPORT TextInput {
private:
    PMMA::Events::Key_Control *Control_KeyEventPtr = nullptr;
    PMMA::Events::Key_Shift *Shift_KeyEventPtr = nullptr;
    PMMA::Events::Key_V *V_KeyEventPtr = nullptr;
    PMMA::Events::Key_Insert *Insert_KeyEventPtr = nullptr;
    PMMA::Events::Key_Delete *Delete_KeyEventPtr = nullptr;
    PMMA::Events::Key_Backspace *Backspace_KeyEventPtr = nullptr;
    std::string TextBuffer = "";
    bool IsEnabled = true;

public:
    TextInput();

    ~TextInput();

    inline void Update(std::string NewTextContent) {
        if (!IsEnabled) {
            return;
        }
        TextBuffer += NewTextContent;
    };

    void GenericUpdate(GLFWwindow *window);

    void RemoveBack();

    void RemoveFront();

    inline std::string GetText() {
        return TextBuffer;
    };

    inline void SetEnabled(bool NewIsEnabled) {
        IsEnabled = NewIsEnabled;
    };

    inline bool GetEnabled() {
        return IsEnabled;
    };

    inline void ClearText() {
        TextBuffer = "";
    };

    void Set_ControlKey_DoublePressDuration(float NewDuration);

    void Set_ControlKey_LongPressDuration(float NewDuration);

    void Set_ControlKey_RepeatPressDuration(float NewDuration);

    void Set_ShiftKey_DoublePressDuration(float NewDuration);

    void Set_ShiftKey_LongPressDuration(float NewDuration);

    void Set_ShiftKey_RepeatPressDuration(float NewDuration);

    void Set_VKey_DoublePressDuration(float NewDuration);

    void Set_VKey_LongPressDuration(float NewDuration);

    void Set_VKey_RepeatPressDuration(float NewDuration);

    void Set_InsertKey_DoublePressDuration(float NewDuration);

    void Set_InsertKey_LongPressDuration(float NewDuration);

    void Set_InsertKey_RepeatPressDuration(float NewDuration);

    void Set_DeleteKey_DoublePressDuration(float NewDuration);

    void Set_DeleteKey_LongPressDuration(float NewDuration);

    void Set_DeleteKey_RepeatPressDuration(float NewDuration);

    void Set_BackspaceKey_DoublePressDuration(float NewDuration);

    void Set_BackspaceKey_LongPressDuration(float NewDuration);

    void Set_BackspaceKey_RepeatPressDuration(float NewDuration);
};
} // namespace PMMA::Events