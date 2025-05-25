from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class MemoryManager:
    """
    🟩 **R** -
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MEMORY_MANAGER_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MEMORY_MANAGER_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.memory_utils import MemoryManagerIntermediary as _MemoryManagerIntermediary
            _MemoryManagerIntermediary()

        self._memory_manager = _Registry.pmma_module_spine[_InternalConstants.MEMORY_MANAGER_INTERMEDIARY_OBJECT]

    def add(
            self,
            obj,
            custom_id=None,
            object_lifetime=None,
            object_creation_time=None,
            recreatable_object=False,
            pre_locked=False):
        """
        🟩 **R** -
        """

        return self._memory_manager.add_object(
            obj,
            custom_id=custom_id,
            object_lifetime=object_lifetime,
            object_creation_time=object_creation_time,
            recreatable_object=recreatable_object,
            pre_locked=pre_locked)

    def get(self, object_identifier):
        """
        🟩 **R** -
        """
        return self._memory_manager.get_object(object_identifier)

    def remove(self, object_identifier):
        """
        🟩 **R** -
        """
        return self._memory_manager.remove_object(object_identifier)