# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string
from libcpp.vector cimport vector

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

    cdef cppclass CPP_ControllerEvent:
        CPP_ControllerEvent(unsigned int new_ID) except + nogil

        CPP_ButtonPressedEvent* A_Button
        CPP_ButtonPressedEvent* B_Button
        CPP_ButtonPressedEvent* X_Button
        CPP_ButtonPressedEvent* Y_Button
        CPP_ButtonPressedEvent* Left_Bumper_Button
        CPP_ButtonPressedEvent* Right_Bumper_Button
        CPP_ButtonPressedEvent* Back_Button
        CPP_ButtonPressedEvent* Start_Button
        CPP_ButtonPressedEvent* Guide_Button
        CPP_ButtonPressedEvent* Left_Thumb_Button
        CPP_ButtonPressedEvent* Right_Thumb_Button
        CPP_ButtonPressedEvent* DPad_Up_Button
        CPP_ButtonPressedEvent* DPad_Down_Button
        CPP_ButtonPressedEvent* DPad_Left_Button
        CPP_ButtonPressedEvent* DPad_Right_Button

        bool GetConnected() except + nogil
        bool GetActive() except + nogil

        string GetRawName() except + nogil
        string GetGamePadName() except + nogil
        string GetGUID() except + nogil

        float GetRawAxis_Decimal(int AxisID) except + nogil
        float GetRawAxis_Percentage(int AxisID) except + nogil
        bool GetRawButtonPressed(int ButtonID) except + nogil
        string GetRawHatState(int HatID) except + nogil

        float Get_Right_Stick_X_Axis_Percentage(float DeadZone) except + nogil
        float Get_Right_Stick_Y_Axis_Percentage(float DeadZone) except + nogil

        float Get_Right_Stick_X_Axis_Decimal(float DeadZone) except + nogil
        float Get_Right_Stick_Y_Axis_Decimal(float DeadZone) except + nogil

        float Get_Left_Stick_X_Axis_Percentage(float DeadZone) except + nogil
        float Get_Left_Stick_Y_Axis_Percentage(float DeadZone) except + nogil

        float Get_Left_Stick_X_Axis_Decimal(float DeadZone) except + nogil
        float Get_Left_Stick_Y_Axis_Decimal(float DeadZone) except + nogil

        float Get_Right_Trigger_Axis_Percentage(float DeadZone) except + nogil
        float Get_Left_Trigger_Axis_Percentage(float DeadZone) except + nogil

        float Get_Right_Trigger_Axis_Decimal(float DeadZone) except + nogil
        float Get_Left_Trigger_Axis_Decimal(float DeadZone) except + nogil

        void Get_Left_Stick_Position_Percentage(float DeadZone, float* out) except + nogil
        void Get_Left_Stick_Position_Decimal(float DeadZone, float* out) except + nogil

        void Get_Right_Stick_Position_Percentage(float DeadZone, float* out) except + nogil
        void Get_Right_Stick_Position_Decimal(float DeadZone, float* out) except + nogil

cdef class ButtonPressedEvent:
    cdef CPP_ButtonPressedEvent* cpp_base_class_ptr

    def get_pressed(self):
        if (self.cpp_base_class_ptr == NULL):
            return False
        return self.cpp_base_class_ptr.GetPressed()

    def get_pressed_toggle(self):
        if (self.cpp_base_class_ptr == NULL):
            return False
        return self.cpp_base_class_ptr.GetPressedToggle()

    def get_double_pressed(self):
        if (self.cpp_base_class_ptr == NULL):
            return False
        return self.cpp_base_class_ptr.GetDoublePressed()

    def get_long_pressed(self):
        if (self.cpp_base_class_ptr == NULL):
            return False
        return self.cpp_base_class_ptr.GetLongPressed()

    def poll_long_pressed(self):
        if (self.cpp_base_class_ptr == NULL):
            return False
        return self.cpp_base_class_ptr.PollLongPressed()

    def get_repeat_press_duration(self):
        if (self.cpp_base_class_ptr == NULL):
            return 0
        return self.cpp_base_class_ptr.GetRepeatPressDuration()

    def get_long_press_duration(self):
        if (self.cpp_base_class_ptr == NULL):
            return 0
        return self.cpp_base_class_ptr.GetLongPressDuration()

    def get_double_press_duration(self):
        if (self.cpp_base_class_ptr == NULL):
            return 0
        return self.cpp_base_class_ptr.GetDoublePressDuration()

    def set_repeat_press_duration(self, duration):
        if (self.cpp_base_class_ptr == NULL):
            return
        self.cpp_base_class_ptr.SetRepeatPressDuration(duration)

    def set_double_press_duration(self, duration):
        if (self.cpp_base_class_ptr == NULL):
            return
        self.cpp_base_class_ptr.SetDoublePressDuration(duration)

    def set_long_press_duration(self, duration):
        if (self.cpp_base_class_ptr == NULL):
            return
        self.cpp_base_class_ptr.SetLongPressDuration(duration)

cdef class Controller:
    cdef:
        CPP_ControllerEvent* cpp_class_ptr
        ButtonPressedEvent cpp_a_button
        ButtonPressedEvent cpp_b_button
        ButtonPressedEvent cpp_x_button
        ButtonPressedEvent cpp_y_button
        ButtonPressedEvent cpp_left_bumper_button
        ButtonPressedEvent cpp_right_bumper_button
        ButtonPressedEvent cpp_back_button
        ButtonPressedEvent cpp_start_button
        ButtonPressedEvent cpp_guide_button
        ButtonPressedEvent cpp_left_thumb_button
        ButtonPressedEvent cpp_right_thumb_button
        ButtonPressedEvent cpp_dpad_up_button
        ButtonPressedEvent cpp_dpad_down_button
        ButtonPressedEvent cpp_dpad_left_button
        ButtonPressedEvent cpp_dpad_right_button

    def __cinit__(self, controller_id):
        self.cpp_class_ptr = new CPP_ControllerEvent(controller_id)

        self.cpp_a_button = ButtonPressedEvent()
        self.cpp_a_button.cpp_base_class_ptr = self.cpp_class_ptr.A_Button

        self.cpp_b_button = ButtonPressedEvent()
        self.cpp_b_button.cpp_base_class_ptr = self.cpp_class_ptr.B_Button

        self.cpp_x_button = ButtonPressedEvent()
        self.cpp_x_button.cpp_base_class_ptr = self.cpp_class_ptr.X_Button

        self.cpp_y_button = ButtonPressedEvent()
        self.cpp_y_button.cpp_base_class_ptr = self.cpp_class_ptr.Y_Button

        self.cpp_left_bumper_button = ButtonPressedEvent()
        self.cpp_left_bumper_button.cpp_base_class_ptr = self.cpp_class_ptr.Left_Bumper_Button

        self.cpp_right_bumper_button = ButtonPressedEvent()
        self.cpp_right_bumper_button.cpp_base_class_ptr = self.cpp_class_ptr.Right_Bumper_Button

        self.cpp_back_button = ButtonPressedEvent()
        self.cpp_back_button.cpp_base_class_ptr = self.cpp_class_ptr.Back_Button

        self.cpp_start_button = ButtonPressedEvent()
        self.cpp_start_button.cpp_base_class_ptr = self.cpp_class_ptr.Start_Button

        self.cpp_guide_button = ButtonPressedEvent()
        self.cpp_guide_button.cpp_base_class_ptr = self.cpp_class_ptr.Guide_Button

        self.cpp_left_thumb_button = ButtonPressedEvent()
        self.cpp_left_thumb_button.cpp_base_class_ptr = self.cpp_class_ptr.Left_Thumb_Button

        self.cpp_right_thumb_button = ButtonPressedEvent()
        self.cpp_right_thumb_button.cpp_base_class_ptr = self.cpp_class_ptr.Right_Thumb_Button

        self.cpp_dpad_up_button = ButtonPressedEvent()
        self.cpp_dpad_up_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Up_Button

        self.cpp_dpad_down_button = ButtonPressedEvent()
        self.cpp_dpad_down_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Down_Button

        self.cpp_dpad_left_button = ButtonPressedEvent()
        self.cpp_dpad_left_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Left_Button

        self.cpp_dpad_right_button = ButtonPressedEvent()
        self.cpp_dpad_right_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Right_Button


    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_connected(self):
        return self.cpp_class_ptr.GetConnected()

    def get_active(self):
        return self.cpp_class_ptr.GetActive()

    def get_raw_axis_decimal(self, axis_id):
        return self.cpp_class_ptr.GetRawAxis_Decimal(axis_id)

    def get_raw_axis_percentage(self, axis_id):
        return self.cpp_class_ptr.GetRawAxis_Percentage(axis_id)

    def get_raw_button_pressed(self, button_id):
        return self.cpp_class_ptr.GetRawButtonPressed(button_id)

    def get_raw_hat_state(self, hat_id):
        cdef string cpp_str = self.cpp_class_ptr.GetRawHatState(hat_id)
        return cpp_str.c_str().decode('utf-8')

    def get_raw_name(self):
        cdef string cpp_str = self.cpp_class_ptr.GetRawName()
        return cpp_str.c_str().decode('utf-8')

    def get_gamepad_name(self):
        cdef string cpp_str = self.cpp_class_ptr.GetGamePadName()
        return cpp_str.c_str().decode('utf-8')

    def get_GUID(self):
        cdef string cpp_str = self.cpp_class_ptr.GetGUID()
        return cpp_str.c_str().decode('utf-8')

    property a_button:
        def __get__(self):
            self.cpp_a_button.cpp_base_class_ptr = self.cpp_class_ptr.A_Button
            return self.cpp_a_button

    property b_button:
        def __get__(self):
            self.cpp_b_button.cpp_base_class_ptr = self.cpp_class_ptr.B_Button
            return self.cpp_b_button

    property x_button:
        def __get__(self):
            self.cpp_x_button.cpp_base_class_ptr = self.cpp_class_ptr.X_Button
            return self.cpp_x_button

    property y_button:
        def __get__(self):
            self.cpp_y_button.cpp_base_class_ptr = self.cpp_class_ptr.Y_Button
            return self.cpp_y_button

    property left_bumper_button:
        def __get__(self):
            self.cpp_left_bumper_button.cpp_base_class_ptr = self.cpp_class_ptr.Left_Bumper_Button
            return self.cpp_left_bumper_button

    property right_bumper_button:
        def __get__(self):
            self.cpp_right_bumper_button.cpp_base_class_ptr = self.cpp_class_ptr.Right_Bumper_Button
            return self.cpp_right_bumper_button

    property back_button:
        def __get__(self):
            self.cpp_back_button.cpp_base_class_ptr = self.cpp_class_ptr.Back_Button
            return self.cpp_back_button

    property start_button:
        def __get__(self):
            self.cpp_start_button.cpp_base_class_ptr = self.cpp_class_ptr.Start_Button
            return self.cpp_start_button

    property guide_button:
        def __get__(self):
            self.cpp_guide_button.cpp_base_class_ptr = self.cpp_class_ptr.Guide_Button
            return self.cpp_guide_button

    property left_thumb_button:
        def __get__(self):
            self.cpp_left_thumb_button.cpp_base_class_ptr = self.cpp_class_ptr.Left_Thumb_Button
            return self.cpp_left_thumb_button

    property right_thumb_button:
        def __get__(self):
            self.cpp_right_thumb_button.cpp_base_class_ptr = self.cpp_class_ptr.Right_Thumb_Button
            return self.cpp_right_thumb_button

    property dpad_up_button:
        def __get__(self):
            self.cpp_dpad_up_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Up_Button
            return self.cpp_dpad_up_button

    property dpad_down_button:
        def __get__(self):
            self.cpp_dpad_down_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Down_Button
            return self.cpp_dpad_down_button

    property dpad_left_button:
        def __get__(self):
            self.cpp_dpad_left_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Left_Button
            return self.cpp_dpad_left_button

    property dpad_right_button:
        def __get__(self):
            self.cpp_dpad_right_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Right_Button
            return self.cpp_dpad_right_button

    def get_right_stick_X_axis_percentage(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Right_Stick_X_Axis_Percentage(dead_zone)

    def get_right_stick_Y_axis_percentage(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Right_Stick_Y_Axis_Percentage(dead_zone)


    def get_right_stick_X_axis_decimal(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Right_Stick_X_Axis_Decimal(dead_zone)

    def get_right_stick_Y_axis_decimal(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Right_Stick_Y_Axis_Decimal(dead_zone)


    def get_left_stick_X_axis_percentage(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Left_Stick_X_Axis_Percentage(dead_zone)

    def get_Left_stick_Y_axis_percentage(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Left_Stick_Y_Axis_Percentage(dead_zone)


    def get_left_stick_X_axis_decimal(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Left_Stick_X_Axis_Decimal(dead_zone)

    def get_Left_stick_Y_axis_decimal(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Left_Stick_Y_Axis_Decimal(dead_zone)


    def get_right_trigger_axis_percentage(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Right_Trigger_Axis_Percentage(dead_zone)

    def get_left_trigger_axis_percentage(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Left_Trigger_Axis_Percentage(dead_zone)


    def get_right_trigger_axis_decimal(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Right_Trigger_Axis_Decimal(dead_zone)

    def get_left_trigger_axis_decimal(self, dead_zone=0):
        return self.cpp_class_ptr.Get_Left_Trigger_Axis_Decimal(dead_zone)

    def get_left_stick_position_percentage(self, dead_zone=0, using_numpy_arrays=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            float* out_ptr;

        out_np = np.empty(2, dtype=np.float32, order='C')
        out_ptr = <float*>&out_np[0]

        self.cpp_class_ptr.Get_Left_Stick_Position_Percentage(dead_zone, out_ptr)

        if using_numpy_arrays:
            return out_np
        else:
            return out_np.tolist()

    def get_right_stick_position_percentage(self, dead_zone=0, using_numpy_arrays=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            float* out_ptr;

        out_np = np.empty(2, dtype=np.float32, order='C')
        out_ptr = <float*>&out_np[0]

        self.cpp_class_ptr.Get_Right_Stick_Position_Percentage(dead_zone, out_ptr)

        if using_numpy_arrays:
            return out_np
        else:
            return out_np.tolist()

    def get_left_stick_position_decimal(self, dead_zone=0, using_numpy_arrays=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            float* out_ptr;

        out_np = np.empty(2, dtype=np.float32, order='C')
        out_ptr = <float*>&out_np[0]

        self.cpp_class_ptr.Get_Left_Stick_Position_Decimal(dead_zone, out_ptr)

        if using_numpy_arrays:
            return out_np
        else:
            return out_np.tolist()

    def get_right_stick_position_decimal(self, dead_zone=0, using_numpy_arrays=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            float* out_ptr;

        out_np = np.empty(2, dtype=np.float32, order='C')
        out_ptr = <float*>&out_np[0]

        self.cpp_class_ptr.Get_Right_Stick_Position_Decimal(dead_zone, out_ptr)

        if using_numpy_arrays:
            return out_np
        else:
            return out_np.tolist()