import gc as _gc
import random as _random
import math as _math

from pmma.python_src.constants import Constants
from pmma.python_src.noise import Perlin as _Perlin

from pmma.python_src.utility.number_converter_utils import ColorIntermediary as _ColorIntermediary
from pmma.python_src.utility.number_converter_utils import CoordinateIntermediary as _CoordinateIntermediary
from pmma.python_src.utility.number_converter_utils import PointIntermediary as _PointIntermediary
from pmma.python_src.utility.general_utils import initialize as _initialize

class AngleConverter:
    def __init__(self):
        _initialize(self)

        self._angle = 0

    def set_angle(self, angle, format=Constants.DEGREES):
        if format == Constants.DEGREES:
            self._angle = angle
        elif format == Constants.RADIANS:
            self._angle = (angle / _math.pi) * 180
        elif format == Constants.GRADIANS:
            self._angle = angle * (10/9)

    def get_angle(self, format=Constants.DEGREES):
        if format == Constants.DEGREES:
            return self._angle
        elif format == Constants.RADIANS:
            return (self._angle / 180) * _math.pi
        elif format == Constants.GRADIANS:
            return self._angle / (10/9)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class ProportionConverter:
    def __init__(self):
        _initialize(self)

        self._value = None

    def set_value(self, value, format=Constants.DECIMAL):
        if format == Constants.DECIMAL:
            self._value = value
        elif format == Constants.PERCENTAGE:
            self._value = value / 100

    def get_value(self, format=Constants.DECIMAL):
        if format == Constants.DECIMAL:
            return self._value
        elif format == Constants.PERCENTAGE:
            return self._value * 100

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class ColorConverter:
    def __init__(self, seed=None):
        _initialize(self)

        self._color_intermediary = _ColorIntermediary()

        self._red_noise = _Perlin(seed=seed)
        self._green_noise = _Perlin(seed=seed)
        self._blue_noise = _Perlin(seed=seed)
        self._alpha_noise = _Perlin(seed=seed)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_intermediary.set_color(color, format)

    def get_color(self, format):
        return self._color_intermediary.get_color(format)

    def get_color_format(self):
        return self._color_intermediary.get_color_format()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def generate_random_color(self, format=Constants.RGBA):
        color = [_random.randint(0, 255), _random.randint(0, 255), _random.randint(0, 255), _random.randint(0, 255)]
        self._color_intermediary.set_color(
            color,
            Constants.RGBA)
        return self.get_color(format)

    def generate_color(
            self,
            value,
            format=Constants.RGBA,
            color_range=[0, 255],
            red_color_range=[0, 255],
            green_color_range=[0, 255],
            blue_color_range=[0, 255],
            alpha_color_range=[0, 255]):

        if color_range != [0, 255]:
            if red_color_range == [0, 255]:
                red_color_range = color_range
            elif green_color_range == [0, 255]:
                green_color_range = color_range
            elif blue_color_range == [0, 255]:
                blue_color_range = color_range
            elif alpha_color_range == [0, 255]:
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

        self._color_intermediary.set_color(
            color,
            Constants.RGBA)
        return self.get_color(format)

class PointConverter:
    def __init__(self):
        _initialize(self)

        self._intermediary = _PointIntermediary()

    def set_point(self, point, format=Constants.CONVENTIONAL_COORDINATES):
        self._intermediary.set_point(point, in_type=format)

    def output_point(self, format=Constants.CONVENTIONAL_COORDINATES):
        return self._intermediary.get_point(out_type=format)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class CoordinateConverter:
    def __init__(self):
        _initialize(self)

        self._intermediary = _CoordinateIntermediary()

    def set_coordinates(self, coordinate, format=Constants.CONVENTIONAL_COORDINATES):
        self._intermediary.set_coordinate(coordinate, in_type=format)

    def get_coordinates(self, format=Constants.CONVENTIONAL_COORDINATES):
        return self._intermediary.get_coordinate(out_type=format)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True