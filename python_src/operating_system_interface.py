import platform
import ctypes
from ctypes import wintypes
import subprocess
import locale

import getostheme
import psutil

import pmma.python_src.core as core
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

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