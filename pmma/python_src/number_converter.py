from gc import collect as _gc__collect
import random as _random
import math as _math

import numpy as _numpy

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.noise import Perlin as _Perlin

from pmma.python_src.utility.number_converter_utils import ColorIntermediary as _ColorIntermediary
from pmma.python_src.utility.number_converter_utils import DisplayCoordinatesIntermediary as _DisplayCoordinatesIntermediary
from pmma.python_src.utility.number_converter_utils import DisplayScalarIntermediary as _DisplayScalarIntermediary
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.error_utils import DisplayNotYetCreatedError as _DisplayNotYetCreatedError

class AngleConverter:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._angle = 0
        self._angle_cache = {}
        self._angle_set = False

    def set_angle(self, angle, format=_Constants.DEGREES):
        """
        🟩 **R** -
        """
        if not (format in self._angle_cache and self._angle_cache[format] == angle):
            self._angle_cache = {}
            self._angle_cache[format] = angle

            if format == _Constants.DEGREES:
                self._angle = angle
            elif format == _Constants.RADIANS:
                self._angle = (angle / _math.pi) * 180
            elif format == _Constants.GRADIANS:
                self._angle = angle * (10/9)
            self._angle_set = True
            return True
        return False

    def get_angle_set(self):
        """
        🟩 **R** -
        """
        return self._angle_set

    def get_angle(self, format=_Constants.DEGREES):
        """
        🟩 **R** -
        """
        if format in self._angle_cache:
            return self._angle_cache[format]
        else:
            if format == _Constants.DEGREES:
                angle =  self._angle
            elif format == _Constants.RADIANS:
                angle = (self._angle / 180) * _math.pi
            elif format == _Constants.GRADIANS:
                angle = self._angle / (10/9)

            self._angle_cache[format] = angle
            return angle

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class ProportionConverter:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._value = None
        self._value_cache = {}
        self._proportion_set = False

    def set_value(self, value, format=_Constants.DECIMAL):
        """
        🟩 **R** -
        """
        if not (format in self._value_cache and self._value_cache[format] == value):
            self._value_cache = {}
            self._value_cache[format] = value
            if format == _Constants.DECIMAL:
                self._value = value
            elif format == _Constants.PERCENTAGE:
                self._value = value / 100
            self._proportion_set = True
            return True
        return False

    def get_proportion_set(self):
        """
        🟩 **R** -
        """
        return self._proportion_set

    def get_value(self, format=_Constants.DECIMAL):
        """
        🟩 **R** -
        """
        if format in self._value_cache:
            return self._value_cache[format]
        else:
            if format == _Constants.DECIMAL:
                point = self._value
            elif format == _Constants.PERCENTAGE:
                point = self._value * 100

            self._value_cache[format] = point
            return point

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class ColorConverter:
    """
    🟩 **R** -
    """
    def __init__(self, seed=None):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._color_intermediary = _ColorIntermediary()

        self._seed = seed

        self._red_noise = None
        self._green_noise = None
        self._blue_noise = None
        self._alpha_noise = None

        self._color_cache = {}

        self._color_set = False

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        if format == _Constants.RGB:
            color = [int(color[0]), int(color[1]), int(color[2])]
        elif format == _Constants.RGBA:
            color = [int(color[0]), int(color[1]), int(color[2]), int(color[3])]
        ### extend this, ignore HEX and SMALL values!!!

        if not (format in self._color_cache and self._color_cache[format].tolist() == color):
            self._color_cache = {}
            self._color_intermediary.set_color(color, format)
            self._color_cache[format] = self._color_intermediary.get_color(_Constants.RGBA)
            self._color_set = True
            return True
        return False

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._color_set

    def get_color(self, format):
        """
        🟩 **R** -
        """
        if format in self._color_cache:
            return self._color_cache[format]
        else:
            point = self._color_intermediary.get_color(out_type=format)
            self._color_cache[format] = point
            return point

    def get_color_format(self):
        """
        🟩 **R** -
        """
        return self._color_intermediary.get_color_format()

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def generate_random_color(
            self,
            format=_Constants.RGBA,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """

        if red_color_range is None:
            red_color_range = color_range
        if green_color_range is None:
            green_color_range = color_range
        if blue_color_range is None:
            blue_color_range = color_range
        if alpha_color_range is None:
            alpha_color_range = color_range

        color = [_random.randint(*red_color_range), _random.randint(*green_color_range), _random.randint(*blue_color_range), _random.randint(*alpha_color_range)]

        self.set_color(
            color,
            _Constants.RGBA)

        return self.get_color(format)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            format=_Constants.RGBA,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """

        if self._red_noise is None:
            self._red_noise = _Perlin(seed=self._seed)
        if self._green_noise is None:
            self._green_noise = _Perlin(seed=self._seed)
        if self._blue_noise is None:
            self._blue_noise = _Perlin(seed=self._seed)
        if self._alpha_noise is None:
            self._alpha_noise = _Perlin(seed=self._seed)

        if red_color_range is None:
            red_color_range = color_range
        if green_color_range is None:
            green_color_range = color_range
        if blue_color_range is None:
            blue_color_range = color_range
        if alpha_color_range is None:
            alpha_color_range = color_range

        color = [
            self._red_noise.generate_1D_perlin_noise(
                value,
                new_range=red_color_range),
            self._green_noise.generate_1D_perlin_noise(
                value,
                new_range=green_color_range),
            self._blue_noise.generate_1D_perlin_noise(
                value,
                new_range=blue_color_range),
            self._alpha_noise.generate_1D_perlin_noise(
                value,
                new_range=alpha_color_range)]

        self.set_color(
            color,
            _Constants.RGBA)

        return self.get_color(format)

class DisplayScalarConverter:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._point_intermediary = _DisplayScalarIntermediary()
        self._point_cache = {}

        self._point_set = False

        if not _Registry.display_initialized:
            self._logger = _InternalLogger()
            self._logger.log_development("You need to initialize a display before using \
coordinate converter, because we dont know what size to convert the coordinates to/from \
with no window created. Initialize the Display component and use `display.create()` to \
create the window onscreen")
            raise _DisplayNotYetCreatedError()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._display_size = self._display.get_size()

    def set_point(self, point, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if format == _Constants.CONVENTIONAL_COORDINATES:
            point = int(point)

        if not (format in self._point_cache and self._point_cache[format] == point):
            self._point_cache = {}
            self._point_cache[format] = point
            self._point_intermediary.set_point(point, in_type=format)
            self._point_set = True
            return True
        return False

    def get_point_set(self):
        """
        🟩 **R** -
        """
        return self._point_set

    def get_point(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        display_size = self._display.get_size()
        if display_size != self._display_size:
            self._display_size = display_size
            self._point_cache = {}

        if format in self._point_cache:
            return self._point_cache[format]
        else:
            point = self._point_intermediary.get_point(out_type=format)
            self._point_cache[format] = point
            return point

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class DisplayCoordinatesConverter:
    """
    🟩 **R** -
    """
    def __init__(self, seed=None):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._coordinate_intermediary = _DisplayCoordinatesIntermediary()
        self._coordinate_cache = {}

        self._seed = seed

        self._x_noise = None
        self._y_noise = None

        self._coordinate_set = False

        if not _Registry.display_initialized:
            self._logger = _InternalLogger()
            self._logger.log_development("You need to initialize a display before using \
coordinate converter, because we dont know what size to convert the coordinates to/from \
with no window created. Initialize the Display component and use `display.create()` to \
create the window onscreen")
            raise _DisplayNotYetCreatedError()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._display_size = self._display.get_size()

    def set_coordinates(self, coordinate, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if format == _Constants.CONVENTIONAL_COORDINATES:
            coordinate = _numpy.array([int(coordinate[0]), int(coordinate[1])])
        else:
            coordinate = _numpy.array(coordinate, dtype=_numpy.float32)

        if not (format in self._coordinate_cache and self._coordinate_cache[format].tobytes() == coordinate.tobytes()):
            self._coordinate_cache = {}
            self._coordinate_intermediary.set_coordinate(coordinate, in_type=format)
            self._coordinate_cache[format] = coordinate
            self._coordinate_set = True
            return True
        return False

    def get_coordinate_set(self):
        """
        🟩 **R** -
        """
        return self._coordinate_set

    def get_coordinates(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        display_size = self._display.get_size()
        if display_size != self._display_size:
            self._display_size = display_size
            self._coordinate_cache = {}

        if format in self._coordinate_cache:
            return self._coordinate_cache[format]
        else:
            coordinate = self._coordinate_intermediary.get_coordinate(out_type=format)
            self._coordinate_cache[format] = coordinate
            return coordinate

    def generate_random_coordinate(
            self,
            format=_Constants.CONVENTIONAL_COORDINATES,
            coordinate_range=None,
            x_coordinate_range=None,
            y_coordinate_range=None):
        """
        🟩 **R** -
        """

        if coordinate_range is None:
            if _Registry.display_initialized:
                display = self._display
                coordinate_range = [0, min(display.get_size())]
            else:
                coordinate_range = [0, 100]

        if x_coordinate_range is None:
            x_coordinate_range = coordinate_range
        if y_coordinate_range is None:
            y_coordinate_range = coordinate_range

        coordinate = [_random.randint(*x_coordinate_range), _random.randint(*y_coordinate_range)]

        self.set_coordinates(
            coordinate,
            _Constants.CONVENTIONAL_COORDINATES)

        return self.get_coordinates(format)

    def generate_coordinate_from_perlin_noise(
            self,
            value=None,
            format=_Constants.CONVENTIONAL_COORDINATES,
            coordinate_range=None,
            x_coordinate_range=None,
            y_coordinate_range=None):
        """
        🟩 **R** -
        """

        if self._x_noise is None:
            self._x_noise = _Perlin(seed=self._seed)

        if self._y_noise is None:
            self._y_noise = _Perlin(seed=self._seed)

        if x_coordinate_range is None:
            if coordinate_range is None:
                x_coordinate_range = [0, self._display.get_width()]
            else:
                x_coordinate_range = coordinate_range

        if y_coordinate_range is None:
            if coordinate_range is None:
                y_coordinate_range = [0, self._display.get_height()]
            else:
                y_coordinate_range = coordinate_range

        color = [
            self._x_noise.generate_1D_perlin_noise(
                value,
                new_range=x_coordinate_range),
            self._y_noise.generate_1D_perlin_noise(
                value,
                new_range=y_coordinate_range)]

        self.set_coordinates(
            color,
            _Constants.CONVENTIONAL_COORDINATES)

        return self.get_coordinates(format)

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True