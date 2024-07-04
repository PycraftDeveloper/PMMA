from tkinter import font
import re
import random

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.color import Color
from pmma.python_src.file import File

class Text:
    def __init__(self, canvas=None):
        self.canvas = canvas

    def get_system_font(self, size=None, bold=None, italic=None):
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
            return Registry.graphics_backend.font.SysFont(name, size)

    def render(
            self,
            text,
            position=None,
            font=None,
            size=11,
            foreground_color=(255, 255, 255),
            background_color=None,
            bold=False,
            italic=False,
            underline=False,
            strikethrough=False,
            canvas=None,
            word_separator = r"(\s+)"):

        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        if font is None:
            font = self.get_system_font(size, bold, italic)
        else:
            file_object = File(font)
            font_argument_is_path = file_object.exists()
            if font_argument_is_path:
                font = Registry.graphics_backend.font.Font(font, size)
            else:
                font = Registry.graphics_backend.font.SysFont(font, size)

        if position is None:
            position = (0, 0)

        x, y = position

        if position[0] == Constants.CENTER:
            x = canvas.get_width() / 2
        elif position[0] == Constants.RIGHT:
            x = canvas.get_width()
        elif position[0] == Constants.LEFT:
            x = 0

        if position[1] == Constants.CENTER:
            y = canvas.get_height() / 2
        elif position[1] == Constants.BOTTOM:
            y = canvas.get_height()
        elif position[1] == Constants.TOP:
            y = 0

        defaults = {
            "foreground_color": foreground_color,
            "background_color": background_color,
            "bold": bold,
            "italic": italic,
            "underline": underline,
            "size": size,
            "position": (x, y)
        }

        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self.canvas

        pattern = "(\$\{[a-zA-Z =\()\0-9]+})|"+word_separator

        split_text = [token for token in re.split(pattern, text) if token and not token.isspace()]

        for word in split_text:
            font.bold = bold
            font.italic = italic
            font.underline = underline
            font.strikethrough = strikethrough

            if word.startswith("${") and word.endswith("}"):
                content = word[2:-1]
                split_content = content.split(" ")
                for syntax in split_content:
                    foreground_color_pattern = r'^cfg=\(([^()]+)\)$'
                    foreground_color_pattern_match = re.match(foreground_color_pattern, syntax)
                    background_color_pattern = r'^cbg=\(([^()]+)\)$'
                    background_color_pattern_match = re.match(background_color_pattern, syntax)
                    size_pattern = r'^sze=\(([^()]+)\)$'
                    size_pattern_match = re.match(size_pattern, syntax)
                    if foreground_color_pattern_match:
                        raw_foreground_color = foreground_color_pattern_match.group(1)
                        foreground_color = Color(raw_foreground_color).convert_format(Constants.RGBA)
                    elif background_color_pattern_match:
                        raw_background_color = background_color_pattern_match.group(1)
                        background_color = Color(raw_background_color).convert_format(Constants.RGBA)
                    elif size_pattern_match:
                        raw_size = size_pattern_match.group(1)
                        size = int(raw_size)
                    elif syntax == "und":
                        underline = not underline
                    elif syntax == "bld":
                        bold = not bold
                    elif syntax == "itl":
                        italic = not italic
                    elif syntax == "str":
                        strikethrough = not strikethrough
                    elif syntax == "nln":
                        temporary_text = font.render(" ", Registry.do_anti_aliasing, foreground_color, background_color)
                        y += temporary_text.get_height()
                        x = defaults["position"][0]
                    elif syntax == "clr":
                        foreground_color = defaults["foreground_color"]
                        background_color = defaults["background_color"]
                        bold = defaults["bold"]
                        italic = defaults["italic"]
                        underline = defaults["underline"]
                        size = defaults["size"]
                    elif syntax in Constants.TEXT_BASED_COLORS.keys():
                        foreground_color = Constants.TEXT_BASED_COLORS[syntax]
                    elif syntax.upper() in Constants.TEXT_BASED_COLORS.keys() and syntax != syntax.upper():
                        background_color = Constants.TEXT_BASED_COLORS[syntax.upper()]

            else:
                rendered_word = font.render(word+" ", Registry.do_anti_aliasing, foreground_color, background_color)
                if rendered_word.get_width() > canvas.get_width():
                    word = word+" "
                    for letter in word:
                        rendered_word = font.render(letter, Registry.do_anti_aliasing, foreground_color, background_color)

                        if rendered_word.get_width() + x > canvas.get_width():
                            x = defaults["position"][0]
                            y += rendered_word.get_height()
                        canvas.blit(rendered_word, (x, y))
                        x += rendered_word.get_width()

                if rendered_word.get_width() + x > canvas.get_width():
                    x = defaults["position"][0]
                    y += rendered_word.get_height()
                canvas.blit(rendered_word, (x, y))
                x += rendered_word.get_width()