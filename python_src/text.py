from tkinter import font
import re
import time

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.color import Color
from pmma.python_src.file import File

class Text:
    def __init__(self, canvas=None):
        self.canvas = canvas

        self.memory_manager_instance = Registry.pmma_module_spine[Constants.MEMORYMANAGER_OBJECT]

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

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
            return Registry.graphics_backend.font.SysFont(name, size), [name, size]

    def render_text_with_transparent_background(self, in_text, bg_color):
        # Create a new surface with an alpha channel (same size as in_text)
        width, height = in_text.get_size()
        alpha_surface = Registry.graphics_backend.Surface(
            (width, height),
            Registry.graphics_backend.SRCALPHA)

        # Fill this surface with the background color and set alpha transparency
        alpha_surface.fill(bg_color)

        # Blit the in_text onto the alpha_surface, keeping the text opaque
        alpha_surface.blit(in_text, (0, 0))

        return alpha_surface

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

        if "\n" in text:
            text = text.replace("\n", "${nln}")

        canvas_identifiable_data = "param_based_canvas"

        if self.canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
            canvas_identifiable_data = Constants.DISPLAY_OBJECT
        if canvas is None:
            canvas = self.canvas
            canvas_identifiable_data = "class_based_canvas"

        if font is None:
            font, font_identifiable_data = self.get_system_font(size, bold, italic)
        else:
            font_identifiable_data = [font, size]
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

        identifier = (
            str(font_identifiable_data)+\
            str(canvas_identifiable_data)+\
            str(text)+\
            str(position)+\
            str(foreground_color)+\
            str(background_color)+\
            str(bold)+\
            str(italic)+\
            str(underline)+\
            str(strikethrough)+\
            str(word_separator)+\
            str(canvas.get_size))

        result = self.memory_manager_instance.get_object(identifier)
        if result is None:
            start = time.perf_counter()
            x, y = 0, 0
            surface = Registry.graphics_backend.Surface(
                (canvas.get_width(), canvas.get_height()),
                Registry.graphics_backend.SRCALPHA)

            pattern = "(\$\{[a-zA-Z =\()\0-9]+})|"+word_separator

            split_text = [token for token in re.split(pattern, text) if token and not token.isspace()]

            for word in split_text:
                if y > surface.get_height():
                    break
                font.bold = bold
                font.italic = italic
                font.underline = underline
                font.strikethrough = strikethrough

                if word.startswith("${") and word.endswith("}"):
                    content = word[2:-1]
                    split_content = content.split(" ")
                    for syntax in split_content:
                        foreground_color_pattern = r'^cfg=\(([^()]+)\)$'
                        foreground_color_pattern_match = re.match(
                            foreground_color_pattern,
                            syntax)

                        background_color_pattern = r'^cbg=\(([^()]+)\)$'
                        background_color_pattern_match = re.match(
                            background_color_pattern,
                            syntax)

                        size_pattern = r'^sze=\(([^()]+)\)$'
                        size_pattern_match = re.match(size_pattern, syntax)
                        if foreground_color_pattern_match:
                            raw_foreground_color = foreground_color_pattern_match.group(1)
                            foreground_color = Color(raw_foreground_color).convert_format(
                                Constants.RGBA)

                        elif background_color_pattern_match:
                            raw_background_color = background_color_pattern_match.group(1)
                            background_color = Color(raw_background_color).convert_format(
                                Constants.RGBA)

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
                            temporary_text = font.render(
                                " ",
                                Registry.do_anti_aliasing,
                                foreground_color,
                                background_color)

                            y += temporary_text.get_height()
                            x = 0
                        elif syntax == "clr":
                            foreground_color = defaults["foreground_color"]
                            background_color = defaults["background_color"]
                            bold = defaults["bold"]
                            italic = defaults["italic"]
                            underline = defaults["underline"]
                            size = defaults["size"]
                        elif syntax in Constants.TEXT_BASED_COLORS.keys():
                            foreground_color = Constants.TEXT_BASED_COLORS[syntax]

                        elif (syntax.upper() in Constants.TEXT_BASED_COLORS.keys() and
                                syntax != syntax.upper()):

                            background_color = Constants.TEXT_BASED_COLORS[syntax.upper()]

                else:
                    rendered_word = font.render(
                        word+" ",
                        Registry.do_anti_aliasing,
                        foreground_color)

                    if rendered_word.get_width() > surface.get_width():
                        word = word+" "
                        for letter in word:
                            rendered_word = font.render(
                                letter,
                                Registry.do_anti_aliasing,
                                foreground_color)

                            if rendered_word.get_width() + x > surface.get_width():
                                x = 0
                                y += rendered_word.get_height()
                            if (x < surface.get_width() and
                                    y < surface.get_height() and
                                    x + defaults["position"][0] + surface.get_width() > 0 and
                                    y + defaults["position"][1] + surface.get_height() > 0):

                                alpha = False
                                if len(foreground_color) == 4 and foreground_color[3] > 0:
                                    rendered_word.set_alpha(foreground_color[3])
                                    alpha = True
                                if (background_color is None or
                                        (len(background_color) == 4 and background_color[3] > 0)):

                                    if background_color is not None and len(background_color) == 4:
                                        rendered_word = self.render_text_with_transparent_background(
                                            rendered_word,
                                            background_color)

                                    alpha = True

                                if alpha is False:
                                    rendered_word.convert()
                                else:
                                    rendered_word.convert_alpha()

                                surface.blit(rendered_word, (x, y))
                            x += rendered_word.get_width()

                    if rendered_word.get_width() + x > surface.get_width():
                        x = 0
                        y += rendered_word.get_height()
                    if x < surface.get_width() and y < surface.get_height():
                        alpha = False
                        if len(foreground_color) == 4 and foreground_color[3] > 0:
                            rendered_word.set_alpha(foreground_color[3])
                            alpha = True
                        if background_color is None or (len(background_color) == 4 and background_color[3] > 0):
                            if background_color is not None and len(background_color) == 4:
                                rendered_word = self.render_text_with_transparent_background(
                                    rendered_word,
                                    background_color)

                            alpha = True

                        if alpha is False:
                            rendered_word.convert()
                        else:
                            rendered_word.convert_alpha()

                        surface.blit(rendered_word, (x, y))
                    x += rendered_word.get_width()
            canvas.blit(surface, defaults["position"])
            end = time.perf_counter()
            object_creation_time = end-start
            self.memory_manager_instance.add_object(
                surface,
                custom_id=identifier,
                object_creation_time=object_creation_time,
                recreatable_object=True)

        else:
            canvas.blit(result, defaults["position"])