import gc as _gc
import time as _time

import numpy as _numpy

from pmma.python_src.constants import Constants

from pmma.python_src.utility.transition_utils import TransitionManager as _TransitionManager
from pmma.python_src.utility.registry_utils import Registry as _Registry

class Transition:
    def __init__(self):
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
        self._animation_keyword_arguments = None
        self._animation_current_position = None
        self._animation_max_speed = None
        self._animation_acceleration_time = None
        self._animation_deceleration_time = None

        self._transition_manager: "_TransitionManager" = _Registry.pmma_module_spine[Constants.TRANSITION_MANAGER_OBJECT]
        self._transition_manager.add(self._transition_id, self)

    def create(self, transition_type, start, end, duration, transition_mode=Constants.LINEAR_TRANSITION, object=None, max_speed=None, acceleration_time=None, deceleration_time=None, **kwargs):
        if type(start) == _numpy.ndarray:
            start = start.tolist()

        if type(end) == _numpy.ndarray:
            end = end.tolist()

        self._animation_object = object
        self._animation_type = transition_type
        self._animation_start = start
        self._animation_end = end
        self._animation_mode = transition_mode
        self._animation_duration = duration
        self._animation_keyword_arguments = kwargs
        self._animation_current_position = self._animation_start
        self._animation_max_speed = max_speed
        self._animation_acceleration_time = acceleration_time
        self._animation_deceleration_time = deceleration_time

    def get_acceleration_time(self):
        return self._animation_acceleration_time

    def get_deceleration_time(self):
        return self._animation_deceleration_time

    def get_max_speed(self):
        return self._animation_max_speed

    def set_animation_running(self, value):
        self._animation_running = value

    def get_start_time(self):
        return self._animation_start_time

    def get_end_time(self):
        return self._animation_end_time

    def get_start(self):
        return self._animation_start

    def get_end(self):
        return self._animation_end

    def get_object(self):
        return self._animation_object

    def get_type(self):
        return self._animation_type

    def get_mode(self):
        return self._animation_mode

    def get_kwargs(self):
        return self._animation_keyword_arguments

    def get_duration(self):
        return self._animation_duration

    def get_animated_value(self):
        return self._animation_current_position

    def get_animation_running(self):
        return self._animation_running

    def set_current_position(self, value):
        self._animation_current_position = value

    def pause(self): # test this behavior
        now_time = _time.perf_counter()
        self._animation_duration -= (now_time - self._animation_start_time)
        self._animation_running = False

    def resume(self): # test this behavior
        self._animation_start_time = _time.perf_counter()
        self._animation_end_time = self._animation_start_time + self._animation_duration
        self._animation_running = True

    def start(self):
        self._animation_start_time = _time.perf_counter()
        self._animation_end_time = self._animation_start_time + self._animation_duration
        self._animation_running = True

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._transition_manager.remove(self._transition_id)

            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True