import threading as _threading
import gc as _gc
import time as _time

import waiting as _waiting
import numpy as _numpy

from pmma.python_src.constants import Constants
#from pmma.python_src.transitions import Transition as _Transition

from pmma.python_src.utility.general_utils import initialize as _initialize

class TransitionManager:
    def __init__(self):
        _initialize(
            self,
            unique_instance=Constants.TRANSITION_MANAGER_OBJECT,
            add_to_pmma_module_spine=True)

        self._transitions = {}

        self._transition_manager = _threading.Thread(target=self._manage_transitions)
        self._transition_manager.daemon = True
        self._transition_manager.name = "TransitionManager:Manage_Transitions_Thread"
        self._transition_manager.start()

        self._enable_transition_management = True

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._enable_transition_management = False

            self._transition_manager.join()

            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _wait_for_transitions(self):
        return len(self._transitions) != 0 or self._enable_transition_management is False

    def add(self, key, transition):
        self._transitions[key] = transition

    def remove(self, key):
        del self._transitions[key]

    def _manage_transitions(self):
        while self._enable_transition_management:
            _waiting.wait(self._wait_for_transitions)
            if len(self._transitions) == 0:
                continue
            pass
            for key in self._transitions:
                transition: "_Transition" = self._transitions[key]
                if transition._animation_running:
                    if transition._animation_mode == Constants.LINEAR_TRANSITION:
                        if transition._animation_type == Constants.COORDINATE_TRANSITION:
                            np_start = _numpy.array(transition._animation_start)
                            np_end = _numpy.array(transition._animation_end)
                            difference = _numpy.absolute(np_start - np_end)
                            current_run_duration = _time.perf_counter() - transition._animation_start_time
                            transition_duration = transition._animation_duration
                            result = difference * (current_run_duration / transition_duration) + np_start
                            if current_run_duration >= transition_duration:
                                transition._animation_running = False
                                transition._animation_current_position = transition._animation_end
                            else:
                                transition._animation_current_position = result.tolist()