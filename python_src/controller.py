import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

import pmma.python_src.utility.event_utils as _event_utils

class Controllers:
    def __init__(self):
        self._controllers = []
        for joy_num in range(_pygame.joystick.get_count()):
            self._controllers.append(_Controller(joy_num))

class _Controller:
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