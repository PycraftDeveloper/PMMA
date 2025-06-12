# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_Space_KeyEvent:
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

    cdef cppclass CPP_Apostrophe_KeyEvent:
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

    cdef cppclass CPP_Comma_KeyEvent:
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

    cdef cppclass CPP_Minus_KeyEvent:
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

    cdef cppclass CPP_Period_KeyEvent:
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

    cdef cppclass CPP_Slash_KeyEvent:
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

    cdef cppclass CPP_0_KeyEvent:
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

    cdef cppclass CPP_1_KeyEvent:
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

    cdef cppclass CPP_2_KeyEvent:
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

    cdef cppclass CPP_3_KeyEvent:
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

    cdef cppclass CPP_4_KeyEvent:
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

    cdef cppclass CPP_5_KeyEvent:
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

    cdef cppclass CPP_6_KeyEvent:
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

    cdef cppclass CPP_7_KeyEvent:
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

    cdef cppclass CPP_8_KeyEvent:
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

    cdef cppclass CPP_9_KeyEvent:
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

    cdef cppclass CPP_Semicolon_KeyEvent:
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

    cdef cppclass CPP_Equal_KeyEvent:
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

    cdef cppclass CPP_A_KeyEvent:
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

    cdef cppclass CPP_B_KeyEvent:
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

    cdef cppclass CPP_C_KeyEvent:
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

    cdef cppclass CPP_D_KeyEvent:
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

    cdef cppclass CPP_E_KeyEvent:
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

    cdef cppclass CPP_F_KeyEvent:
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

    cdef cppclass CPP_G_KeyEvent:
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

    cdef cppclass CPP_H_KeyEvent:
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

    cdef cppclass CPP_I_KeyEvent:
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

    cdef cppclass CPP_J_KeyEvent:
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

    cdef cppclass CPP_K_KeyEvent:
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

    cdef cppclass CPP_L_KeyEvent:
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

    cdef cppclass CPP_M_KeyEvent:
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

    cdef cppclass CPP_N_KeyEvent:
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

    cdef cppclass CPP_O_KeyEvent:
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

    cdef cppclass CPP_P_KeyEvent:
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

    cdef cppclass CPP_Q_KeyEvent:
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

    cdef cppclass CPP_R_KeyEvent:
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

    cdef cppclass CPP_S_KeyEvent:
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

    cdef cppclass CPP_T_KeyEvent:
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

    cdef cppclass CPP_U_KeyEvent:
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

    cdef cppclass CPP_V_KeyEvent:
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

    cdef cppclass CPP_W_KeyEvent:
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

    cdef cppclass CPP_X_KeyEvent:
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

    cdef cppclass CPP_Y_KeyEvent:
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

    cdef cppclass CPP_Z_KeyEvent:
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

    cdef cppclass CPP_Left_Bracket_KeyEvent:
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

    cdef cppclass CPP_Backslash_KeyEvent:
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

    cdef cppclass CPP_Right_Bracket_KeyEvent:
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

    cdef cppclass CPP_Grave_Accent_KeyEvent:
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

    cdef cppclass CPP_World_1_KeyEvent:
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

    cdef cppclass CPP_World_2_KeyEvent:
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

    cdef cppclass CPP_Escape_KeyEvent:
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

    cdef cppclass CPP_Enter_KeyEvent:
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

    cdef cppclass CPP_Tab_KeyEvent:
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

    cdef cppclass CPP_Backspace_KeyEvent:
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

    cdef cppclass CPP_Insert_KeyEvent:
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

    cdef cppclass CPP_Delete_KeyEvent:
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

    cdef cppclass CPP_Right_KeyEvent:
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

    cdef cppclass CPP_Left_KeyEvent:
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

    cdef cppclass CPP_Down_KeyEvent:
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

    cdef cppclass CPP_Up_KeyEvent:
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

    cdef cppclass CPP_Page_Up_KeyEvent:
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

    cdef cppclass CPP_Page_Down_KeyEvent:
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

    cdef cppclass CPP_Home_KeyEvent:
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

    cdef cppclass CPP_End_KeyEvent:
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

    cdef cppclass CPP_Caps_Lock_KeyEvent:
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

    cdef cppclass CPP_Scroll_Lock_KeyEvent:
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

    cdef cppclass CPP_Num_Lock_KeyEvent:
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

    cdef cppclass CPP_Print_Screen_KeyEvent:
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

    cdef cppclass CPP_Pause_KeyEvent:
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

    cdef cppclass CPP_F1_KeyEvent:
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

    cdef cppclass CPP_F2_KeyEvent:
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

    cdef cppclass CPP_F3_KeyEvent:
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

    cdef cppclass CPP_F4_KeyEvent:
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

    cdef cppclass CPP_F5_KeyEvent:
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

    cdef cppclass CPP_F6_KeyEvent:
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

    cdef cppclass CPP_F7_KeyEvent:
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

    cdef cppclass CPP_F8_KeyEvent:
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

    cdef cppclass CPP_F9_KeyEvent:
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

    cdef cppclass CPP_F10_KeyEvent:
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

    cdef cppclass CPP_F11_KeyEvent:
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

    cdef cppclass CPP_F12_KeyEvent:
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

    cdef cppclass CPP_F13_KeyEvent:
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

    cdef cppclass CPP_F14_KeyEvent:
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

    cdef cppclass CPP_F15_KeyEvent:
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

    cdef cppclass CPP_F16_KeyEvent:
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

    cdef cppclass CPP_F17_KeyEvent:
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

    cdef cppclass CPP_F18_KeyEvent:
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

    cdef cppclass CPP_F19_KeyEvent:
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

    cdef cppclass CPP_F20_KeyEvent:
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

    cdef cppclass CPP_F21_KeyEvent:
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

    cdef cppclass CPP_F22_KeyEvent:
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

    cdef cppclass CPP_F23_KeyEvent:
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

    cdef cppclass CPP_F24_KeyEvent:
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

    cdef cppclass CPP_F25_KeyEvent:
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

    cdef cppclass CPP_0_KeyPadEvent:
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

    cdef cppclass CPP_1_KeyPadEvent:
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

    cdef cppclass CPP_2_KeyPadEvent:
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

    cdef cppclass CPP_3_KeyPadEvent:
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

    cdef cppclass CPP_4_KeyPadEvent:
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

    cdef cppclass CPP_5_KeyPadEvent:
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

    cdef cppclass CPP_6_KeyPadEvent:
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

    cdef cppclass CPP_7_KeyPadEvent:
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

    cdef cppclass CPP_8_KeyPadEvent:
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

    cdef cppclass CPP_9_KeyPadEvent:
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

    cdef cppclass CPP_Decimal_KeyPadEvent:
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

    cdef cppclass CPP_Divide_KeyPadEvent:
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

    cdef cppclass CPP_Multiply_KeyPadEvent:
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

    cdef cppclass CPP_Subtract_KeyPadEvent:
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

    cdef cppclass CPP_Add_KeyPadEvent:
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

    cdef cppclass CPP_Enter_KeyPadEvent:
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

    cdef cppclass CPP_Equal_KeyPadEvent:
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

    cdef cppclass CPP_Left_Shift_KeyEvent:
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

    cdef cppclass CPP_Left_Control_KeyEvent:
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

    cdef cppclass CPP_Left_Alt_KeyEvent:
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

    cdef cppclass CPP_Left_Super_KeyEvent:
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

    cdef cppclass CPP_Right_Shift_KeyEvent:
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

    cdef cppclass CPP_Right_Control_KeyEvent:
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

    cdef cppclass CPP_Right_Alt_KeyEvent:
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

    cdef cppclass CPP_Right_Super_KeyEvent:
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

    cdef cppclass CPP_Menu_KeyEvent:
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

cdef class KeyEvent_Space:
    cdef:
        CPP_Space_KeyEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Space_KeyEvent()

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

cdef class KeyEvent_Apostrophe:
    cdef:
        CPP_Apostrophe_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Apostrophe_KeyEvent()

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

cdef class KeyEvent_Comma:
    cdef:
        CPP_Comma_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Comma_KeyEvent()

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

cdef class KeyEvent_Minus:
    cdef:
        CPP_Minus_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Minus_KeyEvent()

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

cdef class KeyEvent_Period:
    cdef:
        CPP_Period_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Period_KeyEvent()

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

cdef class KeyEvent_Slash:
    cdef:
        CPP_Slash_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Slash_KeyEvent()

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

cdef class KeyEvent_0:
    cdef:
        CPP_0_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_0_KeyEvent()

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

cdef class KeyEvent_1:
    cdef:
        CPP_1_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_1_KeyEvent()

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

cdef class KeyEvent_2:
    cdef:
        CPP_2_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_2_KeyEvent()

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

cdef class KeyEvent_3:
    cdef:
        CPP_3_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_3_KeyEvent()

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

cdef class KeyEvent_4:
    cdef:
        CPP_4_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_4_KeyEvent()

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

cdef class KeyEvent_5:
    cdef:
        CPP_5_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_5_KeyEvent()

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

cdef class KeyEvent_6:
    cdef:
        CPP_6_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_6_KeyEvent()

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

cdef class KeyEvent_7:
    cdef:
        CPP_7_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_7_KeyEvent()

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

cdef class KeyEvent_8:
    cdef:
        CPP_8_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_8_KeyEvent()

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

cdef class KeyEvent_9:
    cdef:
        CPP_9_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_9_KeyEvent()

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

cdef class KeyEvent_Semicolon:
    cdef:
        CPP_Semicolon_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Semicolon_KeyEvent()

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

cdef class KeyEvent_Equal:
    cdef:
        CPP_Equal_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Equal_KeyEvent()

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

cdef class KeyEvent_A:
    cdef:
        CPP_A_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_A_KeyEvent()

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

cdef class KeyEvent_B:
    cdef:
        CPP_B_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_B_KeyEvent()

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

cdef class KeyEvent_C:
    cdef:
        CPP_C_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_C_KeyEvent()

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

cdef class KeyEvent_D:
    cdef:
        CPP_D_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_D_KeyEvent()

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

cdef class KeyEvent_E:
    cdef:
        CPP_E_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_E_KeyEvent()

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

cdef class KeyEvent_F:
    cdef:
        CPP_F_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F_KeyEvent()

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

cdef class KeyEvent_G:
    cdef:
        CPP_G_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_G_KeyEvent()

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

cdef class KeyEvent_H:
    cdef:
        CPP_H_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_H_KeyEvent()

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

cdef class KeyEvent_I:
    cdef:
        CPP_I_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_I_KeyEvent()

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

cdef class KeyEvent_J:
    cdef:
        CPP_J_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_J_KeyEvent()

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

cdef class KeyEvent_K:
    cdef:
        CPP_K_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_K_KeyEvent()

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

cdef class KeyEvent_L:
    cdef:
        CPP_L_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_L_KeyEvent()

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

cdef class KeyEvent_M:
    cdef:
        CPP_M_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_M_KeyEvent()

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

cdef class KeyEvent_N:
    cdef:
        CPP_N_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_N_KeyEvent()

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

cdef class KeyEvent_O:
    cdef:
        CPP_O_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_O_KeyEvent()

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

cdef class KeyEvent_P:
    cdef:
        CPP_P_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_P_KeyEvent()

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

cdef class KeyEvent_Q:
    cdef:
        CPP_Q_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Q_KeyEvent()

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

cdef class KeyEvent_R:
    cdef:
        CPP_R_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_R_KeyEvent()

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

cdef class KeyEvent_S:
    cdef:
        CPP_S_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_S_KeyEvent()

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

cdef class KeyEvent_T:
    cdef:
        CPP_T_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_T_KeyEvent()

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

cdef class KeyEvent_U:
    cdef:
        CPP_U_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_U_KeyEvent()

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

cdef class KeyEvent_V:
    cdef:
        CPP_V_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_V_KeyEvent()

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

cdef class KeyEvent_W:
    cdef:
        CPP_W_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_W_KeyEvent()

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

cdef class KeyEvent_X:
    cdef:
        CPP_X_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_X_KeyEvent()

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

cdef class KeyEvent_Y:
    cdef:
        CPP_Y_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Y_KeyEvent()

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

cdef class KeyEvent_Z:
    cdef:
        CPP_Z_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Z_KeyEvent()

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

cdef class KeyEvent_Left_Bracket:
    cdef:
        CPP_Left_Bracket_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Left_Bracket_KeyEvent()

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

cdef class KeyEvent_Backslash:
    cdef:
        CPP_Backslash_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Backslash_KeyEvent()

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

cdef class KeyEvent_Right_Bracket:
    cdef:
        CPP_Right_Bracket_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Right_Bracket_KeyEvent()

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

cdef class KeyEvent_Grave_Accent:
    cdef:
        CPP_Grave_Accent_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Grave_Accent_KeyEvent()

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

cdef class KeyEvent_World_1:
    cdef:
        CPP_World_1_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_World_1_KeyEvent()

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

cdef class KeyEvent_World_2:
    cdef:
        CPP_World_2_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_World_2_KeyEvent()

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

cdef class KeyEvent_Escape:
    cdef:
        CPP_Escape_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Escape_KeyEvent()

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

cdef class KeyEvent_Enter:
    cdef:
        CPP_Enter_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Enter_KeyEvent()

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

cdef class KeyEvent_Tab:
    cdef:
        CPP_Tab_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Tab_KeyEvent()

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

cdef class KeyEvent_Backspace:
    cdef:
        CPP_Backspace_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Backspace_KeyEvent()

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

cdef class KeyEvent_Insert:
    cdef:
        CPP_Insert_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Insert_KeyEvent()

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

cdef class KeyEvent_Delete:
    cdef:
        CPP_Delete_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Delete_KeyEvent()

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

cdef class KeyEvent_Right:
    cdef:
        CPP_Right_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Right_KeyEvent()

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

cdef class KeyEvent_Left:
    cdef:
        CPP_Left_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Left_KeyEvent()

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

cdef class KeyEvent_Down:
    cdef:
        CPP_Down_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Down_KeyEvent()

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

cdef class KeyEvent_Up:
    cdef:
        CPP_Up_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Up_KeyEvent()

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

cdef class KeyEvent_Page_Up:
    cdef:
        CPP_Page_Up_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Page_Up_KeyEvent()

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

cdef class KeyEvent_Page_Down:
    cdef:
        CPP_Page_Down_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Page_Down_KeyEvent()

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

cdef class KeyEvent_Home:
    cdef:
        CPP_Home_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Home_KeyEvent()

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

cdef class KeyEvent_End:
    cdef:
        CPP_End_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_End_KeyEvent()

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

cdef class KeyEvent_Caps_Lock:
    cdef:
        CPP_Caps_Lock_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Caps_Lock_KeyEvent()

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

cdef class KeyEvent_Scroll_Lock:
    cdef:
        CPP_Scroll_Lock_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Scroll_Lock_KeyEvent()

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

cdef class KeyEvent_Num_Lock:
    cdef:
        CPP_Num_Lock_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Num_Lock_KeyEvent()

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

cdef class KeyEvent_Print_Screen:
    cdef:
        CPP_Print_Screen_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Print_Screen_KeyEvent()

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

cdef class KeyEvent_Pause:
    cdef:
        CPP_Pause_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Pause_KeyEvent()

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

cdef class KeyEvent_F1:
    cdef:
        CPP_F1_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F1_KeyEvent()

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

cdef class KeyEvent_F2:
    cdef:
        CPP_F2_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F2_KeyEvent()

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

cdef class KeyEvent_F3:
    cdef:
        CPP_F3_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F3_KeyEvent()

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

cdef class KeyEvent_F4:
    cdef:
        CPP_F4_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F4_KeyEvent()

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

cdef class KeyEvent_F5:
    cdef:
        CPP_F5_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F5_KeyEvent()

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

cdef class KeyEvent_F6:
    cdef:
        CPP_F6_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F6_KeyEvent()

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

cdef class KeyEvent_F7:
    cdef:
        CPP_F7_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F7_KeyEvent()

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

cdef class KeyEvent_F8:
    cdef:
        CPP_F8_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F8_KeyEvent()

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

cdef class KeyEvent_F9:
    cdef:
        CPP_F9_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F9_KeyEvent()

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

cdef class KeyEvent_F10:
    cdef:
        CPP_F10_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F10_KeyEvent()

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

cdef class KeyEvent_F11:
    cdef:
        CPP_F11_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F11_KeyEvent()

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

cdef class KeyEvent_F12:
    cdef:
        CPP_F12_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F12_KeyEvent()

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

cdef class KeyEvent_F13:
    cdef:
        CPP_F13_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F13_KeyEvent()

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

cdef class KeyEvent_F14:
    cdef:
        CPP_F14_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F14_KeyEvent()

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

cdef class KeyEvent_F15:
    cdef:
        CPP_F15_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F15_KeyEvent()

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

cdef class KeyEvent_F16:
    cdef:
        CPP_F16_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F16_KeyEvent()

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

cdef class KeyEvent_F17:
    cdef:
        CPP_F17_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F17_KeyEvent()

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

cdef class KeyEvent_F18:
    cdef:
        CPP_F18_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F18_KeyEvent()

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

cdef class KeyEvent_F19:
    cdef:
        CPP_F19_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F19_KeyEvent()

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

cdef class KeyEvent_F20:
    cdef:
        CPP_F20_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F20_KeyEvent()

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

cdef class KeyEvent_F21:
    cdef:
        CPP_F21_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F21_KeyEvent()

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

cdef class KeyEvent_F22:
    cdef:
        CPP_F22_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F22_KeyEvent()

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

cdef class KeyEvent_F23:
    cdef:
        CPP_F23_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F23_KeyEvent()

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

cdef class KeyEvent_F24:
    cdef:
        CPP_F24_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F24_KeyEvent()

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

cdef class KeyEvent_F25:
    cdef:
        CPP_F25_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_F25_KeyEvent()

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

cdef class KeyPadEvent_0:
    cdef:
        CPP_0_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_0_KeyPadEvent()

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

cdef class KeyPadEvent_1:
    cdef:
        CPP_1_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_1_KeyPadEvent()

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

cdef class KeyPadEvent_2:
    cdef:
        CPP_2_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_2_KeyPadEvent()

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

cdef class KeyPadEvent_3:
    cdef:
        CPP_3_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_3_KeyPadEvent()

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

cdef class KeyPadEvent_4:
    cdef:
        CPP_4_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_4_KeyPadEvent()

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

cdef class KeyPadEvent_5:
    cdef:
        CPP_5_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_5_KeyPadEvent()

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

cdef class KeyPadEvent_6:
    cdef:
        CPP_6_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_6_KeyPadEvent()

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

cdef class KeyPadEvent_7:
    cdef:
        CPP_7_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_7_KeyPadEvent()

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

cdef class KeyPadEvent_8:
    cdef:
        CPP_8_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_8_KeyPadEvent()

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

cdef class KeyPadEvent_9:
    cdef:
        CPP_9_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_9_KeyPadEvent()

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

cdef class KeyPadEvent_Decimal:
    cdef:
        CPP_Decimal_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Decimal_KeyPadEvent()

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

cdef class KeyPadEvent_Divide:
    cdef:
        CPP_Divide_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Divide_KeyPadEvent()

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

cdef class KeyPadEvent_Multiply:
    cdef:
        CPP_Multiply_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Multiply_KeyPadEvent()

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

cdef class KeyPadEvent_Subtract:
    cdef:
        CPP_Subtract_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Subtract_KeyPadEvent()

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

cdef class KeyPadEvent_Add:
    cdef:
        CPP_Add_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Add_KeyPadEvent()

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

cdef class KeyPadEvent_Enter:
    cdef:
        CPP_Enter_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Enter_KeyPadEvent()

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

cdef class KeyPadEvent_Equal:
    cdef:
        CPP_Equal_KeyPadEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Equal_KeyPadEvent()

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

cdef class KeyEvent_Left_Shift:
    cdef:
        CPP_Left_Shift_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Left_Shift_KeyEvent()

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

cdef class KeyEvent_Left_Control:
    cdef:
        CPP_Left_Control_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Left_Control_KeyEvent()

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

cdef class KeyEvent_Left_Alt:
    cdef:
        CPP_Left_Alt_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Left_Alt_KeyEvent()

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

cdef class KeyEvent_Left_Super:
    cdef:
        CPP_Left_Super_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Left_Super_KeyEvent()

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

cdef class KeyEvent_Right_Shift:
    cdef:
        CPP_Right_Shift_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Right_Shift_KeyEvent()

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

cdef class KeyEvent_Right_Control:
    cdef:
        CPP_Right_Control_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Right_Control_KeyEvent()

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

cdef class KeyEvent_Right_Alt:
    cdef:
        CPP_Right_Alt_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Right_Alt_KeyEvent()

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

cdef class KeyEvent_Right_Super:
    cdef:
        CPP_Right_Super_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Right_Super_KeyEvent()

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

cdef class KeyEvent_Menu:
    cdef:
        CPP_Menu_KeyEvent* cpp_class_ptr

    def __cinit__(self):
            self.cpp_class_ptr = new CPP_Menu_KeyEvent()

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