from gc import collect as _gc__collect

from pygame import joystick as _pygame__joystick
from pygame import init as _pygame__init

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.controller import Controller as _Controller

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

class ControllersIntermediary:
    def __init__(self):
        _initialize(
            self,
            unique_instance=_Constants.CONTROLLER_INTERMEDIARY_OBJECT,
            add_to_pmma_module_spine=True)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
            _pygame__init()

        self._controllers = []
        for joy_num in range(_pygame__joystick.get_count()):
            self._controllers.append(_Controller(joy_num))

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

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
        for joy_num in range(_pygame__joystick.get_count()):
            self._controllers.append(_Controller(joy_num))

    def list_controllers(self):
        return self._controllers