from importlib import import_module as _importlib__import_module
from gc import collect as _gc__collect

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ColorIntermediary:
    """
    🟩 **R** -
    """
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

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if _Registry.cython_acceleration_available:
            self._number_converter_module = _importlib__import_module(
                "pmma.bin.number_converter")
        else:
            self._number_converter_module = _importlib__import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

        self._internal_number_converter = self._number_converter_module.Color()

    def detect_color_type(self, color):
        """
        🟩 **R** -
        """
        return self._internal_number_converter.detect_color_type(color)

    def set_color(self, color, in_type=_Constants.RGB): # converts to RGBA
        """
        🟩 **R** -
        """
        self._internal_number_converter.set_color(color, in_type=in_type)

    def get_color_format(self):
        """
        🟩 **R** -
        """
        return self._internal_number_converter.in_type

    def get_color(self, out_type): # Converts from RGBA
        """
        🟩 **R** -
        """
        return self._internal_number_converter.get_color(out_type)

class DisplayScalarIntermediary:
    """
    🟩 **R** -
    """
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

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if _Registry.cython_acceleration_available:
            self._number_converter_module = _importlib__import_module(
                "pmma.bin.number_converter")
        else:
            self._number_converter_module = _importlib__import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

        self._internal_number_converter = self._number_converter_module.DisplayScalar()

    def set_point(self, value, in_type=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._internal_number_converter.set_point(value, in_type=in_type)

    def get_point(self, out_type=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._internal_number_converter.get_point(out_type)

class DisplayCoordinatesIntermediary:
    """
    🟩 **R** -
    """
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

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if _Registry.cython_acceleration_available:
            self._number_converter_module = _importlib__import_module(
                "pmma.bin.number_converter")
        else:
            self._number_converter_module = _importlib__import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

        self._internal_number_converter = self._number_converter_module.DisplayCoordinates()

    def set_coordinate(self, coordinate, in_type=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._internal_number_converter.set_coordinate(coordinate, in_type=in_type)

    def get_coordinate(self, out_type=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._internal_number_converter.get_coordinate(out_type)