import gc

import pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.backpack import Backpack

class Events:
    def __init__(self, canvas=None):
        initialize(self, unique_instance=Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True)

        self.raw_events = []
        self.canvas = canvas

        self.display_needs_resize = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            del Registry.pmma_module_spine[Constants.EVENTS_OBJECT]
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def destroy(self):
        Registry.pmma_module_spine[Constants.EVENTS_OBJECT] = None

    def __get(self):
        self.raw_events = []
        if Registry.display_mode == Constants.PYGAME:
            self.raw_events += pygame.event.get()

    def handle(
            self,
            enable_toggle_fullscreen=True,
            enable_close=True,
            return_events=True,
            canvas=None):

        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        self.__get()
        if enable_toggle_fullscreen or enable_close:
            for event in self.raw_events:
                if Registry.display_mode == Constants.PYGAME:
                    if event.type == pygame.QUIT:
                        if enable_close:
                            Registry.running = False
                            Backpack.running = False

                    elif event.type == pygame.VIDEORESIZE:
                        self.display_needs_resize = True

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if enable_close:
                                Registry.running = False
                                Backpack.running = False
                        elif event.key == pygame.K_F11:
                            if enable_toggle_fullscreen:
                                self.display_needs_resize = True
                                canvas.toggle_fullscreen()

        if return_events:
            #events = []
            #for event in self.raw_events:
            return self.raw_events

    def get_events(
            self,
            update_events=False):

        if update_events:
            self.__get()

        return self.events