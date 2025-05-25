from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class Transition:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._time__module = _ModuleManager.import_module("time")

        self._numpy__module = _ModuleManager.import_module("numpy")

        self._transition_utils__module = _ModuleManager.import_module("pmma.python_src.utility.transition_utils")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._animation_start = None
        self._animation_end = None
        self._animation_type = None
        self._animation_mode = None
        self._animation_object = None
        self._animation_running = False
        self._transition_id = id(self)
        self._animation_start_time = None
        self._animation_duration = None
        self._animation_end_time = None
        self._animation_current_position = None
        self._animation_max_speed = None
        self._animation_acceleration_time = None
        self._animation_deceleration_time = None
        self._animation_object_name = None

        self._logger = self._logging_utils__module.InternalLogger()

        if not _InternalConstants.TRANSITION_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.TRANSITION_MANAGER_OBJECT)
            self._transition_utils__module.TransitionManager()

        self._transition_manager = _Registry.pmma_module_spine[_InternalConstants.TRANSITION_MANAGER_OBJECT]
        self._transition_manager.add(self._transition_id, self)

    def create(self, transition_type, start, end, duration, transition_mode=_Constants.LINEAR_TRANSITION, object=None, object_attribute_name=None, max_speed=None, acceleration_time=None, deceleration_time=None):
        """
        🟩 **R** -
        """
        if type(start) == self._numpy__module.ndarray:
            start = start.tolist()

        if type(end) == self._numpy__module.ndarray:
            end = end.tolist()

        self._animation_object = object
        self._animation_type = transition_type
        self._animation_start = start
        self._animation_end = end
        self._animation_mode = transition_mode
        self._animation_duration = duration
        self._animation_current_position = self._animation_start
        self._animation_max_speed = max_speed
        self._animation_acceleration_time = acceleration_time
        self._animation_deceleration_time = deceleration_time
        self._animation_object_name = object_attribute_name

    def get_acceleration_time(self):
        """
        🟩 **R** -
        """
        return self._animation_acceleration_time

    def get_deceleration_time(self):
        """
        🟩 **R** -
        """
        return self._animation_deceleration_time

    def get_max_speed(self):
        """
        🟩 **R** -
        """
        return self._animation_max_speed

    def set_animation_running(self, value):
        """
        🟩 **R** -
        """
        self._animation_running = value

    def get_start_time(self):
        """
        🟩 **R** -
        """
        return self._animation_start_time

    def get_end_time(self):
        """
        🟩 **R** -
        """
        return self._animation_end_time

    def get_start(self):
        """
        🟩 **R** -
        """
        return self._animation_start

    def get_end(self):
        """
        🟩 **R** -
        """
        return self._animation_end

    def get_object(self):
        """
        🟩 **R** -
        """
        return self._animation_object

    def get_type(self):
        """
        🟩 **R** -
        """
        return self._animation_type

    def get_mode(self):
        """
        🟩 **R** -
        """
        return self._animation_mode

    def get_duration(self):
        """
        🟩 **R** -
        """
        return self._animation_duration

    def get_animated_value(self):
        """
        🟩 **R** -
        """
        return self._animation_current_position

    def get_animation_running(self):
        """
        🟩 **R** -
        """
        return self._animation_running

    def set_current_position(self, value):
        """
        🟩 **R** -
        """
        if self._animation_object is not None:
            if self._animation_object_name is not None:
                try:
                    getattr(self._animation_object, self._animation_object_name)
                    setattr(self._animation_object, self._animation_object_name, value)
                except:
                    self._logger.log_development("You need to check what object attribute \
you are attempting to set your transition result too, because it appears that, that \
specific attribute doesn't already exist in that class. It is important that you \
specify the class attribute upon its definition as this can otherwise cause \
unexpected problems later on.")
        self._animation_current_position = value

    def set_current_value(self, value):
        """
        🟩 **R** -
        """
        self.set_current_position(value)

    def get_current_position(self):
        """
        🟩 **R** -
        """
        self._logger.log_development("Did you know that you can directly modify \
instantiated object attributes by specifying the object and attribute name when \
creating your transition?")
        return self._animation_current_position

    def get_current_value(self):
        """
        🟩 **R** -
        """
        return self.get_current_position()

    def pause(self): # test this behavior
        """
        🟩 **R** -
        """
        now_time = self._time__module.perf_counter()
        self._animation_duration -= (now_time - self._animation_start_time)
        self._animation_running = False

    def resume(self): # test this behavior
        """
        🟩 **R** -
        """
        self._animation_start_time = self._time__module.perf_counter()
        self._animation_end_time = self._animation_start_time + self._animation_duration
        self._animation_running = True

    def start(self):
        """
        🟩 **R** -
        """
        self._animation_start_time = self._time__module.perf_counter()
        self._animation_end_time = self._animation_start_time + self._animation_duration
        self._animation_running = True

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._transition_manager.remove(self._transition_id)

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True