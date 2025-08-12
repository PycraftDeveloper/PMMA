# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string
from libcpp cimport bool

import os
import platform
import os
import distutils

from pmma.core.py_src.Constants import Constants

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

cdef class General:
    def __cinit__(self):
        print("Did you know you don't need to make an instance of this class in order to use it?")

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