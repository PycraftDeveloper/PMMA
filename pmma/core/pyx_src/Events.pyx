# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string
from libcpp.vector cimport vector

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_TextEvent:
        string GetText() except + nogil

        void SetEnabled(bool NewIsEnabled) except + nogil
        bool GetEnabled() except + nogil

        void ClearText() except + nogil

        void Set_ControlKey_DoublePressDuration(float NewDuration) except + nogil
        void Set_ControlKey_LongPressDuration(float NewDuration) except + nogil
        void Set_ControlKey_RepeatPressDuration(float NewDuration) except + nogil

        void Set_ShiftKey_DoublePressDuration(float NewDuration) except + nogil
        void Set_ShiftKey_LongPressDuration(float NewDuration) except + nogil
        void Set_ShiftKey_RepeatPressDuration(float NewDuration) except + nogil

        void Set_VKey_DoublePressDuration(float NewDuration) except + nogil
        void Set_VKey_LongPressDuration(float NewDuration) except + nogil
        void Set_VKey_RepeatPressDuration(float NewDuration) except + nogil

        void Set_InsertKey_DoublePressDuration(float NewDuration) except + nogil
        void Set_InsertKey_LongPressDuration(float NewDuration) except + nogil
        void Set_InsertKey_RepeatPressDuration(float NewDuration) except + nogil

        void Set_DeleteKey_DoublePressDuration(float NewDuration) except + nogil
        void Set_DeleteKey_LongPressDuration(float NewDuration) except + nogil
        void Set_DeleteKey_RepeatPressDuration(float NewDuration) except + nogil

        void Set_BackspaceKey_DoublePressDuration(float NewDuration) except + nogil
        void Set_BackspaceKey_LongPressDuration(float NewDuration) except + nogil
        void Set_BackspaceKey_RepeatPressDuration(float NewDuration) except + nogil

    cdef cppclass CPP_MousePositionEvent:
        void GetPosition(float* out) except + nogil

        void GetDelta(float* out) except + nogil
        void GetDeltaToggle(float* out) except + nogil

    cdef cppclass CPP_MouseEnterWindowEvent:
        bool GetEntered() except + nogil
        bool GetEnteredToggle() except + nogil

    cdef cppclass CPP_MouseButtonEvent_Left:
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

    cdef cppclass CPP_MouseButtonEvent_Right:
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

    cdef cppclass CPP_MouseButtonEvent_Middle:
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

    cdef cppclass CPP_MouseButtonEvent_0:
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

    cdef cppclass CPP_MouseButtonEvent_1:
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

    cdef cppclass CPP_MouseButtonEvent_2:
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

    cdef cppclass CPP_MouseButtonEvent_3:
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

    cdef cppclass CPP_MouseButtonEvent_4:
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

    cdef cppclass CPP_MouseScrollEvent:
        void GetPosition(float* out) except + nogil
        void ClearPosition() except + nogil
        float GetHorizontalPosition() except + nogil
        float GetVerticalPosition() except + nogil

        void GetDelta(float* out) except + nogil
        float GetHorizontalDelta() except + nogil
        float GetVerticalDelta() except + nogil

        void GetDeltaToggle(float* out) except + nogil
        float GetHorizontalDeltaToggle() except + nogil
        float GetVerticalDeltaToggle() except + nogil

        bool GetEnabled() except + nogil
        void SetEnabled(bool NewIsEnabled) except + nogil

    cdef cppclass CPP_ControllerEvent:
        bool GetConnected() except + nogil

        float GetAxis_Decimal(int AxisID) except + nogil
        float GetAxis_Percentage(int AxisID) except + nogil

    cdef cppclass CPP_KeyEvent_Space:
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

    cdef cppclass CPP_KeyEvent_Apostrophe:
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

    cdef cppclass CPP_KeyEvent_Comma:
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

    cdef cppclass CPP_KeyEvent_Minus:
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

    cdef cppclass CPP_KeyEvent_Period:
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

    cdef cppclass CPP_KeyEvent_Slash:
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

    cdef cppclass CPP_KeyEvent_0:
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

    cdef cppclass CPP_KeyEvent_1:
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

    cdef cppclass CPP_KeyEvent_2:
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

    cdef cppclass CPP_KeyEvent_3:
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

    cdef cppclass CPP_KeyEvent_4:
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

    cdef cppclass CPP_KeyEvent_5:
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

    cdef cppclass CPP_KeyEvent_6:
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

    cdef cppclass CPP_KeyEvent_7:
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

    cdef cppclass CPP_KeyEvent_8:
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

    cdef cppclass CPP_KeyEvent_9:
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

    cdef cppclass CPP_KeyEvent_Semicolon:
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

    cdef cppclass CPP_KeyEvent_Equal:
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

    cdef cppclass CPP_KeyEvent_A:
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

    cdef cppclass CPP_KeyEvent_B:
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

    cdef cppclass CPP_KeyEvent_C:
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

    cdef cppclass CPP_KeyEvent_D:
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

    cdef cppclass CPP_KeyEvent_E:
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

    cdef cppclass CPP_KeyEvent_F:
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

    cdef cppclass CPP_KeyEvent_G:
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

    cdef cppclass CPP_KeyEvent_H:
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

    cdef cppclass CPP_KeyEvent_I:
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

    cdef cppclass CPP_KeyEvent_J:
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

    cdef cppclass CPP_KeyEvent_K:
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

    cdef cppclass CPP_KeyEvent_L:
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

    cdef cppclass CPP_KeyEvent_M:
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

    cdef cppclass CPP_KeyEvent_N:
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

    cdef cppclass CPP_KeyEvent_O:
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

    cdef cppclass CPP_KeyEvent_P:
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

    cdef cppclass CPP_KeyEvent_Q:
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

    cdef cppclass CPP_KeyEvent_R:
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

    cdef cppclass CPP_KeyEvent_S:
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

    cdef cppclass CPP_KeyEvent_T:
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

    cdef cppclass CPP_KeyEvent_U:
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

    cdef cppclass CPP_KeyEvent_V:
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

    cdef cppclass CPP_KeyEvent_W:
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

    cdef cppclass CPP_KeyEvent_X:
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

    cdef cppclass CPP_KeyEvent_Y:
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

    cdef cppclass CPP_KeyEvent_Z:
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

    cdef cppclass CPP_KeyEvent_Left_Bracket:
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

    cdef cppclass CPP_KeyEvent_Backslash:
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

    cdef cppclass CPP_KeyEvent_Right_Bracket:
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

    cdef cppclass CPP_KeyEvent_Grave_Accent:
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

    cdef cppclass CPP_KeyEvent_World_1:
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

    cdef cppclass CPP_KeyEvent_World_2:
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

    cdef cppclass CPP_KeyEvent_Escape:
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

    cdef cppclass CPP_KeyEvent_Enter:
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

    cdef cppclass CPP_KeyEvent_Tab:
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

    cdef cppclass CPP_KeyEvent_Backspace:
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

    cdef cppclass CPP_KeyEvent_Insert:
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

    cdef cppclass CPP_KeyEvent_Delete:
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

    cdef cppclass CPP_KeyEvent_Right:
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

    cdef cppclass CPP_KeyEvent_Left:
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

    cdef cppclass CPP_KeyEvent_Down:
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

    cdef cppclass CPP_KeyEvent_Up:
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

    cdef cppclass CPP_KeyEvent_Page_Up:
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

    cdef cppclass CPP_KeyEvent_Page_Down:
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

    cdef cppclass CPP_KeyEvent_Home:
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

    cdef cppclass CPP_KeyEvent_End:
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

    cdef cppclass CPP_KeyEvent_Caps_Lock:
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

    cdef cppclass CPP_KeyEvent_Scroll_Lock:
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

    cdef cppclass CPP_KeyEvent_Num_Lock:
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

    cdef cppclass CPP_KeyEvent_Print_Screen:
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

    cdef cppclass CPP_KeyEvent_Pause:
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

    cdef cppclass CPP_KeyEvent_F1:
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

    cdef cppclass CPP_KeyEvent_F2:
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

    cdef cppclass CPP_KeyEvent_F3:
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

    cdef cppclass CPP_KeyEvent_F4:
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

    cdef cppclass CPP_KeyEvent_F5:
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

    cdef cppclass CPP_KeyEvent_F6:
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

    cdef cppclass CPP_KeyEvent_F7:
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

    cdef cppclass CPP_KeyEvent_F8:
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

    cdef cppclass CPP_KeyEvent_F9:
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

    cdef cppclass CPP_KeyEvent_F10:
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

    cdef cppclass CPP_KeyEvent_F11:
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

    cdef cppclass CPP_KeyEvent_F12:
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

    cdef cppclass CPP_KeyEvent_F13:
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

    cdef cppclass CPP_KeyEvent_F14:
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

    cdef cppclass CPP_KeyEvent_F15:
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

    cdef cppclass CPP_KeyEvent_F16:
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

    cdef cppclass CPP_KeyEvent_F17:
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

    cdef cppclass CPP_KeyEvent_F18:
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

    cdef cppclass CPP_KeyEvent_F19:
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

    cdef cppclass CPP_KeyEvent_F20:
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

    cdef cppclass CPP_KeyEvent_F21:
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

    cdef cppclass CPP_KeyEvent_F22:
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

    cdef cppclass CPP_KeyEvent_F23:
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

    cdef cppclass CPP_KeyEvent_F24:
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

    cdef cppclass CPP_KeyEvent_F25:
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

    cdef cppclass CPP_KeyEvent_Left_Shift:
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

    cdef cppclass CPP_KeyEvent_Left_Control:
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

    cdef cppclass CPP_KeyEvent_Left_Alt:
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

    cdef cppclass CPP_KeyEvent_Left_Super:
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

    cdef cppclass CPP_KeyEvent_Right_Shift:
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

    cdef cppclass CPP_KeyEvent_Right_Control:
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

    cdef cppclass CPP_KeyEvent_Right_Alt:
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

    cdef cppclass CPP_KeyEvent_Right_Super:
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

    cdef cppclass CPP_KeyEvent_Shift:
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

    cdef cppclass CPP_KeyEvent_Control:
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

    cdef cppclass CPP_KeyEvent_Alt:
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

    cdef cppclass CPP_KeyEvent_Super:
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

    cdef cppclass CPP_KeyEvent_Menu:
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

    cdef cppclass CPP_KeyPadEvent_0:
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

    cdef cppclass CPP_KeyPadEvent_1:
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

    cdef cppclass CPP_KeyPadEvent_2:
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

    cdef cppclass CPP_KeyPadEvent_3:
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

    cdef cppclass CPP_KeyPadEvent_4:
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

    cdef cppclass CPP_KeyPadEvent_5:
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

    cdef cppclass CPP_KeyPadEvent_6:
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

    cdef cppclass CPP_KeyPadEvent_7:
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

    cdef cppclass CPP_KeyPadEvent_8:
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

    cdef cppclass CPP_KeyPadEvent_9:
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

    cdef cppclass CPP_KeyPadEvent_Decimal:
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

    cdef cppclass CPP_KeyPadEvent_Divide:
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

    cdef cppclass CPP_KeyPadEvent_Multiply:
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

    cdef cppclass CPP_KeyPadEvent_Subtract:
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

    cdef cppclass CPP_KeyPadEvent_Add:
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

    cdef cppclass CPP_KeyPadEvent_Enter:
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

    cdef cppclass CPP_KeyPadEvent_Equal:
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

cdef extern from "PMMA_Core.hpp" namespace "PMMA" nogil:
    cdef vector[CPP_ControllerEvent*] ControllerEventInstances

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
        CPP_MouseButtonEvent_Left* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_Left()

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
        CPP_MouseButtonEvent_Right* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_Right()

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
        CPP_MouseButtonEvent_Middle* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_Middle()

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
        CPP_MouseButtonEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_0()

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
        CPP_MouseButtonEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_1()

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
        CPP_MouseButtonEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_2()

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
        CPP_MouseButtonEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_3()

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
        CPP_MouseButtonEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseButtonEvent_4()

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

cdef class MouseScrollEvent:
    cdef:
        CPP_MouseScrollEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_MouseScrollEvent()

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

cdef class ControllerEvent:
    cdef:
        CPP_ControllerEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = NULL

    def __dealloc__(self):
        self.cpp_class_ptr = NULL

    def __init__(self, controller_id):
        cdef CPP_ControllerEvent* ptr
        ptr = ControllerEventInstances[controller_id]
        self.cpp_class_ptr = ptr

    def get_axis_decimal(self, axis_id):
        return self.cpp_class_ptr.GetAxis_Decimal(axis_id)

    def get_axis_percentage(self, axis_id):
        return self.cpp_class_ptr.GetAxis_Percentage(axis_id)

cdef class KeyEvent_Space:
    cdef:
        CPP_KeyEvent_Space* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Space()

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
        CPP_KeyEvent_Apostrophe* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Apostrophe()

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
        CPP_KeyEvent_Comma* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Comma()

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
        CPP_KeyEvent_Minus* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Minus()

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
        CPP_KeyEvent_Period* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Period()

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
        CPP_KeyEvent_Slash* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Slash()

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
        CPP_KeyEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_0()

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
        CPP_KeyEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_1()

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
        CPP_KeyEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_2()

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
        CPP_KeyEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_3()

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
        CPP_KeyEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_4()

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
        CPP_KeyEvent_5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_5()

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
        CPP_KeyEvent_6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_6()

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
        CPP_KeyEvent_7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_7()

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
        CPP_KeyEvent_8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_8()

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
        CPP_KeyEvent_9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_9()

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
        CPP_KeyEvent_Semicolon* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Semicolon()

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
        CPP_KeyEvent_Equal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Equal()

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
        CPP_KeyEvent_A* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_A()

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
        CPP_KeyEvent_B* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_B()

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
        CPP_KeyEvent_C* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_C()

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
        CPP_KeyEvent_D* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_D()

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
        CPP_KeyEvent_E* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_E()

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
        CPP_KeyEvent_F* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F()

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
        CPP_KeyEvent_G* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_G()

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
        CPP_KeyEvent_H* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_H()

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
        CPP_KeyEvent_I* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_I()

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
        CPP_KeyEvent_J* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_J()

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
        CPP_KeyEvent_K* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_K()

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
        CPP_KeyEvent_L* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_L()

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
        CPP_KeyEvent_M* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_M()

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
        CPP_KeyEvent_N* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_N()

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
        CPP_KeyEvent_O* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_O()

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
        CPP_KeyEvent_P* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_P()

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
        CPP_KeyEvent_Q* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Q()

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
        CPP_KeyEvent_R* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_R()

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
        CPP_KeyEvent_S* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_S()

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
        CPP_KeyEvent_T* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_T()

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
        CPP_KeyEvent_U* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_U()

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
        CPP_KeyEvent_V* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_V()

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
        CPP_KeyEvent_W* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_W()

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
        CPP_KeyEvent_X* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_X()

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
        CPP_KeyEvent_Y* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Y()

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
        CPP_KeyEvent_Z* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Z()

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
        CPP_KeyEvent_Left_Bracket* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Bracket()

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
        CPP_KeyEvent_Backslash* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Backslash()

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
        CPP_KeyEvent_Right_Bracket* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Bracket()

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
        CPP_KeyEvent_Grave_Accent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Grave_Accent()

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
        CPP_KeyEvent_World_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_World_1()

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
        CPP_KeyEvent_World_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_World_2()

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
        CPP_KeyEvent_Escape* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Escape()

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
        CPP_KeyEvent_Enter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Enter()

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
        CPP_KeyEvent_Tab* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Tab()

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
        CPP_KeyEvent_Backspace* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Backspace()

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
        CPP_KeyEvent_Insert* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Insert()

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
        CPP_KeyEvent_Delete* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Delete()

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
        CPP_KeyEvent_Right* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right()

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
        CPP_KeyEvent_Left* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left()

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
        CPP_KeyEvent_Down* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Down()

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
        CPP_KeyEvent_Up* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Up()

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
        CPP_KeyEvent_Page_Up* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Page_Up()

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
        CPP_KeyEvent_Page_Down* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Page_Down()

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
        CPP_KeyEvent_Home* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Home()

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
        CPP_KeyEvent_End* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_End()

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
        CPP_KeyEvent_Caps_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Caps_Lock()

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
        CPP_KeyEvent_Scroll_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Scroll_Lock()

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
        CPP_KeyEvent_Num_Lock* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Num_Lock()

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
        CPP_KeyEvent_Print_Screen* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Print_Screen()

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
        CPP_KeyEvent_Pause* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Pause()

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
        CPP_KeyEvent_F1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F1()

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
        CPP_KeyEvent_F2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F2()

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
        CPP_KeyEvent_F3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F3()

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
        CPP_KeyEvent_F4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F4()

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
        CPP_KeyEvent_F5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F5()

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
        CPP_KeyEvent_F6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F6()

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
        CPP_KeyEvent_F7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F7()

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
        CPP_KeyEvent_F8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F8()

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
        CPP_KeyEvent_F9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F9()

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
        CPP_KeyEvent_F10* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F10()

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
        CPP_KeyEvent_F11* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F11()

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
        CPP_KeyEvent_F12* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F12()

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
        CPP_KeyEvent_F13* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F13()

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
        CPP_KeyEvent_F14* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F14()

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
        CPP_KeyEvent_F15* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F15()

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
        CPP_KeyEvent_F16* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F16()

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
        CPP_KeyEvent_F17* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F17()

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
        CPP_KeyEvent_F18* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F18()

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
        CPP_KeyEvent_F19* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F19()

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
        CPP_KeyEvent_F20* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F20()

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
        CPP_KeyEvent_F21* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F21()

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
        CPP_KeyEvent_F22* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F22()

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
        CPP_KeyEvent_F23* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F23()

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
        CPP_KeyEvent_F24* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F24()

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
        CPP_KeyEvent_F25* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_F25()

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
        CPP_KeyEvent_Left_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Shift()

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
        CPP_KeyEvent_Left_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Control()

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
        CPP_KeyEvent_Left_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Alt()

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
        CPP_KeyEvent_Left_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Left_Super()

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
        CPP_KeyEvent_Right_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Shift()

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
        CPP_KeyEvent_Right_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Control()

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
        CPP_KeyEvent_Right_Alt * cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Alt()

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
        CPP_KeyEvent_Right_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Right_Super()

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

cdef class KeyEvent_Shift:
    cdef:
        CPP_KeyEvent_Shift* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Shift()

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

cdef class KeyEvent_Control:
    cdef:
        CPP_KeyEvent_Control* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Control()

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

cdef class KeyEvent_Alt:
    cdef:
        CPP_KeyEvent_Alt* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Alt()

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

cdef class KeyEvent_Super:
    cdef:
        CPP_KeyEvent_Super* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Super()

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
        CPP_KeyEvent_Menu* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyEvent_Menu()

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
        CPP_KeyPadEvent_0* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_0()

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
        CPP_KeyPadEvent_1* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_1()

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
        CPP_KeyPadEvent_2* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_2()

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
        CPP_KeyPadEvent_3* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_3()

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
        CPP_KeyPadEvent_4* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_4()

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
        CPP_KeyPadEvent_5* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_5()

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
        CPP_KeyPadEvent_6* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_6()

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
        CPP_KeyPadEvent_7* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_7()

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
        CPP_KeyPadEvent_8* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_8()

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
        CPP_KeyPadEvent_9* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_9()

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
        CPP_KeyPadEvent_Decimal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Decimal()

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
        CPP_KeyPadEvent_Divide* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Divide()

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
        CPP_KeyPadEvent_Multiply* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Multiply()

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
        CPP_KeyPadEvent_Subtract* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Subtract()

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
        CPP_KeyPadEvent_Add* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Add()

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
        CPP_KeyPadEvent_Enter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Enter()

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
        CPP_KeyPadEvent_Equal* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_KeyPadEvent_Equal()

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
