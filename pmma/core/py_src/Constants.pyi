from typing import Literal

class Constants:
    DECIMAL: str
    PERCENTAGE: str

    VALUE: str
    UPDATING: str
    MANUALLY_SET: str

    WINDOWS: str
    LINUX: str
    MACOS: str
    JAVA: str
    ANDROID: str

class InternalConstants:
    DATA_COLLECTION_METHODS: str

    SMI: str
    WMI: str
    PYADL: str

    CREATE_NO_WINDOW: Literal[0x08000000]