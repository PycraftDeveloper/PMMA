from sys import executable as _sys__executable
from os import devnull as _os__devnull

from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.constants import Constants as _Constants

class CythonIntermediary:
    def __init__(self):
        """
        🟩 **R** -
        """
        self._subprocess__module = _ModuleManager.import_module("subprocess")
        self._os__module = _ModuleManager.import_module("os")
        self._threading__module = _ModuleManager.import_module("threading")

        self._file__module = _ModuleManager.import_module("pmma.python_src.file")

    def setup(self):
        """
        🟩 **R** -
        """
        try:
            self._os__module.mkdir(self._file__module.path_builder(_Registry.base_path, "bin"))
        except FileExistsError:
            pass

    def compile_libraries(self):
        """
        🟩 **R** -
        """
        try:
            import pmma.bin.perlin_noise
            import pmma.bin.extended_perlin_noise
            import pmma.bin.number_converter
            import pmma.bin.math_utils
            import pmma.bin.render_pipeline_utils
            import pmma.bin.render_pipeline_manager_utils
            _Registry.cython_acceleration_available = True
        except ImportError:
            try:
                if _Registry.development_mode:
                    self._subprocess__module.call([_sys__executable, f"{_Registry.base_path}{_Constants.PATH_SEPARATOR}c_setup.py", "build_ext", "--build-lib", f"{_Registry.base_path}{_Constants.PATH_SEPARATOR}bin", "--build-temp", "temporary"])
                else:
                    with open(_os__devnull, 'w') as devnull:
                        self._subprocess__module.call([_sys__executable, f"{_Registry.base_path}{_Constants.PATH_SEPARATOR}c_setup.py", "build_ext", "--build-lib", f"{_Registry.base_path}{_Constants.PATH_SEPARATOR}bin", "--build-temp", "temporary"], stdout=devnull, stderr=devnull)
            except:
                pass
            _Registry.cython_acceleration_available = self.check_for_compiled_libraries()

    def check_for_compiled_libraries(self):
        """
        🟩 **R** -
        """
        try:
            import pmma.bin.perlin_noise
            import pmma.bin.extended_perlin_noise
            import pmma.bin.number_converter
            import pmma.bin.math_utils
            import pmma.bin.render_pipeline_utils
            import pmma.bin.render_pipeline_manager_utils
            _Registry.cython_acceleration_available = True
        except ImportError:
            _Registry.cython_acceleration_available = False

        return _Registry.cython_acceleration_available

    def compile_intermediary(self):
        """
        🟩 **R** -
        """
        if self.check_for_compiled_libraries() is False:
            self.compile_libraries()

    def compile(self):
        """
        🟩 **R** -
        """
        thread = self._threading__module.Thread(target=self.compile_intermediary)
        thread.name = "cython_compile"
        thread.start()
        return thread