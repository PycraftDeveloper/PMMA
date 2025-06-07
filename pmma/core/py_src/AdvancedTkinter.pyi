from typing import Literal

class Tkinter:
    @staticmethod
    def style(widget: Literal[
            "TButton", "TCheckbutton", "TCombobox", "TEntry", "TFrame",
            "TLabel", "TLabelFrame", "TMenubutton", "TNotebook",
            "TPanedwindow", "Horizontal.TProgressbar",
            "Vertical.TProgressbar", "TRadiobutton", "Horizontal.TScale",
            "Vertical.TScale", "Horizontal.TScrollbar",
            "Vertical.TScrollbar", "TSeparator", "TSizegrip",
            "Treeview"]) -> None: ...