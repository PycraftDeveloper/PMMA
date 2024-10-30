from locale import windows_locale as _locale__windows_locale
from subprocess import check_output as _subprocess__check_output
from subprocess import run as _subprocess__run
from subprocess import CalledProcessError as _subprocess__CalledProcessorError
import os as _os
from distutils import spawn as _spawn
from random import random as _random__random
from random import randint as _random__randint
from platform import system as _platform__system
from gc import collect as _gc__collect
from inspect import isclass as _inspect__isclass
from inspect import isfunction as _inspect__isfunction
from time import perf_counter as _time__perf_counter
from sys import exit as _sys__exit
from json import dump as _json__dump

from pygame import quit as _pygame__quit
from psutil import sensors_battery as _psutil__sensors_battery
from getostheme import isDarkMode as _getostheme__isDarkMode
from num2words import num2words as _num2words__num2words

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.backpack import Backpack as _Backpack
from pmma.python_src.formatters import TimeFormatter as _TimeFormatter
from pmma.python_src.utility.settings_utils import set_allow_anti_aliasing as _set_allow_anti_aliasing
from pmma.python_src.utility.settings_utils import set_anti_aliasing_level as _set_anti_aliasing_level

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

if _platform__system() == "Windows":
    from ctypes import windll as _ctypes__windll

def get_execution_time(function, *args, **kwargs):
    start_time = _time__perf_counter()
    result = function(*args, **kwargs)
    end_time = _time__perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

def get_execution_inverse_time(function, *args, **kwargs):
    start_time = _time__perf_counter()
    result = function(*args, **kwargs)
    end_time = _time__perf_counter()
    execution_time = end_time - start_time
    return result, 1/execution_time

def targeted_profile_start():
    if _Registry.profiler is None:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
            "Just a quick heads up, you are attempting to profile this specifically \
however you haven't enabled profiling in 'pmma.init()'. Therefore this has no effect.")

        return
    if _Registry.targeted_profile_application:
        _Registry.profiler.enable()
    else:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
            "Just a quick heads up, you are attempting to profile this specifically \
however you already specified that you want to profile everything, so this has no effect. \
This behavior can be configured in 'pmma.init()'.")

def targeted_profile_end():
    if _Registry.profiler is None:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
            "Just a quick heads up, you are attempting to profile this specifically \
however you haven't enabled profiling in 'pmma.init()'. Therefore this has no effect.")

        return
    if _Registry.targeted_profile_application:
        _Registry.profiler.disable()
    else:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
            "Just a quick heads up, you are attempting to profile this specifically \
however you already specified that you want to profile everything, so this has no effect. \
This behavior can be configured in 'pmma.init()'.")

def check_if_object_is_class_or_function(param):
    if _inspect__isclass(param):
        return _Constants.CLASS
    elif isinstance(param, object) and not _inspect__isfunction(param):
        return _Constants.CLASS_INSTANCE
    elif _inspect__isfunction(param):
        return _Constants.FUNCTION
    else:
        return _Constants.UNKNOWN

def get_theme():
    if _getostheme__isDarkMode():
        return _Constants.DARK
    else:
        return _Constants.LIGHT

def convert_number_to_text(value):
    try:
        return _num2words__num2words(value, lang=_Registry.language)
    except OverflowError:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
            "Woah! {} is a very large number - too big \
unfortunately to convert to words. Instead the value will be returned as a string.", variables=[value])
        return str(value)

def quit(show_statistics=None, terminate_application=True):
    if _Registry.profiler is not None:
        _Registry.profiler.disable()
        if _Registry.profile_result_path is None:
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                "We are using the default locations for storing profile information as you never \
specified where you would like them to be placed. This can be done through: \
`pmma.set_profile_result_path(path)`. Instead we are going to be storing your profiled results here: {}",
                variables=[", ".join(_Registry.logging_path)])
            path =_Registry.logging_path
        else:
            path = _Registry.profile_result_path

        if type(path) == list or type(path) == tuple:
            for locations in path:
                _Registry.profiler.dump_stats(locations)
        else:
            with open(path, "w") as file:
                _Registry.profiler.dump_stats(file)

    if _PassportIntermediary.passport_file_location is not None:
        passport = {"components used": _PassportIntermediary.components_used}
        with open(_PassportIntermediary.passport_file_location, "w") as file:
            _json__dump(passport, file)

    if show_statistics is None:
        show_statistics = _Registry.development_mode

    if show_statistics:
        app_name = _PassportIntermediary.name
        if app_name is None:
            app_name = "The application"

        if _Registry.display_initialized:
            time_formatter_instance = _TimeFormatter()
            time_formatter_instance.set_from_second(_time__perf_counter() - _Registry.application_start_time)
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(
                "PMMA statistics: {} ran for: {}", variables=[app_name, time_formatter_instance.get_in_sentence_format()])

        if _Registry.application_finished_loading_time is not None:
            time_formatter_instance.set_from_second(_Registry.application_finished_loading_time - _Registry.application_start_time)
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(
                "PMMA statistics: {} loaded in: {}", variables=[app_name, time_formatter_instance.get_in_sentence_format()])

        if _Registry.display_initialized:
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information("PMMA statistics: {} had an average \
frame rate of {} Hz.", variables=[app_name, _Registry.application_average_frame_rate['Mean']])

        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(
            "PMMA statistics: {} used {} instances of PMMA operations.", variables=[app_name, _Registry.number_of_instantiated_objects])

        if _Registry.perlin_noise_prefill_single_samples != 0 or _Registry.perlin_noise_prefill_array_samples != 0:
            logged_noise_statistics = _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(
                "PMMA statistics: {} used Noise component. In the prefilling process, {} single \
samples where used, and {}/10 array samples where used.",
                variables=[app_name, _Registry.perlin_noise_prefill_single_samples,
                _Registry.perlin_noise_prefill_array_samples])

            if logged_noise_statistics:
                _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
                    "The Noise component of PMMA uses a prefilling process to try \
and identify the minimum and maximum values for each noise method. This is required as depending \
on how PMMA uses compilation - or not uses compilation - the ranges can change as the precision \
used to represent floating point numbers may change. Also, 'single samples' refers to the methods \
that return single values, rather than an nD-array of values - known as 'array samples' here. The \
reason why the 'single samples' attribute is often much higher is that for 'array samples' many \
single values are returned in a single call, rather than the one returned by the 'single samples' \
operations, meaning that fewer need to be called for every single call. Additionally, a limit of a \
nD size of 10 is enforced as larger values often result in excessive memory usage, especially when \
generating 3D arrays.")

    _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].clear_internal_logs()
    _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].clear_external_logs()

    _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development(
        "PMMA is now exiting. Thanks for using PMMA!")

    if _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(
            "Quitting PMMA object with ID: {}",
            variables=[_Constants.DISPLAY_OBJECT],
            repeat_for_effect=True)

        _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].quit(do_garbage_collection=False)
        del _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

    logger = _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT]
    del _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT]

    keys = list(_Registry.pmma_module_spine.keys())

    for key in keys:
        logger.log_information(
            "Quitting PMMA object with ID: {}",
            variables=[key],
            repeat_for_effect=True)

        _Registry.pmma_module_spine[key].quit(do_garbage_collection=False)

    del _Registry.pmma_module_spine

    _pygame__quit()

    _gc__collect()

    logger.log_information(
        "Quitting PMMA object with ID: logging intermediary",
        repeat_for_effect=True)

    logger.quit(do_garbage_collection=True)

    if terminate_application:
        _sys__exit(0)

def compute(allow_anti_aliasing_adjustments_for_low_power_mode=True, allow_shape_quality_adjustments_for_low_power_mode=True):
    if (_Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine and
            _Constants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine):
        if _Registry.pmma_module_spine[_Constants.WINDOWRESIZED_EVENT_OBJECT].get_value():
            _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].on_window_size_changed()

    if _time__perf_counter() - _Registry.power_status_checked_time > 10:
        _Registry.power_saving_mode = is_battery_saver_enabled()

    if _Registry.power_saving_mode:
        if allow_anti_aliasing_adjustments_for_low_power_mode:
            _set_allow_anti_aliasing(False)
            _set_anti_aliasing_level(0)

        if allow_shape_quality_adjustments_for_low_power_mode and _Registry.initial_shape_quality is None:
            _Registry.initial_shape_quality = _Registry.shape_quality
            _Registry.shape_quality /= 0.5
            if _Registry.shape_quality < 0.4:
                _Registry.shape_quality = 0.4
    else:
        if allow_anti_aliasing_adjustments_for_low_power_mode:
            if _Registry.manually_set_do_anti_aliasing is None:
                _set_allow_anti_aliasing(True)
            else:
                _set_allow_anti_aliasing(_Registry.manually_set_do_anti_aliasing)

            if _Registry.manually_set_anti_aliasing_level is None:
                _set_anti_aliasing_level(2)
            else:
                _set_anti_aliasing_level(_Registry.manually_set_anti_aliasing_level)

        if allow_shape_quality_adjustments_for_low_power_mode and _Registry.initial_shape_quality is not None:
            _Registry.shape_quality = _Registry.initial_shape_quality
            _Registry.initial_shape_quality = None

    if _Registry.in_game_loop is False: # first run detection
        _Registry.application_finished_loading_time = _time__perf_counter()

    _Registry.in_game_loop = True

    _Registry.compute_component_called = True

    new_iteration_id = _random__random()
    while new_iteration_id == _Registry.iteration_id:
        new_iteration_id = _random__random()
    _Registry.iteration_id = new_iteration_id

    number_of_render_updates = _Registry.number_of_render_updates
    total_time_spent_drawing = _Registry.total_time_spent_drawing
    _Registry.number_of_render_updates = 0
    _Registry.total_time_spent_drawing = 0

    if _PassportIntermediary.passport_changed:
        _PassportIntermediary.passport_changed = False
        register_application()

    if _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys() and not _Constants.EVENTS_OBJECT in _Registry.pmma_module_spine.keys():
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("You have created a display through PMMA, but haven't \
created an events object. Handling events for your PMMA display is important as \
it tells the operating system that the application is still running and allows the \
user to interact with your application. Failure to do this can lead to an unresponsive \
window which can cause unexpected behavior.")

    if number_of_render_updates > 600 and _Registry.application_average_frame_rate['Samples'] > 3:
        _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("Your application performance might soon be degraded by \
the time spent handling draw calls. Consider switching to the more optimized Render \
Pipeline through PMMA to avoid any potential slowdowns.")

    if total_time_spent_drawing != 0:
        if 1/(total_time_spent_drawing) < _Registry.refresh_rate * 0.9 and _Registry.application_average_frame_rate['Samples'] > 3:
            time_formatter_instance = _TimeFormatter()
            time_formatter_instance.set_from_second(total_time_spent_drawing)

            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_development("Your application performance is limited by the total \
number of draw calls being made. The program spent {} on \
{} total render calls, limiting your maximum refresh rate to: \
{} Hz. Switching to the more optimized Render Pipeline will \
likely improve application performance. Note that this message will only appear once, but \
may reflect any degraded performance beyond this point.", variables=[time_formatter_instance.get_in_sentence_format(), number_of_render_updates, 1/(total_time_spent_drawing)])

    if _Registry.display_initialized:
        if (_Constants.WINDOWRESTORED_EVENT_OBJECT in _Registry.pmma_module_spine and
                _Registry.pmma_module_spine[_Constants.WINDOWRESTORED_EVENT_OBJECT].get_value()):
            _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].set_window_minimized(False)
        elif (_Constants.WINDOWMINIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine and
                _Registry.pmma_module_spine[_Constants.WINDOWMINIMIZED_EVENT_OBJECT].get_value()):
            _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].set_window_minimized(True)
        if (_Constants.WINDOWFOCUSGAINED_EVENT_OBJECT in _Registry.pmma_module_spine and
                _Registry.pmma_module_spine[_Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].get_value()):
            _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].set_window_in_focus(True)
        elif (_Constants.WINDOWFOCUSLOST_EVENT_OBJECT in _Registry.pmma_module_spine and
                _Registry.pmma_module_spine[_Constants.WINDOWFOCUSLOST_EVENT_OBJECT].get_value()):
            _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].set_window_in_focus(False)

def register_application():
    if get_operating_system() == _Constants.WINDOWS:
        VERSION = _PassportIntermediary.version
        AUTHOR = _PassportIntermediary.author
        APPLICATION_NAME = _PassportIntermediary.name
        SUB_APPLICATION_NAME = _PassportIntermediary.sub_name
        myappid = f"{AUTHOR}.{APPLICATION_NAME}.{SUB_APPLICATION_NAME}.{VERSION}"
        _ctypes__windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def get_operating_system():
    if _platform__system() == "Windows":
        return _Constants.WINDOWS
    elif _platform__system() == "Linux":
        if "ANDROID_STORAGE" in _os.environ:
            return _Constants.ANDROID
        return _Constants.LINUX
    elif _platform__system() == "Darwin":
        return _Constants.MACOS
    elif _platform__system() == "Java":
        return _Constants.JAVA

def is_battery_saver_enabled(
        fallback_battery_power_saving_threshold_percentage=30,
        care_if_running_on_battery=True):
    try:
        battery = _psutil__sensors_battery()
        if battery is None:
            return False

        using_battery = battery.power_plugged == False

        if care_if_running_on_battery is False:
            using_battery = True

        if get_operating_system() == _Constants.WINDOWS:
            result = _subprocess__check_output(['powercfg', '/getactivescheme'], text=True)
            result = result.lower()

            if ("saver" in result or "efficiency" in result) and using_battery:
                return True

        elif get_operating_system() == _Constants.MACOS:
            output = _subprocess__check_output(['pmset', '-g', 'batt'], text=True)
            # Check if battery saver is mentioned in the output
            return using_battery and "Low Power Mode: 1" in output
        else:
            return battery.percent < fallback_battery_power_saving_threshold_percentage and using_battery
    except Exception as error:
        print(error)
        return battery.percent < fallback_battery_power_saving_threshold_percentage and using_battery

def random_real_number(negatives=True):
    integer = _random__randint(-100, 100)
    decimal = _random__random()
    if negatives:
        return integer + decimal
    else:
        return abs(integer + decimal)

def up(path: str) -> str:
    return path[::-1].split(_Constants.PATH_SEPARATOR, 1)[-1][::-1]

def find_executable_nvidia_smi():
    if get_operating_system() == _Constants.WINDOWS:
        # If the platform is Windows and nvidia-smi
        # could not be found from the environment path,
        # try to find it from system drive with default installation path
        nvidia_smi = _spawn.find_executable("nvidia-smi")
        if nvidia_smi is None:
            nvidia_smi = f"{_os.environ['systemdrive']}\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe"
            if not _os.path.isfile(nvidia_smi):
                nvidia_smi = None
    else:
        nvidia_smi = "nvidia-smi"

    return nvidia_smi

def update_language():
    if get_operating_system() == _Constants.WINDOWS:
        try:
            windll = _ctypes__windll.kernel32
            detected_language = _locale__windows_locale[
                windll.GetUserDefaultUILanguage()]
        except:
            try:
                result = _subprocess__run(
                    ['locale'],
                    capture_output=True,
                    text=True,
                    check=True)

                for line in result.stdout.split('\n'):
                    if line.startswith('LANG='):
                        detected_language = line.split('=')[1]
            except _subprocess__CalledProcessorError:
                detected_language = None
    else:
        try:
            result = _subprocess__run(
                ['locale'],
                capture_output=True,
                text=True,
                check=True)

            for line in result.stdout.split('\n'):
                if line.startswith('LANG='):
                    detected_language = line.split('=')[1]
        except _subprocess__CalledProcessorError:
            detected_language = None

    if detected_language is None:
        detected_language = "en_US"

    _Registry.language = detected_language
    _Backpack.language = detected_language

def create_cache_id(*args):
    cache_id = ""
    for arg in args:
        if callable(arg):
            cache_id += id(arg)
        else:
            cache_id += str(arg)
    return cache_id

def swizzle(in_format, data, out_format, handle_alpha=False):
    if in_format == out_format:
        return data
    elif len(data) != len(in_format):
        raise AttributeError("Data length is not compatible")
    else:
        out_data = []
        for character in out_format:
            if not character in in_format:
                if handle_alpha and character.lower() == "a":
                    out_data.append(_Constants.ALPHA)
                else:
                    out_data.append(0)
            else:
                out_data.append(data[in_format.index(character)])
        return out_data

def can_swizzle(in_format, data, out_format):
    if in_format == out_format:
        return True
    elif len(data) != len(in_format):
        return False
    return True

def get_application_run_time():
    return _time__perf_counter() - _Registry.application_start_time

def get_application_startup_duration():
    return _Registry.application_finished_loading_time - _Registry.application_start_time