import subprocess
import sys
import os
import threading

from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

def setup():
    try:
        os.mkdir(f"{Registry.base_path}{os.sep}bin")
    except FileExistsError:
        pass

def compile_perlin_noise():
    try:
        import pmma.bin.perlin_noise
        Registry.cython_acceleration_available[Constants.COMPILED_PERLIN_NOISE] = True
    except ImportError:
        try:
            exit_code = subprocess.call([sys.executable, "c_setup.py", "build_ext", "--inplace", "--build-lib", f"{Registry.base_path}{Constants.PATH_SEPARATOR}bin", "--build-temp", "temporary"])
            Registry.cython_acceleration_available[Constants.COMPILED_PERLIN_NOISE] = exit_code == 0
        except:
            Registry.cython_acceleration_available[Constants.COMPILED_PERLIN_NOISE] = False
        # clean up with FileCore

def check_for_compiled_perlin_noise():
    try:
        import pmma.bin.perlin_noise
        Registry.cython_acceleration_available[Constants.COMPILED_PERLIN_NOISE] = True
    except ImportError:
        Registry.cython_acceleration_available[Constants.COMPILED_PERLIN_NOISE] = False

    return Registry.cython_acceleration_available[Constants.COMPILED_PERLIN_NOISE]

def compile_intermediary():
    if check_for_compiled_perlin_noise() is False:
        compile_perlin_noise()

def compile():
    thread = threading.Thread(target=compile_intermediary)
    thread.name = "cython_compile"
    thread.start()
    return thread