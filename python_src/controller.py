import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

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

    def get_instance_id(self):
        return self._joy.get_instance_id()

    def get_guid():
        return _pygame.joystick.Joystick.get_guid()

    def get_power_level(self):
        return self._joy.get_power_level()

    def get_name(self):
        return self._joy.get_name()

    def get_number_of_axes(self):
        return self._joy.get_numaxes()

    def get_axis(self, axis_num): #####################
        return self._joy.get_axis(axis_num)

    def get_number_of_balls(self):
        return self._joy.get_numballs()

    def get_ball(self, ball_num): ####################
        return self._joy.get_ball(ball_num)

    def get_number_of_buttons(self):
        return self._joy.get_numbuttons()

    def get_number_of_hats(self):
        return self._joy.get_numhats()

    def get_hat(self, hat_num): #######################
        return self._joy.get_hat(hat_num)

    def start_rumble(self, strong_rumble, weak_rumble, duration):
        if weak_rumble > 0:
            log_development("You are asking the controller to perform a weak rumble. Note that some controllers only support the strong rumble and in such events, setting the weak rumble value has no effect. Unfortunately its not possible to determine if the associated controller has support for weak rumble at the moment.")
        result = self._joy.rumble(strong_rumble, weak_rumble, duration)

        if result is False:
            log_development("This controller does not support strong or weak rumbling.")

        return result

    def stop_rumble(self):
        return self._joy.stop_rumble()