import subprocess
import sys
import os
import threading

from pmma.python_src.constants import Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry

def setup():
    try:
        os.mkdir(f"{_Registry.base_path}{os.sep}bin")
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
            exit_code = subprocess.call([sys.executable, f"{_Registry.base_path}{Constants.PATH_SEPARATOR}c_setup.py", "build_ext", "--build-lib", f"{_Registry.base_path}{Constants.PATH_SEPARATOR}bin", "--build-temp", "temporary"])
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
    thread = threading.Thread(target=compile_intermediary)
    thread.name = "cython_compile"
    thread.start()
    return thread