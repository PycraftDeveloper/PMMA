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
        return locale.windows_locale[windll.GetUserDefaultUILanguage()]
    else:
        try:
            result = subprocess.run(['locale'], capture_output=True, text=True, check=True)
            for line in result.stdout.split('\n'):
                if line.startswith('LANG='):
                    return line.split('=')[1]
        except subprocess.CalledProcessError:
            return None

def __fallback_is_battery_saver_enabled():
    battery = psutil.sensors_battery()
    if battery is None:
        return False
    # You might consider a threshold to determine battery saver mode
    return battery.power_plugged == False and battery.percent < 30  # Example threshold

def is_battery_saver_enabled():
    try:
        if get_operating_system() == Constants.WINDOWS:
            # Define the necessary constants and structures
            SYSTEM_POWER_STATUS_ACLINE = 0x00000001
            SYSTEM_POWER_STATUS_BATTERY_SAVER_ON = 0x00000010

            class SYSTEM_POWER_STATUS(ctypes.Structure):
                _fields_ = [
                    ('ACLineStatus', wintypes.BYTE),
                    ('BatteryFlag', wintypes.BYTE),
                    ('BatteryLifePercent', wintypes.BYTE),
                    ('Reserved1', wintypes.BYTE),
                    ('BatteryLifeTime', wintypes.DWORD),
                    ('BatteryFullLifeTime', wintypes.DWORD),
                ]

            # Instantiate the structure
            status = SYSTEM_POWER_STATUS()

            # Call the Windows API to get the power status
            result = ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status))

            # Check if the API call was successful
            if result == 0:
                raise ctypes.WinError()

            # Check if battery saver is on
            return bool(status.BatteryFlag & SYSTEM_POWER_STATUS_BATTERY_SAVER_ON)

        elif get_operating_system() == Constants.MACOS:
            output = subprocess.check_output(['pmset', '-g', 'batt'], text=True)
            # Check if battery saver is mentioned in the output
            return "Power Source: Battery" in output and "Low Power Mode: 1" in output
        else:
            return __fallback_is_battery_saver_enabled()
    except Exception as error:
        print(error)
        return __fallback_is_battery_saver_enabled()