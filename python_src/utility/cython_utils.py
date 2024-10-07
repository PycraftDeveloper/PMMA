from subprocess import call as _subprocess__call
from sys import executable as _sys__executable
from os import mkdir as _os__mkdir
from threading import Thread as _threading__Thread

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.registry_utils import Registry as _Registry

def setup():
    try:
        _os__mkdir(_path_builder(_Registry.base_path, "bin"))
    except FileExistsError:
        pass

def compile_libraries():
    try:
        import pmma.bin.perlin_noise
        import pmma.bin.extended_perlin_noise
        import pmma.bin.number_converter
        _Registry.cython_acceleration_available = True
    except ImportError:
        try:
            exit_code = _subprocess__call([_sys__executable, f"{_Registry.base_path}{_Constants.PATH_SEPARATOR}c_setup.py", "build_ext", "--build-lib", f"{_Registry.base_path}{_Constants.PATH_SEPARATOR}bin", "--build-temp", "temporary"])
            _Registry.cython_acceleration_available = exit_code == 0
        except:
            _Registry.cython_acceleration_available = False

def check_for_compiled_libraries():
    try:
        import pmma.bin.perlin_noise
        import pmma.bin.extended_perlin_noise
        import pmma.bin.number_converter
        _Registry.cython_acceleration_available = True
    except ImportError:
        _Registry.cython_acceleration_available = False

    return _Registry.cython_acceleration_available

def compile_intermediary():
    if check_for_compiled_libraries() is False:
        compile_libraries()

def compile():
    thread = _threading__Thread(target=compile_intermediary)
    thread.name = "cython_compile"
    thread.start()
    return thread