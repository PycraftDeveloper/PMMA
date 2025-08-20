import os
import platform
import ctypes
import sys
import threading

system = platform.system()

pmma_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(pmma_dir, "build"))

pmma_lib_dir = os.path.join(pmma_dir, "lib")

if system == "Windows":
    if "PMMA_DEBUG" in os.environ and os.environ["PMMA_DEBUG"] == "1":
        try:
            extern_binaries = os.path.join(pmma_dir, "extern - DEBUG", "bin")
            ctypes.CDLL(os.path.join(extern_binaries, "zlibd.dll"))
            ctypes.CDLL(os.path.join(extern_binaries, "libpng16d.dll"))
            print("You are using a DEBUGGING version of PMMA, this is not \
meant for prime time and is used only for debugging or development testing.")
        except FileNotFoundError:
            print("Could not find DEBUG files, please run: 'build_tools/main - debug.py'. Using release files instead")
            extern_binaries = os.path.join(pmma_dir, "extern", "bin")
            ctypes.CDLL(os.path.join(extern_binaries, "zlib.dll"))
            ctypes.CDLL(os.path.join(extern_binaries, "libpng16.dll"))
    else:
        extern_binaries = os.path.join(pmma_dir, "extern", "bin")
        ctypes.CDLL(os.path.join(extern_binaries, "zlib.dll"))
        ctypes.CDLL(os.path.join(extern_binaries, "libpng16.dll"))

    ctypes.CDLL(os.path.join(pmma_lib_dir, "PMMA_Core.dll"))

elif system == "Linux":
    if "PMMA_DEBUG" in os.environ and os.environ["PMMA_DEBUG"] == "1":
        print("We don't currently support Linux debugging. You might be \
the person to help change this! Defaulting to release files instead.")

    extern_libs = os.path.join(pmma_dir, "extern", "lib")

    ctypes.CDLL(os.path.join(extern_libs, "libz.so"))
    ctypes.CDLL(os.path.join(extern_libs, "libpng16.so"))
    ctypes.CDLL(os.path.join(pmma_lib_dir, "libPMMA_Core.so"))

elif system == "Darwin":
    if "PMMA_DEBUG" in os.environ and os.environ["PMMA_DEBUG"] == "1":
        print("We don't currently support Apple platform debugging. You \
might be the person to help change this! Defaulting to release files \
instead.")

    extern_libs = os.path.join(pmma_dir, "extern", "lib")

    ctypes.CDLL(os.path.join(extern_libs, "zlib.dylib"))
    ctypes.CDLL(os.path.join(extern_libs, "libpng16.dylib"))
    ctypes.CDLL(os.path.join(pmma_lib_dir, "libPMMA_Core.dylib"))

import pmma.build.PMMA_Core as _PMMA_Core
_PMMA_Core.initialize()

from pmma.build.General import General

General.set_pmma_location(pmma_dir)
General.set_path_separator()

from pmma.core.py_src.Utility import Registry as _Registry
_Registry.update_checking_thread = threading.Thread(target=General.internal_check_for_updates, daemon=True)
_Registry.update_checking_thread.start()

from pmma.build.AdvancedMathematics import AdvancedMathematics
from pmma.build.PerlinNoise import PerlinNoise
from pmma.build.FractalBrownianMotion import FractalBrownianMotion
from pmma.build.Display import Display
import pmma.build.NumberFormats as NumberFormats
import pmma.build.KeyEvents as KeyEvents
import pmma.build.KeyPadEvents as KeyPadEvents
import pmma.build.WindowEvents as WindowEvents
import pmma.build.ControllerEvents as ControllerEvents
import pmma.build.MouseEvents as MouseEvents
from pmma.build.TextRenderer import *
import pmma.build.Shapes2D as Shapes2D
from pmma.build.Passport import Passport
from pmma.build.Logger import Logger
import pmma.build.Animation as Animation

from pmma.core.py_src.Backpack import Backpack
from pmma.core.py_src.Audio import *
from pmma.core.py_src.Executor import Executor, AdvancedExecutor
from pmma.core.py_src.GPU import GPUs
from pmma.core.py_src.AdvancedThreading import AdvancedThread
import pmma.core.py_src.DataStructures as DataStructures
from pmma.core.py_src.Sampler import Sampler
from pmma.core.py_src.DateTimeFormatter import TimeFormatter
import pmma.core.py_src.FileManagement as FileManagement