import gc as _gc

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class MemoryManager:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)

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