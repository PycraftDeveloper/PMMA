# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "Events/WindowEvents.hpp" nogil:
    cdef cppclass CPP_TextEvent:
        inline string GetText() except + nogil

        inline void SetEnabled(bool NewIsEnabled) except + nogil
        inline bool GetEnabled() except + nogil

        inline void ClearText() except + nogil

        inline void Set_ControlKey_DoublePressDuration(float NewDuration) except + nogil
        inline void Set_ControlKey_LongPressDuration(float NewDuration) except + nogil
        inline void Set_ControlKey_RepeatPressDuration(float NewDuration) except + nogil

        inline void Set_ShiftKey_DoublePressDuration(float NewDuration) except + nogil
        inline void Set_ShiftKey_LongPressDuration(float NewDuration) except + nogil
        inline void Set_ShiftKey_RepeatPressDuration(float NewDuration) except + nogil

        inline void Set_VKey_DoublePressDuration(float NewDuration) except + nogil
        inline void Set_VKey_LongPressDuration(float NewDuration) except + nogil
        inline void Set_VKey_RepeatPressDuration(float NewDuration) except + nogil

        inline void Set_InsertKey_DoublePressDuration(float NewDuration) except + nogil
        inline void Set_InsertKey_LongPressDuration(float NewDuration) except + nogil
        inline void Set_InsertKey_RepeatPressDuration(float NewDuration) except + nogil

        inline void Set_DeleteKey_DoublePressDuration(float NewDuration) except + nogil
        inline void Set_DeleteKey_LongPressDuration(float NewDuration) except + nogil
        inline void Set_DeleteKey_RepeatPressDuration(float NewDuration) except + nogil

        inline void Set_BackspaceKey_DoublePressDuration(float NewDuration) except + nogil
        inline void Set_BackspaceKey_LongPressDuration(float NewDuration) except + nogil
        inline void Set_BackspaceKey_RepeatPressDuration(float NewDuration) except + nogil

    cdef cppclass CPP_DropEvent:
        inline const char** GetFilePaths() except + nogil
        inline const char** GetFilePathsToggle() except + nogil

        inline unsigned int GetNumberOfFilePaths() except + nogil
        inline void ClearFilePaths() except + nogil

        inline bool GetEnabled() except + nogil
        inline void SetEnabled(bool NewIsEnabled) except + nogil

cdef class TextInput:
    cdef:
        CPP_TextEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_TextEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def get_text(self):
        cdef string cpp_str = self.cpp_class_ptr.GetText()
        return cpp_str.c_str().decode("utf-8")

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, value):
        self.cpp_class_ptr.SetEnabled(value)

    def clear_text(self):
        self.cpp_class_ptr.ClearText()

    def set_control_key_double_press_duration(self, duration):
        self.cpp_class_ptr.Set_ControlKey_DoublePressDuration(duration)

    def set_control_key_long_press_duration(self, duration):
        self.cpp_class_ptr.Set_ControlKey_LongPressDuration(duration)

    def set_control_key_repeat_press_duration(self, duration):
        self.cpp_class_ptr.Set_ControlKey_RepeatPressDuration(duration)

    def set_shift_key_double_press_duration(self, duration):
        self.cpp_class_ptr.Set_ShiftKey_DoublePressDuration(duration)

    def set_shift_key_long_press_duration(self, duration):
        self.cpp_class_ptr.Set_ShiftKey_LongPressDuration(duration)

    def set_shift_key_repeat_press_duration(self, duration):
        self.cpp_class_ptr.Set_ShiftKey_RepeatPressDuration(duration)

    def set_v_key_double_press_duration(self, duration):
        self.cpp_class_ptr.Set_VKey_DoublePressDuration(duration)

    def set_v_key_long_press_duration(self, duration):
        self.cpp_class_ptr.Set_VKey_LongPressDuration(duration)

    def set_v_key_repeat_press_duration(self, duration):
        self.cpp_class_ptr.Set_VKey_RepeatPressDuration(duration)

    def set_insert_key_double_press_duration(self, duration):
        self.cpp_class_ptr.Set_InsertKey_DoublePressDuration(duration)

    def set_insert_key_long_press_duration(self, duration):
        self.cpp_class_ptr.Set_InsertKey_LongPressDuration(duration)

    def set_insert_key_repeat_press_duration(self, duration):
        self.cpp_class_ptr.Set_InsertKey_RepeatPressDuration(duration)

    def set_delete_key_double_press_duration(self, duration):
        self.cpp_class_ptr.Set_DeleteKey_DoublePressDuration(duration)

    def set_delete_key_long_press_duration(self, duration):
        self.cpp_class_ptr.Set_DeleteKey_LongPressDuration(duration)

    def set_delete_key_repeat_press_duration(self, duration):
        self.cpp_class_ptr.Set_DeleteKey_RepeatPressDuration(duration)

    def set_backspace_key_double_press_duration(self, duration):
        self.cpp_class_ptr.Set_BackspaceKey_DoublePressDuration(duration)

    def set_backspace_key_long_press_duration(self, duration):
        self.cpp_class_ptr.Set_BackspaceKey_LongPressDuration(duration)

    def set_backspace_key_repeat_press_duration(self, duration):
        self.cpp_class_ptr.Set_BackspaceKey_RepeatPressDuration(duration)

cdef class FileDropped:
    cdef:
        CPP_DropEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DropEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def get_file_paths(self):
        cdef const char** paths = self.cpp_class_ptr.GetFilePaths()
        count = self.cpp_class_ptr.GetNumberOfFilePaths()

        return [paths[i].decode("utf-8") for i in range(count)]

    def get_file_paths_toggle(self):
        count = self.cpp_class_ptr.GetNumberOfFilePaths()
        cdef const char** paths = self.cpp_class_ptr.GetFilePathsToggle()

        return [paths[i].decode("utf-8") for i in range(count)]

    def get_file_path_count(self):
        return self.cpp_class_ptr.GetNumberOfFilePaths()

    def clear_file_paths(self):
        self.cpp_class_ptr.ClearFilePaths()

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, enabled):
        self.cpp_class_ptr.SetEnabled(enabled)