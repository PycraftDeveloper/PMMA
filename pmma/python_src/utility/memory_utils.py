from time import perf_counter as _time__perf_counter
from threading import Thread as _threading__Thread
from threading import Lock as _threading__Lock
from sys import getsizeof as _sys__getsizeof
from tempfile import NamedTemporaryFile as _tempfile__NamedTemporaryFile
from os import mkdir as _os__mkdir
from os import remove as _os__remove
from shutil import rmtree as _shutil__rmtree
from gc import collect as _gc__collect
from traceback import format_exc as _traceback__format_exc

from psutil import virtual_memory as _psutil__virtual_memory
from dill import dumps as _dill__dumps
from dill import loads as _dill__loads
from dill import dump as _dill__dump
from waiting import wait as _waiting__wait

from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.data_structures import InvertedPriorityList as _InvertedPriorityList

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

class MemoryManagerIntermediary:
    def __init__(
            self,
            object_lifetime=2.5,
            target_size=_Constants.AUTOMATIC):

        _initialize(self, unique_instance=_Constants.MEMORY_MANAGER_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        self._logger = _InternalLogger()

        self.limited_max_size = False
        if target_size == _Constants.AUTOMATIC:
            target_size = (1/8) * _psutil__virtual_memory().available
            if target_size > 1000000000:
                self.target_size = 1000000000 # 1 GB
                self.limited_max_size = True
                self._logger.log_development("Limiting targeted memory management \
size to 1 GB, from automatically calculated size of: {} \
GB. If needed, this target will be raised on the fly.", variables=[target_size/1000000000])
            else:
                self.target_size = target_size

            self._logger.log_development("Max memory management size has not been set, \
therefore PMMA has determined that: {} GB shall be \
targeted. Consider specifying a max size yourself if you find yourself exceeding \
this limit.", variables=[self.target_size/1000000000])

            self.assigned_target_size = False
        else:
            self.assigned_target_size = True
            self.target_size = target_size

        self._logger.log_development("Note, PMMA will attempt to target: \
{} GB as its max size for memory management, \
however this is a target NOT a maximum, and this limit can be exceeded, \
with PMMA automatically taking corrective action in such cases. Additionally, \
this memory will not be used until it's needed by PMMA.", variables=[self.target_size/1000000000])

        if self.assigned_target_size is False and _PassportIntermediary.project_size is not None:
            self._logger.log_development("For applications with a defined project size, \
leaving the target size variable can be dangerous.")

        self.objects = {}
        self.linker = {}
        self.object_lifetime = object_lifetime

        self.enable_memory_management = True
        self.total_size = 0
        self.temporary_files = {}
        self.manager_thread_organized_data = _InvertedPriorityList()
        self.manager_thread_organized_data_minimum_priority_changed = True

        self.manager_thread = _threading__Thread(target=self.object_dictionary_manager)
        self.manager_thread.daemon = True
        self.manager_thread.name = "MemoryManagerIntermediary:Object_Memory_Management_Thread"
        self.manager_thread.start()
        self.max_obj_creation_time = float("-inf")
        self.max_obj_size = 0

        self.memory_manager_thread_lock = _threading__Lock()

        self.memory_management_directory = _path_builder(
            _Registry.base_path,
            "temporary",
            "memory management dumps")

        _shutil__rmtree(
            self.memory_management_directory,
            ignore_errors=True)

        _os__mkdir(self.memory_management_directory)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self.enable_memory_management = False

            self.manager_thread.join()

            _shutil__rmtree(
                self.memory_management_directory,
                ignore_errors=True)

            _os__mkdir(self.memory_management_directory)

            self.linker = {}
            self.objects = {}
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add_object(
            self,
            obj,
            custom_id=None,
            object_lifetime=None,
            object_creation_time=None,
            recreatable_object=False,
            pre_locked=False):

        if self.enable_memory_management:
            if pre_locked:
                if recreatable_object is False:
                    try:
                        byte_data = _dill__dumps(obj)
                        _dill__loads(byte_data)
                        stay_in_memory = False
                    except:
                        stay_in_memory = True

                if custom_id is not None:
                    identifier = custom_id
                else:
                    identifier = id(obj)
                if identifier in self.linker.keys():
                    raise KeyError("Object already exists")

                obj_size = _sys__getsizeof(obj)
                if ((_PassportIntermediary.project_size is None or
                            _PassportIntermediary.project_size == _Constants.LARGE_APPLICATION) and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.75:
                        self._logger.log_development("No single object is recommended to take up \
more than 75% of the assigned memory")

                elif (_PassportIntermediary.project_size == _Constants.MEDIUM_APPLICATION and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.5:
                        self._logger.log_development("No single object is recommended to take up \
more than 50% of the assigned memory")

                elif (_PassportIntermediary.project_size == _Constants.SMALL_APPLICATION and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.25:
                        self._logger.log_development("No single object is recommended to take up \
more than 25% of the assigned memory")

                if obj_size > self.max_obj_size:
                    self.max_obj_size = obj_size
                relative_object_creation_time = obj_size / self.max_obj_size
                if object_creation_time is None:
                    relative_object_creation_time = 1
                else:
                    if object_creation_time > self.max_obj_creation_time:
                        self.max_obj_creation_time = object_creation_time
                    relative_object_creation_time = object_creation_time / self.max_obj_creation_time
                if object_lifetime is None:
                    object_lifetime = self.object_lifetime * ((relative_object_creation_time + relative_object_creation_time) / 2)
                current_time = str(_time__perf_counter())
                self.linker[identifier] = current_time
                self.objects[current_time] = [
                    obj,
                    identifier,
                    object_lifetime,
                    object_creation_time,
                    recreatable_object,
                    stay_in_memory]

                object_priority = object_lifetime+_time__perf_counter()

                if self.manager_thread_organized_data.peek_next_priority() > object_priority:
                    self.manager_thread_organized_data_minimum_priority_changed = True

                self.manager_thread_organized_data.add(identifier, object_priority)

                self.total_size += obj_size
                return identifier
            else:
                with self.memory_manager_thread_lock:
                    if recreatable_object is False:
                        try:
                            byte_data = _dill__dumps(obj)
                            _dill__loads(byte_data)
                            stay_in_memory = False
                        except:
                            stay_in_memory = True

                    if custom_id is not None:
                        identifier = custom_id
                    else:
                        identifier = id(obj)
                    if identifier in self.linker.keys():
                        raise KeyError("Object already exists")

                    obj_size = _sys__getsizeof(obj)
                    if ((_PassportIntermediary.project_size is None or
                                _PassportIntermediary.project_size == _Constants.LARGE_APPLICATION) and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.75:
                            self._logger.log_development("No single object is recommended to take up \
more than 75% of the assigned memory")

                    elif (_PassportIntermediary.project_size == _Constants.MEDIUM_APPLICATION and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.5:
                            self._logger.log_development("No single object is recommended to take up \
more than 50% of the assigned memory")

                    elif (_PassportIntermediary.project_size == _Constants.SMALL_APPLICATION and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.25:
                            self._logger.log_development("No single object is recommended to take up \
more than 25% of the assigned memory")

                    if obj_size > self.max_obj_size:
                        self.max_obj_size = obj_size
                    relative_object_creation_time = obj_size / self.max_obj_size
                    if object_creation_time is None:
                        relative_object_creation_time = 1
                    else:
                        if object_creation_time > self.max_obj_creation_time:
                            self.max_obj_creation_time = object_creation_time
                        relative_object_creation_time = object_creation_time / self.max_obj_creation_time
                    if object_lifetime is None:
                        object_lifetime = self.object_lifetime * ((relative_object_creation_time + relative_object_creation_time) / 2)

                    current_time = str(_time__perf_counter())
                    self.linker[identifier] = current_time
                    self.objects[current_time] = [
                        obj,
                        identifier,
                        object_lifetime,
                        object_creation_time,
                        recreatable_object,
                        stay_in_memory]

                    self.manager_thread_organized_data.add(identifier, object_lifetime+_time__perf_counter())

                    self.total_size += obj_size
                    return identifier
        else:
            raise Exception("Memory management is disabled")

    def get_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    current_time = str(_time__perf_counter())
                    obj = self.objects[self.linker[obj_id]][0]
                    obj_lifetime = self.objects[self.linker[obj_id]][2]
                    obj_creation_time = self.objects[self.linker[obj_id]][3]
                    obj_recreatable_object = self.objects[self.linker[obj_id]][4]
                    obj_stay_in_memory = self.objects[self.linker[obj_id]][5]
                    obj_time = self.linker[obj_id]
                    del self.linker[self.objects[obj_time][1]]
                    del self.objects[obj_time]
                    self.linker[obj_id] = current_time
                    self.objects[current_time] = [
                        obj,
                        obj_id,
                        obj_lifetime,
                        obj_creation_time,
                        obj_recreatable_object,
                        obj_stay_in_memory]

                    self.manager_thread_organized_data.update_priority(obj_id, object_lifetime)

                    return obj
                elif obj_id in self.temporary_files:
                    self._logger.log_development("Loading object w/ ID: '{}' from temporary file.", variables=[obj_id])
                    with open(self.temporary_files[obj_id], "rb") as file:
                        (stored_object,
                            identifier,
                            object_lifetime,
                            object_creation_time,
                            recreatable_object,
                            stay_in_memory) = _dill__loads(file.read())

                    self.add_object(
                        stored_object,
                        obj_id,
                        object_lifetime=object_lifetime,
                        object_creation_time=object_creation_time,
                        recreatable_object=recreatable_object,
                        pre_locked=True)

                    _os__remove(self.temporary_files[obj_id])
                    del self.temporary_files[obj_id]
                    return stored_object
        else:
            raise Exception("Memory management is disabled")

    def remove_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    self._logger.log_development("Removing object w/ ID: \
'{}' from memory.", variables=[obj_id])

                    self.manager_thread_organized_data.remove_item(obj_id)

                    self.linker[obj_id] = None
                    del self.linker[obj_id]
                    self.objects[obj_id] = None
                    del self.objects[obj_id]
                    _gc__collect()
                    return True
                elif obj_id in self.temporary_files:
                    self._logger.log_development("Removing temporary memory object w/ ID: \
'{}' from disk.", variables=[obj_id])

                    _os__remove(self.temporary_files[obj_id])
                    del self.temporary_files[obj_id]
                    _gc__collect()
                    return True
                return False
        else:
            raise Exception("Memory management is disabled")

    def _manager_thread_organized_data_is_not_empty(self):
        return self.enable_memory_management is False or (not self.manager_thread_organized_data.is_empty())

    def _manager_thread_wait_for_expiry(self):
        return self.manager_thread_organized_data.peek_next_priority() - _time__perf_counter() <= 0 or self.manager_thread_organized_data_minimum_priority_changed or self.enable_memory_management is False

    def object_dictionary_manager(self):
        try:
            while self.enable_memory_management:
                if self.total_size / self.target_size > 0.9:
                    self._logger.log_warning("Caution - memory management utilization \
is currently at: {}%. Consider \
lowering this percentage before performance is negatively affected.", variables=[round((self.total_size / self.target_size)*100, 2)])

                if self.total_size / self.target_size >= 1:
                    self._logger.log_warning("Caution - memory management utilization is \
currently at or above the target threshold. Performance may be negatively affected \
as PMMA attempts to correct this.")
                if self.manager_thread_organized_data.is_empty():
                    _waiting__wait(self._manager_thread_organized_data_is_not_empty)
                else:
                    _waiting__wait(self._manager_thread_wait_for_expiry)
                    if not self.manager_thread_organized_data.peek_next_priority() - _time__perf_counter() <= 0:
                        continue
                    items_to_remove = self.manager_thread_organized_data.remove_highest_priority()
                    with self.memory_manager_thread_lock:
                        for key in items_to_remove:
                            obj_time = self.linker[key]
                            try:
                                recreatable_object = self.objects[obj_time][3]
                                stay_in_memory = self.objects[obj_time][4]
                                if stay_in_memory is False:
                                    self.total_size -= _sys__getsizeof(self.objects[obj_time][0])
                                    if not recreatable_object:
                                        self._logger.log_information("Dumping object w/ ID: \
'{}' to temporary file.", variables=[self.objects[obj_time][1]])

                                        with _tempfile__NamedTemporaryFile(
                                                dir=self.memory_management_directory,
                                                delete=False) as file:

                                            file_name = file.name
                                            _dill__dump(self.objects[obj_time], file)

                                        self.temporary_files[self.objects[obj_time][1]] = file_name
                                        self._logger.log_information("Dumped object w/ ID: \
'{}' to temporary file.", variables=[self.objects[obj_time][1]])

                                    self._logger.log_information("Removing object w/ ID: \
'{}' from memory.", variables=[self.objects[obj_time][1]])

                                    self.manager_thread_organized_data.remove_item(self.objects[obj_time][1])

                                    self.linker[self.objects[obj_time][1]] = None
                                    del self.linker[self.objects[obj_time][1]]
                                    self.objects[obj_time] = None
                                    del self.objects[obj_time]
                                    _gc__collect()
                            except FileNotFoundError as error:
                                raise error

                            except Exception as error:
                                print(error)
                                print(_traceback__format_exc())

        except Exception as error:
            print(error)
            self.enable_memory_management = False
            self.linker = {}
            self.objects = {}