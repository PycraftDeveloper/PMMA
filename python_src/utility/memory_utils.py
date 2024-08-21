import time as _time
import threading as _threading
import sys as _sys
import tempfile as _tempfile
import os as _os
import shutil as _shutil
import gc as _gc
import traceback as _traceback

import psutil as _psutil
import dill as _dill
import waiting as _waiting

from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.data_structures import InvertedPriorityList as _InvertedPriorityList

from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class MemoryManagerIntermediary:
    def __init__(
            self,
            object_lifetime=2.5,
            target_size=Constants.AUTOMATIC):

        initialize(self, unique_instance=Constants.MEMORY_MANAGER_INTERMEDIARY_OBJECT, add_to_pmma_module_spine=True)

        self.limited_max_size = False
        if target_size == Constants.AUTOMATIC:
            target_size = (1/8) * _psutil.virtual_memory().available
            if target_size > 1000000000:
                self.target_size = 1000000000 # 1 GB
                self.limited_max_size = True
                log_development(f"Limiting targeted memory management \
size to 1 GB, from automatically calculated size of: {target_size/1000000000} \
GB. If needed, this target will be raised on the fly.")
            else:
                self.target_size = target_size

            log_development(f"Max memory management size has not been set, \
therefore PMMA has determined that: {self.target_size/1000000000} GB shall be \
targeted. Consider specifying a max size yourself if you find yourself exceeding \
this limit.")

            self.assigned_target_size = False
        else:
            self.assigned_target_size = True
            self.target_size = target_size

        log_development(f"Note, PMMA will attempt to target: \
{self.target_size/1000000000} GB as its max size for memory management, \
however this is a target NOT a maximum, and this limit can be exceeded, \
with PMMA automatically taking corrective action in such cases. Additionally, \
this memory will not be used until it's needed by PMMA.")

        if self.assigned_target_size is False and _PassportIntermediary.project_size is not None:
            log_development("For applications with a defined project size, \
leaving the target size variable can be dangerous.")

        self.objects = {}
        self.linker = {}
        self.object_lifetime = object_lifetime
        self.enable_memory_management = True

        self.manager_thread = _threading.Thread(target=self.object_dictionary_manager)
        self.manager_thread.daemon = True
        self.manager_thread.name = "MemoryManagerIntermediary:Object_Memory_Management_Thread"
        self.manager_thread.start()
        self.max_obj_creation_time = float("-inf")
        self.max_obj_size = 0
        self.total_size = 0

        self.manager_thread_organized_data = _InvertedPriorityList()

        self.temporary_files = {}

        self.memory_manager_thread_lock = _threading.Lock()

        self.memory_management_directory = _path_builder(
            Registry.base_path,
            "temporary",
            "memory management dumps")

        _shutil.rmtree(
            self.memory_management_directory,
            ignore_errors=True)

        _os.mkdir(self.memory_management_directory)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self.enable_memory_management = False

            self.manager_thread.join()

            _shutil.rmtree(
                self.memory_management_directory,
                ignore_errors=True)

            _os.mkdir(self.memory_management_directory)

            self.linker = {}
            self.objects = {}
            del self
            if do_garbage_collection:
                _gc.collect()

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
                        byte_data = _dill.dumps(obj)
                        _dill.loads(byte_data)
                        stay_in_memory = False
                    except:
                        stay_in_memory = True

                if custom_id is not None:
                    identifier = custom_id
                else:
                    identifier = id(obj)
                if identifier in self.linker.keys():
                    raise KeyError("Object already exists")

                obj_size = _sys.getsizeof(obj)
                if ((_PassportIntermediary.project_size is None or
                            _PassportIntermediary.project_size == Constants.LARGE_APPLICATION) and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.75:
                        log_development("No single object is recommended to take up \
more than 75% of the assigned memory")

                elif (_PassportIntermediary.project_size == Constants.MEDIUM_APPLICATION and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.5:
                        log_development("No single object is recommended to take up \
more than 50% of the assigned memory")

                elif (_PassportIntermediary.project_size == Constants.SMALL_APPLICATION and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.25:
                        log_development("No single object is recommended to take up \
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
                current_time = str(_time.perf_counter())
                self.linker[identifier] = current_time
                self.objects[current_time] = [
                    obj,
                    identifier,
                    object_lifetime,
                    object_creation_time,
                    recreatable_object,
                    stay_in_memory]

                self.manager_thread_organized_data.add(identifier, object_lifetime+_time.perf_counter())

                self.total_size += obj_size
                return identifier
            else:
                with self.memory_manager_thread_lock:
                    if recreatable_object is False:
                        try:
                            byte_data = _dill.dumps(obj)
                            _dill.loads(byte_data)
                            stay_in_memory = False
                        except:
                            stay_in_memory = True

                    if custom_id is not None:
                        identifier = custom_id
                    else:
                        identifier = id(obj)
                    if identifier in self.linker.keys():
                        raise KeyError("Object already exists")

                    obj_size = _sys.getsizeof(obj)
                    if ((_PassportIntermediary.project_size is None or
                                _PassportIntermediary.project_size == Constants.LARGE_APPLICATION) and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.75:
                            log_development("No single object is recommended to take up \
more than 75% of the assigned memory")

                    elif (_PassportIntermediary.project_size == Constants.MEDIUM_APPLICATION and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.5:
                            log_development("No single object is recommended to take up \
more than 50% of the assigned memory")

                    elif (_PassportIntermediary.project_size == Constants.SMALL_APPLICATION and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.25:
                            log_development("No single object is recommended to take up \
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

                    current_time = str(_time.perf_counter())
                    self.linker[identifier] = current_time
                    self.objects[current_time] = [
                        obj,
                        identifier,
                        object_lifetime,
                        object_creation_time,
                        recreatable_object,
                        stay_in_memory]

                    self.manager_thread_organized_data.add(identifier, object_lifetime+_time.perf_counter())

                    self.total_size += obj_size
                    return identifier
        else:
            raise Exception("Memory management is disabled")

    def get_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    current_time = str(_time.perf_counter())
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
                    log_development(f"Loading object w/ ID: '{obj_id}' from temporary file.")
                    with open(self.temporary_files[obj_id], "rb") as file:
                        (stored_object,
                            identifier,
                            object_lifetime,
                            object_creation_time,
                            recreatable_object,
                            stay_in_memory) = _dill.loads(file.read())

                    self.add_object(
                        stored_object,
                        obj_id,
                        object_lifetime=object_lifetime,
                        object_creation_time=object_creation_time,
                        recreatable_object=recreatable_object,
                        pre_locked=True)

                    _os.remove(self.temporary_files[obj_id])
                    del self.temporary_files[obj_id]
                    return stored_object
        else:
            raise Exception("Memory management is disabled")

    def remove_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    log_development(f"Removing object w/ ID: \
'{obj_id}' from memory.")

                    self.manager_thread_organized_data.remove_item(obj_id)

                    self.linker[obj_id] = None
                    del self.linker[obj_id]
                    self.objects[obj_id] = None
                    del self.objects[obj_id]
                    _gc.collect()
                    return True
                elif obj_id in self.temporary_files:
                    log_development(f"Removing temporary memory object w/ ID: \
'{obj_id}' from disk.")

                    _os.remove(self.temporary_files[obj_id])
                    del self.temporary_files[obj_id]
                    _gc.collect()
                    return True
                return False
        else:
            raise Exception("Memory management is disabled")

    def _manager_thread_organized_data_is_not_empty(self):
        return self.enable_memory_management is False or (not self.manager_thread_organized_data.is_empty())

    def _manager_thread_wait_for_expiry(self):
        return self.manager_thread_organized_data.peek_next_priority() - _time.perf_counter() <= 0 or self.manager_thread_organized_data.changed() or self.enable_memory_management is False

    def object_dictionary_manager(self):
        try:
            while self.enable_memory_management:
                if self.total_size / self.target_size > 0.9:
                    log_warning(f"Caution - memory management utilization \
is currently at: {round((self.total_size / self.target_size)*100, 2)}%. Consider \
lowering this percentage before performance is negatively affected.")

                if self.total_size / self.target_size >= 1:
                    log_warning(f"Caution - memory management utilization is \
currently at or above the target threshold. Performance may be negatively affected \
as PMMA attempts to correct this.")
                if self.manager_thread_organized_data.is_empty():
                    _waiting.wait(self._manager_thread_organized_data_is_not_empty)
                else:
                    _waiting.wait(self._manager_thread_wait_for_expiry)
                    if not self.manager_thread_organized_data.peek_next_priority() - _time.perf_counter() <= 0:
                        continue
                    items_to_remove = self.manager_thread_organized_data.remove_highest_priority()
                    with self.memory_manager_thread_lock:
                        for key in items_to_remove:
                            obj_time = self.linker[key]
                            try:
                                recreatable_object = self.objects[obj_time][3]
                                stay_in_memory = self.objects[obj_time][4]
                                if stay_in_memory is False:
                                    self.total_size -= _sys.getsizeof(self.objects[obj_time][0])
                                    if not recreatable_object:
                                        log_information(f"Dumping object w/ ID: \
'{self.objects[obj_time][1]}' to temporary file.")

                                        with _tempfile.NamedTemporaryFile(
                                                dir=self.memory_management_directory,
                                                delete=False) as file:

                                            file_name = file.name
                                            _dill.dump(self.objects[obj_time], file)

                                        self.temporary_files[self.objects[obj_time][1]] = file_name
                                        log_information(f"Dumped object w/ ID: \
'{self.objects[obj_time][1]}' to temporary file.")

                                    log_information(f"Removing object w/ ID: \
'{self.objects[obj_time][1]}' from memory.")

                                    self.manager_thread_organized_data.remove_item(self.objects[obj_time][1])

                                    self.linker[self.objects[obj_time][1]] = None
                                    del self.linker[self.objects[obj_time][1]]
                                    self.objects[obj_time] = None
                                    del self.objects[obj_time]
                                    _gc.collect()
                            except FileNotFoundError as error:
                                raise error

                            except Exception as error:
                                print(error)
                                print(_traceback.format_exc())

        except Exception as error:
            print(error)
            self.enable_memory_management = False
            self.linker = {}
            self.objects = {}