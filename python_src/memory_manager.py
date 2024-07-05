import time
import threading

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class MemoryManager:
    def __init__(self):
        if Constants.MEMORYMANAGER_OBJECT in Registry.pmma_module_spine.keys():
            raise Exception("MemoryManager object already exists")

        self.objects = {}
        self.linker = {}
        self.object_lifetime = 2.5
        self.manager_thread = threading.Thread(target=self.object_dictionary_manager)
        self.manager_thread.daemon = True
        self.manager_thread.start()

        Registry.pmma_module_spine[Constants.MEMORYMANAGER_OBJECT] = self

    def add_object(self, obj, custom_id=None):
        if custom_id is not None:
            identifier = custom_id
        else:
            identifier = id(obj)
        if identifier in self.linker.keys():
            raise KeyError("Object already exists")
        current_time = str(time.perf_counter())
        self.linker[identifier] = current_time
        self.objects[current_time] = [obj, identifier]
        return identifier

    def get_object(self, obj_id):
        if obj_id in self.linker:
            current_time = str(time.perf_counter())
            obj = self.objects[self.linker[obj_id]][0]
            obj_time = self.linker[obj_id]
            del self.linker[self.objects[obj_time][1]]
            del self.objects[obj_time]
            self.linker[obj_id] = current_time
            self.objects[current_time] = [obj, obj_id]
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
                    if current_time - float(obj_time) > self.object_lifetime:
                        del self.linker[self.objects[obj_time][1]]
                        del self.objects[obj_time]
                except Exception as error:
                    print(error)

            time.sleep(self.object_lifetime/2)