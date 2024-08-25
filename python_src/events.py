import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.backpack import Backpack as _Backpack

class Events:
    def __init__(self, canvas=None):
        initialize(self, unique_instance=Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True)

        self._raw_events = []
        self._canvas = canvas

        self._display_needs_resize = False

    def get_display_needs_resize(self):
        return self._display_needs_resize

    def set_display_needs_resize(self, value):
        self._display_needs_resize = value

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            del Registry.pmma_module_spine[Constants.EVENTS_OBJECT]
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def destroy(self):
        Registry.pmma_module_spine[Constants.EVENTS_OBJECT] = None

    def __get(self):
        self._raw_events = []
        if Registry.display_mode == Constants.PYGAME:
            self._raw_events += _pygame.event.get()

    def handle(
            self,
            enable_toggle_fullscreen=True,
            enable_close=True,
            return_events=True,
            canvas=None):

        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        self.__get()
        if enable_toggle_fullscreen or enable_close:
            for event in self._raw_events:
                if Registry.display_mode == Constants.PYGAME:
                    if event.type == _pygame.QUIT:
                        if enable_close:
                            Registry.running = False
                            _Backpack.running = False

                    elif event.type == _pygame.VIDEORESIZE:
                        self._display_needs_resize = True

                    elif event.type == _pygame.KEYDOWN:
                        if event.key == _pygame.K_ESCAPE:
                            if enable_close:
                                Registry.running = False
                                _Backpack.running = False
                        elif event.key == _pygame.K_F11:
                            if enable_toggle_fullscreen:
                                self._display_needs_resize = True
                                canvas.toggle_fullscreen()

        if return_events:
            #events = []
            #for event in self.raw_events:
            return self._raw_events

    def get_events(
            self,
            update_events=False):

        if update_events:
            self.__get()

        return self._events