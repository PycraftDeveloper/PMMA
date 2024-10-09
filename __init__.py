import sys as _sys
from os import sep as _os__sep
from tkinter import Tk as _tkinter__Tk
from io import StringIO as _io__StringIO
from contextlib import redirect_stdout as _contextlib__redirect_stdout
from time import perf_counter as _time__perf_counter

from pprofile import Profile as _pprofile__Profile

def _up(path: str) -> str:
    return path[::-1].split(_os__sep, 1)[-1][::-1]

_base_path = _up(__file__)

_temporary_files_path = _base_path + _os__sep + "temporary"
_sys.pycache_prefix = _temporary_files_path

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.constants import *

_Registry.temporary_files_path = _temporary_files_path
_Registry.base_path = _base_path

_buffer = _io__StringIO()

with _contextlib__redirect_stdout(_buffer):
    import pygame as _pygame
    del _pygame

_Registry.pygame_launch_message = _buffer.getvalue().strip()

from pmma.python_src.utility.error_utils import *
from pmma.python_src.gpu_distribution import *
from pmma.python_src.number_converter import *
from pmma.python_src.render_pipeline import *
from pmma.python_src.data_structures import *
from pmma.python_src.memory_manager import *
from pmma.python_src.advthreading import *
from pmma.python_src.transitions import *
from pmma.python_src.controller import *
from pmma.python_src.advtkinter import *
from pmma.python_src.formatters import *
from pmma.python_src.quickstart import *
from pmma.python_src.projection import *
from pmma.python_src.optimizer import *
from pmma.python_src.backpack import *
from pmma.python_src.passport import *
from pmma.python_src.executor import *
from pmma.python_src.settings import *
from pmma.python_src.sampler import *
from pmma.python_src.display import *
from pmma.python_src.surface import *
from pmma.python_src.general import *
from pmma.python_src.advmath import *
from pmma.python_src.opengl import *
from pmma.python_src.events import *
from pmma.python_src.error import *
from pmma.python_src.noise import *
from pmma.python_src.image import *
from pmma.python_src.audio import *
from pmma.python_src.video import *
from pmma.python_src.draw import *
from pmma.python_src.file import *
from pmma.python_src.text import *
from pmma.python_src.gpu import *

from pmma.python_src.utility import cython_utils as _cython_utils
from pmma.python_src.utility.memory_utils import MemoryManagerIntermediary as _MemoryManagerIntermediary
import pmma.python_src.utility.event_utils as _event_utils
from pmma.python_src.utility.gpu_utils import GPUsIntermediary as _GPUsIntermediary
from pmma.python_src.utility.controller_utils import ControllersIntermediary as _ControllersIntermediary
import pmma.python_src.utility.general_utils as _general_utils
from pmma.python_src.utility.logging_utils import LoggerIntermediary as _LoggerIntermediary
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.shader_utils import LoadedShaderReferenceManager as _LoadedShaderReferenceManager
from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
from pmma.python_src.utility.transition_utils import TransitionManager as _TransitionManager
from pmma.python_src.utility.gpu_distribution_utils import GPUDistributionManager as _GPUDistributionManager
from pmma.python_src.utility.projection_utils import ProjectionIntermediary as _ProjectionIntermediary

def init(
            optimize_python_extensions=True,
            compile_c_extensions=True,
            memory_management_max_object_lifetime=2.5,
            memory_management_max_size=Constants.AUTOMATIC,
            general_profile_application=False,
            targeted_profile_application=False):

    _Registry.general_profile_application = general_profile_application
    _Registry.targeted_profile_application = targeted_profile_application and not general_profile_application

    if general_profile_application or targeted_profile_application:
        _Registry.profiler = _pprofile__Profile()
        if general_profile_application:
            _Registry.profiler.enable()

    startup_time = _time__perf_counter()

    _Registry.pmma_initialized = True

    _LoggerIntermediary()

    if compile_c_extensions: # needs to be paired before "if optimize_python_extensions:" and as early as possible for max threading benefit.
        cython_thread = _cython_utils.compile()

    root = _tkinter__Tk()
    root.withdraw()

    _Registry.application_start_time = startup_time
    Backpack.application_start_time = startup_time

    _Registry.python_acceleration_enabled = optimize_python_extensions
    _Registry.cython_acceleration_enabled = compile_c_extensions
    _Registry.power_saving_mode = is_battery_saver_enabled()
    _Registry.power_status_checked_time = _time__perf_counter()

    _general_utils.update_language()

    _MemoryManagerIntermediary(
        object_lifetime=memory_management_max_object_lifetime,
        target_size=memory_management_max_size)

    logger = _InternalLogger()

    logger.log_information("Thank you for using PMMA! Please note that PMMA \
is still in an early stage of its development, bear with us as we \
continue to work on improving it!")

    if get_operating_system() == Constants.LINUX:
        try:
            import pyaudio as _pyaudio
        except ModuleNotFoundError as error:
            logger.log_development("Pyaudio hasn't been installed yet. Because your running on a \
Linux platform make sure to run this command first: 'sudo apt-get install portaudio19-dev' \
first otherwise attempting to install the 'PyAudio' module may fail.")
            raise error

        logger.log_development("You might have just seen something in terminal about ALSA. \
If you didn't, you can disregard this message. Otherwise; we currently dont have any \
control over this, but its most likely worrying about there not being any valid audio output \
devices. We are working on a better way to handle this situation.")

    register_application()

    _TransitionManager()
    _GPUsIntermediary()
    _GPUDistributionManager()
    _ControllersIntermediary()
    _ProjectionIntermediary()
    _LoadedShaderReferenceManager()

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
    _event_utils.Quit_EVENT()
    _event_utils.RenderTargetsReset_EVENT()
    _event_utils.RenderDeviceReset_EVENT()
    _event_utils.SysWMEvent_EVENT()
    _event_utils.WindowShown_EVENT()
    _event_utils.WindowHidden_EVENT()
    _event_utils.WindowExposed_EVENT()
    _event_utils.WindowMoved_EVENT()
    _event_utils.WindowResized_EVENT()
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

    _DisplayIntermediary()

    cython_thread.join()

    if optimize_python_extensions: # needs to be paired before "if compile_c_extensions:" and as early as possible for max threading benefit.
        benchmark = Benchmark() # cache this unique to device
        benchmark.test_all()

# Jessy