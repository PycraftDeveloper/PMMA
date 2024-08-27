import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.backpack import Backpack as _Backpack

class Events:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        initialize(self, unique_instance=Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True, requires_display_mode_set=True)

    def handle(self, automatically_apply_events_to_application=True):
        if Registry.display_mode == Constants.PYGAME:
            raw_events = _pygame.event.get()
            for event in raw_events:
                if event.type == _pygame.QUIT:
                    pass