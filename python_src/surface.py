import gc

import pygame
import pyglet

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class Surface:
    def __init__(self):
        initialize(self)

        if Registry.display_mode is None:
            raise Exception("Display mode not set")

        self.alpha = None
        self.surface_initialized = False

        self.attributes = []

    def __del__(self):
        if self._shut_down is False:
            if self.surface_initialized:
                if Registry.display_mode == Constants.PYGAME:
                    self.pygame_surface = None
                    del self.pygame_surface

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def create(self, width, height, alpha=False):
        self.alpha = alpha
        if Registry.display_mode == Constants.PYGAME:
            if alpha:
                flags = pygame.SRCALPHA
            else:
                flags = 0

            self.pygame_surface = pygame.Surface(
                (width, height),
                flags)

            self.surface_initialized = True
        else:
            raise NotImplementedError

    def blit(self, content, position=[0, 0]):
        if self.surface_initialized:
            self.pygame_surface.blit(content, position)

    def get_size(self):
        if self.surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                return self.pygame_surface.get_size()
            else:
                raise NotImplementedError

    def get_height(self):
        if self.surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                return self.pygame_surface.get_height()
            else:
                raise NotImplementedError

    def get_width(self):
        if self.surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                return self.pygame_surface.get_width()
            else:
                raise NotImplementedError

    def clear(self, *args):
        if self.surface_initialized:
            if args == ():
                args = (0, 0, 0)
            if Registry.display_mode == Constants.PYGAME:
                self.pygame_surface.fill(args)
            else:
                raise NotImplementedError

    def get_center(self, as_integer=True):
        if self.surface_initialized:
            if Registry.display_mode == Constants.PYGAME:
                if as_integer:
                    return self.pygame_surface.get_width() // 2, self.pygame_surface.get_height() // 2
                return self.pygame_surface.get_width() / 2, self.pygame_surface.get_height() / 2
            else:
                raise NotImplementedError

    def to_string(self, color_format=None, flipped=False):
        if self.surface_initialized:
            if color_format is None:
                if self.alpha:
                    color_format = "RGBA"
                else:
                    color_format = "RGB"

            if Registry.display_mode == Constants.PYGAME:
                return pygame.image.tostring(
                    self.pygame_surface,
                    color_format,
                    flipped)
