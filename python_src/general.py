import gc
import inspect
import platform
import ctypes
import subprocess
import locale
import os

import getostheme
import psutil
import pyglet
import pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.passport import PassportIntermediary

def up(path: str) -> str:
    return path[::-1].split(os.sep, 1)[-1][::-1]

class OpenGLObject:
    def __init__(self, _object):
        initialize(self)

        self.object = _object

    def get(self):
        return self.object

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __del__(self, do_garbage_collection=False):
        if self.shutdown is False:
            self.object.release()
            del self.object
            del self
            if do_garbage_collection:
                gc.collect()

def initialize(instance, unique_instance=None, add_to_pmma_module_spine=False):
    instance._shut_down = False
    instance.attributes = []

    if Registry.pmma_initialized is False:
        log_development("You haven't yet initialized PMMA. This can be \
done by calling 'pmma.init()' any time before using any of PMMA functions. It \
is vital that you do this prior to using PMMA as it ensures optimal configuration \
with your machine, and gets PMMA ready to be used.")
        log_error("PMMA has not been initialized. Call 'pmma.init()' before using PMMA.")
        raise DidNotInitializeError("Call 'pmma.init()' before using PMMA")

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

    Registry.pmma_object_instances[id(instance)] = instance

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
        if check_key in os.environ:
            value = os.environ[check_key]
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

def register_application():
    if get_operating_system() == Constants.WINDOWS:
        VERSION = PassportIntermediary.version
        AUTHOR = PassportIntermediary.author
        APPLICATION_NAME = PassportIntermediary.name
        SUB_APPLICATION_NAME = PassportIntermediary.sub_name
        myappid = f"{AUTHOR}.{APPLICATION_NAME}.{SUB_APPLICATION_NAME}.{VERSION}"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def compute():
    Registry.power_saving_mode = is_battery_saver_enabled()

    number_of_draw_calls = Registry.number_of_draw_calls
    total_time_spent_drawing = Registry.total_time_spent_drawing
    Registry.number_of_draw_calls = 0
    Registry.total_time_spent_drawing = 0

    if PassportIntermediary.passport_changed:
        PassportIntermediary.passport_changed = False
        register_application()

    if Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys() and not Constants.EVENTS_OBJECT in Registry.pmma_module_spine.keys():
        log_development("You have created a display through PMMA, but haven't \
created an events object. Handling events for your PMMA display is important as \
it tells the operating system that the application is still running and allows the \
user to interact with your application.")

    if number_of_draw_calls > 600:
        log_development(f"Your application performance might soon be degraded by \
the time spent handling draw calls. Consider switching to the more optimized Render \
Pipeline through PMMA to avoid any potential slowdowns.")

    if total_time_spent_drawing == 0:
        return

    if 1/(total_time_spent_drawing) < Registry.refresh_rate:
        if not "render performance is limiting" in Registry.formatted_developer_messages:
            Registry.formatted_developer_messages.append("render performance is limiting")
            log_development(f"Your application performance is limited by the total \
number of draw calls being made. The program spent {total_time_spent_drawing}s on \
{number_of_draw_calls} total render calls, limiting your maximum refresh rate to: \
{1/(total_time_spent_drawing)}. Switching to the more optimized Render Pipeline will \
likely improve application performance. Note that this message will only appear once, but \
may reflect any degraded performance beyond this point.")

def quit():
    keys = list(Registry.pmma_object_instances.keys())
    for key in keys:
        Registry.pmma_object_instances[key].quit()
        del Registry.pmma_object_instances[key]

    if Registry.display_mode == Constants.PYGAME:
        pygame.quit()

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