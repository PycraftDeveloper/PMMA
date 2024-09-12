import colorsys
import importlib as _importlib

from pmma.python_src.constants import Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.error_utils import DisplayNotYetCreatedError as _DisplayNotYetCreatedError
from pmma.python_src.utility.general_utils import swizzle as _swizzle

class ColorIntermediary:
    def __init__(self):
        if _Registry.cython_acceleration_available:
            self._number_converter_module = _importlib.import_module(
                "pmma.bin.number_converter")
        else:
            self._number_converter_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

        self._internal_number_converter = self._number_converter_module.Color()

    def detect_color_type(self, color):
        return self._internal_number_converter.detect_color_type(color)

    def set_color(self, color, in_type=Constants.AUTODETECT): # converts to RGBA
        self._internal_number_converter.set_color(color, in_type=in_type)

    def get_color_format(self):
        return self._internal_number_converter.in_type

    def get_color(self, out_type): # Converts from RGBA
        return self._internal_number_converter.get_color(out_type)

class PointIntermediary:
    def __init__(self):
        self._point = None
        self._logger = _InternalLogger()

    def set_point(self, value, in_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL values vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if in_type == Constants.CONVENTIONAL_COORDINATES:
            self._point = value
        elif in_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            half_display_height = display_size[1] / 2
            self._point = (value * half_display_height)

    def get_point(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._point
        elif out_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            return self._point / (display_size[1] / 2)

class CoordinateIntermediary:
    def __init__(self):
        self._coordinate = None
        self._logger = _InternalLogger()

    def set_coordinate(self, coordinate, in_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(coordinate) == list or type(coordinate) == tuple:
            coordinate = list(coordinate)
        else:
            coordinate = [float(coordinate)]

        if len(coordinate) == 0:
            coordinate = [0, 0]
            in_type == Constants.CONVENTIONAL_COORDINATES
        elif len(coordinate) == 1:
            coordinate = [coordinate[0], 0]
        elif len(coordinate) > 2:
            self._logger.log_development("This process is only required for coordinates in 2D or 1D space.")
            coordinate = coordinate[:2]


        if in_type == Constants.CONVENTIONAL_COORDINATES:
            self._coordinate = coordinate
        elif in_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            half_display_size = [display_size[0] / 2, display_size[1] / 2]
            x = half_display_size[0] * (coordinate[0] + 1)
            y = -half_display_size[1] * (coordinate[1] - 1)
            self._coordinate = [x, y]

    def get_coordinate(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        if _Registry.display_initialized is False:
            self._logger.log_development("You need to have first created a display in \
order to be able to use this function. This is because OpenGL coordinates vary depending \
on the screen size and aspect ratio.")
            raise _DisplayNotYetCreatedError()
        else:
            display = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if out_type == Constants.CONVENTIONAL_COORDINATES:
            return self._coordinate
        elif out_type == Constants.OPENGL_COORDINATES:
            display_size = display.get_size()
            x = (2 * self._coordinate[0]) / display_size[0] - 1  # Removed the extra negative
            y = 1 - (2 * self._coordinate[1]) / display_size[1]  # This is correct
            return [x, y]