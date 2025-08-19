# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

import os
import platform
import os
import distutils
import json
import datetime
import random

import requests

from pmma.core.py_src.Constants import Constants
from pmma.core.py_src.Utility import Registry

from Logger cimport Logger

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" namespace "CPP_General" nogil:
    void Set_PMMA_Location(string location) except + nogil
    void Set_Path_Separator(string separator) except + nogil

    string Get_PMMA_Location() except + nogil

    bool Is_Power_Saving_Mode_Enabled(bool ForceRefresh) except + nogil
    bool Is_DebugModeEnabled() except + nogil
    void Set_DebugModeEnabled(bool DebugMode) except + nogil

    bool IsWindowCreated() except + nogil
    bool IsApplicationRunning() except + nogil

    bool IsEscapeKeyToCloseWindow() except + nogil
    void SetEscapeKeyToCloseWindow(bool EscapeKeyToCloseWindow) except + nogil

    bool IsF11KeyToToggleFullscreen() except + nogil
    void SetF11KeyToToggleFullscreen(bool F11KeyToToggleFullscreen) except + nogil

    string GetCurrent_PMMA_Version() except + nogil
    string GetLatest_PMMA_Version() except + nogil

    void SetLatest_PMMA_Version(string latest_version) except + nogil

    bool IsUpdateAvailable() except + nogil

def internal_update_config(update_configuration_location):
    try:
        tag_data = requests.get(
            "https://api.github.com/repos/PycraftDeveloper/PMMA/tags")
        latest_version = json.loads(tag_data.text)[0]["name"]
    except Exception as error:
        return

    current_date_code = datetime.datetime.now().strftime("%Y%m%d")
    future_date = datetime.datetime.now() + datetime.timedelta(
        days=random.randint(14, 30))
    future_date_code = future_date.strftime("%Y%m%d")

    data = {
        "LastCheckDate": current_date_code,
        "NextCheckDate": future_date_code,
        "LatestVersion": latest_version
    }
    with open(update_configuration_location, "w") as update_config_file:
        json.dump(data, update_config_file)

    return latest_version

cdef class General:
    cdef:
        Logger logger

    def __cinit__(self):
        self.logger = Logger()

        self.logger.internal_log_debug(
            24,
            ("General.init - You don't need to instantiate "
                "this class in order to use it."),
            False
        )

    @staticmethod
    def set_pmma_location(path):
        cdef:
            string encoded_path = path.encode('utf-8')

        Set_PMMA_Location(encoded_path)

    @staticmethod
    def set_path_separator():
        cdef:
            string encoded_separator = str(os.sep).encode('utf-8')

        Set_Path_Separator(encoded_separator)

    @staticmethod
    def get_pmma_install_directory():
        cdef string pmma_location = Get_PMMA_Location()
        return pmma_location.c_str().decode('utf-8')

    @staticmethod
    def is_power_saving_mode_enabled(force_refresh=False):
        return Is_Power_Saving_Mode_Enabled(force_refresh)

    @staticmethod
    def get_operating_system():
        if platform.system() == "Windows":
            return Constants.WINDOWS
        elif platform.system() == "Linux":
            if "ANDROID_STORAGE" in os.environ:
                return Constants.ANDROID
            return Constants.LINUX
        elif platform.system() == "Darwin":
            return Constants.MACOS
        elif platform.system() == "Java":
            return Constants.JAVA

    @staticmethod
    def find_executable_nvidia_smi():
        if General.get_operating_system() == Constants.WINDOWS:
            # If the platform is Windows and nvidia-smi
            # could not be found from the environment path,
            # try to find it from system drive with default installation path
            nvidia_smi = distutils.spawn.find_executable("nvidia-smi")
            if nvidia_smi is None:
                nvidia_smi = f"{os.environ['systemdrive']}\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe"
                if not os.path.isfile(nvidia_smi):
                    nvidia_smi = None
        else:
            nvidia_smi = "nvidia-smi"

        return nvidia_smi

    @staticmethod
    def set_debug_mode(is_debug_mode):
        Set_DebugModeEnabled(is_debug_mode)

    @staticmethod
    def is_debug_mode_enabled():
        return Is_DebugModeEnabled()

    @staticmethod
    def is_window_created():
        return IsWindowCreated()

    @staticmethod
    def is_escape_key_to_close_window():
        return IsEscapeKeyToCloseWindow();

    @staticmethod
    def set_escape_key_to_close_window(escape_key_to_close_window):
        return SetEscapeKeyToCloseWindow(escape_key_to_close_window)

    @staticmethod
    def is_f11_key_to_toggle_full_screen():
        return IsF11KeyToToggleFullscreen()

    @staticmethod
    def set_f11_key_to_toggle_full_screen(f11_key_to_toggle_full_screen):
        SetF11KeyToToggleFullscreen(f11_key_to_toggle_full_screen)

    @staticmethod
    def is_application_running():
        return IsApplicationRunning()

    @staticmethod
    def get_current_pmma_version():
        cdef string cpp_str = GetCurrent_PMMA_Version()
        return cpp_str.c_str().decode('utf-8')

    @staticmethod
    def get_latest_pmma_version():
        if Registry.checking_for_updates and Registry.update_checking_thread is not None:
            Registry.update_checking_thread.join()

        cdef encoded_latest_version
        cdef string cpp_str = GetLatest_PMMA_Version()

        return cpp_str.c_str().decode('utf-8')

    @staticmethod
    def is_update_available():
        if Registry.checking_for_updates and Registry.update_checking_thread is not None:
            Registry.update_checking_thread.join()
        return IsUpdateAvailable()

    @staticmethod
    def internal_check_for_updates():
        cdef encoded_latest_version
        cdef string pmma_location = Get_PMMA_Location()
        cdef string current_pmma_version_cpp_str = GetCurrent_PMMA_Version()

        current_pmma_version = current_pmma_version_cpp_str.c_str().decode('utf-8')

        pmma_install_location = pmma_location.c_str().decode('utf-8')

        configuration_location = pmma_install_location + os.sep + "config"

        os.makedirs(configuration_location, exist_ok=True)

        update_configuration_location = configuration_location + os.sep + "update_config.json"

        display_update_prompt = False

        if os.path.exists(update_configuration_location):
            with open(update_configuration_location, "r") as update_config_file:
                data = json.load(update_config_file)

            current_date_code = datetime.datetime.now().strftime("%Y%m%d")

            if current_date_code >= data["NextCheckDate"]:
                latest_version = internal_update_config(update_configuration_location)
                if latest_version is None:
                    latest_version = data["LatestVersion"]
                display_update_prompt = True

            else:
                latest_version = data["LatestVersion"]

        else:
            latest_version = internal_update_config(update_configuration_location)
            if latest_version is None:
                latest_version = "0.0.0"
            display_update_prompt = True

        encoded_latest_version = latest_version.encode("utf-8")
        SetLatest_PMMA_Version(encoded_latest_version)

        if display_update_prompt and IsUpdateAvailable():
            logger = Logger()

            logger.internal_log_debug(
                17,
                ("Did you know there is a new version of PMMA? You are "
f"currently on version: {current_pmma_version} and the latest version is: "
f"{latest_version}. You can check out the latest features here: "
"'https://github.com/PycraftDeveloper/PMMA/releases' and use `pip install "
"--upgrade pmma` to perform the update!"),
                False
            )

        Registry.checking_for_updates = False