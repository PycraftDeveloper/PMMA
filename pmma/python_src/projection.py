from numpy import tan as _numpy__tan
from numpy import array as _numpy__array
from numpy import float32 as _numpy__float32

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import AngleConverter as _AngleConverter

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class PredefinedProjections:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if not _Constants.PROJECTION_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PROJECTION_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.projection_utils import ProjectionIntermediary as _ProjectionIntermediary
            _ProjectionIntermediary()

        self._projections_intermediary = _Registry.pmma_module_spine[_Constants.PROJECTION_INTERMEDIARY_OBJECT]

    def get_orthographic_projection(self):
        """
        🟩 **R** -
        """
        return self._projections_intermediary.get_orthographic_projection()

    def get_perspective_projection(self):
        """
        🟩 **R** -
        """
        return self._projections_intermediary.get_perspective_projection()

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class PerspectiveProjection:
    """
    🟩 **R** -
    """
    def __init__(self, fov, aspect_ratio, near, far, fov_format=_Constants.DEGREES):
        """
        🟩 **R** -
        """
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
        """
        🟩 **R** -
        """
        return self._fov.get_angle(format=format)

    def set_fov(self, fov, format=_Constants.DEGREES):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        if type(fov) is not _AngleConverter:
            fov = _AngleConverter(fov, format)
        self._fov = fov

    def get_aspect_ratio(self):
        """
        🟩 **R** -
        """
        return self._aspect_ratio

    def set_aspect_ratio(self, aspect_ratio):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._aspect_ratio = aspect_ratio

    def get_near(self):
        """
        🟩 **R** -
        """
        return self._near

    def set_near(self, near):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._near = near

    def get_far(self):
        """
        🟩 **R** -
        """
        return self._far

    def set_far(self, far):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._far = far

    def get_projection_matrix(self):
        """
        🟩 **R** -
        """
        if self._projection is None or self._projection_changed is True:
            self._projection_changed = False
            f = 1.0 / _numpy__tan(self._fov.get_angle(format=_Constants.RADIANS) / 2)
            self._projection = _numpy__array([
                [f / self._aspect_ratio, 0,  0,  0],
                [0, f,  0,  0],
                [0, 0,  (self._far + self._near) / (self._near - self._far), (2 * self._far * self._near) / (self._near - self._far)],
                [0, 0, -1,  0]
            ], dtype=_numpy__float32)
        return self._projection

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

class OrthographicProjection:
    """
    🟩 **R** -
    """
    def __init__(self, min_x_size, max_x_size, max_y_size, min_y_size, near, far):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._min_x_size = min_x_size
        self._max_x_size = max_x_size
        self._max_y_size = max_y_size
        self._min_y_size = min_y_size
        self._near = near
        self._far = far

        self._projection_changed = True
        self._projection = None

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def set_minimum_x_size(self, min_x_size):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._min_x_size = min_x_size

    def get_minimum_x_size(self):
        """
        🟩 **R** -
        """
        return self._min_x_size

    def set_maximum_x_size(self, max_x_size):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._max_x_size = max_x_size

    def get_maximum_x_size(self):
        """
        🟩 **R** -
        """
        return self._max_x_size

    def set_maximum_y_size(self, max_y_size):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._max_y_size = max_y_size

    def get_maximum_y_size(self):
        """
        🟩 **R** -
        """
        return self._max_y_size

    def set_minimum_y_size(self, min_y_size):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._min_y_size = min_y_size

    def get_minimum_y_size(self):
        """
        🟩 **R** -
        """
        return self._min_y_size

    def set_near(self, near):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._near = near

    def get_near(self):
        """
        🟩 **R** -
        """
        return self._near

    def set_far(self, far):
        """
        🟩 **R** -
        """
        self._projection_changed = True
        self._far = far

    def get_far(self):
        """
        🟩 **R** -
        """
        return self._far

    def get_projection_matrix(self):
        """
        🟩 **R** -
        """
        if self._projection is None or self._projection_changed is True:
            self._projection_changed = False
            self._projection = _numpy__array([
                [2 / (self._max_x_size - self._min_x_size), 0, 0, -(self._max_x_size + self._min_x_size) / (self._max_x_size - self._min_x_size)],
                [0, 2 / (self._min_y_size - self._max_y_size), 0, -(self._min_y_size + self._max_y_size) / (self._min_y_size - self._max_y_size)],
                [0, 0, -2 / (self._far - self._near), -(self._far + self._near) / (self._far - self._near)],
                [0, 0, 0, 1]
            ], dtype='float32')

        return self._projection