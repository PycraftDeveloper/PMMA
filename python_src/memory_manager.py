from gc import collect as _gc__collect

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class MemoryManager:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)

        if not _Constants.MEMORY_MANAGER_INTERMEDIARY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MEMORY_MANAGER_INTERMEDIARY_OBJECT)
            from pmma.python_src.utility.memory_utils import MemoryManagerIntermediary as _MemoryManagerIntermediary
            _MemoryManagerIntermediary()

        self._memory_manager = _Registry.pmma_module_spine[_Constants.MEMORY_MANAGER_INTERMEDIARY_OBJECT]

    def add(
            self,
            obj,
            custom_id=None,
            object_lifetime=None,
            object_creation_time=None,
            recreatable_object=False,
            pre_locked=False):

        return self._memory_manager.add_object(
            obj,
            custom_id=custom_id,
            object_lifetime=object_lifetime,
            object_creation_time=object_creation_time,
            recreatable_object=recreatable_object,
            pre_locked=pre_locked)

    def get(self, object_identifier):
        return self._memory_manager.get_object(object_identifier)

    def remove(self, object_identifier):
        return self._memory_manager.remove_object(object_identifier)