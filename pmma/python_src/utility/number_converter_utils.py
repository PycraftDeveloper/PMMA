from importlib import import_module as _importlib__import_module

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class ConverterIntermediaryManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_Constants.CONVERTER_INTERMEDIARY_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self.converter_intermediary = None

        if _Registry.cython_acceleration_available:
            self.converter_intermediary = _importlib__import_module(
                "pmma.bin.number_converter")

        else:
            self.converter_intermediary = _importlib__import_module(
                "pmma.python_src.pyx_alternatives.utility.number_converter")

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def get_converter(self):
        """
        🟩 **R** -
        """
        return self.converter_intermediary

class ColorIntermediary:
    """
    🟩 **R** -
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        if not _Constants.CONVERTER_INTERMEDIARY_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CONVERTER_INTERMEDIARY_MANAGER_OBJECT)
            from pmma.python_src.utility.number_converter_utils import ConverterIntermediaryManager as _number_converter_utils
            _number_converter_utils()

        self._number_converter_module = _Registry.pmma_module_spine[_Constants.CONVERTER_INTERMEDIARY_MANAGER_OBJECT].get_converter()

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