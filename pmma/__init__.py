print("Welcome to Python Multi-Media API, PMMA!")
print("Please note, this API is still in early development.")

import os
import platform
import ctypes

system = platform.system()

pmma_dir = os.path.dirname(os.path.abspath(__file__))

pmma_lib_dir = os.path.join(pmma_dir, "lib")

if system == "Windows":
    extern_binaries = os.path.join(pmma_dir, "extern", "bin")

    ctypes.CDLL(os.path.join(extern_binaries, "zlib.dll"))
    ctypes.CDLL(os.path.join(extern_binaries, "libpng16.dll"))
    ctypes.CDLL(os.path.join(pmma_lib_dir, "PMMA_Core.dll"))

elif system == "Linux":
    extern_libs = os.path.join(pmma_dir, "extern", "lib")

    ctypes.CDLL(os.path.join(extern_libs, "libz.so"))
    ctypes.CDLL(os.path.join(extern_libs, "libpng16.so"))
    ctypes.CDLL(os.path.join(pmma_lib_dir, "libPMMA_Core.so"))

elif system == "Darwin":
    extern_libs = os.path.join(pmma_dir, "extern", "lib")

    ctypes.CDLL(os.path.join(extern_libs, "zlib.dylib"))
    ctypes.CDLL(os.path.join(extern_libs, "libpng16.dylib"))
    ctypes.CDLL(os.path.join(pmma_lib_dir, "libPMMA_Core.dylib"))

from pmma.build.General import General

General.set_pmma_location(pmma_dir)
General.set_path_separator()

from pmma.build.AdvancedMathematics import AdvancedMathematics
from pmma.build.PerlinNoise import PerlinNoise
from pmma.build.FractalBrownianMotion import FractalBrownianMotion
from pmma.build.Display import Display
from pmma.build.NumberConverter import (
    ColorConverter, DisplayCoordinatesConverter, AngleConverter,
    DisplayScalarConverter, ProportionConverter)
import pmma.build.Events as Events
from pmma.build.TextRenderer import *

from pmma.core.py_src.Backpack import Backpack
from pmma.core.py_src.Audio import *
from pmma.core.py_src.Executor import Executor, AdvancedExecutor
from pmma.core.py_src.General import General
from pmma.core.py_src.GPU import GPUs