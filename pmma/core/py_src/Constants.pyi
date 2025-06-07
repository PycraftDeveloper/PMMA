from typing import Literal, Iterable

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

    TKINTER_STYLE_BUTTON: str
    TKINTER_STYLE_CHECKBUTTON: str
    TKINTER_STYLE_COMBOBOX: str
    TKINTER_STYLE_ENTRY: str
    TKINTER_STYLE_FRAME: str
    TKINTER_STYLE_LABEL: str
    TKINTER_STYLE_LABELFRAME: str
    TKINTER_STYLE_MENUBUTTON: str
    TKINTER_STYLE_NOTEBOOK: str
    TKINTER_STYLE_PANEDWINDOW: str
    TKINTER_STYLE_HORIZONTAL_PROGRESSBAR: str
    TKINTER_STYLE_VERTICAL_PROGRESSBAR: str
    TKINTER_STYLE_RADIOBUTTON: str
    TKINTER_STYLE_HORIZONTAL_SCALE: str
    TKINTER_STYLE_VERTICAL_SCALE: str
    TKINTER_STYLE_HORIZONTAL_SCROLLBAR: str
    TKINTER_STYLE_VERTICAL_SCROLLBAR: str
    TKINTER_STYLE_SEPARATOR: str
    TKINTER_STYLE_SIZEGRIP: str
    TKINTER_STYLE_TREEVIEW: str

class InternalConstants:
    DATA_COLLECTION_METHODS: str

    SMI: str
    WMI: str
    PYADL: str

    CREATE_NO_WINDOW: Literal[0x08000000]

    TKINTER_STYLES: Iterable[
        Literal[
            "TButton", "TCheckbutton", "TCombobox", "TEntry", "TFrame",
            "TLabel", "TLabelFrame", "TMenubutton", "TNotebook",
            "TPanedwindow", "Horizontal.TProgressbar",
            "Vertical.TProgressbar", "TRadiobutton", "Horizontal.TScale",
            "Vertical.TScale", "Horizontal.TScrollbar",
            "Vertical.TScrollbar", "TSeparator", "TSizegrip", "Treeview"]]