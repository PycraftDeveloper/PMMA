import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.backpack import Backpack as _Backpack

class Events:
    def __init__(self, canvas=None):
        initialize(self, unique_instance=Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True, requires_display_mode_set=True)

        self._raw_events = []
        self._canvas = canvas

        self._display_needs_resize = False

    def update_controllers(self):
        joysticks = [_pygame.joystick.Joystick(x) for x in range(_pygame.joystick.get_count())]