import sys
import os
import tkinter
import io
import contextlib

import numba

def _up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

base_path = _up(__file__)

temporary_files_path = base_path + os.sep + "temporary"
sys.pycache_prefix = temporary_files_path
numba.config.CACHE_DIR = temporary_files_path

from pmma.python_src.registry import *
from pmma.python_src.constants import *

Registry.temporary_files_path = temporary_files_path
Registry.base_path = base_path

buffer = io.StringIO()

with contextlib.redirect_stdout(buffer):
    import pygame

Registry.pygame_launch_message = buffer.getvalue().strip()

from pmma.python_src.general import *

if get_operating_system() == Constants.LINUX:
    try:
        import pyaudio
    except ModuleNotFoundError:
        log_development("Pyaudio hasn't been installed yet. Because your running on a \
Linux platform make sure to run this command first: 'sudo apt-get install portaudio19-dev' \
first otherwise attempting to install the 'PyAudio' module may fail.")

environ_to_registry()

from pmma.python_src.render_pipeline import *
from pmma.python_src.advthreading import *
from pmma.python_src.advtkinter import *
from pmma.python_src.coordinate import *
from pmma.python_src.quickstart import *
from pmma.python_src.optimizer import *
from pmma.python_src.recorder import *
from pmma.python_src.backpack import *
from pmma.python_src.passport import *
from pmma.python_src.executor import *
from pmma.python_src.display import *
from pmma.python_src.surface import *
from pmma.python_src.advmath import *
from pmma.python_src.opengl import *
from pmma.python_src.events import *
from pmma.python_src.shader import *
from pmma.python_src.noise import *
from pmma.python_src.color import *
from pmma.python_src.image import *
from pmma.python_src.draw import *
from pmma.python_src.file import *
from pmma.python_src.text import *
from pmma.python_src.gpu import *

from pmma.python_src.utility import cython_utils
from pmma.python_src.memory_manager import MemoryManager
from pmma.python_src.logging import Logger

def init(
            optimize_python_extensions=True,
            compile_c_extensions=True,
            wait_for_initialization=True,
            memory_management_max_object_lifetime=2.5,
            memory_management_max_size=Constants.AUTOMATIC,
            log_development=None,
            log_information=False,
            log_warning=False,
            log_error=True,
            log_to_file=False,
            log_file=None,
            log_to_terminal=True):

    root = tkinter.Tk()
    root.withdraw()

    Registry.pmma_initialized = True
    Registry.python_acceleration_enabled = optimize_python_extensions
    Registry.cython_acceleration_enabled = compile_c_extensions
    Registry.power_saving_mode = is_battery_saver_enabled()

    if optimize_python_extensions:
        benchmark = Benchmark() # cache this unique to device
        benchmark.test_all()

    if compile_c_extensions:
        cython_thread = cython_utils.compile()

    MemoryManager(
        object_lifetime=memory_management_max_object_lifetime,
        target_size=memory_management_max_size)

    Logger(
        log_development=log_development,
        log_information=log_information,
        log_warning=log_warning,
        log_error=log_error,
        log_to_file=log_to_file,
        log_file=log_file,
        log_to_terminal=log_to_terminal)

    register_application()

    GPUs()

    if wait_for_initialization:
        cython_thread.join()

del base_path
del temporary_files_path
del sys
del numba
del environ_to_registry