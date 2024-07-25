import time
import threading
import sys

import psutil

import pmma.python_src.core as core
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.passport import PassportIntermediary

class MemoryManager:
    def __init__(self, object_lifetime=2.5, target_size=Constants.AUTOMATIC):
        if Constants.MEMORYMANAGER_OBJECT in Registry.pmma_module_spine.keys():
            raise Exception("MemoryManager object already exists")

        self.limited_max_size = False
        if target_size == Constants.AUTOMATIC:
            target_size = (1/8) * psutil.virtual_memory().available
            if target_size > 1000000000:
                self.target_size = 1000000000 # 1 GB
                self.limited_max_size = True
                core.log_development(f"Limiting targeted memory management size to 1 GB, from automatically calculated size of: {target_size/1000000000} GB. If needed, this target will be raised on the fly.")
            else:
                self.target_size = target_size

            core.log_development(f"Max memory management size has not been set, therefore PMMA has determined that: {self.target_size/1000000000} GB shall be targeted. Consider specifying a max size yourself if you find yourself exceeding this limit.")

            self.assigned_target_size = False
        else:
            self.assigned_target_size = True
            self.target_size = target_size

        core.log_development(f"Note, PMMA will attempt to target: {self.target_size/1000000000} GB as its max size for memory management, however this is a target NOT a maximum, and this limit can be exceeded, with PMMA automatically taking corrective action in such cases. Additionally, this memory will not be used until it's needed by PMMA.")

        if self.assigned_target_size is False and PassportIntermediary.project_size is not None:
            core.log_development("For applications with a defined project size, leaving the target size variable can be dangerous.")

        self.objects = {}
        self.linker = {}
        self.object_lifetime = object_lifetime
        self.manager_thread = threading.Thread(target=self.object_dictionary_manager)
        self.manager_thread.daemon = True
        self.manager_thread.start()
        self.max_obj_creation_time = 0
        self.max_obj_size = 0
        self.total_size = 0

        self.enable_memory_management = True

        self.memory_manager_thread_lock = threading.Lock()

        Registry.pmma_module_spine[Constants.MEMORYMANAGER_OBJECT] = self

    def add_object(self, obj, custom_id=None, object_lifetime=None, object_creation_time=None):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if custom_id is not None:
                    identifier = custom_id
                else:
                    identifier = id(obj)
                if identifier in self.linker.keys():
                    raise KeyError("Object already exists")

                obj_size = sys.getsizeof(obj)
                if (PassportIntermediary.project_size is None or PassportIntermediary.project_size == Constants.LARGE_APPLICATION) and self.assigned_target_size is False:
                    if obj_size / self.target_size > 0.75:
                        core.log_development("No single object is recommended to take up more than 75% of the assigned memory")
                elif PassportIntermediary.project_size == Constants.MEDIUM_APPLICATION and self.assigned_target_size is False:
                    if obj_size / self.target_size > 0.5:
                        core.log_development("No single object is recommended to take up more than 50% of the assigned memory")
                elif PassportIntermediary.project_size == Constants.SMALL_APPLICATION and self.assigned_target_size is False:
                    if obj_size / self.target_size > 0.25:
                        core.log_development("No single object is recommended to take up more than 25% of the assigned memory")

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
                self.objects[current_time] = [obj, identifier, object_lifetime]
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
                    obj_time = self.linker[obj_id]
                    del self.linker[self.objects[obj_time][1]]
                    del self.objects[obj_time]
                    self.linker[obj_id] = current_time
                    self.objects[current_time] = [obj, obj_id, obj_lifetime]
                    return obj
        else:
            raise Exception("Memory management is disabled")

    def remove_object(self, obj_id):
        if self.enable_memory_management:
            with self.memory_manager_thread_lock:
                if obj_id in self.linker:
                    del self.linker[self.objects[self.linker[obj_id]][1]]
                    del self.objects[self.linker[obj_id]]
                    return True
                return False
        else:
            raise Exception("Memory management is disabled")

    def object_dictionary_manager(self):
        try:
            while True:
                current_time = time.perf_counter()
                if self.total_size / self.target_size > 0.9:
                    core.log_warning(f"Caution - memory management utilization is currently at: {round((self.total_size / self.target_size)*100, 2)}%. Consider lowering this percentage before performance is negatively affected.")
                if self.total_size / self.target_size >= 1:
                    core.log_warning(f"Caution - memory management utilization is currently at or above the target threshold. Performance may be negatively affected as PMMA attempts to correct this.")
                with self.memory_manager_thread_lock:
                    for obj_time in list(self.objects.keys()):
                        try:
                            if current_time - float(obj_time) > self.objects[obj_time][2]:
                                self.total_size -= sys.getsizeof(self.objects[obj_time][0])
                                del self.linker[self.objects[obj_time][1]]
                                del self.objects[obj_time]
                        except Exception as error:
                            print(error)

                time.sleep(1/30)
        except:
            self.enable_memory_management = False
            self.linker = {}
            self.objects = {}