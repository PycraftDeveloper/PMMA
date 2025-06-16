# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_InternalKeyEvent:
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

    cdef cppclass CPP_InternalKeyPadEvent(CPP_InternalKeyEvent):
        pass

cdef extern from "PMMA_Core.hpp" namespace "PMMA" nogil:
    cdef CPP_InternalKeyEvent* KeyEvent_Space_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Apostrophe_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Comma_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Minus_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Period_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Slash_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_0_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_1_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_2_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_3_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_4_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_5_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_6_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_7_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_8_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_9_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Semicolon_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Equal_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_A_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_B_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_C_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_D_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_E_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_G_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_H_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_I_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_J_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_K_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_L_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_M_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_N_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_O_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_P_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Q_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_R_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_S_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_T_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_U_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_V_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_W_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_X_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Y_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Z_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Left_Bracket_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Backslash_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Right_Bracket_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Grave_Accent_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_World_1_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_World_2_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Escape_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Enter_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Tab_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Backspace_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Insert_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Delete_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Right_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Left_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Down_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Up_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Page_Up_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Page_Down_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Home_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_End_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Caps_Lock_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Scroll_Lock_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Num_Lock_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Print_Screen_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Pause_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F1_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F2_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F3_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F4_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F5_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F6_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F7_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F8_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F9_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F10_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F11_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F12_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F13_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F14_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F15_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F16_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F17_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F18_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F19_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F20_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F21_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F22_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F23_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F24_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_F25_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_0_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_1_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_2_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_3_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_4_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_5_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_6_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_7_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_8_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_9_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Decimal_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Divide_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Multiply_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Subtract_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Add_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Enter_Instance
    cdef CPP_InternalKeyPadEvent* KeyPadEvent_Equal_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Left_Shift_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Left_Control_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Left_Alt_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Left_Super_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Right_Shift_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Right_Control_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Right_Alt_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Right_Super_Instance
    cdef CPP_InternalKeyEvent* KeyEvent_Menu_Instance

cdef class _KeyEventGeneric:
    cdef:
        CPP_InternalKeyEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = NULL

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

cdef class _KeyPadEventGeneric:
    cdef:
        CPP_InternalKeyPadEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = NULL

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

cdef class KeyEvent_Space(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Space_Instance

cdef class KeyEvent_Apostrophe(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Apostrophe_Instance

cdef class KeyEvent_Comma(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Comma_Instance

cdef class KeyEvent_Minus(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Minus_Instance

cdef class KeyEvent_Period(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Period_Instance

cdef class KeyEvent_Slash(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Slash_Instance

cdef class KeyEvent_0(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_0_Instance

cdef class KeyEvent_1(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_1_Instance

cdef class KeyEvent_2(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_2_Instance

cdef class KeyEvent_3(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_3_Instance

cdef class KeyEvent_4(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_4_Instance

cdef class KeyEvent_5(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_5_Instance

cdef class KeyEvent_6(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_6_Instance

cdef class KeyEvent_7(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_7_Instance

cdef class KeyEvent_8(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_8_Instance

cdef class KeyEvent_9(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_9_Instance

cdef class KeyEvent_Semicolon(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Semicolon_Instance

cdef class KeyEvent_Equal(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Equal_Instance

cdef class KeyEvent_A(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_A_Instance

cdef class KeyEvent_B(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_B_Instance

cdef class KeyEvent_C(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_C_Instance

cdef class KeyEvent_D(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_D_Instance

cdef class KeyEvent_E(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_E_Instance

cdef class KeyEvent_F(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F_Instance

cdef class KeyEvent_G(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_G_Instance

cdef class KeyEvent_H(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_H_Instance

cdef class KeyEvent_I(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_I_Instance

cdef class KeyEvent_J(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_J_Instance

cdef class KeyEvent_K(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_K_Instance

cdef class KeyEvent_L(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_L_Instance

cdef class KeyEvent_M(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_M_Instance

cdef class KeyEvent_N(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_N_Instance

cdef class KeyEvent_O(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_O_Instance

cdef class KeyEvent_P(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_P_Instance

cdef class KeyEvent_Q(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Q_Instance

cdef class KeyEvent_R(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_R_Instance

cdef class KeyEvent_S(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_S_Instance

cdef class KeyEvent_T(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_T_Instance

cdef class KeyEvent_U(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_U_Instance

cdef class KeyEvent_V(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_V_Instance

cdef class KeyEvent_W(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_W_Instance

cdef class KeyEvent_X(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_X_Instance

cdef class KeyEvent_Y(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Y_Instance

cdef class KeyEvent_Z(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Z_Instance

cdef class KeyEvent_Left_Bracket(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Left_Bracket_Instance

cdef class KeyEvent_Backslash(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Backslash_Instance

cdef class KeyEvent_Right_Bracket(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Right_Bracket_Instance

cdef class KeyEvent_Grave_Accent(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Grave_Accent_Instance

cdef class KeyEvent_World_1(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_World_1_Instance

cdef class KeyEvent_World_2(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_World_2_Instance

cdef class KeyEvent_Escape(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Escape_Instance

cdef class KeyEvent_Enter(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Enter_Instance

cdef class KeyEvent_Tab(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Tab_Instance

cdef class KeyEvent_Backspace(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Backspace_Instance

cdef class KeyEvent_Insert(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Insert_Instance

cdef class KeyEvent_Delete(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Delete_Instance

cdef class KeyEvent_Right(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Right_Instance

cdef class KeyEvent_Left(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Left_Instance

cdef class KeyEvent_Down(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Down_Instance

cdef class KeyEvent_Up(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Up_Instance

cdef class KeyEvent_Page_Up(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Page_Up_Instance

cdef class KeyEvent_Page_Down(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Page_Down_Instance

cdef class KeyEvent_Home(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Home_Instance

cdef class KeyEvent_End(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_End_Instance

cdef class KeyEvent_Caps_Lock(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Caps_Lock_Instance

cdef class KeyEvent_Scroll_Lock(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Scroll_Lock_Instance

cdef class KeyEvent_Num_Lock(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Num_Lock_Instance

cdef class KeyEvent_Print_Screen(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Print_Screen_Instance

cdef class KeyEvent_Pause(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Pause_Instance

cdef class KeyEvent_F1(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F1_Instance

cdef class KeyEvent_F2(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F2_Instance

cdef class KeyEvent_F3(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F3_Instance

cdef class KeyEvent_F4(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F4_Instance

cdef class KeyEvent_F5(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F5_Instance

cdef class KeyEvent_F6(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F6_Instance

cdef class KeyEvent_F7(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F7_Instance

cdef class KeyEvent_F8(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F8_Instance

cdef class KeyEvent_F9(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F9_Instance

cdef class KeyEvent_F10(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F10_Instance

cdef class KeyEvent_F11(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F11_Instance

cdef class KeyEvent_F12(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F12_Instance

cdef class KeyEvent_F13(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F13_Instance

cdef class KeyEvent_F14(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F14_Instance

cdef class KeyEvent_F15(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F15_Instance

cdef class KeyEvent_F16(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F16_Instance

cdef class KeyEvent_F17(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F17_Instance

cdef class KeyEvent_F18(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F18_Instance

cdef class KeyEvent_F19(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F19_Instance

cdef class KeyEvent_F20(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F20_Instance

cdef class KeyEvent_F21(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F21_Instance

cdef class KeyEvent_F22(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F22_Instance

cdef class KeyEvent_F23(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F23_Instance

cdef class KeyEvent_F24(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F24_Instance

cdef class KeyEvent_F25(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_F25_Instance

cdef class KeyPadEvent_0(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_0_Instance

cdef class KeyPadEvent_1(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_1_Instance

cdef class KeyPadEvent_2(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_2_Instance

cdef class KeyPadEvent_3(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_3_Instance

cdef class KeyPadEvent_4(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_4_Instance

cdef class KeyPadEvent_5(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_5_Instance

cdef class KeyPadEvent_6(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_6_Instance

cdef class KeyPadEvent_7(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_7_Instance

cdef class KeyPadEvent_8(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_8_Instance

cdef class KeyPadEvent_9(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_9_Instance

cdef class KeyPadEvent_Decimal(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Decimal_Instance

cdef class KeyPadEvent_Divide(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Divide_Instance

cdef class KeyPadEvent_Multiply(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Multiply_Instance

cdef class KeyPadEvent_Subtract(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Subtract_Instance

cdef class KeyPadEvent_Add(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Add_Instance

cdef class KeyPadEvent_Enter(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Enter_Instance

cdef class KeyPadEvent_Equal(_KeyPadEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyPadEvent_Equal_Instance

cdef class KeyEvent_Left_Shift(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Left_Shift_Instance

cdef class KeyEvent_Left_Control(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Left_Control_Instance

cdef class KeyEvent_Left_Alt(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Left_Alt_Instance

cdef class KeyEvent_Left_Super(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Left_Super_Instance

cdef class KeyEvent_Right_Shift(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Right_Shift_Instance

cdef class KeyEvent_Right_Control(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Right_Control_Instance

cdef class KeyEvent_Right_Alt(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Right_Alt_Instance

cdef class KeyEvent_Right_Super(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Right_Super_Instance

cdef class KeyEvent_Menu(_KeyEventGeneric):
    def __cinit__(self):
        self.cpp_class_ptr = KeyEvent_Menu_Instance