# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_TextEvent:
        string GetText() except + nogil

        void SetEnabled(bool NewIsEnabled) except + nogil
        bool GetEnabled() except + nogil

        void ClearText() except + nogil

    cdef cppclass CPP_MousePositionEvent:
        void GetPosition(float* out) except + nogil

        void GetDelta(float* out) except + nogil
        void GetDeltaToggle(float* out) except + nogil

    cdef cppclass CPP_MouseEnterWindowEvent:
        bool GetEntered() except + nogil
        bool GetEnteredToggle() except + nogil

    cdef cppclass CPP_MouseButton_Left_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_Right_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_Middle_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_0_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_1_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_2_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_3_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

    cdef cppclass CPP_MouseButton_4_Event:
        bool GetPressed() except + nogil
        bool GetPressedToggle() except + nogil
        bool GetDoublePressed() except + nogil
        bool GetLongPressed() except + nogil

        float GetRepeatPressDuration() except + nogil
        float GetLongPressDuration() except + nogil
        float GetDoublePressDuration() except + nogil

        bool PollLongPressed() except + nogil

        void SetDoublePressDuration(float Duration) except + nogil
        void SetLongPressDuration(float Duration) except + nogil
        void SetRepeatPressDuration(float Duration) except + nogil

cdef class TextEvent:
    cdef:
        CPP_TextEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_TextEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_text(self):
        cdef string cpp_str = self.cpp_class_ptr.GetText()
        return cpp_str.c_str().decode("utf-8")

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, value):
        self.cpp_class_ptr.SetEnabled(value)

    def clear_text(self):
        self.cpp_class_ptr.ClearText()

cdef class MousePositionEvent:
    cdef:
        CPP_MousePositionEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MousePositionEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_position(self, using_numpy=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] position_np
            float* position_ptr

        position_np = np.empty(2, dtype=np.float32, order='C')

        position_ptr = <float*>&position_np[0]

        self.cpp_class_ptr.GetPosition(position_ptr)

        if using_numpy:
            return position_np
        else:
            return position_np.tolist()

    def get_delta(self, using_numpy=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] delta_np
            float* delta_ptr

        delta_np = np.empty(2, dtype=np.float32, order='C')

        delta_ptr = <float*>&delta_np[0]

        self.cpp_class_ptr.GetDelta(delta_ptr)

        if using_numpy:
            return delta_np
        else:
            return delta_np.tolist()

    def get_delta_toggle(self, using_numpy=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] delta_toggle_np
            float* delta_toggle_ptr

        delta_toggle_np = np.empty(2, dtype=np.float32, order='C')

        delta_toggle_ptr = <float*>&delta_toggle_np[0]

        self.cpp_class_ptr.GetDeltaToggle(delta_toggle_ptr)

        if using_numpy:
            return delta_toggle_np
        else:
            return delta_toggle_np.tolist()

cdef class MouseEnterWindowEvent:
    cdef:
        CPP_MouseEnterWindowEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseEnterWindowEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_entered(self):
        return self.cpp_class_ptr.GetEntered()

    def get_entered_toggle(self):
        return self.cpp_class_ptr.GetEnteredToggle()

cdef class MouseButton_Left_Event:
    cdef:
        CPP_MouseButton_Left_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_Left_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_Right_Event:
    cdef:
        CPP_MouseButton_Right_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_Right_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_Middle_Event:
    cdef:
        CPP_MouseButton_Middle_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_Middle_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_0_Event:
    cdef:
        CPP_MouseButton_0_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_0_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_1_Event:
    cdef:
        CPP_MouseButton_1_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_1_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_2_Event:
    cdef:
        CPP_MouseButton_2_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_2_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_3_Event:
    cdef:
        CPP_MouseButton_3_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_3_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)

cdef class MouseButton_4_Event:
    cdef:
        CPP_MouseButton_4_Event* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_MouseButton_4_Event()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_class_ptr.SetLongPressDuration(duration)