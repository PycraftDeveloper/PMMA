from typing import Literal

class General:
    @staticmethod
    def is_power_saving_mode_enabled() -> bool: ...

    @staticmethod
    def get_operating_system() -> Literal["windows", "linux", "macOS", "java", "android"]: ...

    @staticmethod
    def find_executable_nvidia_smi() -> str: ...

    @staticmethod
    def get_pmma_install_dir() -> str: ...

    @staticmethod
    def set_debug_mode(is_debug_mode: bool) -> None: ...

    @staticmethod
    def is_debug_mode_enabled() -> bool: ...