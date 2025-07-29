# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_ButtonPressedEvent:
        inline bool GetPressed() except + nogil

        inline bool GetPressedToggle() except + nogil
        inline bool GetDoublePressed() except + nogil

        inline void SetLongPressDuration(float Duration) except + nogil
        inline void SetRepeatPressDuration(float Duration) except + nogil
        inline void SetDoublePressDuration(float Duration) except + nogil

        inline bool GetLongPressed() except + nogil
        inline bool PollLongPressed() except + nogil

        inline float GetRepeatPressDuration() except + nogil
        inline float GetLongPressDuration() except + nogil
        inline float GetDoublePressDuration() except + nogil

    cdef cppclass CPP_MousePositionEvent:
        inline void GetPosition(float* out) except + nogil

        inline void GetDelta(float* out) except + nogil
        inline void GetDeltaToggle(float* out) except + nogil

        inline bool GetEnabled() except + nogil
        inline void SetEnabled(bool NewIsEnabled) except + nogil

    cdef cppclass CPP_MouseEnterWindowEvent:
        inline bool GetEntered() except + nogil
        inline bool GetEnteredToggle() except + nogil

        inline bool GetEnabled() except + nogil
        inline void SetEnabled(bool NewIsEnabled) except + nogil

    cdef cppclass CPP_MouseButtonEvent_Left(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_Right(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_Middle(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_0(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_1(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_2(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_3(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseButtonEvent_4(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_MouseScrollEvent:
        inline void GetPosition(float* out) except + nogil
        inline void ClearPosition() except + nogil
        inline float GetHorizontalPosition() except + nogil
        inline float GetVerticalPosition() except + nogil

        inline void GetDelta(float* out) except + nogil
        inline float GetHorizontalDelta() except + nogil
        inline float GetVerticalDelta() except + nogil

        inline void GetDeltaToggle(float* out) except + nogil
        inline float GetHorizontalDeltaToggle() except + nogil
        inline float GetVerticalDeltaToggle() except + nogil

        inline bool GetEnabled() except + nogil
        inline void SetEnabled(bool NewIsEnabled) except + nogil

cdef class ButtonPressedEvent:
    cdef CPP_ButtonPressedEvent* cpp_base_class_ptr

    def get_pressed(self):
        return self.cpp_base_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        return self.cpp_base_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        return self.cpp_base_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        return self.cpp_base_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        return self.cpp_base_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        return self.cpp_base_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        return self.cpp_base_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        return self.cpp_base_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        self.cpp_base_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        self.cpp_base_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        self.cpp_base_class_ptr.SetLongPressDuration(duration)

cdef class MousePosition:
    cdef:
        CPP_MousePositionEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MousePositionEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

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

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, value):
        self.cpp_class_ptr.SetEnabled(value)

cdef class MouseEnterWindow:
    cdef:
        CPP_MouseEnterWindowEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseEnterWindowEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def get_entered(self):
        return self.cpp_class_ptr.GetEntered()

    def get_entered_toggle(self):
        return self.cpp_class_ptr.GetEnteredToggle()

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, value):
        self.cpp_class_ptr.SetEnabled(value)

cdef class MouseButton_Left(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_Left* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_Left()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_Right(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_Right* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_Right()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_Middle(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_Middle* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_Middle()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_0(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_0()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_1(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_2(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_3(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_4(ButtonPressedEvent):
    cdef:
        CPP_MouseButtonEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseScroll:
    cdef:
        CPP_MouseScrollEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseScrollEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

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

    def clear_position(self):
        self.cpp_class_ptr.ClearPosition()

    def get_horizontal_position(self):
        return self.cpp_class_ptr.GetHorizontalPosition()

    def get_vertical_position(self):
        return self.cpp_class_ptr.GetVerticalPosition()

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

    def get_horizontal_delta(self):
        return self.cpp_class_ptr.GetHorizontalDelta()

    def get_vertical_delta(self):
        return self.cpp_class_ptr.GetVerticalDelta()

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

    def get_horizontal_delta_toggle(self):
        return self.cpp_class_ptr.GetHorizontalDeltaToggle()

    def get_vertical_delta_toggle(self):
        return self.cpp_class_ptr.GetVerticalDeltaToggle()

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, value):
        self.cpp_class_ptr.SetEnabled(value)