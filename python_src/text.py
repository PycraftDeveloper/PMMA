from tkinter import font
import re

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class Text:
    def __init__(self, canvas=None):
        self.canvas = canvas

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

    def render(
            self,
            text,
            foreground_color=(255, 255, 255),
            background_color=None,
            bold=False,
            italic=False,
            underline=False,
            surface=None,
            word_separator=" "):

        if surface is None:
            surface = self.canvas

        split_text = re.split(f"$( |{word_separator} ", text)
        print(split_text)