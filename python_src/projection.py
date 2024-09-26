import numpy as _numpy
import gc as _gc

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class PerspectiveProjection:
    def __init__(self):
        _initialize(self)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class OrthographicProjection:
    def __init__(self, left_aspect_ratio, right_aspect_ratio, bottom_aspect_ratio, top_aspect_ratio, near, far):
        _initialize(self)

        self._left_aspect_ratio = left_aspect_ratio
        self._right_aspect_ratio = right_aspect_ratio
        self._bottom_aspect_ratio = bottom_aspect_ratio
        self._top_aspect_ratio = top_aspect_ratio
        self._near = near
        self._far = far

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_left_aspect_ratio(self, left_aspect_ratio):
        self._left_aspect_ratio = left_aspect_ratio

    def get_left_aspect_ratio(self):
        return self._left_aspect_ratio

    def set_right_aspect_ratio(self, right_aspect_ratio):
        self._right_aspect_ratio = right_aspect_ratio

    def get_right_aspect_ratio(self):
        return self._right_aspect_ratio

    def set_bottom_aspect_ratio(self, bottom_aspect_ratio):
        self._bottom_aspect_ratio = bottom_aspect_ratio

    def get_bottom_aspect_ratio(self):
        return self._bottom_aspect_ratio

    def set_top_aspect_ratio(self, top_aspect_ratio):
        self._top_aspect_ratio = top_aspect_ratio

    def get_top_aspect_ratio(self):
        return self._top_aspect_ratio

    def set_near(self, near):
        self._near = near

    def get_near(self):
        return self._near

    def set_far(self, far):
        self._far = far

    def get_far(self):
        return self._far

    def get_projection_matrix(self):
        return _numpy.array([
            [2 / (self._right_aspect_ratio - self._left_aspect_ratio), 0, 0, -(self._right_aspect_ratio + self._left_aspect_ratio) / (self._right_aspect_ratio - self._left_aspect_ratio)],
            [0, 2 / (self._top_aspect_ratio - self._bottom_aspect_ratio), 0, -(self._top_aspect_ratio + self._bottom_aspect_ratio) / (self._top_aspect_ratio - self._bottom_aspect_ratio)],
            [0, 0, -2 / (self._far - self._near), -(self._far + self._near) / (self._far - self._near)],
            [0, 0, 0, 1]
        ], dtype='float32')