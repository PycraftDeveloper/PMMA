import sys as _sys
import os as _os
import tkinter as _tkinter
import io as _io
import contextlib as _contextlib
import time as _time

import numba as _numba

def _up(path: str) -> str:
    return path[::-1].split(_os.sep, 1)[-1][::-1]

_base_path = _up(__file__)

_temporary_files_path = _base_path + _os.sep + "temporary"
_sys.pycache_prefix = _temporary_files_path
_numba.config.CACHE_DIR = _temporary_files_path

from pmma.python_src.registry import *
from pmma.python_src.constants import *

Registry.temporary_files_path = _temporary_files_path
Registry.base_path = _base_path

_buffer = _io.StringIO()

with _contextlib.redirect_stdout(_buffer):
    import pygame as _pygame

Registry.pygame_launch_message = _buffer.getvalue().strip()

from pmma.python_src.utility.general_utils import environ_to_registry as _environ_to_registry
from pmma.python_src.general import *

if get_operating_system() == Constants.LINUX:
    try:
        import pyaudio as _pyaudio
    except ModuleNotFoundError:
        log_development("Pyaudio hasn't been installed yet. Because your running on a \
Linux platform make sure to run this command first: 'sudo apt-get install portaudio19-dev' \
first otherwise attempting to install the 'PyAudio' module may fail.")

_environ_to_registry()

from pmma.python_src.render_pipeline import *
from pmma.python_src.data_structures import *
from pmma.python_src.memory_manager import *
from pmma.python_src.advthreading import *
from pmma.python_src.controller import *
from pmma.python_src.advtkinter import *
from pmma.python_src.formatters import *
from pmma.python_src.coordinate import *
from pmma.python_src.quickstart import *
from pmma.python_src.optimizer import *
from pmma.python_src.backpack import *
from pmma.python_src.passport import *
from pmma.python_src.executor import *
from pmma.python_src.sampler import *
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

from pmma.python_src.utility import cython_utils as _cython_utils
from pmma.python_src.logging import Logger as _Logger
from pmma.python_src.utility.memory_utils import MemoryManagerIntermediary as _MemoryManagerIntermediary
import pmma.python_src.utility.event_utils as _event_utils
from pmma.python_src.utility.gpu_utils import GPUsIntermediary as _GPUsIntermediary
from pmma.python_src.utility.controller_utils import ControllersIntermediary as _ControllersIntermediary
import pmma.python_src.utility.general_utils as _general_utils

def init(
            optimize_python_extensions=True,
            compile_c_extensions=True,
            wait_for_initialization=True,
            memory_management_max_object_lifetime=2.5,
            memory_management_max_size=Constants.AUTOMATIC,
            log_development=None,
            log_information=True,
            log_warning=False,
            log_error=True,
            log_to_file=False,
            log_file=None,
            log_to_terminal=True):

    root = _tkinter.Tk()
    root.withdraw()

    startup_time = _time.perf_counter()
    Registry.application_start_time = startup_time
    Backpack.application_start_time = startup_time

    Registry.pmma_initialized = True
    Registry.python_acceleration_enabled = optimize_python_extensions
    Registry.cython_acceleration_enabled = compile_c_extensions
    Registry.power_saving_mode = is_battery_saver_enabled()

    _general_utils.update_language()

    if optimize_python_extensions:
        benchmark = Benchmark() # cache this unique to device
        benchmark.test_all()

    if compile_c_extensions:
        cython_thread = _cython_utils.compile()

    _MemoryManagerIntermediary(
        object_lifetime=memory_management_max_object_lifetime,
        target_size=memory_management_max_size)

    _Logger(
        log_development=log_development,
        log_information=log_information,
        log_warning=log_warning,
        log_error=log_error,
        log_to_file=log_to_file,
        log_file=log_file,
        log_to_terminal=log_to_terminal)

    register_application()

    _GPUsIntermediary()
    _ControllersIntermediary()

    _event_utils.Backspace_KEY()
    _event_utils.Tab_KEY()
    _event_utils.Clear_KEY()
    _event_utils.Return_KEY()
    _event_utils.Pause_KEY()
    _event_utils.Escape_KEY()
    _event_utils.Space_KEY()
    _event_utils.ExclamationMark_KEY()
    _event_utils.DoubleQuote_KEY()
    _event_utils.Hashtag_KEY()
    _event_utils.Dollar_KEY()
    _event_utils.Ampersand_KEY()
    _event_utils.SingleQuote_KEY()
    _event_utils.LeftParenthesis_KEY()
    _event_utils.RightParenthesis_KEY()
    _event_utils.Asterisk_KEY()
    _event_utils.Plus_KEY()
    _event_utils.Comma_KEY()
    _event_utils.Minus_KEY()
    _event_utils.Period_KEY()
    _event_utils.ForwardSlash_KEY()
    _event_utils.Primary0_KEY()
    _event_utils.Primary1_KEY()
    _event_utils.Primary2_KEY()
    _event_utils.Primary3_KEY()
    _event_utils.Primary4_KEY()
    _event_utils.Primary5_KEY()
    _event_utils.Primary6_KEY()
    _event_utils.Primary7_KEY()
    _event_utils.Primary8_KEY()
    _event_utils.Primary9_KEY()
    _event_utils.Colon_KEY()
    _event_utils.SemiColon_KEY()
    _event_utils.LessThan_KEY()
    _event_utils.Equals_KEY()
    _event_utils.GreaterThan_KEY()
    _event_utils.QuestionMark_KEY()
    _event_utils.At_KEY()
    _event_utils.LeftBracket_KEY()
    _event_utils.BackSlash_KEY()
    _event_utils.RightBracket_KEY()
    _event_utils.Caret_KEY()
    _event_utils.Underscore_KEY()
    _event_utils.Grave_KEY()
    _event_utils.PrimaryA_KEY()
    _event_utils.PrimaryB_KEY()
    _event_utils.PrimaryC_KEY()
    _event_utils.PrimaryD_KEY()
    _event_utils.PrimaryE_KEY()
    _event_utils.PrimaryF_KEY()
    _event_utils.PrimaryG_KEY()
    _event_utils.PrimaryH_KEY()
    _event_utils.PrimaryI_KEY()
    _event_utils.PrimaryJ_KEY()
    _event_utils.PrimaryK_KEY()
    _event_utils.PrimaryL_KEY()
    _event_utils.PrimaryM_KEY()
    _event_utils.PrimaryN_KEY()
    _event_utils.PrimaryO_KEY()
    _event_utils.PrimaryP_KEY()
    _event_utils.PrimaryQ_KEY()
    _event_utils.PrimaryR_KEY()
    _event_utils.PrimaryS_KEY()
    _event_utils.PrimaryT_KEY()
    _event_utils.PrimaryU_KEY()
    _event_utils.PrimaryV_KEY()
    _event_utils.PrimaryW_KEY()
    _event_utils.PrimaryX_KEY()
    _event_utils.PrimaryY_KEY()
    _event_utils.PrimaryZ_KEY()
    _event_utils.Delete_KEY()
    _event_utils.Numpad0_KEY()
    _event_utils.Numpad1_KEY()
    _event_utils.Numpad2_KEY()
    _event_utils.Numpad3_KEY()
    _event_utils.Numpad4_KEY()
    _event_utils.Numpad5_KEY()
    _event_utils.Numpad6_KEY()
    _event_utils.Numpad7_KEY()
    _event_utils.Numpad8_KEY()
    _event_utils.Numpad9_KEY()
    _event_utils.NumpadPeriod_KEY()
    _event_utils.NumpadDivide_KEY()
    _event_utils.NumpadMultiply_KEY()
    _event_utils.NumpadMinus_KEY()
    _event_utils.NumpadPlus_KEY()
    _event_utils.NumpadEnter_KEY()
    _event_utils.NumpadEquals_KEY()
    _event_utils.Up_KEY()
    _event_utils.Down_KEY()
    _event_utils.Right_KEY()
    _event_utils.Left_KEY()
    _event_utils.Insert_KEY()
    _event_utils.Home_KEY()
    _event_utils.End_KEY()
    _event_utils.PageUp_KEY()
    _event_utils.PageDown_KEY()
    _event_utils.Function1_KEY()
    _event_utils.Function2_KEY()
    _event_utils.Function3_KEY()
    _event_utils.Function4_KEY()
    _event_utils.Function5_KEY()
    _event_utils.Function6_KEY()
    _event_utils.Function7_KEY()
    _event_utils.Function8_KEY()
    _event_utils.Function9_KEY()
    _event_utils.Function10_KEY()
    _event_utils.Function11_KEY()
    _event_utils.Function12_KEY()
    _event_utils.Function13_KEY()
    _event_utils.Function14_KEY()
    _event_utils.Function15_KEY()
    _event_utils.NumLock_KEY()
    _event_utils.CapsLock_KEY()
    _event_utils.ScrollLock_KEY()
    _event_utils.RightShift_KEY()
    _event_utils.LeftShift_KEY()
    _event_utils.Shift_KEY()
    _event_utils.RightControl_KEY()
    _event_utils.LeftControl_KEY()
    _event_utils.Control_KEY()
    _event_utils.RightAlt_KEY()
    _event_utils.LeftAlt_KEY()
    _event_utils.Alt_KEY()
    _event_utils.RightMeta_KEY()
    _event_utils.LeftMeta_KEY()
    _event_utils.Meta_KEY()
    _event_utils.LeftSuper_KEY()
    _event_utils.RightSuper_KEY()
    _event_utils.Super_KEY()
    _event_utils.Mode_KEY()
    _event_utils.Help_KEY()
    _event_utils.Print_KEY()
    _event_utils.SystemRequest_KEY()
    _event_utils.Break_KEY()
    _event_utils.Menu_KEY()
    _event_utils.Power_KEY()
    _event_utils.Euro_KEY()
    _event_utils.AndroidBack_KEY()

    _event_utils.LeftButton_MOUSE()
    _event_utils.MiddleButton_MOUSE()
    _event_utils.RightButton_MOUSE()
    _event_utils.Mouse_SCROLL()
    _event_utils.Mouse_POSITION()
    _event_utils.AppTerminating_EVENT()
    _event_utils.AppLowMemory_EVENT()
    _event_utils.AppWillEnterBackground_EVENT()
    _event_utils.AppDidEnterBackground_EVENT()
    _event_utils.AppWillEnterForeground_EVENT()
    _event_utils.AppDidEnterForeground_EVENT()
    _event_utils.AudioDeviceAdded_EVENT()
    _event_utils.AudioDeviceRemoved_EVENT()
    _event_utils.ClipBoardUpdate_EVENT()
    _event_utils.DropFile_EVENT()
    _event_utils.DropText_EVENT()
    _event_utils.DropBegin_EVENT()
    _event_utils.DropComplete_EVENT()
    _event_utils.FingerMotion_EVENT()
    _event_utils.FingerDown_EVENT()
    _event_utils.FingerUp_EVENT()
    _event_utils.KeyMapChanged_EVENT()
    _event_utils.LocaleChanged_EVENT()
    _event_utils.MultiGesture_EVENT()
    _event_utils.NoEvent_EVENT()
    _event_utils.Quit_EVENT()
    _event_utils.RenderTargetsReset_EVENT()
    _event_utils.RenderDeviceReset_EVENT()
    _event_utils.SysWMEvent_EVENT()
    _event_utils.MidiIn_EVENT()
    _event_utils.MidiOut_EVENT()
    _event_utils.WindowShown_EVENT()
    _event_utils.WindowHidden_EVENT()
    _event_utils.WindowExposed_EVENT()
    _event_utils.WindowMoved_EVENT()
    _event_utils.WindowResized_EVENT()
    _event_utils.WindowSizeChanged_EVENT()
    _event_utils.WindowMinimized_EVENT()
    _event_utils.WindowMaximized_EVENT()
    _event_utils.WindowRestored_EVENT()
    _event_utils.WindowEnter_EVENT()
    _event_utils.WindowLeave_EVENT()
    _event_utils.WindowFocusGained_EVENT()
    _event_utils.WindowFocusLost_EVENT()
    _event_utils.WindowClose_EVENT()
    _event_utils.WindowTakeFocus_EVENT()
    _event_utils.WindowHitTest_EVENT()
    _event_utils.WindowICCPROFChanged_EVENT()
    _event_utils.WindowDisplayChanged_EVENT()
    _event_utils.JoyDeviceAdded_EVENT()
    _event_utils.JoyDeviceRemoved_EVENT()

    if wait_for_initialization:
        cython_thread.join()