from typing import Literal

class General:
    @staticmethod
    def get_operating_system() -> Literal["windows", "linux", "macOS", "java", "android"]: ...

    @staticmethod
    def find_executable_nvidia_smi() -> str: ...