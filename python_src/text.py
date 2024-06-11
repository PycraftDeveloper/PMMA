from tkinter import font

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Text:
    def __init__(self):
        pass

    def get_system_font(size=None, bold=None, italic=None):
        system_font = font.nametofont("TkTextFont")
        system_font_dictionary = system_font.actual()

        name = system_font_dictionary["family"]
        if size is None:
            size = system_font_dictionary["size"]

        if bold is None:
            bold = system_font_dictionary["weight"] == "bold"

        if italic is None:
            italic = system_font_dictionary["slant"] == "italic"

        if Registry.display_mode == Constants.PYGAME:
            return Registry.graphics_backend.font.SysFont(name, size, bold, italic)

