from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Controllers:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CONTROLLER_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.CONTROLLER_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.controller_utils import ControllersIntermediary as _ControllersIntermediary
            _ControllersIntermediary()

        self._controller_intermediary = _Registry.pmma_module_spine[_InternalConstants.CONTROLLER_INTERMEDIARY_OBJECT]

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def identify_controllers(self):
        """
        🟩 **R** -
        """
        self._controller_intermediary.identify_controllers()

    def get_controller(self, controller_index) -> 'Controller':
        """
        🟩 **R** -
        """
        return self._controller_intermediary.get_controller(controller_index)

    def update_controllers(self):
        """
        🟩 **R** -
        """
        self._controller_intermediary.update_controllers()

    def list_controllers(self):
        """
        🟩 **R** -
        """
        return self._controller_intermediary.list_controllers()

class Controller:
    """
    🟩 **R** -
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self, joy_num):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._pygame__module = _ModuleManager.import_module("pygame")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._event_utils__module = _ModuleManager.import_module("pmma.python_src.utility.event_utils")

        self._joy_num = joy_num
        self._joy = self._pygame__module.joystick.Joystick(joy_num)
        self._joy.init()

        self._y_button = self._event_utils__module.Y_BUTTON()
        self._b_button = self._event_utils__module.B_BUTTON()
        self._a_button = self._event_utils__module.A_BUTTON()
        self._x_button = self._event_utils__module.X_BUTTON()
        self._home_button = self._event_utils__module.Home_BUTTON()
        self._right_joystick_button = self._event_utils__module.RightJoystick_BUTTON()
        self._left_joystick_button = self._event_utils__module.LeftJoystick_BUTTON()
        self._options_button = self._event_utils__module.Options_BUTTON()
        self._share_button = self._event_utils__module.Share_BUTTON()
        self._right_trigger = self._event_utils__module.Right_TRIGGER()
        self._left_trigger = self._event_utils__module.Left_TRIGGER()
        self._right_bumper = self._event_utils__module.Right_BUMPER()
        self._left_bumper = self._event_utils__module.Left_BUMPER()
        self._center_button = self._event_utils__module.Center_BUTTON()
        self._left_joystick_axis = self._event_utils__module.LeftJoystick_AXIS()
        self._right_joystick_axis = self._event_utils__module.RightJoystick_AXIS()
        self._up_hat_button = self._event_utils__module.UpHat_BUTTON()
        self._down_hat_button = self._event_utils__module.DownHat_BUTTON()
        self._left_hat_button = self._event_utils__module.LeftHat_BUTTON()
        self._right_hat_button = self._event_utils__module.RightHat_BUTTON()

        self._track_balls = []
        for instance in range(self._joy.get_numballs()):
            track_ball = self._event_utils__module.Track_BALL()
            track_ball.set_id(instance)
            self._track_balls.append(track_ball)

        self._logger = self._logging_utils__module.InternalLogger()

    def get_track_ball_from_id(self, id):
        """
        🟩 **R** -
        """
        return self._track_balls[id]

    def set_y_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._y_button.set_double_tapped(value)

    def get_y_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._y_button.get_double_tapped()

    def get_y_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._y_button.get_last_tap_time()

    def set_y_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._y_button.set_last_tap_time(value)

    def get_y_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._y_button.get_pressed()

    def set_y_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._y_button.set_pressed(value)

    def get_y_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._y_button.get_double_tap_timing()

    def set_y_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._y_button.set_double_tap_timing(value)

    def set_b_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._b_button.set_double_tapped(value)

    def get_b_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._b_button.get_double_tapped()

    def get_b_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._b_button.get_last_tap_time()

    def set_b_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._b_button.set_last_tap_time(value)

    def get_b_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._b_button.get_pressed()

    def set_b_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._b_button.set_pressed(value)

    def get_b_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._b_button.get_double_tap_timing()

    def set_b_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._b_button.set_double_tap_timing(value)

    def set_a_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._a_button.set_double_tapped(value)

    def get_a_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._a_button.get_double_tapped()

    def get_a_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._a_button.get_last_tap_time()

    def set_a_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._a_button.set_last_tap_time(value)

    def get_a_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._a_button.get_pressed()

    def set_a_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._a_button.set_pressed(value)

    def get_a_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._a_button.get_double_tap_timing()

    def set_a_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._a_button.set_double_tap_timing(value)

    def set_x_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._x_button.set_double_tapped(value)

    def get_x_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._x_button.get_double_tapped()

    def get_x_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._x_button.get_last_tap_time()

    def set_x_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._x_button.set_last_tap_time(value)

    def get_x_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._x_button.get_pressed()

    def set_x_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._x_button.set_pressed(value)

    def get_x_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._x_button.get_double_tap_timing()

    def set_x_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._x_button.set_double_tap_timing(value)

    def set_home_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._home_button.set_double_tapped(value)

    def get_home_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._home_button.get_double_tapped()

    def get_home_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._home_button.get_last_tap_time()

    def set_home_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._home_button.set_last_tap_time(value)

    def get_home_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._home_button.get_pressed()

    def set_home_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._home_button.set_pressed(value)

    def get_home_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._home_button.get_double_tap_timing()

    def set_home_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._home_button.set_double_tap_timing(value)

    def set_right_joystick_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._right_joystick_button.set_double_tapped(value)

    def get_right_joystick_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._right_joystick_button.get_double_tapped()

    def get_right_joystick_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._right_joystick_button.get_last_tap_time()

    def set_right_joystick_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._right_joystick_button.set_last_tap_time(value)

    def get_right_joystick_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._right_joystick_button.get_pressed()

    def set_right_joystick_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._right_joystick_button.set_pressed(value)

    def get_right_joystick_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._right_joystick_button.get_double_tap_timing()

    def set_right_joystick_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._right_joystick_button.set_double_tap_timing(value)

    def set_left_joystick_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._left_joystick_button.set_double_tapped(value)

    def get_left_joystick_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._left_joystick_button.get_double_tapped()

    def get_left_joystick_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._left_joystick_button.get_last_tap_time()

    def set_left_joystick_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._left_joystick_button.set_last_tap_time(value)

    def get_left_joystick_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._left_joystick_button.get_pressed()

    def set_left_joystick_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._left_joystick_button.set_pressed(value)

    def get_left_joystick_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._left_joystick_button.get_double_tap_timing()

    def set_left_joystick_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._left_joystick_button.set_double_tap_timing(value)

    def set_options_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._options_button.set_double_tapped(value)

    def get_options_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._options_button.get_double_tapped()

    def get_options_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._options_button.get_last_tap_time()

    def set_options_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._options_button.set_last_tap_time(value)

    def get_options_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._options_button.get_pressed()

    def set_options_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._options_button.set_pressed(value)

    def get_options_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._options_button.get_double_tap_timing()

    def set_options_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._options_button.set_double_tap_timing(value)

    def set_share_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._share_button.set_double_tapped(value)

    def get_share_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._share_button.get_double_tapped()

    def get_share_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._share_button.get_last_tap_time()

    def set_share_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._share_button.set_last_tap_time(value)

    def get_share_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._share_button.get_pressed()

    def set_share_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._share_button.set_pressed(value)

    def get_share_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._share_button.get_double_tap_timing()

    def set_share_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._share_button.set_double_tap_timing(value)

    def get_left_trigger_value(self):
        """
        🟩 **R** -
        """
        return self._left_trigger.get_value()

    def set_left_trigger_value(self, value):
        """
        🟩 **R** -
        """
        self._left_trigger.set_value(value)

    def get_right_trigger_value(self):
        """
        🟩 **R** -
        """
        return self._right_trigger.get_value()

    def set_right_trigger_value(self, value):
        """
        🟩 **R** -
        """
        self._right_trigger.set_value(value)

    def set_right_bumper_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._right_bumper.set_double_tapped(value)

    def get_right_bumper_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._right_bumper.get_double_tapped()

    def get_right_bumper_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._right_bumper.get_last_tap_time()

    def set_right_bumper_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._right_bumper.set_last_tap_time(value)

    def get_right_bumper_pressed(self):
        """
        🟩 **R** -
        """
        return self._right_bumper.get_pressed()

    def set_right_bumper_pressed(self, value):
        """
        🟩 **R** -
        """
        self._right_bumper.set_pressed(value)

    def get_right_bumper_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._right_bumper.get_double_tap_timing()

    def set_right_bumper_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._right_bumper.set_double_tap_timing(value)

    def set_left_bumper_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._left_bumper.set_double_tapped(value)

    def get_left_bumper_double_tapped(self):
        return self._left_bumper.get_double_tapped()

    def get_left_bumper_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._left_bumper.get_last_tap_time()

    def set_left_bumper_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._left_bumper.set_last_tap_time(value)

    def get_left_bumper_pressed(self):
        """
        🟩 **R** -
        """
        return self._left_bumper.get_pressed()

    def set_left_bumper_pressed(self, value):
        """
        🟩 **R** -
        """
        self._left_bumper.set_pressed(value)

    def get_left_bumper_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._left_bumper.get_double_tap_timing()

    def set_left_bumper_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._left_bumper.set_double_tap_timing(value)

    def set_center_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._center_button.set_double_tapped(value)

    def get_center_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._center_button.get_double_tapped()

    def get_center_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._center_button.get_last_tap_time()

    def set_center_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._center_button.set_last_tap_time(value)

    def get_center_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._center_button.get_pressed()

    def set_center_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._center_button.set_pressed(value)

    def get_center_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._center_button.get_double_tap_timing()

    def set_center_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._center_button.set_double_tap_timing(value)

    def get_left_joystick_axis_x_axis(self):
        """
        🟩 **R** -
        """
        return self._left_joystick_axis.get_x_axis()

    def get_left_joystick_axis_y_axis(self):
        """
        🟩 **R** -
        """
        return self._left_joystick_axis.get_y_axis()

    def set_left_joystick_axis_x_axis(self, value):
        """
        🟩 **R** -
        """
        self._left_joystick_axis.set_x_axis(value)

    def set_left_joystick_axis_y_axis(self, value):
        """
        🟩 **R** -
        """
        self._left_joystick_axis.set_y_axis(value)

    def get_right_joystick_axis_x_axis(self):
        """
        🟩 **R** -
        """
        return self._right_joystick_axis.get_x_axis()

    def get_right_joystick_axis_y_axis(self):
        """
        🟩 **R** -
        """
        return self._right_joystick_axis.get_y_axis()

    def set_right_joystick_axis_x_axis(self, value):
        """
        🟩 **R** -
        """
        self._right_joystick_axis.set_x_axis(value)

    def set_right_joystick_axis_y_axis(self, value):
        """
        🟩 **R** -
        """
        self._right_joystick_axis.set_y_axis(value)

    def set_up_hat_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._up_hat_button.set_double_tapped(value)

    def get_up_hat_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._up_hat_button.get_double_tapped()

    def get_up_hat_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._up_hat_button.get_last_tap_time()

    def set_up_hat_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._up_hat_button.set_last_tap_time(value)

    def get_up_hat_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._up_hat_button.get_pressed()

    def set_up_hat_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._up_hat_button.set_pressed(value)

    def get_up_hat_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._up_hat_button.get_double_tap_timing()

    def set_up_hat_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._up_hat_button.set_double_tap_timing(value)

    def set_down_hat_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._down_hat_button.set_double_tapped(value)

    def get_down_hat_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._down_hat_button.get_double_tapped()

    def get_down_hat_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._down_hat_button.get_last_tap_time()

    def set_down_hat_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._down_hat_button.set_last_tap_time(value)

    def get_down_hat_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._down_hat_button.get_pressed()

    def set_down_hat_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._down_hat_button.set_pressed(value)

    def get_down_hat_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._down_hat_button.get_double_tap_timing()

    def set_down_hat_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._down_hat_button.set_double_tap_timing(value)

    def set_left_hat_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._left_hat_button.set_double_tapped(value)

    def get_left_hat_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._left_hat_button.get_double_tapped()

    def get_left_hat_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._left_hat_button.get_last_tap_time()

    def set_left_hat_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._left_hat_button.set_last_tap_time(value)

    def get_left_hat_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._left_hat_button.get_pressed()

    def set_left_hat_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._left_hat_button.set_pressed(value)

    def get_left_hat_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._left_hat_button.get_double_tap_timing()

    def set_left_hat_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._left_hat_button.set_double_tap_timing(value)

    def set_right_hat_button_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._right_hat_button.set_double_tapped(value)

    def get_right_hat_button_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._right_hat_button.get_double_tapped()

    def get_right_hat_button_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._right_hat_button.get_last_tap_time()

    def set_right_hat_button_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._right_hat_button.set_last_tap_time(value)

    def get_right_hat_button_pressed(self):
        """
        🟩 **R** -
        """
        return self._right_hat_button.get_pressed()

    def set_right_hat_button_pressed(self, value):
        """
        🟩 **R** -
        """
        self._right_hat_button.set_pressed(value)

    def get_right_hat_button_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._right_hat_button.get_double_tap_timing()

    def set_right_hat_button_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._right_hat_button.set_double_tap_timing(value)

    def get_instance_id(self):
        """
        🟩 **R** -
        """
        return self._joy.get_instance_id()

    def get_guid(self):
        """
        🟩 **R** -
        """
        return self._joy.get_guid()

    def get_power_level(self):
        """
        🟩 **R** -
        """
        return self._joy.get_power_level()

    def get_name(self):
        """
        🟩 **R** -
        """
        return self._joy.get_name()

    def get_number_of_axes(self):
        """
        🟩 **R** -
        """
        return self._joy.get_numaxes()

    def get_number_of_balls(self):
        """
        🟩 **R** -
        """
        return self._joy.get_numballs()

    def get_number_of_buttons(self):
        """
        🟩 **R** -
        """
        return self._joy.get_numbuttons()

    def get_number_of_hats(self):
        """
        🟩 **R** -
        """
        return self._joy.get_numhats()

    def start_rumble(self, strong_rumble, weak_rumble, duration):
        """
        🟩 **R** -
        """
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
        """
        🟩 **R** -
        """
        return self._joy.stop_rumble()