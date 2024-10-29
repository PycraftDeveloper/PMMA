import sys as _sys
from os import sep as _os__sep
from tkinter import Tk as _tkinter__Tk
from io import StringIO as _io__StringIO
from contextlib import redirect_stdout as _contextlib__redirect_stdout
from time import perf_counter as _time__perf_counter
from json import load as _json__load
from json import dump as _json__dump

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

from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

from pmma.python_src.utility import cython_utils as _cython_utils
import pmma.python_src.utility.general_utils as _general_utils
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

def init(
            optimize_python_extensions=True,
            compile_c_extensions=True,
            memory_management_max_object_lifetime=2.5,
            memory_management_max_size=Constants.AUTOMATIC,
            general_profile_application=False,
            targeted_profile_application=False):

    passport = {"components used": []}
    if _PassportIntermediary.passport_file_location is not None:
        try:
            with open(_PassportIntermediary.passport_file_location, "r") as file:
                passport = _json__load(file)
        except:
            with open(_PassportIntermediary.passport_file_location, "w") as file:
                _json__dump(passport, file)

    _PassportIntermediary.components_used = passport["components used"]

    _Registry.general_profile_application = general_profile_application
    _Registry.targeted_profile_application = targeted_profile_application and not general_profile_application

    if general_profile_application or targeted_profile_application:
        _Registry.profiler = _pprofile__Profile()
        if general_profile_application:
            _Registry.profiler.enable()

    startup_time = _time__perf_counter()

    _Registry.pmma_initialized = True

    if Constants.LOGGING_INTERMEDIARY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.logging_utils import LoggerIntermediary as _LoggerIntermediary
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

    if Constants.MEMORY_MANAGER_INTERMEDIARY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.memory_utils import MemoryManagerIntermediary as _MemoryManagerIntermediary
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

    if Constants.TRANSITION_MANAGER_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.transition_utils import TransitionManager as _TransitionManager
        _TransitionManager()

    if Constants.GPUS_INTERMEDIARY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.gpu_utils import GPUsIntermediary as _GPUsIntermediary
        _GPUsIntermediary()

    if Constants.GPU_DISTRIBUTION_MANAGER_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.gpu_distribution_utils import GPUDistributionManager as _GPUDistributionManager
        _GPUDistributionManager()

    if Constants.CONTROLLER_INTERMEDIARY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.controller_utils import ControllersIntermediary as _ControllersIntermediary
        _ControllersIntermediary()

    if Constants.PROJECTION_INTERMEDIARY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.projection_utils import ProjectionIntermediary as _ProjectionIntermediary
        _ProjectionIntermediary()

    if Constants.SHADER_REFERENCE_MANAGER_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.shader_utils import LoadedShaderReferenceManager as _LoadedShaderReferenceManager
        _LoadedShaderReferenceManager()

    if Constants.BACKSPACE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Backspace_KEY as _Backspace_KEY
        _Backspace_KEY()

    if Constants.TAB_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Tab_KEY as _Tab_KEY
        _Tab_KEY()

    if Constants.CLEAR_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Clear_KEY as _Clear_KEY
        _Clear_KEY()

    if Constants.RETURN_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Return_KEY as _Return_KEY
        _Return_KEY()

    if Constants.PAUSE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Pause_KEY as _Pause_KEY
        _Pause_KEY()

    if Constants.ESCAPE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Escape_KEY as _Escape_KEY
        _Escape_KEY()

    if Constants.SPACE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Space_KEY as _Space_KEY
        _Space_KEY()

    if Constants.EXCLAMATIONMARK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import ExclamationMark_KEY as _ExclamationMark_KEY
        _ExclamationMark_KEY()

    if Constants.DOUBLEQUOTE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import DoubleQuote_KEY as _DoubleQuote_KEY
        _DoubleQuote_KEY()

    if Constants.HASHTAG_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Hashtag_KEY as _Hashtag_KEY
        _Hashtag_KEY()

    if Constants.DOLLAR_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Dollar_KEY as _Dollar_KEY
        _Dollar_KEY()

    if Constants.AMPERSAND_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Ampersand_KEY as _Ampersand_KEY
        _Ampersand_KEY()

    if Constants.SINGLEQUOTE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import SingleQuote_KEY as _SingleQuote_KEY
        _SingleQuote_KEY()

    if Constants.LEFTPARENTHESIS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftParenthesis_KEY as _LeftParenthesis_KEY
        _LeftParenthesis_KEY()

    if Constants.RIGHTPARENTHESIS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightParenthesis_KEY as _RightParenthesis_KEY
        _RightParenthesis_KEY()

    if Constants.ASTERISK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Asterisk_KEY as _Asterisk_KEY
        _Asterisk_KEY()

    if Constants.PLUS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Plus_KEY as _Plus_KEY
        _Plus_KEY()

    if Constants.COMMA_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Comma_KEY as _Comma_KEY
        _Comma_KEY()

    if Constants.MINUS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Minus_KEY as _Minus_KEY
        _Minus_KEY()

    if Constants.PERIOD_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Period_KEY as _Period_KEY
        _Period_KEY()

    if Constants.FORWARDSLASH_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import ForwardSlash_KEY as _ForwardSlash_KEY
        _ForwardSlash_KEY()

    if Constants.PRIMARY0_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary0_KEY as _Primary0_KEY
        _Primary0_KEY()

    if Constants.PRIMARY1_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary1_KEY as _Primary1_KEY
        _Primary1_KEY()

    if Constants.PRIMARY2_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary2_KEY as _Primary2_KEY
        _Primary2_KEY()

    if Constants.PRIMARY3_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary3_KEY as _Primary3_KEY
        _Primary3_KEY()

    if Constants.PRIMARY4_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary4_KEY as _Primary4_KEY
        _Primary4_KEY()

    if Constants.PRIMARY5_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary5_KEY as _Primary5_KEY
        _Primary5_KEY()

    if Constants.PRIMARY6_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary6_KEY as _Primary6_KEY
        _Primary6_KEY()

    if Constants.PRIMARY7_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary7_KEY as _Primary7_KEY
        _Primary7_KEY()

    if Constants.PRIMARY8_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary8_KEY as _Primary8_KEY
        _Primary8_KEY()

    if Constants.PRIMARY9_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Primary9_KEY as _Primary9_KEY
        _Primary9_KEY()

    if Constants.COLON_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Colon_KEY as _Colon_KEY
        _Colon_KEY()

    if Constants.SEMICOLON_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import SemiColon_KEY as _SemiColon_KEY
        _SemiColon_KEY()

    if Constants.LESSTHAN_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LessThan_KEY as _LessThan_KEY
        _LessThan_KEY()

    if Constants.EQUALS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Equals_KEY as _Equals_KEY
        _Equals_KEY()

    if Constants.GREATERTHAN_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import GreaterThan_KEY as _GreaterThan_KEY
        _GreaterThan_KEY()

    if Constants.QUESTIONMARK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import QuestionMark_KEY as _QuestionMark_KEY
        _QuestionMark_KEY()

    if Constants.AT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import At_KEY as _At_KEY
        _At_KEY()

    if Constants.LEFTBRACKET_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftBracket_KEY as _LeftBracket_KEY
        _LeftBracket_KEY()

    if Constants.BACKSLASH_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import BackSlash_KEY as _BackSlash_KEY
        _BackSlash_KEY()

    if Constants.RIGHTBRACKET_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightBracket_KEY as _RightBracket_KEY
        _RightBracket_KEY()

    if Constants.CARET_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Caret_KEY as _Caret_KEY
        _Caret_KEY()

    if Constants.UNDERSCORE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Underscore_KEY as _Underscore_KEY
        _Underscore_KEY()

    if Constants.GRAVE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Grave_KEY as _Grave_KEY
        _Grave_KEY()

    if Constants.PRIMARYA_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryA_KEY as _PrimaryA_KEY
        _PrimaryA_KEY()

    if Constants.PRIMARYB_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryB_KEY as _PrimaryB_KEY
        _PrimaryB_KEY()

    if Constants.PRIMARYC_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryC_KEY as _PrimaryC_KEY
        _PrimaryC_KEY()

    if Constants.PRIMARYD_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryD_KEY as _PrimaryD_KEY
        _PrimaryD_KEY()

    if Constants.PRIMARYE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryE_KEY as _PrimaryE_KEY
        _PrimaryE_KEY()

    if Constants.PRIMARYF_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryF_KEY as _PrimaryF_KEY
        _PrimaryF_KEY()

    if Constants.PRIMARYG_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryG_KEY as _PrimaryG_KEY
        _PrimaryG_KEY()

    if Constants.PRIMARYH_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryH_KEY as _PrimaryH_KEY
        _PrimaryH_KEY()

    if Constants.PRIMARYI_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryI_KEY as _PrimaryI_KEY
        _PrimaryI_KEY()

    if Constants.PRIMARYJ_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryJ_KEY as _PrimaryJ_KEY
        _PrimaryJ_KEY()

    if Constants.PRIMARYK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryK_KEY as _PrimaryK_KEY
        _PrimaryK_KEY()

    if Constants.PRIMARYL_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryL_KEY as _PrimaryL_KEY
        _PrimaryL_KEY()

    if Constants.PRIMARYM_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryM_KEY as _PrimaryM_KEY
        _PrimaryM_KEY()

    if Constants.PRIMARYN_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryN_KEY as _PrimaryN_KEY
        _PrimaryN_KEY()

    if Constants.PRIMARYO_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryO_KEY as _PrimaryO_KEY
        _PrimaryO_KEY()

    if Constants.PRIMARYP_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryP_KEY as _PrimaryP_KEY
        _PrimaryP_KEY()

    if Constants.PRIMARYQ_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryQ_KEY as _PrimaryQ_KEY
        _PrimaryQ_KEY()

    if Constants.PRIMARYR_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryR_KEY as _PrimaryR_KEY
        _PrimaryR_KEY()

    if Constants.PRIMARYS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryS_KEY as _PrimaryS_KEY
        _PrimaryS_KEY()

    if Constants.PRIMARYT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryT_KEY as _PrimaryT_KEY
        _PrimaryT_KEY()

    if Constants.PRIMARYU_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryU_KEY as _PrimaryU_KEY
        _PrimaryU_KEY()

    if Constants.PRIMARYV_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryV_KEY as _PrimaryV_KEY
        _PrimaryV_KEY()

    if Constants.PRIMARYW_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryW_KEY as _PrimaryW_KEY
        _PrimaryW_KEY()

    if Constants.PRIMARYX_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryX_KEY as _PrimaryX_KEY
        _PrimaryX_KEY()

    if Constants.PRIMARYY_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryY_KEY as _PrimaryY_KEY
        _PrimaryY_KEY()

    if Constants.PRIMARYZ_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PrimaryZ_KEY as _PrimaryZ_KEY
        _PrimaryZ_KEY()

    if Constants.DELETE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Delete_KEY as _Delete_KEY
        _Delete_KEY()

    if Constants.NUMPAD0_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad0_KEY as _Numpad0_KEY
        _Numpad0_KEY()

    if Constants.NUMPAD1_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad1_KEY as _Numpad1_KEY
        _Numpad1_KEY()

    if Constants.NUMPAD2_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad2_KEY as _Numpad2_KEY
        _Numpad2_KEY()

    if Constants.NUMPAD3_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad3_KEY as _Numpad3_KEY
        _Numpad3_KEY()

    if Constants.NUMPAD4_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad4_KEY as _Numpad4_KEY
        _Numpad4_KEY()

    if Constants.NUMPAD5_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad5_KEY as _Numpad5_KEY
        _Numpad5_KEY()

    if Constants.NUMPAD6_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad6_KEY as _Numpad6_KEY
        _Numpad6_KEY()

    if Constants.NUMPAD7_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad7_KEY as _Numpad7_KEY
        _Numpad7_KEY()

    if Constants.NUMPAD8_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad8_KEY as _Numpad8_KEY
        _Numpad8_KEY()

    if Constants.NUMPAD9_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Numpad9_KEY as _Numpad9_KEY
        _Numpad9_KEY()

    if Constants.NUMPADPERIOD_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadPeriod_KEY as _NumpadPeriod_KEY
        _NumpadPeriod_KEY()

    if Constants.NUMPADDIVIDE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadDivide_KEY as _NumpadDivide_KEY
        _NumpadDivide_KEY()

    if Constants.NUMPADMULTIPLY_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadMultiply_KEY as _NumpadMultiply_KEY
        _NumpadMultiply_KEY()

    if Constants.NUMPADMINUS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadMinus_KEY as _NumpadMinus_KEY
        _NumpadMinus_KEY()

    if Constants.NUMPADPLUS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadPlus_KEY as _NumpadPlus_KEY
        _NumpadPlus_KEY()

    if Constants.NUMPADENTER_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadEnter_KEY as _NumpadEnter_KEY
        _NumpadEnter_KEY()

    if Constants.NUMPADEQUALS_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumpadEquals_KEY as _NumpadEquals_KEY
        _NumpadEquals_KEY()

    if Constants.UP_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Up_KEY as _Up_KEY
        _Up_KEY()

    if Constants.DOWN_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Down_KEY as _Down_KEY
        _Down_KEY()

    if Constants.RIGHT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Right_KEY as _Right_KEY
        _Right_KEY()

    if Constants.LEFT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Left_KEY as _Left_KEY
        _Left_KEY()

    if Constants.INSERT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Insert_KEY as _Insert_KEY
        _Insert_KEY()

    if Constants.HOME_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Home_KEY as _Home_KEY
        _Home_KEY()

    if Constants.END_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import End_KEY as _End_KEY
        _End_KEY()

    if Constants.PAGEUP_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PageUp_KEY as _PageUp_KEY
        _PageUp_KEY()

    if Constants.PAGEDOWN_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import PageDown_KEY as _PageDown_KEY
        _PageDown_KEY()

    if Constants.FUNCTION1_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function1_KEY as _Function1_KEY
        _Function1_KEY()

    if Constants.FUNCTION2_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function2_KEY as _Function2_KEY
        _Function2_KEY()

    if Constants.FUNCTION3_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function3_KEY as _Function3_KEY
        _Function3_KEY()

    if Constants.FUNCTION4_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function4_KEY as _Function4_KEY
        _Function4_KEY()

    if Constants.FUNCTION5_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function5_KEY as _Function5_KEY
        _Function5_KEY()

    if Constants.FUNCTION6_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function6_KEY as _Function6_KEY
        _Function6_KEY()

    if Constants.FUNCTION7_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function7_KEY as _Function7_KEY
        _Function7_KEY()

    if Constants.FUNCTION8_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function8_KEY as _Function8_KEY
        _Function8_KEY()

    if Constants.FUNCTION9_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function9_KEY as _Function9_KEY
        _Function9_KEY()

    if Constants.FUNCTION10_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function10_KEY as _Function10_KEY
        _Function10_KEY()

    if Constants.FUNCTION11_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function11_KEY as _Function11_KEY
        _Function11_KEY()

    if Constants.FUNCTION12_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function12_KEY as _Function12_KEY
        _Function12_KEY()

    if Constants.FUNCTION13_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function13_KEY as _Function13_KEY
        _Function13_KEY()

    if Constants.FUNCTION14_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function14_KEY as _Function14_KEY
        _Function14_KEY()

    if Constants.FUNCTION15_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Function15_KEY as _Function15_KEY
        _Function15_KEY()

    if Constants.NUMLOCK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import NumLock_KEY as _NumLock_KEY
        _NumLock_KEY()

    if Constants.CAPSLOCK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import CapsLock_KEY as _CapsLock_KEY
        _CapsLock_KEY()

    if Constants.SCROLLLOCK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import ScrollLock_KEY as _ScrollLock_KEY
        _ScrollLock_KEY()

    if Constants.RIGHTSHIFT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightShift_KEY as _RightShift_KEY
        _RightShift_KEY()

    if Constants.LEFTSHIFT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftShift_KEY as _LeftShift_KEY
        _LeftShift_KEY()

    if Constants.SHIFT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Shift_KEY as _Shift_KEY
        _Shift_KEY()

    if Constants.RIGHTCONTROL_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightControl_KEY as _RightControl_KEY
        _RightControl_KEY()

    if Constants.LEFTCONTROL_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftControl_KEY as _LeftControl_KEY
        _LeftControl_KEY()

    if Constants.CONTROL_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Control_KEY as _Control_KEY
        _Control_KEY()

    if Constants.RIGHTALT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightAlt_KEY as _RightAlt_KEY
        _RightAlt_KEY()

    if Constants.LEFTALT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftAlt_KEY as _LeftAlt_KEY
        _LeftAlt_KEY()

    if Constants.ALT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Alt_KEY as _Alt_KEY
        _Alt_KEY()

    if Constants.RIGHTMETA_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightMeta_KEY as _RightMeta_KEY
        _RightMeta_KEY()

    if Constants.LEFTMETA_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftMeta_KEY as _LeftMeta_KEY
        _LeftMeta_KEY()

    if Constants.META_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Meta_KEY as _Meta_KEY
        _Meta_KEY()

    if Constants.LEFTSUPER_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftSuper_KEY as _LeftSuper_KEY
        _LeftSuper_KEY()

    if Constants.RIGHTSUPER_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightSuper_KEY as _RightSuper_KEY
        _RightSuper_KEY()

    if Constants.SUPER_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Super_KEY as _Super_KEY
        _Super_KEY()

    if Constants.MODE_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Mode_KEY as _Mode_KEY
        _Mode_KEY()

    if Constants.HELP_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Help_KEY as _Help_KEY
        _Help_KEY()

    if Constants.PRINT_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Print_KEY as _Print_KEY
        _Print_KEY()

    if Constants.SYSTEMREQUEST_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import SystemRequest_KEY as _SystemRequest_KEY
        _SystemRequest_KEY()

    if Constants.BREAK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Break_KEY as _Break_KEY
        _Break_KEY()

    if Constants.MENU_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Menu_KEY as _Menu_KEY
        _Menu_KEY()

    if Constants.POWER_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Power_KEY as _Power_KEY
        _Power_KEY()

    if Constants.EURO_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Euro_KEY as _Euro_KEY
        _Euro_KEY()

    if Constants.ANDROIDBACK_KEY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AndroidBack_KEY as _AndroidBack_KEY
        _AndroidBack_KEY()


    if Constants.LEFTBUTTON_MOUSE_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LeftButton_MOUSE as _LeftButton_MOUSE
        _LeftButton_MOUSE()

    if Constants.MIDDLEBUTTON_MOUSE_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import MiddleButton_MOUSE as _MiddleButton_MOUSE
        _MiddleButton_MOUSE()

    if Constants.RIGHTBUTTON_MOUSE_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RightButton_MOUSE as _RightButton_MOUSE
        _RightButton_MOUSE()

    if Constants.MOUSE_SCROLL_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Mouse_SCROLL as _Mouse_SCROLL
        _Mouse_SCROLL()

    if Constants.MOUSE_POSITION_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Mouse_POSITION as _Mouse_POSITION
        _Mouse_POSITION()

    if Constants.APPTERMINATING_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AppTerminating_EVENT as _AppTerminating_EVENT
        _AppTerminating_EVENT()

    if Constants.APPLOWMEMORY_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AppLowMemory_EVENT as _AppLowMemory_EVENT
        _AppLowMemory_EVENT()

    if Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AppWillEnterBackground_EVENT as _AppWillEnterBackground_EVENT
        _AppWillEnterBackground_EVENT()

    if Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AppDidEnterBackground_EVENT as _AppDidEnterBackground_EVENT
        _AppDidEnterBackground_EVENT()

    if Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AppWillEnterForeground_EVENT as _AppWillEnterForeground_EVENT
        _AppWillEnterForeground_EVENT()

    if Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AppDidEnterForeground_EVENT as _AppDidEnterForeground_EVENT
        _AppDidEnterForeground_EVENT()

    if Constants.AUDIODEVICEADDED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AudioDeviceAdded_EVENT as _AudioDeviceAdded_EVENT
        _AudioDeviceAdded_EVENT()

    if Constants.AUDIODEVICEREMOVED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import AudioDeviceRemoved_EVENT as _AudioDeviceRemoved_EVENT
        _AudioDeviceRemoved_EVENT()

    if Constants.CLIPBOARDUPDATE_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import ClipBoardUpdate_EVENT as _ClipBoardUpdate_EVENT
        _ClipBoardUpdate_EVENT()

    if Constants.DROPFILE_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import DropFile_EVENT as _DropFile_EVENT
        _DropFile_EVENT()

    if Constants.DROPTEXT_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import DropText_EVENT as _DropText_EVENT
        _DropText_EVENT()

    if Constants.DROPBEGIN_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import DropBegin_EVENT as _DropBegin_EVENT
        _DropBegin_EVENT()

    if Constants.DROPCOMPLETE_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import DropComplete_EVENT as _DropComplete_EVENT
        _DropComplete_EVENT()

    if Constants.FINGERMOTION_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import FingerMotion_EVENT as _FingerMotion_EVENT
        _FingerMotion_EVENT()

    if Constants.FINGERDOWN_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import FingerDown_EVENT as _FingerDown_EVENT
        _FingerDown_EVENT()

    if Constants.FINGERUP_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import FingerUp_EVENT as _FingerUp_EVENT
        _FingerUp_EVENT()

    if Constants.KEYMAPCHANGED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import KeyMapChanged_EVENT as _KeyMapChanged_EVENT
        _KeyMapChanged_EVENT()

    if Constants.LOCALECHANGED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import LocaleChanged_EVENT as _LocaleChanged_EVENT
        _LocaleChanged_EVENT()

    if Constants.MULTIGESTURE_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import MultiGesture_EVENT as _MultiGesture_EVENT
        _MultiGesture_EVENT()

    if Constants.QUIT_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import Quit_EVENT as _Quit_EVENT
        _Quit_EVENT()

    if Constants.RENDERTARGETSRESET_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RenderTargetsReset_EVENT as _RenderTargetsReset_EVENT
        _RenderTargetsReset_EVENT()

    if Constants.RENDERDEVICERESET_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import RenderDeviceReset_EVENT as _RenderDeviceReset_EVENT
        _RenderDeviceReset_EVENT()

    if Constants.SYSWMEVENT_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import SysWMEvent_EVENT as _SysWMEvent_EVENT
        _SysWMEvent_EVENT()

    if Constants.WINDOWSHOWN_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowShown_EVENT as _WindowShown_EVENT
        _WindowShown_EVENT()

    if Constants.WINDOWHIDDEN_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowHidden_EVENT as _WindowHidden_EVENT
        _WindowHidden_EVENT()

    if Constants.WINDOWEXPOSED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowExposed_EVENT as _WindowExposed_EVENT
        _WindowExposed_EVENT()

    if Constants.WINDOWMOVED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowMoved_EVENT as _WindowMoved_EVENT
        _WindowMoved_EVENT()

    if Constants.WINDOWRESIZED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowResized_EVENT as _WindowResized_EVENT
        _WindowResized_EVENT()

    if Constants.WINDOWMINIMIZED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowMinimized_EVENT as _WindowMinimized_EVENT
        _WindowMinimized_EVENT()

    if Constants.WINDOWMAXIMIZED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowMaximized_EVENT as _WindowMaximized_EVENT
        _WindowMaximized_EVENT()

    if Constants.WINDOWRESTORED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowRestored_EVENT as _WindowRestored_EVENT
        _WindowRestored_EVENT()

    if Constants.WINDOWENTER_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowEnter_EVENT as _WindowEnter_EVENT
        _WindowEnter_EVENT()

    if Constants.WINDOWLEAVE_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowLeave_EVENT as _WindowLeave_EVENT
        _WindowLeave_EVENT()

    if Constants.WINDOWFOCUSGAINED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowFocusGained_EVENT as _WindowFocusGained_EVENT
        _WindowFocusGained_EVENT()

    if Constants.WINDOWFOCUSLOST_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowFocusLost_EVENT as _WindowFocusLost_EVENT
        _WindowFocusLost_EVENT()

    if Constants.WINDOWCLOSE_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowClose_EVENT as _WindowClose_EVENT
        _WindowClose_EVENT()

    if Constants.WINDOWTAKEFOCUS_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowTakeFocus_EVENT as _WindowTakeFocus_EVENT
        _WindowTakeFocus_EVENT()

    if Constants.WINDOWHITTEST_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowHitTest_EVENT as _WindowHitTest_EVENT
        _WindowHitTest_EVENT()

    if Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowICCPROFChanged_EVENT as _WindowICCPROFChanged_EVENT
        _WindowICCPROFChanged_EVENT()

    if Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import WindowDisplayChanged_EVENT as _WindowDisplayChanged_EVENT
        _WindowDisplayChanged_EVENT()

    if Constants.JOYDEVICEADDED_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import JoyDeviceAdded_EVENT as _JoyDeviceAdded_EVENT
        _JoyDeviceAdded_EVENT()

    if Constants.JOYDEVICEREMOVED_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.event_utils import JoyDeviceRemoved_EVENT as _JoyDeviceRemoved_EVENT
        _JoyDeviceRemoved_EVENT()

    if Constants.DISPLAY_OBJECT in _PassportIntermediary.components_used:
        from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
        _DisplayIntermediary()

    if compile_c_extensions:
        cython_thread.join()

# Jessy