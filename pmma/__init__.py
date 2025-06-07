import os
import platform
import ctypes

system = platform.system()

pmma_lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")

if system == "Windows":
    ctypes.CDLL(os.path.join(pmma_lib_dir, "PMMA_Core.dll"))
elif system == "Linux":
    ctypes.CDLL(os.path.join(pmma_lib_dir, "libPMMA_Core.so"))

from pmma.build.AdvancedMathematics import AdvancedMathematics
from pmma.build.PerlinNoise import PerlinNoise
from pmma.build.FractalBrownianMotion import FractalBrownianMotion
from pmma.build.Display import Display
from pmma.build.NumberConverter import (
    ColorConverter, DisplayCoordinatesConverter, AngleConverter,
    DisplayScalarConverter, ProportionConverter)

from pmma.core.py_src.Backpack import Backpack
from pmma.core.py_src.Audio import *
from pmma.core.py_src.Executor import Executor, AdvancedExecutor
from pmma.core.py_src.General import General
from pmma.core.py_src.GPU import GPUs