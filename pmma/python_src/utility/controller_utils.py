from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants
from pmma.python_src.utility.registry_utils import Registry as _Registry

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ControllersIntermediary:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(
            self,
            unique_instance=_InternalConstants.CONTROLLER_INTERMEDIARY_OBJECT,
            add_to_pmma_module_spine=True)

        self._pygame__module = _ModuleManager.import_module("pygame")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._controller__module = _ModuleManager.import_module("pmma.python_src.controller")

        self._logger = self._logging_utils__module.InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            self._pygame__module.init()

        self._controllers = []
        for joy_num in range(self._pygame__module.joystick.get_count()):
            self._controllers.append(self._controller__module.Controller(joy_num))

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def identify_controllers(self):
        """
        🟩 **R** -
        """
        for i in range(len(self._controllers)):
            print(f"Controller: {i}, has name: {self._controllers[i].get_name()}")

    def get_controller(self, controller_index):
        """
        🟩 **R** -
        """
        return self._controllers[controller_index]

    def update_controllers(self):
        """
        🟩 **R** -
        """
        self._controllers = []
        for joy_num in range(self._pygame__module.joystick.get_count()):
            self._controllers.append(self._controller__module.Controller(joy_num))

    def list_controllers(self):
        """
        🟩 **R** -
        """
        return self._controllers