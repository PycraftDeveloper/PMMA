import gc as _gc

import pygame as _pygame
import pyglet as _pyglet

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Surface:
    def __init__(self):
        initialize(self)

        if Registry.display_mode is None:
            raise Exception("Display mode not set")

        self._alpha = None
        self._surface_initialized = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            if self._surface_initialized:
                if Registry.display_mode == Constants.PYGAME:
                    self._pygame_surface = None
                    del self._pygame_surface
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def create(self, width, height, alpha=False):
        self._alpha = alpha
        if Registry.display_mode == Constants.PYGAME:
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

    def blit(self, content, position=[0, 0]):
        if self._surface_initialized:
            self._pygame_surface.blit(content, position)

    def get_size(self):
        if self._surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                return self._pygame_surface.get_size()
            else:
                raise NotImplementedError

    def get_height(self):
        if self._surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                return self._pygame_surface.get_height()
            else:
                raise NotImplementedError

    def get_width(self):
        if self._surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                return self._pygame_surface.get_width()
            else:
                raise NotImplementedError

    def clear(self, *args):
        if self._surface_initialized:
            if args == ():
                args = (0, 0, 0)
            if Registry.display_mode == Constants.PYGAME:
                self._pygame_surface.fill(args)
            else:
                raise NotImplementedError

    def get_center(self, as_integer=True):
        if self._surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                if as_integer:
                    return self._pygame_surface.get_width() // 2, self._pygame_surface.get_height() // 2
                return self._pygame_surface.get_width() / 2, self._pygame_surface.get_height() / 2
            else:
                raise NotImplementedError

    def to_string(self, color_format=None, flipped=False):
        if self._surface_initialized:
            if color_format is None:
                if self.alpha:
                    color_format = "RGBA"
                else:
                    color_format = "RGB"

            if Registry.display_mode == Constants.PYGAME:
                return _pygame.image.tostring(
                    self._pygame_surface,
                    color_format,
                    flipped)
