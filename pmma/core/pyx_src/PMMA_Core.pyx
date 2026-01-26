# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

import atexit, ctypes, subprocess, locale, os, datetime

from pmma.build.General import General

from pmma.core.py_src.Constants import Constants
from pmma.core.py_src.Utility import Registry

cdef extern from "PMMA_Core.hpp" nogil:
    cdef void PMMA_Initialize(string location)

    cdef void PMMA_Uninitialize()

cdef extern from "General.hpp" namespace "CPP_General" nogil:
    void SetLocale(string locale_) except + nogil

def initialize(path):
    cdef:
        encoded_locale
        string encoded_path = path.encode('utf-8')

    PMMA_Initialize(encoded_path)

    if General.get_operating_system() == Constants.OperatingSystems.WINDOWS:
        try:
            from ctypes import windll
            windll = windll.kernel32
            detected_language = locale.windows_locale[
                windll.GetUserDefaultUILanguage()]
        except:
            try:
                result = subprocess.run(
                    ['locale'],
                    capture_output=True,
                    text=True,
                    check=True)

                for line in result.stdout.split('\n'):
                    if line.startswith('LANG='):
                        detected_language = line.split('=')[1]
            except subprocess.CalledProcessError:
                detected_language = None
    else:
        try:
            result = subprocess.run(
                ['locale'],
                capture_output=True,
                text=True,
                check=True)

            for line in result.stdout.split('\n'):
                if line.startswith('LANG='):
                    detected_language = line.split('=')[1]
        except subprocess.CalledProcessError:
            detected_language = None

    if detected_language is None:
        detected_language = "en_US"

    encoded_locale = detected_language.encode("utf-8")
    SetLocale(encoded_locale)

def uninitialize():
    PMMA_Uninitialize()

    if Registry.passport_instance is not None:
        if Registry.profiler_instance is not None:
            Registry.profiler_instance.disable()
            path = Registry.passport_instance.get_profiling_path()
            if os.path.exists(path):
                now = datetime.datetime.now()
                file_name = now.strftime("%d-%m-%Y at %H-%M-%S") + ".txt"
                with open(path + os.sep + file_name, "w") as profile_file:
                    Registry.profiler_instance.print_stats(stream=profile_file)
            else:
                Registry.profiler_instance.print_stats()
    else:
        if Registry.profiler_instance is not None:
            Registry.profiler_instance.disable()
            Registry.profiler_instance.print_stats()

atexit.register(uninitialize)