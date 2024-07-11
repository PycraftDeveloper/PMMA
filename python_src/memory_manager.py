import time
import threading
import sys

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class MemoryManager:
    def __init__(self, object_lifetime=2.5):
        if Constants.MEMORYMANAGER_OBJECT in Registry.pmma_module_spine.keys():
            raise Exception("MemoryManager object already exists")

        self.objects = {}
        self.linker = {}
        self.object_lifetime = object_lifetime
        self.manager_thread = threading.Thread(target=self.object_dictionary_manager)
        self.manager_thread.daemon = True
        self.manager_thread.start()
        self.max_obj_creation_time = 0
        self.max_obj_size = 0
        self.total_size = 0

        Registry.pmma_module_spine[Constants.MEMORYMANAGER_OBJECT] = self

    def add_object(self, obj, custom_id=None, object_lifetime=None, object_creation_time=None):
        if custom_id is not None:
            identifier = custom_id
        else:
            identifier = id(obj)
        if identifier in self.linker.keys():
            raise KeyError("Object already exists")

        obj_size = sys.getsizeof(obj)
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
            object_lifetime = self.object_lifetime * (relative_object_creation_time + relative_object_creation_time) / 2
            #print(object_lifetime)
        current_time = str(time.perf_counter())
        self.linker[identifier] = current_time
        self.objects[current_time] = [obj, identifier, object_lifetime]
        self.total_size += obj_size
        return identifier

    def get_object(self, obj_id):
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
        return None

    def remove_object(self, obj_id):
        if obj_id in self.linker:
            del self.linker[self.objects[self.linker[obj_id]][1]]
            del self.objects[self.linker[obj_id]]
            return True
        return False

    def object_dictionary_manager(self):
        while True:
            current_time = time.perf_counter()
            for obj_time in list(self.objects.keys()):
                try:
                    if current_time - float(obj_time) > self.objects[obj_time][2]:
                        self.total_size -= sys.getsizeof(self.objects[obj_time][0])
                        del self.linker[self.objects[obj_time][1]]
                        del self.objects[obj_time]
                except Exception as error:
                    print(error)

            time.sleep(1/30)