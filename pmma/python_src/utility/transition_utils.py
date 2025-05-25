from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class TransitionManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(
            self,
            unique_instance=_InternalConstants.TRANSITION_MANAGER_OBJECT,
            add_to_pmma_module_spine=True)

        self._threading__module = _ModuleManager.import_module("threading")
        self._time__module = _ModuleManager.import_module("time")
        self._math__module = _ModuleManager.import_module("math")

        self._waiting__module = _ModuleManager.import_module("waiting")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._advmath_module = _ModuleManager.import_module("pmma.python_src.advmath")

        self._transitions = {}

        self._transition_manager = self._threading__module.Thread(target=self._manage_transitions)
        self._transition_manager.daemon = True
        self._transition_manager.name = "TransitionManager:Manage_Transitions_Thread"

        self._enable_transition_management = True

        self._math = self._advmath_module.Math()

        self._transition_manager.start()

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._enable_transition_management = False

            self._transition_manager.join()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def _wait_for_transitions(self):
        """
        🟩 **R** -
        """
        return len(self._transitions) != 0 or self._enable_transition_management is False

    def add(self, key, transition):
        """
        🟩 **R** -
        """
        self._transitions[key] = transition

    def remove(self, key):
        """
        🟩 **R** -
        """
        del self._transitions[key]

    def _linear_coordinate_transition(self, transition):
        """
        🟩 **R** -
        """
        np_start = self._numpy__module.array(transition.get_start())
        np_end = self._numpy__module.array(transition.get_end())
        difference = self._numpy__module.absolute(np_start - np_end)
        current_run_duration = self._time__module.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()
        result = difference * (current_run_duration / transition_duration) + np_start
        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_position(np_end.tolist())
        else:
            transition.set_current_position(result.tolist())

    def _linear_value_transition(self, transition):
        """
        🟩 **R** -
        """
        start = transition.get_start()
        end = transition.get_end()
        difference = abs(start - end)
        current_run_duration = self._time__module.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()
        result = difference * (current_run_duration / transition_duration) + start
        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_value(end)
        else:
            transition.set_current_value(result)

    def _smooth_coordinate_transition(self, transition):
        """
        🟩 **R** -
        """
        current_run_duration = self._time__module.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()

        np_start = self._numpy__module.array(transition.get_start())
        np_end = self._numpy__module.array(transition.get_end())
        difference = self._numpy__module.absolute(np_start - np_end)
        normalized_time = current_run_duration / transition_duration
        # Calculate the velocity based on a sine curve between 0 and pi
        sine_velocity = self._math__module.sin((self._math__module.pi / 2) * normalized_time)
        # Position based on velocity integrated over time
        result = np_start + difference * sine_velocity

        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_position(np_end.tolist())
        else:
            transition.set_current_position(result.tolist())

    def _smooth_value_transition(self, transition):
        """
        🟩 **R** -
        """
        current_run_duration = self._time__module._time__perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()

        start = self._numpy__module.array(transition.get_start())
        end = self._numpy__module.array(transition.get_end())
        difference = abs(start - end)
        normalized_time = current_run_duration / transition_duration
        # Calculate the velocity based on a sine curve between 0 and pi
        sine_velocity = self._math__module.sin((self._math__module.pi / 2) * normalized_time)
        # Position based on velocity integrated over time
        result = start + difference * sine_velocity

        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_value(end)
        else:
            transition.set_current_value(result)

    def _manage_transitions(self):
        """
        🟩 **R** -
        """
        while self._enable_transition_management:
            self._waiting__module.wait(self._wait_for_transitions)
            if len(self._transitions) == 0:
                continue
            for key in self._transitions:
                transition = self._transitions[key]
                if transition.get_animation_running():
                    transition_mode = transition.get_mode()
                    transition_type = transition.get_type()
                    if transition_mode == _Constants.LINEAR_TRANSITION:
                        if transition_type == _Constants.COORDINATE_TRANSITION:
                            self._linear_coordinate_transition(
                                transition)
                        elif transition_type == _Constants.VALUE_TRANSITION:
                            self._linear_value_transition(
                                transition)

                    elif transition_mode == _Constants.SMOOTH_TRANSITION:
                        if transition_type == _Constants.COORDINATE_TRANSITION:
                            self._smooth_coordinate_transition(
                                transition)
                        elif transition_type == _Constants.VALUE_TRANSITION:
                            self._smooth_value_transition(
                                transition)

            self._time__module.sleep(1 / _Registry.refresh_rate)