# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

cdef extern from "Internal/Events/InternalEvents.hpp" nogil:
    cdef cppclass CPP_ButtonPressed "PMMA::Internal::Events::ButtonPressed":
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

cdef extern from "Events/KeyEvents.hpp" nogil:
    cdef cppclass _CPP_Key_Space(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Space CPP_Key_Space "PMMA::Events::Key_Space"

    cdef cppclass _CPP_Key_Apostrophe(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Apostrophe CPP_Key_Apostrophe "PMMA::Events::Key_Apostrophe"

    cdef cppclass _CPP_Key_Comma(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Comma CPP_Key_Comma "PMMA::Events::Key_Comma"

    cdef cppclass _CPP_Key_Minus(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Minus CPP_Key_Minus "PMMA::Events::Key_Minus"

    cdef cppclass _CPP_Key_Period(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Period CPP_Key_Period "PMMA::Events::Key_Period"

    cdef cppclass _CPP_Key_Slash(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Slash CPP_Key_Slash "PMMA::Events::Key_Slash"

    cdef cppclass _CPP_Key_0(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_0 CPP_Key_0 "PMMA::Events::Key_0"

    cdef cppclass _CPP_Key_1(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_1 CPP_Key_1 "PMMA::Events::Key_1"

    cdef cppclass _CPP_Key_2(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_2 CPP_Key_2 "PMMA::Events::Key_2"

    cdef cppclass _CPP_Key_3(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_3 CPP_Key_3 "PMMA::Events::Key_3"

    cdef cppclass _CPP_Key_4(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_4 CPP_Key_4 "PMMA::Events::Key_4"

    cdef cppclass _CPP_Key_5(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_5 CPP_Key_5 "PMMA::Events::Key_5"

    cdef cppclass _CPP_Key_6(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_6 CPP_Key_6 "PMMA::Events::Key_6"

    cdef cppclass _CPP_Key_7(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_7 CPP_Key_7 "PMMA::Events::Key_7"

    cdef cppclass _CPP_Key_8(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_8 CPP_Key_8 "PMMA::Events::Key_8"

    cdef cppclass _CPP_Key_9(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_9 CPP_Key_9 "PMMA::Events::Key_9"

    cdef cppclass _CPP_Key_Semicolon(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Semicolon CPP_Key_Semicolon "PMMA::Events::Key_Semicolon"

    cdef cppclass _CPP_Key_Semicolon(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Semicolon CPP_Key_Semicolon "PMMA::Events::Key_Semicolon"

    cdef cppclass _CPP_Key_Equal(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Equal CPP_Key_Equal "PMMA::Events::Key_Equal"

    cdef cppclass _CPP_Key_A(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_A CPP_Key_A "PMMA::Events::Key_A"

    cdef cppclass _CPP_Key_B(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_B CPP_Key_B "PMMA::Events::Key_B"

    cdef cppclass _CPP_Key_C(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_C CPP_Key_C "PMMA::Events::Key_C"

    cdef cppclass _CPP_Key_D(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_D CPP_Key_D "PMMA::Events::Key_D"

    cdef cppclass _CPP_Key_E(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_E CPP_Key_E "PMMA::Events::Key_E"

    cdef cppclass _CPP_Key_F(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F CPP_Key_F "PMMA::Events::Key_F"

    cdef cppclass _CPP_Key_G(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_G CPP_Key_G "PMMA::Events::Key_G"

    cdef cppclass _CPP_Key_H(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_H CPP_Key_H "PMMA::Events::Key_H"

    cdef cppclass _CPP_Key_I(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_I CPP_Key_I "PMMA::Events::Key_I"

    cdef cppclass _CPP_Key_J(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_J CPP_Key_J "PMMA::Events::Key_J"

    cdef cppclass _CPP_Key_K(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_K CPP_Key_K "PMMA::Events::Key_K"

    cdef cppclass _CPP_Key_L(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_L CPP_Key_L "PMMA::Events::Key_L"

    cdef cppclass _CPP_Key_M(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_M CPP_Key_M "PMMA::Events::Key_M"

    cdef cppclass _CPP_Key_N(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_N CPP_Key_N "PMMA::Events::Key_N"

    cdef cppclass _CPP_Key_O(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_O CPP_Key_O "PMMA::Events::Key_O"

    cdef cppclass _CPP_Key_P(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_P CPP_Key_P "PMMA::Events::Key_P"

    cdef cppclass _CPP_Key_Q(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Q CPP_Key_Q "PMMA::Events::Key_Q"

    cdef cppclass _CPP_Key_R(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_R CPP_Key_R "PMMA::Events::Key_R"

    cdef cppclass _CPP_Key_S(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_S CPP_Key_S "PMMA::Events::Key_S"

    cdef cppclass _CPP_Key_T(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_T CPP_Key_T "PMMA::Events::Key_T"

    cdef cppclass _CPP_Key_U(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_U CPP_Key_U "PMMA::Events::Key_U"

    cdef cppclass _CPP_Key_V(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_V CPP_Key_V "PMMA::Events::Key_V"

    cdef cppclass _CPP_Key_W(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_W CPP_Key_W "PMMA::Events::Key_W"

    cdef cppclass _CPP_Key_X(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_X CPP_Key_X "PMMA::Events::Key_X"

    cdef cppclass _CPP_Key_Y(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Y CPP_Key_Y "PMMA::Events::Key_Y"

    cdef cppclass _CPP_Key_Z(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Z CPP_Key_Z "PMMA::Events::Key_Z"

    cdef cppclass _CPP_Key_Left_Bracket(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Left_Bracket CPP_Key_Left_Bracket "PMMA::Events::Key_Left_Bracket"

    cdef cppclass _CPP_Key_Backslash(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Backslash CPP_Key_Backslash "PMMA::Events::Key_Backslash"

    cdef cppclass _CPP_Key_Right_Bracket(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Right_Bracket CPP_Key_Right_Bracket "PMMA::Events::Key_Right_Bracket"

    cdef cppclass _CPP_Key_Grave_Accent(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Grave_Accent CPP_Key_Grave_Accent "PMMA::Events::Key_Grave_Accent"

    cdef cppclass _CPP_Key_World_1(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_World_1 CPP_Key_World_1 "PMMA::Events::Key_World_1"

    cdef cppclass _CPP_Key_World_2(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_World_2 CPP_Key_World_2 "PMMA::Events::Key_World_2"

    cdef cppclass _CPP_Key_Escape(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Escape CPP_Key_Escape "PMMA::Events::Key_Escape"

    cdef cppclass _CPP_Key_Enter(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Enter CPP_Key_Enter "PMMA::Events::Key_Enter"

    cdef cppclass _CPP_Key_Tab(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Tab CPP_Key_Tab "PMMA::Events::Key_Tab"

    cdef cppclass _CPP_Key_Backspace(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Backspace CPP_Key_Backspace "PMMA::Events::Key_Backspace"

    cdef cppclass _CPP_Key_Insert(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Insert CPP_Key_Insert "PMMA::Events::Key_Insert"

    cdef cppclass _CPP_Key_Delete(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Delete CPP_Key_Delete "PMMA::Events::Key_Delete"

    cdef cppclass _CPP_Key_Right(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Right CPP_Key_Right "PMMA::Events::Key_Right"

    cdef cppclass _CPP_Key_Left(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Left CPP_Key_Left "PMMA::Events::Key_Left"

    cdef cppclass _CPP_Key_Down(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Down CPP_Key_Down "PMMA::Events::Key_Down"

    cdef cppclass _CPP_Key_Up(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Up CPP_Key_Up "PMMA::Events::Key_Up"

    cdef cppclass _CPP_Key_Page_Up(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Page_Up CPP_Key_Page_Up "PMMA::Events::Key_Page_Up"

    cdef cppclass _CPP_Key_Page_Down(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Page_Down CPP_Key_Page_Down "PMMA::Events::Key_Page_Down"

    cdef cppclass _CPP_Key_Home(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Home CPP_Key_Home "PMMA::Events::Key_Home"

    cdef cppclass _CPP_Key_End(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_End CPP_Key_End "PMMA::Events::Key_End"

    cdef cppclass _CPP_Key_Caps_Lock(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Caps_Lock CPP_Key_Caps_Lock "PMMA::Events::Key_Caps_Lock"

    cdef cppclass _CPP_Key_Scroll_Lock(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Scroll_Lock CPP_Key_Scroll_Lock "PMMA::Events::Key_Scroll_Lock"

    cdef cppclass _CPP_Key_Num_Lock(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Num_Lock CPP_Key_Num_Lock "PMMA::Events::Key_Num_Lock"

    cdef cppclass _CPP_Key_Print_Screen(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Print_Screen CPP_Key_Print_Screen "PMMA::Events::Key_Print_Screen"

    cdef cppclass _CPP_Key_Pause(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Pause CPP_Key_Pause "PMMA::Events::Key_Pause"

    cdef cppclass _CPP_Key_F1(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F1 CPP_Key_F1 "PMMA::Events::Key_F1"

    cdef cppclass _CPP_Key_F2(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F2 CPP_Key_F2 "PMMA::Events::Key_F2"

    cdef cppclass _CPP_Key_F3(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F3 CPP_Key_F3 "PMMA::Events::Key_F3"

    cdef cppclass _CPP_Key_F4(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F4 CPP_Key_F4 "PMMA::Events::Key_F4"

    cdef cppclass _CPP_Key_F5(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F5 CPP_Key_F5 "PMMA::Events::Key_F5"

    cdef cppclass _CPP_Key_F6(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F6 CPP_Key_F6 "PMMA::Events::Key_F6"

    cdef cppclass _CPP_Key_F7(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F7 CPP_Key_F7 "PMMA::Events::Key_F7"

    cdef cppclass _CPP_Key_F8(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F8 CPP_Key_F8 "PMMA::Events::Key_F8"

    cdef cppclass _CPP_Key_F9(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F9 CPP_Key_F9 "PMMA::Events::Key_F9"

    cdef cppclass _CPP_Key_F10(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F10 CPP_Key_F10 "PMMA::Events::Key_F10"

    cdef cppclass _CPP_Key_F11(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F11 CPP_Key_F11 "PMMA::Events::Key_F11"

    cdef cppclass _CPP_Key_F12(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F12 CPP_Key_F12 "PMMA::Events::Key_F12"

    cdef cppclass _CPP_Key_F13(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F13 CPP_Key_F13 "PMMA::Events::Key_F13"

    cdef cppclass _CPP_Key_F14(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F14 CPP_Key_F14 "PMMA::Events::Key_F14"

    cdef cppclass _CPP_Key_F15(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F15 CPP_Key_F15 "PMMA::Events::Key_F15"

    cdef cppclass _CPP_Key_F16(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F16 CPP_Key_F16 "PMMA::Events::Key_F16"

    cdef cppclass _CPP_Key_F17(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F17 CPP_Key_F17 "PMMA::Events::Key_F17"

    cdef cppclass _CPP_Key_F18(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F18 CPP_Key_F18 "PMMA::Events::Key_F18"

    cdef cppclass _CPP_Key_F19(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F19 CPP_Key_F19 "PMMA::Events::Key_F19"

    cdef cppclass _CPP_Key_F20(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F20 CPP_Key_F20 "PMMA::Events::Key_F20"

    cdef cppclass _CPP_Key_F21(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F21 CPP_Key_F21 "PMMA::Events::Key_F21"

    cdef cppclass _CPP_Key_F22(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F22 CPP_Key_F22 "PMMA::Events::Key_F22"

    cdef cppclass _CPP_Key_F23(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F23 CPP_Key_F23 "PMMA::Events::Key_F23"

    cdef cppclass _CPP_Key_F24(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F24 CPP_Key_F24 "PMMA::Events::Key_F24"

    cdef cppclass _CPP_Key_F25(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_F25 CPP_Key_F25 "PMMA::Events::Key_F25"

    cdef cppclass _CPP_Key_Left_Shift(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Left_Shift CPP_Key_Left_Shift "PMMA::Events::Key_Left_Shift"

    cdef cppclass _CPP_Key_Left_Control(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Left_Control CPP_Key_Left_Control "PMMA::Events::Key_Left_Control"

    cdef cppclass _CPP_Key_Left_Alt(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Left_Alt CPP_Key_Left_Alt "PMMA::Events::Key_Left_Alt"

    cdef cppclass _CPP_Key_Left_Super(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Left_Super CPP_Key_Left_Super "PMMA::Events::Key_Left_Super"

    cdef cppclass _CPP_Key_Right_Shift(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Right_Shift CPP_Key_Right_Shift "PMMA::Events::Key_Right_Shift"

    cdef cppclass _CPP_Key_Right_Control(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Right_Control CPP_Key_Right_Control "PMMA::Events::Key_Right_Control"

    cdef cppclass _CPP_Key_Right_Alt(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Right_Alt CPP_Key_Right_Alt "PMMA::Events::Key_Right_Alt"

    cdef cppclass _CPP_Key_Right_Super(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Right_Super CPP_Key_Right_Super "PMMA::Events::Key_Right_Super"

    cdef cppclass _CPP_Key_Shift(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Shift CPP_Key_Shift "PMMA::Events::Key_Shift"

    cdef cppclass _CPP_Key_Control(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Control CPP_Key_Control "PMMA::Events::Key_Control"

    cdef cppclass _CPP_Key_Alt(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Alt CPP_Key_Alt "PMMA::Events::Key_Alt"

    cdef cppclass _CPP_Key_Super(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Super CPP_Key_Super "PMMA::Events::Key_Super"

    cdef cppclass _CPP_Key_Menu(CPP_ButtonPressed):
        pass

    ctypedef _CPP_Key_Menu CPP_Key_Menu "PMMA::Events::Key_Menu"

cdef class ButtonPressed:
    cdef CPP_ButtonPressed* cpp_base_class_ptr

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

cdef class Space(ButtonPressed):
    cdef CPP_Key_Space* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Space()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Apostrophe(ButtonPressed):
    cdef CPP_Key_Apostrophe* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Apostrophe()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Comma(ButtonPressed):
    cdef CPP_Key_Comma* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Comma()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Minus(ButtonPressed):
    cdef CPP_Key_Minus* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Minus()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Period(ButtonPressed):
    cdef CPP_Key_Period* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Period()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Slash(ButtonPressed):
    cdef CPP_Key_Slash* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Slash()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Zero(ButtonPressed):
    cdef CPP_Key_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_0()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class One(ButtonPressed):
    cdef CPP_Key_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Two(ButtonPressed):
    cdef CPP_Key_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Three(ButtonPressed):
    cdef CPP_Key_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Four(ButtonPressed):
    cdef CPP_Key_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Five(ButtonPressed):
    cdef CPP_Key_5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_5()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Six(ButtonPressed):
    cdef CPP_Key_6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_6()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Seven(ButtonPressed):
    cdef CPP_Key_7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_7()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Eight(ButtonPressed):
    cdef CPP_Key_8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_8()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Nine(ButtonPressed):
    cdef CPP_Key_9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_9()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Semicolon(ButtonPressed):
    cdef CPP_Key_Semicolon* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Semicolon()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Equal(ButtonPressed):
    cdef CPP_Key_Equal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Equal()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class A(ButtonPressed):
    cdef CPP_Key_A* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_A()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class B(ButtonPressed):
    cdef CPP_Key_B* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_B()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class C(ButtonPressed):
    cdef CPP_Key_C* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_C()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class D(ButtonPressed):
    cdef CPP_Key_D* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_D()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class E(ButtonPressed):
    cdef CPP_Key_E* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_E()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F(ButtonPressed):
    cdef CPP_Key_F* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class G(ButtonPressed):
    cdef CPP_Key_G* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_G()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class H(ButtonPressed):
    cdef CPP_Key_H* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_H()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class I(ButtonPressed):
    cdef CPP_Key_I* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_I()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class J(ButtonPressed):
    cdef CPP_Key_J* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_J()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class K(ButtonPressed):
    cdef CPP_Key_K* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_K()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class L(ButtonPressed):
    cdef CPP_Key_L* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_L()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class M(ButtonPressed):
    cdef CPP_Key_M* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_M()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class N(ButtonPressed):
    cdef CPP_Key_N* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_N()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class O(ButtonPressed):
    cdef CPP_Key_O* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_O()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class P(ButtonPressed):
    cdef CPP_Key_P* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_P()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Q(ButtonPressed):
    cdef CPP_Key_Q* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Q()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class R(ButtonPressed):
    cdef CPP_Key_R* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_R()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class S(ButtonPressed):
    cdef CPP_Key_S* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_S()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class T(ButtonPressed):
    cdef CPP_Key_T* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_T()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class U(ButtonPressed):
    cdef CPP_Key_U* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_U()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class V(ButtonPressed):
    cdef CPP_Key_V* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_V()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class W(ButtonPressed):
    cdef CPP_Key_W* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_W()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class X(ButtonPressed):
    cdef CPP_Key_X* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_X()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Y(ButtonPressed):
    cdef CPP_Key_Y* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Y()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Z(ButtonPressed):
    cdef CPP_Key_Z* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Z()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Left_Bracket(ButtonPressed):
    cdef CPP_Key_Left_Bracket* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Left_Bracket()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Backslash(ButtonPressed):
    cdef CPP_Key_Backslash* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Backslash()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Right_Bracket(ButtonPressed):
    cdef CPP_Key_Right_Bracket* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Right_Bracket()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Grave_Accent(ButtonPressed):
    cdef CPP_Key_Grave_Accent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Grave_Accent()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class World_1(ButtonPressed):
    cdef CPP_Key_World_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_World_1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class World_2(ButtonPressed):
    cdef CPP_Key_World_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_World_2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Escape(ButtonPressed):
    cdef CPP_Key_Escape* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Escape()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Enter(ButtonPressed):
    cdef CPP_Key_Enter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Enter()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Tab(ButtonPressed):
    cdef CPP_Key_Tab* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Tab()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Backspace(ButtonPressed):
    cdef CPP_Key_Backspace* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Backspace()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Insert(ButtonPressed):
    cdef CPP_Key_Insert* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Insert()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Delete(ButtonPressed):
    cdef CPP_Key_Delete* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Delete()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Right(ButtonPressed):
    cdef CPP_Key_Right* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Right()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Left(ButtonPressed):
    cdef CPP_Key_Left* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Left()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Down(ButtonPressed):
    cdef CPP_Key_Down* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Down()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Up(ButtonPressed):
    cdef CPP_Key_Up* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Up()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Page_Up(ButtonPressed):
    cdef CPP_Key_Page_Up* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Page_Up()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Page_Down(ButtonPressed):
    cdef CPP_Key_Page_Down* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Page_Down()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Home(ButtonPressed):
    cdef CPP_Key_Home* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Home()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class End(ButtonPressed):
    cdef CPP_Key_End* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_End()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Caps_Lock(ButtonPressed):
    cdef CPP_Key_Caps_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Caps_Lock()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Scroll_Lock(ButtonPressed):
    cdef CPP_Key_Scroll_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Scroll_Lock()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Num_Lock(ButtonPressed):
    cdef CPP_Key_Num_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Num_Lock()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Print_Screen(ButtonPressed):
    cdef CPP_Key_Print_Screen* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Print_Screen()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Pause(ButtonPressed):
    cdef CPP_Key_Pause* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Pause()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F1(ButtonPressed):
    cdef CPP_Key_F1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F1()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F2(ButtonPressed):
    cdef CPP_Key_F2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F2()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F3(ButtonPressed):
    cdef CPP_Key_F3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F3()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F4(ButtonPressed):
    cdef CPP_Key_F4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F4()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F5(ButtonPressed):
    cdef CPP_Key_F5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F5()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F6(ButtonPressed):
    cdef CPP_Key_F6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F6()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F7(ButtonPressed):
    cdef CPP_Key_F7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F7()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F8(ButtonPressed):
    cdef CPP_Key_F8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F8()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F9(ButtonPressed):
    cdef CPP_Key_F9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F9()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F10(ButtonPressed):
    cdef CPP_Key_F10* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F10()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F11(ButtonPressed):
    cdef CPP_Key_F11* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F11()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F12(ButtonPressed):
    cdef CPP_Key_F12* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F12()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F13(ButtonPressed):
    cdef CPP_Key_F13* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F13()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F14(ButtonPressed):
    cdef CPP_Key_F14* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F14()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F15(ButtonPressed):
    cdef CPP_Key_F15* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F15()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F16(ButtonPressed):
    cdef CPP_Key_F16* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F16()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F17(ButtonPressed):
    cdef CPP_Key_F17* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F17()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F18(ButtonPressed):
    cdef CPP_Key_F18* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F18()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F19(ButtonPressed):
    cdef CPP_Key_F19* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F19()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F20(ButtonPressed):
    cdef CPP_Key_F20* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F20()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F21(ButtonPressed):
    cdef CPP_Key_F21* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F21()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F22(ButtonPressed):
    cdef CPP_Key_F22* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F22()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F23(ButtonPressed):
    cdef CPP_Key_F23* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F23()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F24(ButtonPressed):
    cdef CPP_Key_F24* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F24()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class F25(ButtonPressed):
    cdef CPP_Key_F25* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_F25()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Left_Shift(ButtonPressed):
    cdef CPP_Key_Left_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Left_Shift()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Left_Control(ButtonPressed):
    cdef CPP_Key_Left_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Left_Control()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Left_Alt(ButtonPressed):
    cdef CPP_Key_Left_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Left_Alt()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Left_Super(ButtonPressed):
    cdef CPP_Key_Left_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Left_Super()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Right_Shift(ButtonPressed):
    cdef CPP_Key_Right_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Right_Shift()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Right_Control(ButtonPressed):
    cdef CPP_Key_Right_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Right_Control()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Right_Alt(ButtonPressed):
    cdef CPP_Key_Right_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Right_Alt()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Right_Super(ButtonPressed):
    cdef CPP_Key_Right_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Right_Super()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Shift(ButtonPressed):
    cdef CPP_Key_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Shift()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Control(ButtonPressed):
    cdef CPP_Key_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Control()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Alt(ButtonPressed):
    cdef CPP_Key_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Alt()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Super(ButtonPressed):
    cdef CPP_Key_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Super()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

cdef class Menu(ButtonPressed):
    cdef CPP_Key_Menu* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Key_Menu()
        self.cpp_base_class_ptr = self.cpp_class_ptr

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL