from gc import collect as _gc__collect

import pygame as _pygame

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.events import WindowResized_EVENT as _WindowResized_EVENT

from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

class ShapeTemplate: # add vertex manager and changes to rendering!
    def __init__(self):
        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._color_changed = True
        self._fill_color_manager = _ColorConverter()
        self._color = None
        self._display: "_DisplayIntermediary" = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

        self._resized_event = _WindowResized_EVENT()

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        if type(color) == _ColorConverter:
            color = color.get_color(format=_Constants.RGBA)
            format = _Constants.RGBA

        if self._fill_color_manager.get_color_set():
            original_color = self._fill_color_manager.get_color(format=_Constants.RGBA)
            self._fill_color_manager.set_color(color, format=format)
            if self._fill_color_manager.get_color(format=_Constants.RGBA) != original_color:
                self._color_changed = True
            else:
                self._color_changed = False
                self._fill_color_manager.set_color(original_color, format=_Constants.RGBA)
        else:
            self._color_changed = True
            self._fill_color_manager.set_color(color, format=format)

        if self._color_changed:
            self._color = self._fill_color_manager.get_color(format=_Constants.SMALL_RGBA)

    def get_color_set(self):
        return self._fill_color_manager.get_color_set()

    def get_color(self, format):
        if self._fill_color_manager.get_color_set():
            return self._fill_color_manager.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        self._color_changed = True
        self._color = self._fill_color_manager.generate_random_color(
            format=_Constants.SMALL_RGBA,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        self._color_changed = True
        self._color = self._fill_color_manager.generate_color_from_perlin_noise(
            self,
            value=value,
            format=_Constants.SMALL_RGBA,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

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