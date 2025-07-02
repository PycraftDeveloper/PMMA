#pragma once
#include "PMMA_Exports.hpp"

#include <string>
#include <vector>

#include <GLFW/glfw3.h>

#include "KeyEvents.hpp"

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

        inline const char** GetFilePathsToggle() {
            const char** paths = new const char*[FilePathCount];
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

class EXPORT CPP_TextEvent {
    private:
        CPP_KeyEvent_Control* Control_KeyEventPtr = nullptr;
        CPP_KeyEvent_Shift* Shift_KeyEventPtr = nullptr;
        CPP_KeyEvent_V* V_KeyEventPtr = nullptr;
        CPP_KeyEvent_Insert* Insert_KeyEventPtr = nullptr;
        CPP_KeyEvent_Delete* Delete_KeyEventPtr = nullptr;
        CPP_KeyEvent_Backspace* Backspace_KeyEventPtr = nullptr;
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

        void GenericUpdate(GLFWwindow* window);

        void RemoveBack();

        void RemoveFront();

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

        inline void Set_ControlKey_DoublePressDuration(float NewDuration) {
            Control_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_ControlKey_LongPressDuration(float NewDuration) {
            Control_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_ControlKey_RepeatPressDuration(float NewDuration) {
            Control_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_ShiftKey_DoublePressDuration(float NewDuration) {
            Shift_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_ShiftKey_LongPressDuration(float NewDuration) {
            Shift_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_ShiftKey_RepeatPressDuration(float NewDuration) {
            Shift_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_VKey_DoublePressDuration(float NewDuration) {
            V_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_VKey_LongPressDuration(float NewDuration) {
            V_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_VKey_RepeatPressDuration(float NewDuration) {
            V_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_InsertKey_DoublePressDuration(float NewDuration) {
            Insert_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_InsertKey_LongPressDuration(float NewDuration) {
            Insert_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_InsertKey_RepeatPressDuration(float NewDuration) {
            Insert_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_DeleteKey_DoublePressDuration(float NewDuration) {
            Delete_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_DeleteKey_LongPressDuration(float NewDuration) {
            Delete_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_DeleteKey_RepeatPressDuration(float NewDuration) {
            Delete_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };

        inline void Set_BackspaceKey_DoublePressDuration(float NewDuration) {
            Backspace_KeyEventPtr->SetDoublePressDuration(NewDuration);
        };

        inline void Set_BackspaceKey_LongPressDuration(float NewDuration) {
            Backspace_KeyEventPtr->SetLongPressDuration(NewDuration);
        };

        inline void Set_BackspaceKey_RepeatPressDuration(float NewDuration) {
            Backspace_KeyEventPtr->SetRepeatPressDuration(NewDuration);
        };
};