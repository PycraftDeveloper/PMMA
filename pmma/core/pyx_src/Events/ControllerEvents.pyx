# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string
from libcpp.vector cimport vector

import numpy as np
cimport numpy as np

from Events cimport CPP_ButtonPressed, ButtonPressed

cdef extern from "Events/ControllerEvents.hpp" nogil:
    cdef cppclass CPP_Controller "PMMA::Events::Controller":
        CPP_Controller(unsigned int new_ID) except + nogil

        CPP_ButtonPressed* A_Button
        CPP_ButtonPressed* B_Button
        CPP_ButtonPressed* X_Button
        CPP_ButtonPressed* Y_Button
        CPP_ButtonPressed* Left_Bumper_Button
        CPP_ButtonPressed* Right_Bumper_Button
        CPP_ButtonPressed* Back_Button
        CPP_ButtonPressed* Start_Button
        CPP_ButtonPressed* Guide_Button
        CPP_ButtonPressed* Left_Thumb_Button
        CPP_ButtonPressed* Right_Thumb_Button
        CPP_ButtonPressed* DPad_Up_Button
        CPP_ButtonPressed* DPad_Down_Button
        CPP_ButtonPressed* DPad_Left_Button
        CPP_ButtonPressed* DPad_Right_Button

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

cdef class Controller:
    cdef:
        CPP_Controller* cpp_class_ptr
        ButtonPressed cpp_a_button
        ButtonPressed cpp_b_button
        ButtonPressed cpp_x_button
        ButtonPressed cpp_y_button
        ButtonPressed cpp_left_bumper_button
        ButtonPressed cpp_right_bumper_button
        ButtonPressed cpp_back_button
        ButtonPressed cpp_start_button
        ButtonPressed cpp_guide_button
        ButtonPressed cpp_left_thumb_button
        ButtonPressed cpp_right_thumb_button
        ButtonPressed cpp_dpad_up_button
        ButtonPressed cpp_dpad_down_button
        ButtonPressed cpp_dpad_left_button
        ButtonPressed cpp_dpad_right_button

    def __cinit__(self, controller_id):
        self.cpp_class_ptr = new CPP_Controller(controller_id)

        self.cpp_a_button = ButtonPressed()
        self.cpp_a_button.cpp_base_class_ptr = self.cpp_class_ptr.A_Button

        self.cpp_b_button = ButtonPressed()
        self.cpp_b_button.cpp_base_class_ptr = self.cpp_class_ptr.B_Button

        self.cpp_x_button = ButtonPressed()
        self.cpp_x_button.cpp_base_class_ptr = self.cpp_class_ptr.X_Button

        self.cpp_y_button = ButtonPressed()
        self.cpp_y_button.cpp_base_class_ptr = self.cpp_class_ptr.Y_Button

        self.cpp_left_bumper_button = ButtonPressed()
        self.cpp_left_bumper_button.cpp_base_class_ptr = self.cpp_class_ptr.Left_Bumper_Button

        self.cpp_right_bumper_button = ButtonPressed()
        self.cpp_right_bumper_button.cpp_base_class_ptr = self.cpp_class_ptr.Right_Bumper_Button

        self.cpp_back_button = ButtonPressed()
        self.cpp_back_button.cpp_base_class_ptr = self.cpp_class_ptr.Back_Button

        self.cpp_start_button = ButtonPressed()
        self.cpp_start_button.cpp_base_class_ptr = self.cpp_class_ptr.Start_Button

        self.cpp_guide_button = ButtonPressed()
        self.cpp_guide_button.cpp_base_class_ptr = self.cpp_class_ptr.Guide_Button

        self.cpp_left_thumb_button = ButtonPressed()
        self.cpp_left_thumb_button.cpp_base_class_ptr = self.cpp_class_ptr.Left_Thumb_Button

        self.cpp_right_thumb_button = ButtonPressed()
        self.cpp_right_thumb_button.cpp_base_class_ptr = self.cpp_class_ptr.Right_Thumb_Button

        self.cpp_dpad_up_button = ButtonPressed()
        self.cpp_dpad_up_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Up_Button

        self.cpp_dpad_down_button = ButtonPressed()
        self.cpp_dpad_down_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Down_Button

        self.cpp_dpad_left_button = ButtonPressed()
        self.cpp_dpad_left_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Left_Button

        self.cpp_dpad_right_button = ButtonPressed()
        self.cpp_dpad_right_button.cpp_base_class_ptr = self.cpp_class_ptr.DPad_Right_Button


    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

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