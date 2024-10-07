import threading as _threading
from gc import collect as _gc__collect
import time as _time
import math as _math

import waiting as _waiting
import numpy as _numpy

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.advmath import Math as _Math

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class TransitionManager:
    def __init__(self):
        _initialize(
            self,
            unique_instance=_Constants.TRANSITION_MANAGER_OBJECT,
            add_to_pmma_module_spine=True)

        self._transitions = {}

        self._transition_manager = _threading.Thread(target=self._manage_transitions)
        self._transition_manager.daemon = True
        self._transition_manager.name = "TransitionManager:Manage_Transitions_Thread"

        self._enable_transition_management = True

        self._math = _Math()

        self._transition_manager.start()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._enable_transition_management = False

            self._transition_manager.join()

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _wait_for_transitions(self):
        return len(self._transitions) != 0 or self._enable_transition_management is False

    def add(self, key, transition):
        self._transitions[key] = transition

    def remove(self, key):
        del self._transitions[key]

    def _linear_coordinate_transition(self, transition):
        np_start = _numpy.array(transition.get_start())
        np_end = _numpy.array(transition.get_end())
        difference = _numpy.absolute(np_start - np_end)
        current_run_duration = _time.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()
        result = difference * (current_run_duration / transition_duration) + np_start
        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_position(np_end.tolist())
        else:
            transition.set_current_position(result.tolist())

    def _linear_value_transition(self, transition):
        start = transition.get_start()
        end = transition.get_end()
        difference = abs(start - end)
        current_run_duration = _time.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()
        result = difference * (current_run_duration / transition_duration) + start
        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_value(end)
        else:
            transition.set_current_value(result)

    def _smooth_coordinate_transition(self, transition):
        current_run_duration = _time.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()

        np_start = _numpy.array(transition.get_start())
        np_end = _numpy.array(transition.get_end())
        difference = _numpy.absolute(np_start - np_end)
        normalized_time = current_run_duration / transition_duration
        # Calculate the velocity based on a sine curve between 0 and pi
        sine_velocity = _math.sin((_math.pi / 2) * normalized_time)
        # Position based on velocity integrated over time
        result = np_start + difference * sine_velocity

        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_position(np_end.tolist())
        else:
            transition.set_current_position(result.tolist())

    def _smooth_value_transition(self, transition):
        current_run_duration = _time.perf_counter() - transition.get_start_time()
        transition_duration = transition.get_duration()

        start = _numpy.array(transition.get_start())
        end = _numpy.array(transition.get_end())
        difference = abs(start - end)
        normalized_time = current_run_duration / transition_duration
        # Calculate the velocity based on a sine curve between 0 and pi
        sine_velocity = _math.sin((_math.pi / 2) * normalized_time)
        # Position based on velocity integrated over time
        result = start + difference * sine_velocity

        if current_run_duration >= transition_duration:
            transition.set_animation_running(False)
            transition.set_current_value(end)
        else:
            transition.set_current_value(result)

    def _manage_transitions(self):
        while self._enable_transition_management:
            _waiting.wait(self._wait_for_transitions)
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

            _time.sleep(1 / _Registry.refresh_rate)