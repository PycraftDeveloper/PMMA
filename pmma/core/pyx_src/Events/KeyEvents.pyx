# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

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

    cdef cppclass CPP_KeyEvent_Space(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Apostrophe(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Comma(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Minus(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Period(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Slash(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_0(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_1(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_2(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_3(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_4(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_5(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_6(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_7(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_8(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_9(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Semicolon(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Equal(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_A(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_B(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_C(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_D(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_E(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_G(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_H(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_I(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_J(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_K(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_L(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_M(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_N(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_O(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_P(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Q(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_R(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_S(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_T(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_U(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_V(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_W(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_X(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Y(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Z(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Left_Bracket(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Backslash(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Right_Bracket(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Grave_Accent(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_World_1(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_World_2(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Escape(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Enter(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Tab(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Backspace(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Insert(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Delete(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Right(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Left(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Down(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Up(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Page_Up(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Page_Down(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Home(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_End(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Caps_Lock(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Scroll_Lock(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Num_Lock(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Print_Screen(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Pause(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F1(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F2(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F3(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F4(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F5(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F6(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F7(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F8(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F9(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F10(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F11(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F12(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F13(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F14(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F15(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F16(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F17(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F18(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F19(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F20(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F21(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F22(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F23(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F24(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_F25(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Left_Shift(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Left_Control(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Left_Alt(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Left_Super(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Right_Shift(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Right_Control(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Right_Alt(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Right_Super(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Shift(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Control(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Alt(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Super(CPP_ButtonPressedEvent):
        pass

    cdef cppclass CPP_KeyEvent_Menu(CPP_ButtonPressedEvent):
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

cdef class Space(ButtonPressedEvent):
    cdef CPP_KeyEvent_Space* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Space()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Apostrophe(ButtonPressedEvent):
    cdef CPP_KeyEvent_Apostrophe* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Apostrophe()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Comma(ButtonPressedEvent):
    cdef CPP_KeyEvent_Comma* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Comma()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Minus(ButtonPressedEvent):
    cdef CPP_KeyEvent_Minus* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Minus()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Period(ButtonPressedEvent):
    cdef CPP_KeyEvent_Period* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Period()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Slash(ButtonPressedEvent):
    cdef CPP_KeyEvent_Slash* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Slash()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Zero(ButtonPressedEvent):
    cdef CPP_KeyEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_0()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class One(ButtonPressedEvent):
    cdef CPP_KeyEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Two(ButtonPressedEvent):
    cdef CPP_KeyEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Three(ButtonPressedEvent):
    cdef CPP_KeyEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Four(ButtonPressedEvent):
    cdef CPP_KeyEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Five(ButtonPressedEvent):
    cdef CPP_KeyEvent_5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_5()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Six(ButtonPressedEvent):
    cdef CPP_KeyEvent_6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_6()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Seven(ButtonPressedEvent):
    cdef CPP_KeyEvent_7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_7()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Eight(ButtonPressedEvent):
    cdef CPP_KeyEvent_8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_8()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Nine(ButtonPressedEvent):
    cdef CPP_KeyEvent_9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_9()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Semicolon(ButtonPressedEvent):
    cdef CPP_KeyEvent_Semicolon* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Semicolon()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Equal(ButtonPressedEvent):
    cdef CPP_KeyEvent_Equal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Equal()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class A(ButtonPressedEvent):
    cdef CPP_KeyEvent_A* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_A()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class B(ButtonPressedEvent):
    cdef CPP_KeyEvent_B* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_B()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class C(ButtonPressedEvent):
    cdef CPP_KeyEvent_C* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_C()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class D(ButtonPressedEvent):
    cdef CPP_KeyEvent_D* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_D()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class E(ButtonPressedEvent):
    cdef CPP_KeyEvent_E* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_E()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F(ButtonPressedEvent):
    cdef CPP_KeyEvent_F* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class G(ButtonPressedEvent):
    cdef CPP_KeyEvent_G* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_G()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class H(ButtonPressedEvent):
    cdef CPP_KeyEvent_H* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_H()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class I(ButtonPressedEvent):
    cdef CPP_KeyEvent_I* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_I()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class J(ButtonPressedEvent):
    cdef CPP_KeyEvent_J* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_J()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class K(ButtonPressedEvent):
    cdef CPP_KeyEvent_K* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_K()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class L(ButtonPressedEvent):
    cdef CPP_KeyEvent_L* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_L()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class M(ButtonPressedEvent):
    cdef CPP_KeyEvent_M* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_M()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class N(ButtonPressedEvent):
    cdef CPP_KeyEvent_N* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_N()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class O(ButtonPressedEvent):
    cdef CPP_KeyEvent_O* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_O()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class P(ButtonPressedEvent):
    cdef CPP_KeyEvent_P* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_P()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Q(ButtonPressedEvent):
    cdef CPP_KeyEvent_Q* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Q()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class R(ButtonPressedEvent):
    cdef CPP_KeyEvent_R* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_R()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class S(ButtonPressedEvent):
    cdef CPP_KeyEvent_S* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_S()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class T(ButtonPressedEvent):
    cdef CPP_KeyEvent_T* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_T()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class U(ButtonPressedEvent):
    cdef CPP_KeyEvent_U* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_U()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class V(ButtonPressedEvent):
    cdef CPP_KeyEvent_V* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_V()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class W(ButtonPressedEvent):
    cdef CPP_KeyEvent_W* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_W()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class X(ButtonPressedEvent):
    cdef CPP_KeyEvent_X* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_X()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Y(ButtonPressedEvent):
    cdef CPP_KeyEvent_Y* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Y()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Z(ButtonPressedEvent):
    cdef CPP_KeyEvent_Z* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Z()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Left_Bracket(ButtonPressedEvent):
    cdef CPP_KeyEvent_Left_Bracket* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Bracket()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Backslash(ButtonPressedEvent):
    cdef CPP_KeyEvent_Backslash* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Backslash()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Right_Bracket(ButtonPressedEvent):
    cdef CPP_KeyEvent_Right_Bracket* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Bracket()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Grave_Accent(ButtonPressedEvent):
    cdef CPP_KeyEvent_Grave_Accent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Grave_Accent()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class World_1(ButtonPressedEvent):
    cdef CPP_KeyEvent_World_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_World_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class World_2(ButtonPressedEvent):
    cdef CPP_KeyEvent_World_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_World_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Escape(ButtonPressedEvent):
    cdef CPP_KeyEvent_Escape* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Escape()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Enter(ButtonPressedEvent):
    cdef CPP_KeyEvent_Enter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Enter()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Tab(ButtonPressedEvent):
    cdef CPP_KeyEvent_Tab* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Tab()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Backspace(ButtonPressedEvent):
    cdef CPP_KeyEvent_Backspace* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Backspace()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Insert(ButtonPressedEvent):
    cdef CPP_KeyEvent_Insert* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Insert()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Delete(ButtonPressedEvent):
    cdef CPP_KeyEvent_Delete* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Delete()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Right(ButtonPressedEvent):
    cdef CPP_KeyEvent_Right* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Left(ButtonPressedEvent):
    cdef CPP_KeyEvent_Left* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Down(ButtonPressedEvent):
    cdef CPP_KeyEvent_Down* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Down()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Up(ButtonPressedEvent):
    cdef CPP_KeyEvent_Up* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Up()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Page_Up(ButtonPressedEvent):
    cdef CPP_KeyEvent_Page_Up* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Page_Up()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Page_Down(ButtonPressedEvent):
    cdef CPP_KeyEvent_Page_Down* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Page_Down()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Home(ButtonPressedEvent):
    cdef CPP_KeyEvent_Home* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Home()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class End(ButtonPressedEvent):
    cdef CPP_KeyEvent_End* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_End()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Caps_Lock(ButtonPressedEvent):
    cdef CPP_KeyEvent_Caps_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Caps_Lock()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Scroll_Lock(ButtonPressedEvent):
    cdef CPP_KeyEvent_Scroll_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Scroll_Lock()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Num_Lock(ButtonPressedEvent):
    cdef CPP_KeyEvent_Num_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Num_Lock()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Print_Screen(ButtonPressedEvent):
    cdef CPP_KeyEvent_Print_Screen* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Print_Screen()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Pause(ButtonPressedEvent):
    cdef CPP_KeyEvent_Pause* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Pause()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F1(ButtonPressedEvent):
    cdef CPP_KeyEvent_F1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F2(ButtonPressedEvent):
    cdef CPP_KeyEvent_F2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F3(ButtonPressedEvent):
    cdef CPP_KeyEvent_F3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F4(ButtonPressedEvent):
    cdef CPP_KeyEvent_F4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F5(ButtonPressedEvent):
    cdef CPP_KeyEvent_F5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F5()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F6(ButtonPressedEvent):
    cdef CPP_KeyEvent_F6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F6()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F7(ButtonPressedEvent):
    cdef CPP_KeyEvent_F7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F7()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F8(ButtonPressedEvent):
    cdef CPP_KeyEvent_F8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F8()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F9(ButtonPressedEvent):
    cdef CPP_KeyEvent_F9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F9()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F10(ButtonPressedEvent):
    cdef CPP_KeyEvent_F10* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F10()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F11(ButtonPressedEvent):
    cdef CPP_KeyEvent_F11* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F11()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F12(ButtonPressedEvent):
    cdef CPP_KeyEvent_F12* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F12()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F13(ButtonPressedEvent):
    cdef CPP_KeyEvent_F13* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F13()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F14(ButtonPressedEvent):
    cdef CPP_KeyEvent_F14* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F14()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F15(ButtonPressedEvent):
    cdef CPP_KeyEvent_F15* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F15()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F16(ButtonPressedEvent):
    cdef CPP_KeyEvent_F16* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F16()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F17(ButtonPressedEvent):
    cdef CPP_KeyEvent_F17* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F17()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F18(ButtonPressedEvent):
    cdef CPP_KeyEvent_F18* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F18()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F19(ButtonPressedEvent):
    cdef CPP_KeyEvent_F19* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F19()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F20(ButtonPressedEvent):
    cdef CPP_KeyEvent_F20* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F20()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F21(ButtonPressedEvent):
    cdef CPP_KeyEvent_F21* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F21()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F22(ButtonPressedEvent):
    cdef CPP_KeyEvent_F22* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F22()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F23(ButtonPressedEvent):
    cdef CPP_KeyEvent_F23* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F23()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F24(ButtonPressedEvent):
    cdef CPP_KeyEvent_F24* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F24()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class F25(ButtonPressedEvent):
    cdef CPP_KeyEvent_F25* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F25()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Left_Shift(ButtonPressedEvent):
    cdef CPP_KeyEvent_Left_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Shift()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Left_Control(ButtonPressedEvent):
    cdef CPP_KeyEvent_Left_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Control()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Left_Alt(ButtonPressedEvent):
    cdef CPP_KeyEvent_Left_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Alt()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Left_Super(ButtonPressedEvent):
    cdef CPP_KeyEvent_Left_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Super()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Right_Shift(ButtonPressedEvent):
    cdef CPP_KeyEvent_Right_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Shift()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Right_Control(ButtonPressedEvent):
    cdef CPP_KeyEvent_Right_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Control()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Right_Alt(ButtonPressedEvent):
    cdef CPP_KeyEvent_Right_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Alt()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Right_Super(ButtonPressedEvent):
    cdef CPP_KeyEvent_Right_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Super()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Shift(ButtonPressedEvent):
    cdef CPP_KeyEvent_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Shift()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Control(ButtonPressedEvent):
    cdef CPP_KeyEvent_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Control()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Alt(ButtonPressedEvent):
    cdef CPP_KeyEvent_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Alt()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Super(ButtonPressedEvent):
    cdef CPP_KeyEvent_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Super()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr

cdef class Menu(ButtonPressedEvent):
    cdef CPP_KeyEvent_Menu* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Menu()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr