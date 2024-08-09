from os import environ
import gc
import inspect
import platform
import ctypes
import subprocess
import locale

import getostheme
import psutil

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.draw import DrawIntermediary

def __create_cache_id(*args):
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
        if check_key in environ:
            value = environ[check_key]
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

def log_development(message, do_traceback=False, repeat_for_effect=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_development(
            message,
            do_traceback=do_traceback,
            repeat_for_effect=repeat_for_effect)

        return True
    return False

def log_information(message, do_traceback=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_information(
            message,
            do_traceback=do_traceback)

        return True
    return False

def log_warning(message, do_traceback=False):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_warning(
            message,
            do_traceback=do_traceback)

        return True
    return False

def log_error(message, do_traceback=True):
    if Constants.LOGGING_OBJECT in Registry.pmma_module_spine.keys():
        Registry.pmma_module_spine[Constants.LOGGING_OBJECT].log_error(
            message,
            do_traceback=do_traceback)
        return True
    return False

def compute():
    Registry.power_saving_mode = is_battery_saver_enabled()

    number_of_draw_calls = DrawIntermediary.number_of_draw_calls
    total_time_spent_drawing = DrawIntermediary.total_time_spent_drawing
    DrawIntermediary.number_of_draw_calls = 0
    DrawIntermediary.total_time_spent_drawing = 0

    if number_of_draw_calls > 600:
        log_development(f"Your application performance might soon be degraded by \
the time spent handling draw calls. Consider switching to the more optimized Render \
Pipeline through PMMA to avoid any potential slowdowns.")

    if total_time_spent_drawing == 0:
        return

    if 1/(total_time_spent_drawing) < Registry.refresh_rate:
        log_development(f"Your application performance is limited by the total \
number of draw calls being made. The program spent {total_time_spent_drawing}s on \
{number_of_draw_calls} total render calls, limiting your maximum refresh rate to: \
{1/(total_time_spent_drawing)}. Switching to the more optimized Render Pipeline will \
likely improve application performance.")

def quit():
    keys = list(Registry.pmma_object_instances.keys())
    for key in keys:
        Registry.pmma_object_instances[key].quit()
        del Registry.pmma_object_instances[key]

    gc.collect()

def check_if_object_is_class_or_function(param):
    if inspect.isclass(param):
        return Constants.CLASS
    elif isinstance(param, object) and not inspect.isfunction(param):
        return Constants.CLASS_INSTANCE
    elif inspect.isfunction(param):
        return Constants.FUNCTION
    else:
        return Constants.UNKNOWN

def get_operating_system():
    if platform.system() == "Windows":
        return Constants.WINDOWS
    elif platform.system() == "Linux":
        return Constants.LINUX
    elif platform.system() == "Darwin":
        return Constants.MACOS
    elif platform.system() == "Java":
        return Constants.JAVA

def get_theme():
    if getostheme.isDarkMode():
        return Constants.DARK
    else:
        return Constants.LIGHT

def get_language():
    if get_operating_system() == Constants.WINDOWS:
        windll = ctypes.windll.kernel32
        return locale.windows_locale[
            windll.GetUserDefaultUILanguage()]
    else:
        try:
            result = subprocess.run(
                ['locale'],
                capture_output=True,
                text=True,
                check=True)

            for line in result.stdout.split('\n'):
                if line.startswith('LANG='):
                    return line.split('=')[1]
        except subprocess.CalledProcessError:
            return None

def is_battery_saver_enabled(
        fallback_battery_power_saving_threshold_percentage=30,
        care_if_running_on_battery=True):
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            return False

        using_battery = battery.power_plugged == False

        if care_if_running_on_battery is False:
            using_battery = True

        if get_operating_system() == Constants.WINDOWS:
            result = subprocess.check_output(['powercfg', '/getactivescheme'], text=True)
            result = result.lower()

            if ("saver" in result or "efficiency" in result) and using_battery:
                return True

        elif get_operating_system() == Constants.MACOS:
            output = subprocess.check_output(['pmset', '-g', 'batt'], text=True)
            # Check if battery saver is mentioned in the output
            return using_battery and "Low Power Mode: 1" in output
        else:
            return battery.percent < fallback_battery_power_saving_threshold_percentage and using_battery
    except Exception as error:
        print(error)
        return battery.percent < fallback_battery_power_saving_threshold_percentage and using_battery