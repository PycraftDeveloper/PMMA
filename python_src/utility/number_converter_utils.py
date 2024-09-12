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
        if _Registry.cython_acceleration_available:
            self._number_converter_module = _importlib.import_module(
                "pmma.bin.number_converter")
        else:
            self._number_converter_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

        self._internal_number_converter = self._number_converter_module.Point()

    def set_point(self, value, in_type=Constants.CONVENTIONAL_COORDINATES):
        self._internal_number_converter.set_point(value, in_type=in_type)

    def get_point(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        return self._internal_number_converter.get_point(out_type)

class CoordinateIntermediary:
    def __init__(self):
        if _Registry.cython_acceleration_available:
            self._number_converter_module = _importlib.import_module(
                "pmma.bin.number_converter")
        else:
            self._number_converter_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

        self._internal_number_converter = self._number_converter_module.Coordinate()

    def set_coordinate(self, coordinate, in_type=Constants.CONVENTIONAL_COORDINATES):
        self._internal_number_converter.set_coordinate(coordinate, in_type=in_type)

    def get_coordinate(self, out_type=Constants.CONVENTIONAL_COORDINATES):
        return self._internal_number_converter.get_coordinate(out_type)