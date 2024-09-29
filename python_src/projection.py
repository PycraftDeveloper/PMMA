import numpy as _numpy
import gc as _gc

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import AngleConverter as _AngleConverter

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class PredefinedProjections:
    def __init__(self):
        _initialize(self)

        self._projections_intermediary = _Registry.pmma_module_spine[_Constants.PROJECTION_INTERMEDIARY_OBJECT]

    def get_orthographic_projection(self):
        return self._projections_intermediary.get_orthographic_projection()

    def get_perspective_projection(self):
        return self._projections_intermediary.get_perspective_projection()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class PerspectiveProjection:
    def __init__(self, fov, aspect_ratio, near, far, fov_format=_Constants.DEGREES):
        _initialize(self)

        if type(fov) is not _AngleConverter:
            fov = _AngleConverter()
            fov.set_angle(fov, format=fov_format)

        self._fov = fov
        self._aspect_ratio = aspect_ratio
        self._near = near
        self._far = far

        self._projection_changed = True
        self._projection = None

    def get_fov(self, format=_Constants.DEGREES):
        return self._fov.get_angle(format=format)

    def set_fov(self, fov, format=_Constants.DEGREES):
        self._projection_changed = True
        if type(fov) is not _AngleConverter:
            fov = _AngleConverter(fov, format)
        self._fov = fov

    def get_aspect_ratio(self):
        return self._aspect_ratio

    def set_aspect_ratio(self, aspect_ratio):
        self._projection_changed = True
        self._aspect_ratio = aspect_ratio

    def get_near(self):
        return self._near

    def set_near(self, near):
        self._projection_changed = True
        self._near = near

    def get_far(self):
        return self._far

    def set_far(self, far):
        self._projection_changed = True
        self._far = far

    def get_projection_matrix(self):
        if self._projection is None or self._projection_changed is True:
            self._projection_changed = False
            f = 1.0 / _numpy.tan(self._fov.get_angle(format=_Constants.RADIANS) / 2)
            self._projection = _numpy.array([
                [f / self._aspect_ratio, 0,  0,  0],
                [0, f,  0,  0],
                [0, 0,  (self._far + self._near) / (self._near - self._far), (2 * self._far * self._near) / (self._near - self._far)],
                [0, 0, -1,  0]
            ], dtype=_numpy.float32)
        return self._projection

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class OrthographicProjection:
    def __init__(self, min_x_size, max_x_size, max_y_size, min_y_size, near, far):
        _initialize(self)

        self._min_x_size = min_x_size
        self._max_x_size = max_x_size
        self._max_y_size = max_y_size
        self._min_y_size = min_y_size
        self._near = near
        self._far = far

        self._projection_changed = True
        self._projection = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_minimum_x_size(self, min_x_size):
        self._projection_changed = True
        self._min_x_size = min_x_size

    def get_minimum_x_size(self):
        return self._min_x_size

    def set_maximum_x_size(self, max_x_size):
        self._projection_changed = True
        self._max_x_size = max_x_size

    def get_maximum_x_size(self):
        return self._max_x_size

    def set_maximum_y_size(self, max_y_size):
        self._projection_changed = True
        self._max_y_size = max_y_size

    def get_maximum_y_size(self):
        return self._max_y_size

    def set_minimum_y_size(self, min_y_size):
        self._projection_changed = True
        self._min_y_size = min_y_size

    def get_minimum_y_size(self):
        return self._min_y_size

    def set_near(self, near):
        self._projection_changed = True
        self._near = near

    def get_near(self):
        return self._near

    def set_far(self, far):
        self._projection_changed = True
        self._far = far

    def get_far(self):
        return self._far

    def get_projection_matrix(self):
        if self._projection is None or self._projection_changed is True:
            self._projection_changed = False
            self._projection = _numpy.array([
                [2 / (self._max_x_size - self._min_x_size), 0, 0, -(self._max_x_size + self._min_x_size) / (self._max_x_size - self._min_x_size)],
                [0, 2 / (self._min_y_size - self._max_y_size), 0, -(self._min_y_size + self._max_y_size) / (self._min_y_size - self._max_y_size)],
                [0, 0, -2 / (self._far - self._near), -(self._far + self._near) / (self._far - self._near)],
                [0, 0, 0, 1]
            ], dtype='float32')

        return self._projection