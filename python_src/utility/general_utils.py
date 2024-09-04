import locale as _locale
import ctypes as _ctypes
import subprocess as _subprocess
import os as _os
from distutils import spawn as _spawn
import random as _random
import platform as _platform
import gc as _gc
import inspect as _inspect
import time as _time
import sys as _sys

import pygame as _pygame
import psutil as _psutil
import pyglet as _pyglet
import getostheme as _getostheme
import num2words as _num2words
from word2number import w2n as _word2number

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.backpack import Backpack
from pmma.python_src.formatters import TimeFormatter as _TimeFormatter

from pmma.python_src.utility.error_utils import *
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

def check_if_object_is_class_or_function(param):
    if _inspect.isclass(param):
        return Constants.CLASS
    elif isinstance(param, object) and not _inspect.isfunction(param):
        return Constants.CLASS_INSTANCE
    elif _inspect.isfunction(param):
        return Constants.FUNCTION
    else:
        return Constants.UNKNOWN

def get_theme():
    if _getostheme.isDarkMode():
        return Constants.DARK
    else:
        return Constants.LIGHT

def get_language():
    return Registry.language

def convert_number_to_text(value):
    try:
        return _num2words.num2words(value, lang=get_language())
    except OverflowError:
        if not "number to word, large value encountered" in Registry.formatted_developer_messages:
            Registry.formatted_developer_messages.append("number to word, large value encountered")
            log_development(f"Woah! {value} is a very large number - too big \
unfortunately to convert to words. Instead the value will be returned as a string.")
        return str(value)

def quit(show_statistics=None, terminate_application=True):
    if show_statistics is None:
        show_statistics = Registry.development_mode

    if show_statistics:
        app_name = _PassportIntermediary.name
        if app_name is None:
            app_name = "The application"

        if Registry.display_initialized:
            time_formatter_instance = _TimeFormatter()
            time_formatter_instance.set_from_second(_time.perf_counter() - Registry.application_start_time)
            log_information(f"PMMA statistics: {app_name} ran for: {time_formatter_instance.get_in_sentence_format()}")
            log_information(f"PMMA statistics: {app_name} had an average \
frame rate of {Registry.application_average_frame_rate['Mean']} Hz.")

        log_information(f"PMMA statistics: {app_name} used {Registry.number_of_instantiated_objects} instances of PMMA operations.")

        if Registry.perlin_noise_prefill_single_samples != 0 or Registry.perlin_noise_prefill_array_samples != 0:
            logged_noise_statistics = log_information(f"PMMA statistics: {app_name} used Noise component. \
In the prefilling process, {Registry.perlin_noise_prefill_single_samples} single \
samples where used, and {Registry.perlin_noise_prefill_array_samples}/10 array samples where used.")
            if logged_noise_statistics:
                log_development("The Noise component of PMMA uses a prefilling process to try \
and identify the minimum and maximum values for each noise method. This is required as depending \
on how PMMA uses compilation - or not uses compilation - the ranges can change as the precision \
used to represent floating point numbers may change. Also, 'single samples' refers to the methods \
that return single values, rather than an nD-array of values - known as 'array samples' here. The \
reason why the 'single samples' attribute is often much higher is that for 'array samples' many \
single values are returned in a single call, rather than the one returned by the 'single samples' \
operations, meaning that fewer need to be called for every single call. Additionally, a limit of a \
nD size of 10 is enforced as larger values often result in excessive memory usage, especially when \
generating 3D arrays.")

    log_development("PMMA is now exiting. Thanks for using PMMA!")
    keys = list(Registry.pmma_module_spine.keys())
    for key in keys:
        log_information(f"Quitting PMMA object with ID: {key}")
        Registry.pmma_module_spine[key].quit(do_garbage_collection=False)

    del Registry.pmma_module_spine

    if Registry.display_mode == Constants.PYGAME:
        _pygame.quit()

    _gc.collect()

    if terminate_application:
        _sys.exit(0)

def compute():
    Registry.power_saving_mode = is_battery_saver_enabled()

    Registry.in_game_loop = True

    Registry.compute_component_called = True

    new_iteration_id = _random.random()
    while new_iteration_id == Registry.iteration_id:
        new_iteration_id = _random.random()
    Registry.iteration_id = new_iteration_id

    number_of_draw_calls = Registry.number_of_draw_calls
    total_time_spent_drawing = Registry.total_time_spent_drawing
    Registry.number_of_draw_calls = 0
    Registry.total_time_spent_drawing = 0

    if _PassportIntermediary.passport_changed:
        _PassportIntermediary.passport_changed = False
        register_application()

    if Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys() and not Constants.EVENTS_OBJECT in Registry.pmma_module_spine.keys():
        log_development("You have created a display through PMMA, but haven't \
created an events object. Handling events for your PMMA display is important as \
it tells the operating system that the application is still running and allows the \
user to interact with your application. Failure to do this can lead to an unresponsive \
window which can cause unexpected behavior.")

    if number_of_draw_calls > 600 and Registry.application_average_frame_rate['Samples'] > 3:
        if not "render performance is limiting" in Registry.formatted_developer_messages:
            log_development(f"Your application performance might soon be degraded by \
    the time spent handling draw calls. Consider switching to the more optimized Render \
    Pipeline through PMMA to avoid any potential slowdowns.")

    if total_time_spent_drawing != 0:
        if 1/(total_time_spent_drawing) < Registry.refresh_rate * 0.9 and Registry.application_average_frame_rate['Samples'] > 3:
            if not "render performance is limiting" in Registry.formatted_developer_messages:
                Registry.formatted_developer_messages.append("render performance is limiting")
                log_development(f"Your application performance is limited by the total \
    number of draw calls being made. The program spent {total_time_spent_drawing}s on \
    {number_of_draw_calls} total render calls, limiting your maximum refresh rate to: \
    {1/(total_time_spent_drawing)}. Switching to the more optimized Render Pipeline will \
    likely improve application performance. Note that this message will only appear once, but \
    may reflect any degraded performance beyond this point.")

    if Constants.DISPLAY_OBJECT in Registry.pmma_module_spine:
        if Registry.pmma_module_spine[Constants.WINDOWRESTORED_EVENT_OBJECT].get_value():
            Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].set_window_minimized(False)
        elif Registry.pmma_module_spine[Constants.WINDOWMINIMIZED_EVENT_OBJECT].get_value():
            Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].set_window_minimized(True)
        if Registry.pmma_module_spine[Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].get_value():
            Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].set_window_in_focus(True)
        elif Registry.pmma_module_spine[Constants.WINDOWFOCUSLOST_EVENT_OBJECT].get_value():
            Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].set_window_in_focus(False)

def register_application():
    if get_operating_system() == Constants.WINDOWS:
        VERSION = _PassportIntermediary.version
        AUTHOR = _PassportIntermediary.author
        APPLICATION_NAME = _PassportIntermediary.name
        SUB_APPLICATION_NAME = _PassportIntermediary.sub_name
        myappid = f"{AUTHOR}.{APPLICATION_NAME}.{SUB_APPLICATION_NAME}.{VERSION}"
        _ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def log_development(message, do_traceback=False, repeat_for_effect=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        return Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_development(
            message,
            do_traceback=do_traceback,
            repeat_for_effect=repeat_for_effect)

    return False

def log_information(message, do_traceback=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        return Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_information(
            message,
            do_traceback=do_traceback)

    return False

def log_warning(message, do_traceback=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        return Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_warning(
            message,
            do_traceback=do_traceback)

    return False

def log_error(message, do_traceback=True):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        return Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_error(
            message,
            do_traceback=do_traceback)
    return False

def get_operating_system():
    if _platform.system() == "Windows":
        return Constants.WINDOWS
    elif _platform.system() == "Linux":
        if "ANDROID_STORAGE" in _os.environ:
            return Constants.ANDROID
        return Constants.LINUX
    elif _platform.system() == "Darwin":
        return Constants.MACOS
    elif _platform.system() == "Java":
        return Constants.JAVA

def is_battery_saver_enabled(
        fallback_battery_power_saving_threshold_percentage=30,
        care_if_running_on_battery=True):
    try:
        battery = _psutil.sensors_battery()
        if battery is None:
            return False

        using_battery = battery.power_plugged == False

        if care_if_running_on_battery is False:
            using_battery = True

        if get_operating_system() == Constants.WINDOWS:
            result = _subprocess.check_output(['powercfg', '/getactivescheme'], text=True)
            result = result.lower()

            if ("saver" in result or "efficiency" in result) and using_battery:
                return True

        elif get_operating_system() == Constants.MACOS:
            output = _subprocess.check_output(['pmset', '-g', 'batt'], text=True)
            # Check if battery saver is mentioned in the output
            return using_battery and "Low Power Mode: 1" in output
        else:
            return battery.percent < fallback_battery_power_saving_threshold_percentage and using_battery
    except Exception as error:
        print(error)
        return battery.percent < fallback_battery_power_saving_threshold_percentage and using_battery

def random_real_number(negatives=True):
    integer = _random.randint(-100, 100)
    decimal = _random.random()
    if negatives:
        return integer + decimal
    else:
        return abs(integer + decimal)

def set_display_mode(display_mode=Constants.PYGAME):
    Registry.display_mode = display_mode
    Registry.display_mode_set = True
    if display_mode == Constants.PYGAME:
        _os.environ["SDL_VIDEO_CENTERED"] = "1"

        if log_information(Registry.pygame_launch_message) is False:
            print(Registry.pygame_launch_message)

        _pygame.init()

def up(path: str) -> str:
    return path[::-1].split(_os.sep, 1)[-1][::-1]

def find_executable_nvidia_smi():
    if get_operating_system() == Constants.WINDOWS:
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
    if get_operating_system() == Constants.WINDOWS:
        try:
            windll = _ctypes.windll.kernel32
            detected_language = _locale.windows_locale[
                windll.GetUserDefaultUILanguage()]
        except:
            try:
                result = _subprocess.run(
                    ['locale'],
                    capture_output=True,
                    text=True,
                    check=True)

                for line in result.stdout.split('\n'):
                    if line.startswith('LANG='):
                        detected_language = line.split('=')[1]
            except _subprocess.CalledProcessError:
                detected_language = None
    else:
        try:
            result = _subprocess.run(
                ['locale'],
                capture_output=True,
                text=True,
                check=True)

            for line in result.stdout.split('\n'):
                if line.startswith('LANG='):
                    detected_language = line.split('=')[1]
        except _subprocess.CalledProcessError:
            detected_language = None

    if detected_language is None:
        detected_language = "en_US"

    Registry.language = detected_language
    Backpack.language = detected_language

def initialize(instance, unique_instance=None, add_to_pmma_module_spine=False, requires_display_mode_set=True):
    instance._shut_down = False
    instance._attributes = []

    if Registry.pmma_initialized is False:
        log_development("You haven't yet initialized PMMA. This can be \
done by calling 'pmma.init()' any time before using any of PMMA functions. It \
is vital that you do this prior to using PMMA as it ensures optimal configuration \
with your machine, and gets PMMA ready to be used.")
        log_error("PMMA has not been initialized. Call 'pmma.init()' before using PMMA.")
        raise DidNotInitializeError("Call 'pmma.init()' before using PMMA")

    if requires_display_mode_set and Registry.display_mode_set is False:
        set_display_mode()

    if unique_instance is not None:
        if unique_instance in Constants.OBJECT_IDENTIFIERS:
            if unique_instance in Registry.pmma_module_spine.keys():
                log_warning(f"{unique_instance.capitalize()} object already exists.")

                log_development("Some PMMA objects can only be initialized once. \
This is to avoid creating unexpected behavior.")

                raise TooManyInstancesError(f"{unique_instance.capitalize()} object already exists.")
        else:
            log_development(f"{unique_instance.capitalize()} name was not recognized to \
PMMA. To register it, make sure it exists in the 'Constants' object, and in its attribute \
'OBJECT_IDENTIFIERS' list.")

    if add_to_pmma_module_spine:
        Registry.pmma_module_spine[unique_instance] = instance

    Registry.number_of_instantiated_objects += 1

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
                    out_data.append(Constants.ALPHA)
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

def environ_to_registry():
    for key in Registry.__dict__:
        check_key = f"PMMA_{key}"
        if check_key in _os.environ:
            value = _os.environ[check_key]
            if "." in value:
                data_type, value = value.split(".")
                data_type = data_type.lower()
                if data_type == "int":
                    value = int(value)
                elif data_type == "float":
                    value = float(value)
                elif data_type == "bool":
                    value = bool(0) if value.lower() == "false" else bool(1)
            setattr(Registry, key, value)