import gc as _gc

import pygame as _pygame
import pyglet as _pyglet

from pmma.python_src.utils.registry import Registry as _Registry
from pmma.python_src.constants import Constants
from pmma.python_src.color import Color as _Color

from pmma.python_src.utility.general_utils import initialize as _initialize

class Surface:
    def __init__(self):
        _initialize(self)

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        if _Registry.display_mode is None:
            raise Exception("Display mode not set")

        self._alpha = None
        self._surface_initialized = False

        self._color_converter = _Color()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._surface_initialized:
                if _Registry.display_mode == Constants.PYGAME:
                    self._pygame_surface = None
                    del self._pygame_surface
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def create(self, width, height, alpha=False):
        self._alpha = alpha
        if _Registry.display_mode == Constants.PYGAME:
            if alpha:
                flags = _pygame.SRCALPHA
            else:
                flags = 0

            self._pygame_surface = _pygame.Surface(
                (width, height),
                flags)

            self._surface_initialized = True
        else:
            raise NotImplementedError

    def get_pygame_surface(self):
        if self._surface_initialized:
            return self._pygame_surface

    def blit(self, content, position=[0, 0]):
        if self._surface_initialized:
            self._pygame_surface.blit(content, position)

    def get_size(self):
        if self._surface_initialized:
            if _Registry.display_mode == Constants.PYGAME:
                return self._pygame_surface.get_size()
            else:
                raise NotImplementedError

    def get_height(self):
        if self._surface_initialized:
            if _Registry.display_mode == Constants.PYGAME:
                return self._pygame_surface.get_height()
            else:
                raise NotImplementedError

    def get_width(self):
        if self._surface_initialized:
            if _Registry.display_mode == Constants.PYGAME:
                return self._pygame_surface.get_width()
            else:
                raise NotImplementedError

    def clear(self, color=None, format=Constants.AUTODETECT):
        if self._surface_initialized:

            if color is None or color == [] or color == ():
                self._color_converter.input_color((0, 0, 0), format=Constants.RGB)

            elif type(color) == _Color:
                raw_color = color.output_color(Constants.RGBA)
                self._color_converter.input_color(raw_color, format=Constants.RGBA)
            else:
                self._color_converter.input_color(color, format=format)

            if _Registry.display_mode == Constants.PYGAME:
                self._pygame_surface.fill(self._color_converter.output_color(Constants.RGBA))
            else:
                raise NotImplementedError

    def get_center(self, as_integer=True):
        if self._surface_initialized:
            if _Registry.display_mode == Constants.PYGAME:
                if as_integer:
                    return self._pygame_surface.get_width() // 2, self._pygame_surface.get_height() // 2
                return self._pygame_surface.get_width() / 2, self._pygame_surface.get_height() / 2
            else:
                raise NotImplementedError

    def to_string(self, color_format=None, flipped=False):
        if self._surface_initialized:
            if color_format is None:
                if self._alpha:
                    color_format = "RGBA"
                else:
                    color_format = "RGB"

            if _Registry.display_mode == Constants.PYGAME:
                return _pygame.image.tostring(
                    self._pygame_surface,
                    color_format,
                    flipped)
