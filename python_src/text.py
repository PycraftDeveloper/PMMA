from tkinter import font
import re

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.color import Color

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
            position,
            size=11,
            foreground_color=(255, 255, 255),
            background_color=None,
            bold=False,
            italic=False,
            underline=False,
            canvas=None,
            word_separator = r"(\s+)"):

        defaults = {
            "foreground_color": foreground_color,
            "background_color": background_color,
            "bold": bold,
            "italic": italic,
            "underline": underline,
            "size": size
        }

        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        pattern = rf"(\$\([a-zA-Z]+\))|{word_separator}"

        split_text = [token for token in re.split(pattern, text) if token and not token.isspace()]
        for word in split_text:
            if word.startswith("$(") and word.endswith(")"):
                syntax = word[2:-1]
                foreground_color_pattern = r'^cfg=\(([^()]+)\)$'
                foreground_color_pattern_match = re.match(foreground_color_pattern, syntax)
                background_color_pattern = r'^cbg=\(([^()]+)\)$'
                background_color_pattern_match = re.match(background_color_pattern, syntax)
                size_pattern = r'^sze=\(([^()]+)\)$'
                size_pattern_match = re.match(size_pattern, syntax)
                if foreground_color_pattern_match:
                    raw_foreground_color = foreground_color_pattern_match.group(1)
                    foreground_color = Color(raw_foreground_color).convert_format(Constants.RGBA)
                if background_color_pattern_match:
                    raw_background_color = background_color_pattern_match.group(1)
                    background_color = Color(raw_background_color).convert_format(Constants.RGBA)
                if size_pattern_match:
                    raw_size = size_pattern_match.group(1)
                    size = int(raw_size)
                if "und" in syntax:
                    underline = not underline
                if "bld" in syntax:
                    bold = not bold
                if "itl" in syntax:
                    italic = not italic
                if "clr" in syntax:
                    foreground_color = defaults["foreground_color"]
                    background_color = defaults["background_color"]
                    bold = defaults["bold"]
                    italic = defaults["italic"]
                    underline = defaults["underline"]
                    size = defaults["size"]

            else:
                print(word)