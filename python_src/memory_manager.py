import time
import threading
import sys
import tempfile
import os
import shutil
import gc
import traceback

import psutil
import dill

from pmma.python_src.file import path_builder

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.passport import PassportIntermediary

class MemoryManager:
    def __init__(
            self,
            object_lifetime=2.5,
            target_size=Constants.AUTOMATIC):

        initialize(self, unique_instance=Constants.MEMORYMANAGER_OBJECT, add_to_pmma_module_spine=True)

        self.attributes = []

        self.limited_max_size = False
        if target_size == Constants.AUTOMATIC:
            target_size = (1/8) * psutil.virtual_memory().available
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

        if self.assigned_target_size is False and PassportIntermediary.project_size is not None:
            log_development("For applications with a defined project size, \
leaving the target size variable can be dangerous.")

        self.objects = {}
        self.linker = {}
        self.object_lifetime = object_lifetime
        self.manager_thread = threading.Thread(target=self.object_dictionary_manager)
        self.manager_thread.daemon = True
        self.manager_thread.start()
        self.max_obj_creation_time = float("-inf")
        self.max_obj_size = 0
        self.total_size = 0

        self.temporary_files = {}

        self.enable_memory_management = True

        self.memory_manager_thread_lock = threading.Lock()

        self.memory_management_directory = path_builder(
            Registry.base_path,
            "temporary",
            "memory management dumps")

        shutil.rmtree(
            self.memory_management_directory,
            ignore_errors=True)

        os.mkdir(self.memory_management_directory)

    def __del__(self):
        if self._shut_down is False:
            self.enable_memory_management = False

            shutil.rmtree(
                self.memory_management_directory,
                ignore_errors=True)

            os.mkdir(self.memory_management_directory)

            self.linker = {}
            self.objects = {}

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
                        byte_data = dill.dumps(obj)
                        dill.loads(byte_data)
                        stay_in_memory = False
                    except:
                        stay_in_memory = True

                if custom_id is not None:
                    identifier = custom_id
                else:
                    identifier = id(obj)
                if identifier in self.linker.keys():
                    raise KeyError("Object already exists")

                obj_size = sys.getsizeof(obj)
                if ((PassportIntermediary.project_size is None or
                            PassportIntermediary.project_size == Constants.LARGE_APPLICATION) and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.75:
                        log_development("No single object is recommended to take up \
more than 75% of the assigned memory")

                elif (PassportIntermediary.project_size == Constants.MEDIUM_APPLICATION and
                        self.assigned_target_size is False):

                    if obj_size / self.target_size > 0.5:
                        log_development("No single object is recommended to take up \
more than 50% of the assigned memory")

                elif (PassportIntermediary.project_size == Constants.SMALL_APPLICATION and
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
                current_time = str(time.perf_counter())
                self.linker[identifier] = current_time
                self.objects[current_time] = [
                    obj,
                    identifier,
                    object_lifetime,
                    object_creation_time,
                    recreatable_object,
                    stay_in_memory]

                self.total_size += obj_size
                return identifier
            else:
                with self.memory_manager_thread_lock:
                    if recreatable_object is False:
                        try:
                            byte_data = dill.dumps(obj)
                            dill.loads(byte_data)
                            stay_in_memory = False
                        except:
                            stay_in_memory = True

                    if custom_id is not None:
                        identifier = custom_id
                    else:
                        identifier = id(obj)
                    if identifier in self.linker.keys():
                        raise KeyError("Object already exists")

                    obj_size = sys.getsizeof(obj)
                    if ((PassportIntermediary.project_size is None or
                                PassportIntermediary.project_size == Constants.LARGE_APPLICATION) and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.75:
                            log_development("No single object is recommended to take up \
more than 75% of the assigned memory")

                    elif (PassportIntermediary.project_size == Constants.MEDIUM_APPLICATION and
                            self.assigned_target_size is False):

                        if obj_size / self.target_size > 0.5:
                            log_development("No single object is recommended to take up \
more than 50% of the assigned memory")

                    elif (PassportIntermediary.project_size == Constants.SMALL_APPLICATION and
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

                    current_time = str(time.perf_counter())
                    self.linker[identifier] = current_time
                    self.objects[current_time] = [
                        obj,
                        identifier,
                        object_lifetime,
                        object_creation_time,
                        recreatable_object,
                        stay_in_memory]

                    self.total_size += obj_size
                    return identifier
        else:
            raise Exception("Memory management is disabled")

    def get_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    current_time = str(time.perf_counter())
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

                    return obj
                elif obj_id in self.temporary_files:
                    log_development(f"Loading object w/ ID: '{obj_id}' from temporary file.")
                    with open(self.temporary_files[obj_id], "rb") as file:
                        (stored_object,
                            identifier,
                            object_lifetime,
                            object_creation_time,
                            recreatable_object,
                            stay_in_memory) = dill.loads(file.read())

                    self.add_object(
                        stored_object,
                        obj_id,
                        object_lifetime=object_lifetime,
                        object_creation_time=object_creation_time,
                        recreatable_object=recreatable_object,
                        pre_locked=True)

                    os.remove(self.temporary_files[obj_id])
                    del self.temporary_files[obj_id]
                    return stored_object
        else:
            raise Exception("Memory management is disabled")

    def remove_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    log_development(f"Removing object w/ ID: \
'{self.objects[obj_id][1]}' from memory.")

                    self.linker[self.objects[obj_id][1]] = None
                    del self.linker[self.objects[obj_id][1]]
                    self.objects[obj_id] = None
                    del self.objects[obj_id]
                    gc.collect()
                    return True
                elif obj_id in self.temporary_files:
                    log_development(f"Removing temporary memory object w/ ID: \
'{self.objects[obj_id][1]}' from disk.")

                    os.remove(self.temporary_files[obj_id])
                    del self.temporary_files[obj_id]
                    gc.collect()
                    return True
                return False
        else:
            raise Exception("Memory management is disabled")

    def object_dictionary_manager(self):
        try:
            while self.enable_memory_management:
                current_time = time.perf_counter()
                if self.total_size / self.target_size > 0.9:
                    log_warning(f"Caution - memory management utilization \
is currently at: {round((self.total_size / self.target_size)*100, 2)}%. Consider \
lowering this percentage before performance is negatively affected.")

                if self.total_size / self.target_size >= 1:
                    log_warning(f"Caution - memory management utilization is \
currently at or above the target threshold. Performance may be negatively affected \
as PMMA attempts to correct this.")

                with self.memory_manager_thread_lock:
                    for obj_time in list(self.objects.keys()):
                        try:
                            recreatable_object = self.objects[obj_time][3]
                            stay_in_memory = self.objects[obj_time][4]
                            if stay_in_memory is False:
                                if current_time - float(obj_time) > self.objects[obj_time][2]:
                                    self.total_size -= sys.getsizeof(self.objects[obj_time][0])
                                    if not recreatable_object:
                                        log_development(f"Dumping object w/ ID: \
'{self.objects[obj_time][1]}' to temporary file.")

                                        with tempfile.NamedTemporaryFile(
                                                dir=self.memory_management_directory,
                                                delete=False) as file:

                                            file_name = file.name
                                            dill.dump(self.objects[obj_time], file)

                                        self.temporary_files[self.objects[obj_time][1]] = file_name
                                        log_development(f"Dumped object w/ ID: \
'{self.objects[obj_time][1]}' to temporary file.")

                                    log_development(f"Removing object w/ ID: \
'{self.objects[obj_time][1]}' from memory.")

                                    self.linker[self.objects[obj_time][1]] = None
                                    del self.linker[self.objects[obj_time][1]]
                                    self.objects[obj_time] = None
                                    del self.objects[obj_time]
                                    gc.collect()
                        except FileNotFoundError as error:
                            raise error

                        except Exception as error:
                            print(error)
                            print(traceback.format_exc())

                if Registry.power_saving_mode:
                    time.sleep(1/15)
                else:
                    time.sleep(1/30)
        except:
            self.enable_memory_management = False
            self.linker = {}
            self.objects = {}