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

def __fallback_is_battery_saver_enabled(
        fallback_battery_power_saving_threshold_percentage):

    battery = psutil.sensors_battery()
    if battery is None:
        return False
    # You might consider a threshold to determine battery saver mode
    return (battery.power_plugged == False and
                battery.percent < fallback_battery_power_saving_threshold_percentage)  # Example threshold

def is_battery_saver_enabled(
        fallback_battery_power_saving_threshold_percentage=30):
    try:
        if get_operating_system() == Constants.WINDOWS:
            # Define the necessary constants and structures
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

            SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

            GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
            GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
            GetSystemPowerStatus.restype = wintypes.BOOL

            status = SYSTEM_POWER_STATUS()
            if not GetSystemPowerStatus(ctypes.pointer(status)):
                raise ctypes.WinError()
            print('ACLineStatus', status.ACLineStatus)
            print('BatteryFlag', status.BatteryFlag)
            print('BatteryLifePercent', status.BatteryLifePercent)
            print('BatteryLifeTime', status.BatteryLifeTime)
            print('BatteryFullLifeTime', status.BatteryFullLifeTime)

            # Check if battery saver is on
            return bool(status.BatteryFlag & SYSTEM_POWER_STATUS_BATTERY_SAVER_ON)

        elif get_operating_system() == Constants.MACOS:
            output = subprocess.check_output(['pmset', '-g', 'batt'], text=True)
            # Check if battery saver is mentioned in the output
            return "Power Source: Battery" in output and "Low Power Mode: 1" in output
        else:
            return __fallback_is_battery_saver_enabled(
                fallback_battery_power_saving_threshold_percentage)
    except Exception as error:
        print(error)
        return __fallback_is_battery_saver_enabled(
            fallback_battery_power_saving_threshold_percentage)