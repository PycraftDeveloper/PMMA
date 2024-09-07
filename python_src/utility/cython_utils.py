import subprocess
import sys
import os
import threading

from pmma.python_src.utils.registry import Registry as _Registry
from pmma.python_src.constants import Constants

def setup():
    try:
        os.mkdir(f"{Registry.base_path}{os.sep}bin")
    except FileExistsError:
        pass

def compile_libraries():
    try:
        import pmma.bin.perlin_noise
        import pmma.bin.extended_perlin_noise
        Registry.cython_acceleration_available = True
    except ImportError:
        try:
            exit_code = subprocess.call([sys.executable, f"{Registry.base_path}{Constants.PATH_SEPARATOR}c_setup.py", "build_ext", "--build-lib", f"{Registry.base_path}{Constants.PATH_SEPARATOR}bin", "--build-temp", "temporary"])
            Registry.cython_acceleration_available = exit_code == 0
        except:
            Registry.cython_acceleration_available = False

def check_for_compiled_libraries():
    try:
        import pmma.bin.perlin_noise
        import pmma.bin.extended_perlin_noise
        Registry.cython_acceleration_available = True
    except ImportError:
        Registry.cython_acceleration_available = False

    return Registry.cython_acceleration_available

def compile_intermediary():
    if check_for_compiled_libraries() is False:
        compile_libraries()

def compile():
    thread = threading.Thread(target=compile_intermediary)
    thread.name = "cython_compile"
    thread.start()
    return thread