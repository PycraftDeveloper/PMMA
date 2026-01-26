# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

cdef extern from "Events/KeyPadEvents.hpp" nogil:
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

    cdef cppclass CPP_KeyPadEvent_0(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_1(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_2(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_3(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_4(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_5(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_6(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_7(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_8(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_9(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Decimal(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Divide(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Multiply(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Subtract(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Add(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Enter(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyPadEvent_Equal(CPP_ButtonPressedEvent):
        pass

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

cdef class Zero(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_0()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class One(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Two(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Three(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Four(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Five(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_5()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Six(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_6()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Seven(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_7()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Eight(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_8()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Nine(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_9()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Decimal(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Decimal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Decimal()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Divide(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Divide* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Divide()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Multiply(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Multiply* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Multiply()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Subtract(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Subtract* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Subtract()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Add(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Add* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Add()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Enter(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Enter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Enter()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Equal(ButtonPressedEvent):
    cdef:
        CPP_KeyPadEvent_Equal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Equal()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL