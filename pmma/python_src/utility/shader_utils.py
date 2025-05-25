from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ShaderIntermediary:
    """
    🟩 **R** -
    """
    loaded_shaders_from_file = {}

class LoadedShaderReferenceManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.SHADER_REFERENCE_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        self._threading__module = _ModuleManager.import_module("threading")

        self._waiting__module = _ModuleManager.import_module("waiting")

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self.reference_manager_lock = self._threading__module.Lock()

        self._reference_manager_thread = self._threading__module.Thread(target=self.reference_manager)
        self._reference_manager_thread.daemon = True
        self._reference_manager_thread.name = "LoadedShaderReferenceManager: Reference_Checker_Thread"

        self._enable_reference_checking = True
        self._shader_intermediary = ShaderIntermediary
        self._loaded_shaders_from_file_changed = False

        self._reference_manager_thread.start()

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._enable_reference_checking = False

            self._reference_manager_thread.join()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def wait_for_shader_filling(self):
        """
        🟩 **R** -
        """
        return self._loaded_shaders_from_file_changed or self._enable_reference_checking is False

    def reference_manager(self):
        """
        🟩 **R** -
        """
        while self._enable_reference_checking:
            self._waiting__module.wait(self.wait_for_shader_filling)
            if self._enable_reference_checking is False:
                break
            if self._shader_intermediary.loaded_shaders_from_file == {}:
                continue

            self._loaded_shaders_from_file_changed = False

            garbage_elements = []
            with self.reference_manager_lock:
                for shader in self._shader_intermediary.loaded_shaders_from_file:
                    shader_object = self._shader_intermediary.loaded_shaders_from_file[shader]
                    if shader_object["reference_count"] == 0:
                        garbage_elements.append(shader)

                for element in garbage_elements:
                    del self._shader_intermediary.loaded_shaders_from_file[element]

class ShaderManager:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SHADER_REFERENCE_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SHADER_REFERENCE_MANAGER_OBJECT)
            LoadedShaderReferenceManager()

        self._shader_reference_manager: "LoadedShaderReferenceManager"= _Registry.pmma_module_spine[_InternalConstants.SHADER_REFERENCE_MANAGER_OBJECT]

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def add_shader_from_file(self, file_name, vertex=None, fragment=None, using_gl_point_size_syntax=False, uniform_values=[], buffer_names=[]):
        """
        🟩 **R** -
        """
        if not file_name in ShaderIntermediary.loaded_shaders_from_file:
            with self._shader_reference_manager.reference_manager_lock:
                ShaderIntermediary.loaded_shaders_from_file[file_name] = {"vertex": vertex, "fragment": fragment, "reference_count": 1, "using_gl_point_size_syntax": using_gl_point_size_syntax, "uniform_values": uniform_values, "buffer_names":buffer_names}

    def check_if_shader_exists(self, file_name, shader_type=_Constants.BOTH):
        """
        🟩 **R** -
        """
        if file_name in ShaderIntermediary.loaded_shaders_from_file:
            if shader_type == _Constants.BOTH:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"] is not None and ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"] is not None
            elif shader_type == _Constants.VERTEX_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"] is not None
            elif shader_type == _Constants.FRAGMENT_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"] is not None
        return False

    def get_shader(self, file_name, shader_type=_Constants.BOTH):
        """
        🟩 **R** -
        """
        if self.check_if_shader_exists(file_name, shader_type):
            ShaderIntermediary.loaded_shaders_from_file[file_name]["reference_count"] += 1
            if shader_type == _Constants.BOTH:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"], ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"], ShaderIntermediary.loaded_shaders_from_file[file_name]["using_gl_point_size_syntax"], ShaderIntermediary.loaded_shaders_from_file[file_name]["uniform_values"].copy(), ShaderIntermediary.loaded_shaders_from_file[file_name]["buffer_names"].copy()
            elif shader_type == _Constants.VERTEX_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["vertex"], ShaderIntermediary.loaded_shaders_from_file[file_name]["using_gl_point_size_syntax"], ShaderIntermediary.loaded_shaders_from_file[file_name]["uniform_values"].copy(), ShaderIntermediary.loaded_shaders_from_file[file_name]["buffer_names"].copy()
            elif shader_type == _Constants.FRAGMENT_ONLY:
                return ShaderIntermediary.loaded_shaders_from_file[file_name]["fragment"], ShaderIntermediary.loaded_shaders_from_file[file_name]["using_gl_point_size_syntax"], ShaderIntermediary.loaded_shaders_from_file[file_name]["uniform_values"].copy(), ShaderIntermediary.loaded_shaders_from_file[file_name]["buffer_names"].copy()

    def remove_shader_from_memory(self, file_name):
        """
        🟩 **R** -
        """
        if file_name in ShaderIntermediary.loaded_shaders_from_file:
            with self._shader_reference_manager.reference_manager_lock:
                ShaderIntermediary.loaded_shaders_from_file[file_name]["reference_count"] -= 1
            self._shader_reference_manager._loaded_shaders_from_file_changed = True