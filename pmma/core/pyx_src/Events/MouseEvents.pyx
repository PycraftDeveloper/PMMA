# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import numpy as np
cimport numpy as np

from Events cimport CPP_ButtonPressed, ButtonPressed

cdef extern from "Events/MouseEvents.hpp" nogil:
    cdef cppclass CPP_Mouse_Position "PMMA::Events::Mouse_Position":
        inline void GetPosition(float* out) except + nogil

        inline void GetDelta(float* out) except + nogil
        inline void GetDeltaToggle(float* out) except + nogil

        inline bool GetEnabled() except + nogil
        inline void SetEnabled(bool NewIsEnabled) except + nogil

    cdef cppclass CPP_Mouse_EnterWindow "PMMA::Events::Mouse_EnterWindow":
        inline bool GetEntered() except + nogil
        inline bool GetEnteredToggle() except + nogil

        inline bool GetEnabled() except + nogil
        inline void SetEnabled(bool NewIsEnabled) except + nogil

    cdef cppclass _CPP_Mouse_Button_Left(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_Left CPP_Mouse_Button_Left "PMMA::Events::Mouse_Button_Left"

    cdef cppclass _CPP_Mouse_Button_Right(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_Right CPP_Mouse_Button_Right "PMMA::Events::Mouse_Button_Right"

    cdef cppclass _CPP_Mouse_Button_Middle(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_Middle CPP_Mouse_Button_Middle "PMMA::Events::Mouse_Button_Middle"

    cdef cppclass _CPP_Mouse_Button_0(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_0 CPP_Mouse_Button_0 "PMMA::Events::Mouse_Button_0"

    cdef cppclass _CPP_Mouse_Button_1(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_1 CPP_Mouse_Button_1 "PMMA::Events::Mouse_Button_1"

    cdef cppclass _CPP_Mouse_Button_2(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_2 CPP_Mouse_Button_2 "PMMA::Events::Mouse_Button_2"

    cdef cppclass _CPP_Mouse_Button_3(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_3 CPP_Mouse_Button_3 "PMMA::Events::Mouse_Button_3"

    cdef cppclass _CPP_Mouse_Button_4(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Mouse_Button_4 CPP_Mouse_Button_4 "PMMA::Events::Mouse_Button_4"

    cdef cppclass CPP_Mouse_Scroll "PMMA::Events::Mouse_Scroll":
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

cdef class Mouse_Position:
    cdef:
        CPP_Mouse_Position* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Position()

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

cdef class Mouse_EnterWindow:
    cdef:
        CPP_Mouse_EnterWindow* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_EnterWindow()

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

cdef class Mouse_Button_Left(ButtonPressed):
    cdef:
        CPP_Mouse_Button_Left* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_Left()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Button_Right(ButtonPressed):
    cdef:
        CPP_Mouse_Button_Right* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_Right()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Button_Middle(ButtonPressed):
    cdef:
        CPP_Mouse_Button_Middle* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_Middle()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Button_0(ButtonPressed):
    cdef:
        CPP_Mouse_Button_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_0()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Button_1(ButtonPressed):
    cdef:
        CPP_Mouse_Button_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class MouseButton_2(ButtonPressed):
    cdef:
        CPP_Mouse_Button_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Button_3(ButtonPressed):
    cdef:
        CPP_Mouse_Button_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Button_4(ButtonPressed):
    cdef:
        CPP_Mouse_Button_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Button_4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Mouse_Scroll:
    cdef:
        CPP_Mouse_Scroll* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Mouse_Scroll()

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