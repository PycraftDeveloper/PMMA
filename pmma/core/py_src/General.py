import platform
import os
import distutils

from pmma.core.py_src.Constants import Constants

class General:
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