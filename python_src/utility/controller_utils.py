import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.controller import Controller as _Controller

class ControllersIntermediary:
    def __init__(self):
        initialize(self, unique_instance=Constants.CONTROLLER_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        self._controllers = []
        for joy_num in range(_pygame.joystick.get_count()):
            self._controllers.append(_Controller(joy_num))

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def identify_controllers(self):
        for i in range(len(self._controllers)):
            print(f"Controller: {i}, has name: {self._controllers[i].get_name()}")

    def get_controller(self, controller_index):
        return self._controllers[controller_index]

    def update_controllers(self):
        self._controllers = []
        for joy_num in range(_pygame.joystick.get_count()):
            self._controllers.append(_Controller(joy_num))

    def list_controllers(self):
        return self._controllers