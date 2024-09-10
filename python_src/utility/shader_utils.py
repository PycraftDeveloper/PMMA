import threading as _threading
import gc as _gc

import waiting as _waiting

from pmma.python_src.constants import Constants

from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.error_utils import ShaderReferenceManagerNotInitializedError as _ShaderReferenceManagerNotInitializedError

class ShaderIntermediary:
    loaded_shaders_from_file = {}

class LoadedShaderReferenceManager:
    def __init__(self):
        _initialize(self, unique_instance=Constants.SHADER_REFERENCE_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self._reference_manager_thread = _threading.Thread(target=self.reference_manager)
        self._reference_manager_thread.daemon = True
        self._reference_manager_thread.name = "LoadedShaderReferenceManager:Reference_Checker_Thread"
        self._reference_manager_thread.start()

        self._enable_reference_checking = True
        self._shader_intermediary = ShaderIntermediary
        self._loaded_shaders_from_file_changed = False

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._enable_reference_checking = False

            self._reference_manager_thread.join()

            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def wait_for_shader_filling(self):
        return self._loaded_shaders_from_file_changed or self._enable_reference_checking is False

    def reference_manager(self):
        while self._enable_reference_checking:
            _waiting.wait(self.wait_for_shader_filling)
            if self._enable_reference_checking is False:
                break
            if self._shader_intermediary.loaded_shaders_from_file == {}:
                continue

            self._loaded_shaders_from_file_changed = False

            for shader in self._shader_intermediary.loaded_shaders_from_file:
                shader_object = self._shader_intermediary.loaded_shaders_from_file[shader]
                if shader_object["reference_count"] == 0:
                    del self._shader_intermediary.loaded_shaders_from_file[shader]

class ShaderManager:
    def __init__(self):
        _initialize(self)

        if not Constants.SHADER_REFERENCE_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            raise _ShaderReferenceManagerNotInitializedError()

        self._shader_reference_manager: "LoadedShaderReferenceManager"= _Registry.pmma_module_spine[Constants.SHADER_REFERENCE_MANAGER_OBJECT]

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add_shader_from_file(self, file_name, vertex=None, fragment=None, using_gl_point_size_syntax=False, uniform_values=[], buffer_names=[]):
        if not file_name in ShaderIntermediary.loaded_shaders_from_file:
            ShaderIntermediary.loaded_shaders_from_file[file_name] = {"vertex": vertex, "fragment": fragment, "reference_count": 1, "using_gl_point_size_syntax": using_gl_point_size_syntax, "uniform_values": uniform_values, "buffer_names":buffer_names}

    def check_if_shader_exists(self, file_name, shader_type=Constants.BOTH):
        if file_name in ShaderIntermediary.loaded_shaders_from_file:
            if shader_type == Constants.BOTH:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"] is not None and ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"] is not None
            elif shader_type == Constants.VERTEX_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"] is not None
            elif shader_type == Constants.FRAGMENT_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"] is not None
        return False

    def get_shader(self, file_name, shader_type=Constants.BOTH):
        if self.check_if_shader_exists(file_name, shader_type):
            ShaderIntermediary.loaded_shaders_from_file[file_name]["reference_count"] += 1
            if shader_type == Constants.BOTH:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"], ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"], ShaderIntermediary.loaded_shaders_from_file[file_name]["using_gl_point_size_syntax"], ShaderIntermediary.loaded_shaders_from_file[file_name]["uniform_values"].copy(), ShaderIntermediary.loaded_shaders_from_file[file_name]["buffer_names"].copy()
            elif shader_type == Constants.VERTEX_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"], ShaderIntermediary.loaded_shaders_from_file[file_name]["using_gl_point_size_syntax"], ShaderIntermediary.loaded_shaders_from_file[file_name]["uniform_values"].copy(), ShaderIntermediary.loaded_shaders_from_file[file_name]["buffer_names"].copy()
            elif shader_type == Constants.FRAGMENT_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"], ShaderIntermediary.loaded_shaders_from_file[file_name]["using_gl_point_size_syntax"], ShaderIntermediary.loaded_shaders_from_file[file_name]["uniform_values"].copy(), ShaderIntermediary.loaded_shaders_from_file[file_name]["buffer_names"].copy()

    def remove_shader_from_memory(self, file_name):
        if file_name in ShaderIntermediary.loaded_shaders_from_file:
            ShaderIntermediary.loaded_shaders_from_file[file_name]["reference_count"] -= 1
            self._shader_reference_manager._loaded_shaders_from_file_changed = True