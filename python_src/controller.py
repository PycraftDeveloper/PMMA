from gc import collect as _gc__collect

import pygame as _pygame

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
import pmma.python_src.utility.event_utils as _event_utils
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class Controllers:
    def __init__(self):
        _initialize(self)

        if not _Constants.CONTROLLER_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CONTROLLER_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.controller_utils import ControllersIntermediary as _ControllersIntermediary
            _ControllersIntermediary()

        self._controller_intermediary = _Registry.pmma_module_spine[_Constants.CONTROLLER_INTERMEDIARY_OBJECT]

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def identify_controllers(self):
        self._controller_intermediary.identify_controllers()

    def get_controller(self, controller_index) -> 'Controller':
        return self._controller_intermediary.get_controller(controller_index)

    def update_controllers(self):
        self._controller_intermediary.update_controllers()

    def list_controllers(self):
        return self._controller_intermediary.list_controllers()

class Controller:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self, joy_num):
        _initialize(self)

        self._joy_num = joy_num
        self._joy = _pygame.joystick.Joystick(joy_num)
        self._joy.init()

        self._y_button = _event_utils.Y_BUTTON()
        self._b_button = _event_utils.B_BUTTON()
        self._a_button = _event_utils.A_BUTTON()
        self._x_button = _event_utils.X_BUTTON()
        self._home_button = _event_utils.Home_BUTTON()
        self._right_joystick_button = _event_utils.RightJoystick_BUTTON()
        self._left_joystick_button = _event_utils.LeftJoystick_BUTTON()
        self._options_button = _event_utils.Options_BUTTON()
        self._share_button = _event_utils.Share_BUTTON()
        self._right_trigger = _event_utils.Right_TRIGGER()
        self._left_trigger = _event_utils.Left_TRIGGER()
        self._right_bumper = _event_utils.Right_BUMPER()
        self._left_bumper = _event_utils.Left_BUMPER()
        self._center_button = _event_utils.Center_BUTTON()
        self._left_joystick_axis = _event_utils.LeftJoystick_AXIS()
        self._right_joystick_axis = _event_utils.RightJoystick_AXIS()
        self._up_hat_button = _event_utils.UpHat_BUTTON()
        self._down_hat_button = _event_utils.DownHat_BUTTON()
        self._left_hat_button = _event_utils.LeftHat_BUTTON()
        self._right_hat_button = _event_utils.RightHat_BUTTON()

        self._track_balls = []
        for instance in range(self._joy.get_numballs()):
            track_ball = _event_utils.Track_BALL()
            track_ball.set_id(instance)
            self._track_balls.append(track_ball)

        self._logger = _InternalLogger()

    def get_track_ball_from_id(self, id) -> '_event_utils.Track_BALL':
        return self._track_balls[id]

    def set_y_button_double_tapped(self, value):
        self._y_button.set_double_tapped(value)

    def get_y_button_double_tapped(self):
        return self._y_button.get_double_tapped()

    def get_y_button_last_tap_time(self):
        return self._y_button.get_last_tap_time()

    def set_y_button_last_tap_time(self, value):
        self._y_button.set_last_tap_time(value)

    def get_y_button_pressed(self):
        return self._y_button.get_pressed()

    def set_y_button_pressed(self, value):
        self._y_button.set_pressed(value)

    def get_y_button_double_tap_timing(self):
        return self._y_button.get_double_tap_timing()

    def set_y_button_double_tap_timing(self, value):
        self._y_button.set_double_tap_timing(value)

    def set_b_button_double_tapped(self, value):
        self._b_button.set_double_tapped(value)

    def get_b_button_double_tapped(self):
        return self._b_button.get_double_tapped()

    def get_b_button_last_tap_time(self):
        return self._b_button.get_last_tap_time()

    def set_b_button_last_tap_time(self, value):
        self._b_button.set_last_tap_time(value)

    def get_b_button_pressed(self):
        return self._b_button.get_pressed()

    def set_b_button_pressed(self, value):
        self._b_button.set_pressed(value)

    def get_b_button_double_tap_timing(self):
        return self._b_button.get_double_tap_timing()

    def set_b_button_double_tap_timing(self, value):
        self._b_button.set_double_tap_timing(value)

    def set_a_button_double_tapped(self, value):
        self._a_button.set_double_tapped(value)

    def get_a_button_double_tapped(self):
        return self._a_button.get_double_tapped()

    def get_a_button_last_tap_time(self):
        return self._a_button.get_last_tap_time()

    def set_a_button_last_tap_time(self, value):
        self._a_button.set_last_tap_time(value)

    def get_a_button_pressed(self):
        return self._a_button.get_pressed()

    def set_a_button_pressed(self, value):
        self._a_button.set_pressed(value)

    def get_a_button_double_tap_timing(self):
        return self._a_button.get_double_tap_timing()

    def set_a_button_double_tap_timing(self, value):
        self._a_button.set_double_tap_timing(value)

    def set_x_button_double_tapped(self, value):
        self._x_button.set_double_tapped(value)

    def get_x_button_double_tapped(self):
        return self._x_button.get_double_tapped()

    def get_x_button_last_tap_time(self):
        return self._x_button.get_last_tap_time()

    def set_x_button_last_tap_time(self, value):
        self._x_button.set_last_tap_time(value)

    def get_x_button_pressed(self):
        return self._x_button.get_pressed()

    def set_x_button_pressed(self, value):
        self._x_button.set_pressed(value)

    def get_x_button_double_tap_timing(self):
        return self._x_button.get_double_tap_timing()

    def set_x_button_double_tap_timing(self, value):
        self._x_button.set_double_tap_timing(value)

    def set_home_button_double_tapped(self, value):
        self._home_button.set_double_tapped(value)

    def get_home_button_double_tapped(self):
        return self._home_button.get_double_tapped()

    def get_home_button_last_tap_time(self):
        return self._home_button.get_last_tap_time()

    def set_home_button_last_tap_time(self, value):
        self._home_button.set_last_tap_time(value)

    def get_home_button_pressed(self):
        return self._home_button.get_pressed()

    def set_home_button_pressed(self, value):
        self._home_button.set_pressed(value)

    def get_home_button_double_tap_timing(self):
        return self._home_button.get_double_tap_timing()

    def set_home_button_double_tap_timing(self, value):
        self._home_button.set_double_tap_timing(value)

    def set_right_joystick_button_double_tapped(self, value):
        self._right_joystick_button.set_double_tapped(value)

    def get_right_joystick_button_double_tapped(self):
        return self._right_joystick_button.get_double_tapped()

    def get_right_joystick_button_last_tap_time(self):
        return self._right_joystick_button.get_last_tap_time()

    def set_right_joystick_button_last_tap_time(self, value):
        self._right_joystick_button.set_last_tap_time(value)

    def get_right_joystick_button_pressed(self):
        return self._right_joystick_button.get_pressed()

    def set_right_joystick_button_pressed(self, value):
        self._right_joystick_button.set_pressed(value)

    def get_right_joystick_button_double_tap_timing(self):
        return self._right_joystick_button.get_double_tap_timing()

    def set_right_joystick_button_double_tap_timing(self, value):
        self._right_joystick_button.set_double_tap_timing(value)

    def set_left_joystick_button_double_tapped(self, value):
        self._left_joystick_button.set_double_tapped(value)

    def get_left_joystick_button_double_tapped(self):
        return self._left_joystick_button.get_double_tapped()

    def get_left_joystick_button_last_tap_time(self):
        return self._left_joystick_button.get_last_tap_time()

    def set_left_joystick_button_last_tap_time(self, value):
        self._left_joystick_button.set_last_tap_time(value)

    def get_left_joystick_button_pressed(self):
        return self._left_joystick_button.get_pressed()

    def set_left_joystick_button_pressed(self, value):
        self._left_joystick_button.set_pressed(value)

    def get_left_joystick_button_double_tap_timing(self):
        return self._left_joystick_button.get_double_tap_timing()

    def set_left_joystick_button_double_tap_timing(self, value):
        self._left_joystick_button.set_double_tap_timing(value)

    def set_options_button_double_tapped(self, value):
        self._options_button.set_double_tapped(value)

    def get_options_button_double_tapped(self):
        return self._options_button.get_double_tapped()

    def get_options_button_last_tap_time(self):
        return self._options_button.get_last_tap_time()

    def set_options_button_last_tap_time(self, value):
        self._options_button.set_last_tap_time(value)

    def get_options_button_pressed(self):
        return self._options_button.get_pressed()

    def set_options_button_pressed(self, value):
        self._options_button.set_pressed(value)

    def get_options_button_double_tap_timing(self):
        return self._options_button.get_double_tap_timing()

    def set_options_button_double_tap_timing(self, value):
        self._options_button.set_double_tap_timing(value)

    def set_share_button_double_tapped(self, value):
        self._share_button.set_double_tapped(value)

    def get_share_button_double_tapped(self):
        return self._share_button.get_double_tapped()

    def get_share_button_last_tap_time(self):
        return self._share_button.get_last_tap_time()

    def set_share_button_last_tap_time(self, value):
        self._share_button.set_last_tap_time(value)

    def get_share_button_pressed(self):
        return self._share_button.get_pressed()

    def set_share_button_pressed(self, value):
        self._share_button.set_pressed(value)

    def get_share_button_double_tap_timing(self):
        return self._share_button.get_double_tap_timing()

    def set_share_button_double_tap_timing(self, value):
        self._share_button.set_double_tap_timing(value)

    def get_left_trigger_value(self):
        return self._left_trigger.get_value()

    def set_left_trigger_value(self, value):
        self._left_trigger.set_value(value)

    def get_right_trigger_value(self):
        return self._right_trigger.get_value()

    def set_right_trigger_value(self, value):
        self._right_trigger.set_value(value)

    def set_right_bumper_double_tapped(self, value):
        self._right_bumper.set_double_tapped(value)

    def get_right_bumper_double_tapped(self):
        return self._right_bumper.get_double_tapped()

    def get_right_bumper_last_tap_time(self):
        return self._right_bumper.get_last_tap_time()

    def set_right_bumper_last_tap_time(self, value):
        self._right_bumper.set_last_tap_time(value)

    def get_right_bumper_pressed(self):
        return self._right_bumper.get_pressed()

    def set_right_bumper_pressed(self, value):
        self._right_bumper.set_pressed(value)

    def get_right_bumper_double_tap_timing(self):
        return self._right_bumper.get_double_tap_timing()

    def set_right_bumper_double_tap_timing(self, value):
        self._right_bumper.set_double_tap_timing(value)

    def set_left_bumper_double_tapped(self, value):
        self._left_bumper.set_double_tapped(value)

    def get_left_bumper_double_tapped(self):
        return self._left_bumper.get_double_tapped()

    def get_left_bumper_last_tap_time(self):
        return self._left_bumper.get_last_tap_time()

    def set_left_bumper_last_tap_time(self, value):
        self._left_bumper.set_last_tap_time(value)

    def get_left_bumper_pressed(self):
        return self._left_bumper.get_pressed()

    def set_left_bumper_pressed(self, value):
        self._left_bumper.set_pressed(value)

    def get_left_bumper_double_tap_timing(self):
        return self._left_bumper.get_double_tap_timing()

    def set_left_bumper_double_tap_timing(self, value):
        self._left_bumper.set_double_tap_timing(value)

    def set_center_button_double_tapped(self, value):
        self._center_button.set_double_tapped(value)

    def get_center_button_double_tapped(self):
        return self._center_button.get_double_tapped()

    def get_center_button_last_tap_time(self):
        return self._center_button.get_last_tap_time()

    def set_center_button_last_tap_time(self, value):
        self._center_button.set_last_tap_time(value)

    def get_center_button_pressed(self):
        return self._center_button.get_pressed()

    def set_center_button_pressed(self, value):
        self._center_button.set_pressed(value)

    def get_center_button_double_tap_timing(self):
        return self._center_button.get_double_tap_timing()

    def set_center_button_double_tap_timing(self, value):
        self._center_button.set_double_tap_timing(value)

    def get_left_joystick_axis_x_axis(self):
        return self._left_joystick_axis.get_x_axis()

    def get_left_joystick_axis_y_axis(self):
        return self._left_joystick_axis.get_y_axis()

    def set_left_joystick_axis_x_axis(self, value):
        self._left_joystick_axis.set_x_axis(value)

    def set_left_joystick_axis_y_axis(self, value):
        self._left_joystick_axis.set_y_axis(value)

    def get_right_joystick_axis_x_axis(self):
        return self._right_joystick_axis.get_x_axis()

    def get_right_joystick_axis_y_axis(self):
        return self._right_joystick_axis.get_y_axis()

    def set_right_joystick_axis_x_axis(self, value):
        self._right_joystick_axis.set_x_axis(value)

    def set_right_joystick_axis_y_axis(self, value):
        self._right_joystick_axis.set_y_axis(value)

    def set_up_hat_button_double_tapped(self, value):
        self._up_hat_button.set_double_tapped(value)

    def get_up_hat_button_double_tapped(self):
        return self._up_hat_button.get_double_tapped()

    def get_up_hat_button_last_tap_time(self):
        return self._up_hat_button.get_last_tap_time()

    def set_up_hat_button_last_tap_time(self, value):
        self._up_hat_button.set_last_tap_time(value)

    def get_up_hat_button_pressed(self):
        return self._up_hat_button.get_pressed()

    def set_up_hat_button_pressed(self, value):
        self._up_hat_button.set_pressed(value)

    def get_up_hat_button_double_tap_timing(self):
        return self._up_hat_button.get_double_tap_timing()

    def set_up_hat_button_double_tap_timing(self, value):
        self._up_hat_button.set_double_tap_timing(value)

    def set_down_hat_button_double_tapped(self, value):
        self._down_hat_button.set_double_tapped(value)

    def get_down_hat_button_double_tapped(self):
        return self._down_hat_button.get_double_tapped()

    def get_down_hat_button_last_tap_time(self):
        return self._down_hat_button.get_last_tap_time()

    def set_down_hat_button_last_tap_time(self, value):
        self._down_hat_button.set_last_tap_time(value)

    def get_down_hat_button_pressed(self):
        return self._down_hat_button.get_pressed()

    def set_down_hat_button_pressed(self, value):
        self._down_hat_button.set_pressed(value)

    def get_down_hat_button_double_tap_timing(self):
        return self._down_hat_button.get_double_tap_timing()

    def set_down_hat_button_double_tap_timing(self, value):
        self._down_hat_button.set_double_tap_timing(value)

    def set_left_hat_button_double_tapped(self, value):
        self._left_hat_button.set_double_tapped(value)

    def get_left_hat_button_double_tapped(self):
        return self._left_hat_button.get_double_tapped()

    def get_left_hat_button_last_tap_time(self):
        return self._left_hat_button.get_last_tap_time()

    def set_left_hat_button_last_tap_time(self, value):
        self._left_hat_button.set_last_tap_time(value)

    def get_left_hat_button_pressed(self):
        return self._left_hat_button.get_pressed()

    def set_left_hat_button_pressed(self, value):
        self._left_hat_button.set_pressed(value)

    def get_left_hat_button_double_tap_timing(self):
        return self._left_hat_button.get_double_tap_timing()

    def set_left_hat_button_double_tap_timing(self, value):
        self._left_hat_button.set_double_tap_timing(value)

    def set_right_hat_button_double_tapped(self, value):
        self._right_hat_button.set_double_tapped(value)

    def get_right_hat_button_double_tapped(self):
        return self._right_hat_button.get_double_tapped()

    def get_right_hat_button_last_tap_time(self):
        return self._right_hat_button.get_last_tap_time()

    def set_right_hat_button_last_tap_time(self, value):
        self._right_hat_button.set_last_tap_time(value)

    def get_right_hat_button_pressed(self):
        return self._right_hat_button.get_pressed()

    def set_right_hat_button_pressed(self, value):
        self._right_hat_button.set_pressed(value)

    def get_right_hat_button_double_tap_timing(self):
        return self._right_hat_button.get_double_tap_timing()

    def set_right_hat_button_double_tap_timing(self, value):
        self._right_hat_button.set_double_tap_timing(value)

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
            self._logger.log_development("You are asking the controller to perform a \
weak rumble. Note that some controllers only support the strong rumble and \
in such events, setting the weak rumble value has no effect. Unfortunately \
its not possible to determine if the associated controller has support for \
weak rumble at the moment.")

        result = self._joy.rumble(strong_rumble, weak_rumble, duration)

        if result is False:
            self._logger.log_development("This controller does not support strong or weak rumbling.")

        return result

    def stop_rumble(self):
        return self._joy.stop_rumble()