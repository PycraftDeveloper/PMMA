import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

import pmma.python_src.utility.event_utils as _event_utils

class Controllers:
    def __init__(self):
        initialize(self)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def identify_controllers(self):
        Registry.pmma_module_spine[Constants.CONTROLLER_INTERMEDIARY_OBJECT].identify_controllers()

    def get_controller(self, controller_index):
        return Registry.pmma_module_spine[Constants.CONTROLLER_INTERMEDIARY_OBJECT].get_controller(controller_index)

    def update_controllers(self):
        Registry.pmma_module_spine[Constants.CONTROLLER_INTERMEDIARY_OBJECT].update_controllers()

    def list_controllers(self):
        return Registry.pmma_module_spine[Constants.CONTROLLER_INTERMEDIARY_OBJECT].list_controllers()

class Controller:
    def __del__(self, do_garbage_collection=False):
            if self._shut_down is False:
                del self
                if do_garbage_collection:
                    _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self, joy_num):
        self._joy_num = joy_num
        self._joy = _pygame.joystick.Joystick(joy_num)
        self._joy.init()

        self.y_button = _event_utils.Y_BUTTON()
        self.b_button = _event_utils.B_BUTTON()
        self.a_button = _event_utils.A_BUTTON()
        self.x_button = _event_utils.X_BUTTON()
        self.home_button = _event_utils.Home_BUTTON()
        self.right_joystick_button = _event_utils.RightJoystick_BUTTON()
        self.left_joystick_button = _event_utils.LeftJoystick_BUTTON()
        self.options_button = _event_utils.Options_BUTTON()
        self.share_button = _event_utils.Share_BUTTON()
        self.right_trigger = _event_utils.Right_TRIGGER()
        self.left_trigger = _event_utils.Left_TRIGGER()
        self.right_bumper = _event_utils.Right_BUMPER()
        self.left_bumper = _event_utils.Left_BUMPER()
        self.center_button = _event_utils.Center_BUTTON()
        self.left_joystick_axis = _event_utils.LeftJoystick_AXIS()
        self.right_joystick_axis = _event_utils.RightJoystick_AXIS()
        self.up_hat_button = _event_utils.UpHat_BUTTON()
        self.down_hat_button = _event_utils.DownHat_BUTTON()
        self.left_hat_button = _event_utils.LeftHat_BUTTON()
        self.right_hat_button = _event_utils.RightHat_BUTTON()

    def set_y_button_double_tapped(self, value):
        self.y_button.set_double_tapped(value)

    def get_y_button_double_tapped(self):
        return self.y_button.get_double_tapped()

    def get_y_button_last_tap_time(self):
        return self.y_button.get_last_tap_time()

    def set_y_button_last_tap_time(self, value):
        self.y_button.set_last_tap_time(value)

    def get_y_button_pressed(self):
        return self.y_button.get_pressed()

    def set_y_button_pressed(self, value):
        self.y_button.set_pressed(value)

    def get_y_button_double_tap_timing(self):
        return self.y_button.get_double_tap_timing()

    def set_y_button_double_tap_timing(self, value):
        self.y_button.set_double_tap_timing(value)

    def set_b_button_double_tapped(self, value):
        self.b_button.set_double_tapped(value)

    def get_b_button_double_tapped(self):
        return self.b_button.get_double_tapped()

    def get_b_button_last_tap_time(self):
        return self.b_button.get_last_tap_time()

    def set_b_button_last_tap_time(self, value):
        self.b_button.set_last_tap_time(value)

    def get_b_button_pressed(self):
        return self.b_button.get_pressed()

    def set_b_button_pressed(self, value):
        self.b_button.set_pressed(value)

    def get_b_button_double_tap_timing(self):
        return self.b_button.get_double_tap_timing()

    def set_b_button_double_tap_timing(self, value):
        self.b_button.set_double_tap_timing(value)

    def set_a_button_double_tapped(self, value):
        self.a_button.set_double_tapped(value)

    def get_a_button_double_tapped(self):
        return self.a_button.get_double_tapped()

    def get_a_button_last_tap_time(self):
        return self.a_button.get_last_tap_time()

    def set_a_button_last_tap_time(self, value):
        self.a_button.set_last_tap_time(value)

    def get_a_button_pressed(self):
        return self.a_button.get_pressed()

    def set_a_button_pressed(self, value):
        self.a_button.set_pressed(value)

    def get_a_button_double_tap_timing(self):
        return self.a_button.get_double_tap_timing()

    def set_a_button_double_tap_timing(self, value):
        self.a_button.set_double_tap_timing(value)

    def set_x_button_double_tapped(self, value):
        self.x_button.set_double_tapped(value)

    def get_x_button_double_tapped(self):
        return self.x_button.get_double_tapped()

    def get_x_button_last_tap_time(self):
        return self.x_button.get_last_tap_time()

    def set_x_button_last_tap_time(self, value):
        self.x_button.set_last_tap_time(value)

    def get_x_button_pressed(self):
        return self.x_button.get_pressed()

    def set_x_button_pressed(self, value):
        self.x_button.set_pressed(value)

    def get_x_button_double_tap_timing(self):
        return self.x_button.get_double_tap_timing()

    def set_x_button_double_tap_timing(self, value):
        self.x_button.set_double_tap_timing(value)

    def set_home_button_double_tapped(self, value):
        self.home_button.set_double_tapped(value)

    def get_home_button_double_tapped(self):
        return self.home_button.get_double_tapped()

    def get_home_button_last_tap_time(self):
        return self.home_button.get_last_tap_time()

    def set_home_button_last_tap_time(self, value):
        self.home_button.set_last_tap_time(value)

    def get_home_button_pressed(self):
        return self.home_button.get_pressed()

    def set_home_button_pressed(self, value):
        self.home_button.set_pressed(value)

    def get_home_button_double_tap_timing(self):
        return self.home_button.get_double_tap_timing()

    def set_home_button_double_tap_timing(self, value):
        self.home_button.set_double_tap_timing(value)

    def set_right_joystick_button_double_tapped(self, value):
        self.right_joystick_button.set_double_tapped(value)

    def get_right_joystick_button_double_tapped(self):
        return self.right_joystick_button.get_double_tapped()

    def get_right_joystick_button_last_tap_time(self):
        return self.right_joystick_button.get_last_tap_time()

    def set_right_joystick_button_last_tap_time(self, value):
        self.right_joystick_button.set_last_tap_time(value)

    def get_right_joystick_button_pressed(self):
        return self.right_joystick_button.get_pressed()

    def set_right_joystick_button_pressed(self, value):
        self.right_joystick_button.set_pressed(value)

    def get_right_joystick_button_double_tap_timing(self):
        return self.right_joystick_button.get_double_tap_timing()

    def set_right_joystick_button_double_tap_timing(self, value):
        self.right_joystick_button.set_double_tap_timing(value)

    def set_left_joystick_button_double_tapped(self, value):
        self.left_joystick_button.set_double_tapped(value)

    def get_left_joystick_button_double_tapped(self):
        return self.left_joystick_button.get_double_tapped()

    def get_left_joystick_button_last_tap_time(self):
        return self.left_joystick_button.get_last_tap_time()

    def set_left_joystick_button_last_tap_time(self, value):
        self.left_joystick_button.set_last_tap_time(value)

    def get_left_joystick_button_pressed(self):
        return self.left_joystick_button.get_pressed()

    def set_left_joystick_button_pressed(self, value):
        self.left_joystick_button.set_pressed(value)

    def get_left_joystick_button_double_tap_timing(self):
        return self.left_joystick_button.get_double_tap_timing()

    def set_left_joystick_button_double_tap_timing(self, value):
        self.left_joystick_button.set_double_tap_timing(value)

    def set_options_button_double_tapped(self, value):
        self.options_button.set_double_tapped(value)

    def get_options_button_double_tapped(self):
        return self.options_button.get_double_tapped()

    def get_options_button_last_tap_time(self):
        return self.options_button.get_last_tap_time()

    def set_options_button_last_tap_time(self, value):
        self.options_button.set_last_tap_time(value)

    def get_options_button_pressed(self):
        return self.options_button.get_pressed()

    def set_options_button_pressed(self, value):
        self.options_button.set_pressed(value)

    def get_options_button_double_tap_timing(self):
        return self.options_button.get_double_tap_timing()

    def set_options_button_double_tap_timing(self, value):
        self.options_button.set_double_tap_timing(value)

    def set_share_button_double_tapped(self, value):
        self.share_button.set_double_tapped(value)

    def get_share_button_double_tapped(self):
        return self.share_button.get_double_tapped()

    def get_share_button_last_tap_time(self):
        return self.share_button.get_last_tap_time()

    def set_share_button_last_tap_time(self, value):
        self.share_button.set_last_tap_time(value)

    def get_share_button_pressed(self):
        return self.share_button.get_pressed()

    def set_share_button_pressed(self, value):
        self.share_button.set_pressed(value)

    def get_share_button_double_tap_timing(self):
        return self.share_button.get_double_tap_timing()

    def set_share_button_double_tap_timing(self, value):
        self.share_button.set_double_tap_timing(value)

    def set_right_trigger_double_tapped(self, value):
        self.right_trigger.set_double_tapped(value)

    def get_right_trigger_double_tapped(self):
        return self.right_trigger.get_double_tapped()

    def get_right_trigger_last_tap_time(self):
        return self.right_trigger.get_last_tap_time()

    def set_right_trigger_last_tap_time(self, value):
        self.right_trigger.set_last_tap_time(value)

    def get_right_trigger_pressed(self):
        return self.right_trigger.get_pressed()

    def set_right_trigger_pressed(self, value):
        self.right_trigger.set_pressed(value)

    def get_right_trigger_double_tap_timing(self):
        return self.right_trigger.get_double_tap_timing()

    def set_right_trigger_double_tap_timing(self, value):
        self.right_trigger.set_double_tap_timing(value)

    def set_left_trigger_double_tapped(self, value):
        self.left_trigger.set_double_tapped(value)

    def get_left_trigger_double_tapped(self):
        return self.left_trigger.get_double_tapped()

    def get_left_trigger_last_tap_time(self):
        return self.left_trigger.get_last_tap_time()

    def set_left_trigger_last_tap_time(self, value):
        self.left_trigger.set_last_tap_time(value)

    def get_left_trigger_pressed(self):
        return self.left_trigger.get_pressed()

    def set_left_trigger_pressed(self, value):
        self.left_trigger.set_pressed(value)

    def get_left_trigger_double_tap_timing(self):
        return self.left_trigger.get_double_tap_timing()

    def set_left_trigger_double_tap_timing(self, value):
        self.left_trigger.set_double_tap_timing(value)

    def set_right_bumper_double_tapped(self, value):
        self.right_bumper.set_double_tapped(value)

    def get_right_bumper_double_tapped(self):
        return self.right_bumper.get_double_tapped()

    def get_right_bumper_last_tap_time(self):
        return self.right_bumper.get_last_tap_time()

    def set_right_bumper_last_tap_time(self, value):
        self.right_bumper.set_last_tap_time(value)

    def get_right_bumper_pressed(self):
        return self.right_bumper.get_pressed()

    def set_right_bumper_pressed(self, value):
        self.right_bumper.set_pressed(value)

    def get_right_bumper_double_tap_timing(self):
        return self.right_bumper.get_double_tap_timing()

    def set_right_bumper_double_tap_timing(self, value):
        self.right_bumper.set_double_tap_timing(value)

    def set_left_bumper_double_tapped(self, value):
        self.left_bumper.set_double_tapped(value)

    def get_left_bumper_double_tapped(self):
        return self.left_bumper.get_double_tapped()

    def get_left_bumper_last_tap_time(self):
        return self.left_bumper.get_last_tap_time()

    def set_left_bumper_last_tap_time(self, value):
        self.left_bumper.set_last_tap_time(value)

    def get_left_bumper_pressed(self):
        return self.left_bumper.get_pressed()

    def set_left_bumper_pressed(self, value):
        self.left_bumper.set_pressed(value)

    def get_left_bumper_double_tap_timing(self):
        return self.left_bumper.get_double_tap_timing()

    def set_left_bumper_double_tap_timing(self, value):
        self.left_bumper.set_double_tap_timing(value)

    def set_center_button_double_tapped(self, value):
        self.center_button.set_double_tapped(value)

    def get_center_button_double_tapped(self):
        return self.center_button.get_double_tapped()

    def get_center_button_last_tap_time(self):
        return self.center_button.get_last_tap_time()

    def set_center_button_last_tap_time(self, value):
        self.center_button.set_last_tap_time(value)

    def get_center_button_pressed(self):
        return self.center_button.get_pressed()

    def set_center_button_pressed(self, value):
        self.center_button.set_pressed(value)

    def get_center_button_double_tap_timing(self):
        return self.center_button.get_double_tap_timing()

    def set_center_button_double_tap_timing(self, value):
        self.center_button.set_double_tap_timing(value)

    def get_left_joystick_axis_x_axis(self):
        return self.left_joystick_axis.get_x_axis()

    def get_left_joystick_axis_y_axis(self):
        return self.left_joystick_axis.get_y_axis()

    def set_left_joystick_axis_x_axis(self, value):
        self.left_joystick_axis.set_x_axis(value)

    def set_left_joystick_axis_y_axis(self, value):
        self.left_joystick_axis.set_y_axis(value)

    def get_right_joystick_axis_x_axis(self):
        return self.right_joystick_axis.get_x_axis()

    def get_right_joystick_axis_y_axis(self):
        return self.right_joystick_axis.get_y_axis()

    def set_right_joystick_axis_x_axis(self, value):
        self.right_joystick_axis.set_x_axis(value)

    def set_right_joystick_axis_y_axis(self, value):
        self.right_joystick_axis.set_y_axis(value)

    def set_up_hat_button_double_tapped(self, value):
        self.up_hat_button.set_double_tapped(value)

    def get_up_hat_button_double_tapped(self):
        return self.up_hat_button.get_double_tapped()

    def get_up_hat_button_last_tap_time(self):
        return self.up_hat_button.get_last_tap_time()

    def set_up_hat_button_last_tap_time(self, value):
        self.up_hat_button.set_last_tap_time(value)

    def get_up_hat_button_pressed(self):
        return self.up_hat_button.get_pressed()

    def set_up_hat_button_pressed(self, value):
        self.up_hat_button.set_pressed(value)

    def get_up_hat_button_double_tap_timing(self):
        return self.up_hat_button.get_double_tap_timing()

    def set_up_hat_button_double_tap_timing(self, value):
        self.up_hat_button.set_double_tap_timing(value)

    def set_down_hat_button_double_tapped(self, value):
        self.down_hat_button.set_double_tapped(value)

    def get_down_hat_button_double_tapped(self):
        return self.down_hat_button.get_double_tapped()

    def get_down_hat_button_last_tap_time(self):
        return self.down_hat_button.get_last_tap_time()

    def set_down_hat_button_last_tap_time(self, value):
        self.down_hat_button.set_last_tap_time(value)

    def get_down_hat_button_pressed(self):
        return self.down_hat_button.get_pressed()

    def set_down_hat_button_pressed(self, value):
        self.down_hat_button.set_pressed(value)

    def get_down_hat_button_double_tap_timing(self):
        return self.down_hat_button.get_double_tap_timing()

    def set_down_hat_button_double_tap_timing(self, value):
        self.down_hat_button.set_double_tap_timing(value)

    def set_left_hat_button_double_tapped(self, value):
        self.left_hat_button.set_double_tapped(value)

    def get_left_hat_button_double_tapped(self):
        return self.left_hat_button.get_double_tapped()

    def get_left_hat_button_last_tap_time(self):
        return self.left_hat_button.get_last_tap_time()

    def set_left_hat_button_last_tap_time(self, value):
        self.left_hat_button.set_last_tap_time(value)

    def get_left_hat_button_pressed(self):
        return self.left_hat_button.get_pressed()

    def set_left_hat_button_pressed(self, value):
        self.left_hat_button.set_pressed(value)

    def get_left_hat_button_double_tap_timing(self):
        return self.left_hat_button.get_double_tap_timing()

    def set_left_hat_button_double_tap_timing(self, value):
        self.left_hat_button.set_double_tap_timing(value)

    def set_right_hat_button_double_tapped(self, value):
        self.right_hat_button.set_double_tapped(value)

    def get_right_hat_button_double_tapped(self):
        return self.right_hat_button.get_double_tapped()

    def get_right_hat_button_last_tap_time(self):
        return self.right_hat_button.get_last_tap_time()

    def set_right_hat_button_last_tap_time(self, value):
        self.right_hat_button.set_last_tap_time(value)

    def get_right_hat_button_pressed(self):
        return self.right_hat_button.get_pressed()

    def set_right_hat_button_pressed(self, value):
        self.right_hat_button.set_pressed(value)

    def get_right_hat_button_double_tap_timing(self):
        return self.right_hat_button.get_double_tap_timing()

    def set_right_hat_button_double_tap_timing(self, value):
        self.right_hat_button.set_double_tap_timing(value)

    def get_instance_id(self):
        return self._joy.get_instance_id()

    def get_guid(self):
        return self._joy.get_guid()

    def get_power_level(self):
        return self._joy.get_power_level()

    def get_name(self):
        return self._joy.get_name()

    def get_number_of_axes(self):
        return self._joy.get_numaxes()

    def get_number_of_balls(self):
        return self._joy.get_numballs()

    def get_number_of_buttons(self):
        return self._joy.get_numbuttons()

    def get_number_of_hats(self):
        return self._joy.get_numhats()

    def start_rumble(self, strong_rumble, weak_rumble, duration):
        if weak_rumble > 0:
            log_development("You are asking the controller to perform a \
weak rumble. Note that some controllers only support the strong rumble and \
in such events, setting the weak rumble value has no effect. Unfortunately \
its not possible to determine if the associated controller has support for \
weak rumble at the moment.")

        result = self._joy.rumble(strong_rumble, weak_rumble, duration)

        if result is False:
            log_development("This controller does not support strong or weak rumbling.")

        return result

    def stop_rumble(self):
        return self._joy.stop_rumble()