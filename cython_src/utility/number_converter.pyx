# cython: language_level=3

from colorsys import hsv_to_rgb as _colorsys__hsv_to_rgb
from colorsys import rgb_to_hsv as _colorsys__rgb_to_hsv

import numpy as _numpy
cimport numpy as cnp

from pmma.python_src.constants import Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.general_utils import swizzle as _swizzle
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

cdef class Color:
    """
    🟩 **R** -
    """
    cdef object in_type
    cdef object color

    def __init__(self):
        """
        🟩 **R** -
        """
        self.in_type = None
        self.color = None

    cpdef void set_color(self, color, str in_type=Constants.RGB):
        """
        🟩 **R** -
        """
        if isinstance(color, str):
            color = color.lower()

        self.in_type = in_type

        cdef list color_list = list(color)
        cdef list sorted_in_type = sorted(in_type)

        if sorted_in_type == Constants.SORTED_RGBA:
            self.color = color_list
        elif sorted_in_type == Constants.SORTED_RGB:
            self.color = color_list + [255]
        elif sorted_in_type == Constants.SORTED_HSL:
            self.color = list(_colorsys__hsv_to_rgb(
                color_list[0] / 360,
                color_list[1] / 100,
                color_list[2] / 100)) + [255]
        elif sorted_in_type == Constants.SORTED_HSLA:
            self.color = list(_colorsys__hsv_to_rgb(
                color_list[0] / 360,
                color_list[1] / 100,
                color_list[2] / 100)) + [(color_list[3] / 100) * 255]
        elif sorted_in_type == Constants.SORTED_SMALL_HSL:
            self.color = list(_colorsys__hsv_to_rgb(color_list[0], color_list[1], color_list[2])) + [255]
        elif sorted_in_type == Constants.SORTED_SMALL_HSLA:
            self.color = list(_colorsys__hsv_to_rgb(color_list[0], color_list[1], color_list[2])) + [255 * color_list[3]]
        elif sorted_in_type == Constants.SORTED_SMALL_RGB:
            self.color = [color_list[0] * 255, color_list[1] * 255, color_list[2] * 255, 255]
        elif sorted_in_type == Constants.SORTED_SMALL_RGBA:
            self.color = [color_list[0] * 255, color_list[1] * 255, color_list[2] * 255, color_list[3] * 255]
        elif in_type == Constants.HEX:
            self.color = [int(color[i:i + 2], 16) for i in (0, 2, 4)] + [255]
        elif in_type == Constants.HEXA:
            self.color = [int(color[i:i + 2], 16) for i in (0, 2, 4, 6)]
        elif in_type == Constants.TEXT:
            self.color = Constants.TEXT_BASED_COLORS[color.upper()] + [255]

    cdef tuple __convert_rgb_to_hsv(self, double red, double green, double blue,
                                    double per_maximum=100, bint do_round=True):
        """
        🟩 **R** -
        """
        cdef double red_percentage = red / 255
        cdef double green_percentage = green / 255
        cdef double blue_percentage = blue / 255
        cdef tuple color_hsv_percentage = _colorsys__rgb_to_hsv(
            red_percentage, green_percentage, blue_percentage)
        cdef double color_h = 360 * color_hsv_percentage[0]

        cdef double color_s
        cdef double color_v
        if do_round:
            color_s = round(per_maximum * color_hsv_percentage[1])
            color_v = round(per_maximum * color_hsv_percentage[2])
        else:
            color_s = per_maximum * color_hsv_percentage[1]
            color_v = per_maximum * color_hsv_percentage[2]
        return (color_h, color_s, color_v)

    cpdef object get_color(self, str out_type):
        """
        🟩 **R** -
        """
        if self.color is None:
            return None
        cdef list sorted_out_type = sorted(out_type)
        if sorted_out_type == Constants.SORTED_RGBA:
            return _numpy.array(_swizzle(Constants.RGBA, self.color, out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_RGB:
            return _numpy.array(_swizzle(Constants.RGB, self.color[0:3], out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_HSL:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2]))
            return _numpy.array(_swizzle(Constants.HSL, color, out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_HSLA:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2])) + [round((100 / 255) * self.color[3])]
            return _numpy.array(_swizzle(Constants.HSLA, color, out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_HSL:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2], per_maximum=1, do_round=False))
            return _numpy.array(_swizzle(Constants.SMALL_HSL, color, out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_HSLA:
            color = list(self.__convert_rgb_to_hsv(self.color[0], self.color[1], self.color[2], per_maximum=1, do_round=False)) + \
                    [round((1 / 255) * self.color[3])]
            return _numpy.array(_swizzle(Constants.SMALL_HSLA, color, out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_RGB:
            color = [self.color[0] / 255, self.color[1] / 255, self.color[2] / 255]
            return _numpy.array(_swizzle(Constants.SMALL_RGB, color, out_type), dtype=_numpy.float32)
        elif sorted_out_type == Constants.SORTED_SMALL_RGBA:
            color = [self.color[0] / 255, self.color[1] / 255, self.color[2] / 255, self.color[3] / 255]
            return _numpy.array(_swizzle(Constants.SMALL_RGBA, color, out_type), dtype=_numpy.float32)
        elif out_type == Constants.HEX:
            return '#%02x%02x%02x' % tuple(self.color[0:3])
        elif out_type == Constants.HEXA:
            return '#%02x%02x%02x%02x' % tuple(self.color)
        elif out_type == Constants.TEXT:
            return [value for value, key in Constants.TEXT_BASED_COLORS.items() if key == self.color]

cdef class DisplayScalar:
    """
    🟩 **R** - Optimized version
    """
    cdef double _point
    cdef object _logger
    cdef double display_height

    def __init__(self):
        """
        🟩 **R** - Optimized
        """
        self._point = 0.0
        self._logger = _InternalLogger()
        self.display_height = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_height()
        _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].add_to_functions_to_call_on_resize(self)

    def __del__(self):
        _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].remove_from_functions_to_call_on_resize(self)

    def _handle_resize(self):
        """ Update display height with stored reference """
        self.display_height = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_height()

    cpdef void set_point(self, double value, str in_type) noexcept:
        """
        🟩 **R** - Optimized
        """
        cdef double half_display_height

        if in_type == Constants.CONVENTIONAL_COORDINATES:  # Constants.CONVENTIONAL_COORDINATES
            self._point = value
        elif in_type == Constants.OPENGL_COORDINATES:  # Constants.OPENGL_COORDINATES
            half_display_height = self.display_height * 0.5
            self._point = value * half_display_height

    cpdef double get_point(self, str out_type) noexcept:
        """
        🟩 **R** - Optimized
        """
        if out_type == Constants.CONVENTIONAL_COORDINATES:  # Constants.CONVENTIONAL_COORDINATES
            return self._point
        elif out_type == Constants.OPENGL_COORDINATES:  # Constants.OPENGL_COORDINATES
            return self._point / (self.display_height * 0.5)

cdef class DisplayCoordinates:
    """
    🟩 **R** - Optimized
    """
    cdef double _coordinate[2]  # Use a fixed-size C array
    cdef object _logger
    cdef double display_width, display_height
    cdef object _display_object  # Store reference for performance

    def __init__(self):
        """
        🟩 **R** - Optimized
        """
        self._coordinate[0] = 0.0
        self._coordinate[1] = 0.0
        self._logger = _InternalLogger()
        self.display_width, self.display_height = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_size()
        _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].add_to_functions_to_call_on_resize(self)

    def __del__(self):
        _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].remove_from_functions_to_call_on_resize(self)

    def _handle_resize(self):
        """ Update display size """
        self.display_width, self.display_height = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_size()

    cpdef void set_coordinate(self, object coordinate, str in_type) noexcept:
        """
        🟩 **R** - Optimized
        """
        cdef double x, y

        try:
            # Assume coordinate is iterable and extract values
            x, y = coordinate[0], coordinate[1]
        except (IndexError, TypeError):
            x, y = 0.0, 0.0  # Default case

        cdef double half_display_width = self.display_width * 0.5
        cdef double half_display_height = self.display_height * 0.5

        if in_type == Constants.CONVENTIONAL_COORDINATES:  # Constants.CONVENTIONAL_COORDINATES
            self._coordinate[0] = x
            self._coordinate[1] = y
        elif in_type == Constants.OPENGL_COORDINATES:  # Constants.OPENGL_COORDINATES
            self._coordinate[0] = half_display_width * (x + 1)
            self._coordinate[1] = -half_display_height * (y - 1)

    cpdef cnp.ndarray[cnp.float32_t, ndim=1] get_coordinate(self, str out_type):
        """
        🟩 **R** - Optimized
        """
        cdef double x, y

        if out_type == Constants.CONVENTIONAL_COORDINATES:  # Constants.CONVENTIONAL_COORDINATES
            return _numpy.array([self._coordinate[0], self._coordinate[1]], dtype=_numpy.float32)

        elif out_type == Constants.OPENGL_COORDINATES:  # Constants.OPENGL_COORDINATES
            x = (2.0 * self._coordinate[0]) / self.display_width - 1.0
            y = 1.0 - (2.0 * self._coordinate[1]) / self.display_height
            return _numpy.array([x, y], dtype=_numpy.float32)