from tkinter import font as _font
import re as _re
import time as _time
from gc import collect as _gc__collect

import pygame as _pygame

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.file import File as _File
from pmma.python_src.memory_manager import MemoryManager as _MemoryManager

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.general_utils import create_cache_id as _create_cache_id
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class _Text:
    def __init__(self, canvas=None):
        _initialize(self)

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
            _pygame.init()

        if not _Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DISPLAY_OBJECT)
            from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
            _DisplayIntermediary()

        self._display_intermediary = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

        self._canvas = canvas

        self._memory_manager_instance = _MemoryManager()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def _quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def _get_system_font(self, size=None, bold=None, italic=None):
        system_font = _font.nametofont("TkTextFont")
        system_font_dictionary = system_font.actual()

        name = system_font_dictionary["family"]
        if size is None:
            size = system_font_dictionary["size"]

        if bold is None:
            bold = system_font_dictionary["weight"] == "bold"

        if italic is None:
            italic = system_font_dictionary["slant"] == "italic"

        return _pygame.font.SysFont(name, size), [name, size]

    def _render_text_with_transparent_background(self, in_text, bg_color):
        # Create a new surface with an alpha channel (same size as in_text)
        width, height = in_text.get_size()
        alpha_surface = _pygame.Surface(
            (width, height),
            _pygame.SRCALPHA)

        # Fill this surface with the background color and set alpha transparency
        alpha_surface.fill(bg_color)

        # Blit the in_text onto the alpha_surface, keeping the text opaque
        alpha_surface.blit(in_text, (0, 0))

        return alpha_surface

    def _render(
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
            word_separator=None):

        if word_separator is None:
            word_separator = r"(\s+)"
        if "\n" in text:
            text = text.replace("\n", "${nln}")

        canvas_identifiable_data = "param_based_canvas"

        if self._canvas is None and canvas is None:
            canvas = self._display_intermediary
            canvas_identifiable_data = _Constants.DISPLAY_OBJECT
        if canvas is None:
            canvas = self._canvas
            canvas_identifiable_data = "class_based_canvas"

        if font is None:
            font, font_identifiable_data = self.get_system_font(size, bold, italic)
        else:
            font_identifiable_data = [font, size]
            file_object = _File(font)
            font_argument_is_path = file_object.exists()
            if font_argument_is_path:
                font = _pygame.font.Font(font, size)
            else:
                font = _pygame.font.SysFont(font, size)

        if position is None:
            position = (0, 0)

        x, y = position

        if position[0] == _Constants.CENTER:
            x = canvas.get_width() / 2
        elif position[0] == _Constants.RIGHT:
            x = canvas.get_width()
        elif position[0] == _Constants.LEFT:
            x = 0

        if position[1] == _Constants.CENTER:
            y = canvas.get_height() / 2
        elif position[1] == _Constants.BOTTOM:
            y = canvas.get_height()
        elif position[1] == _Constants.TOP:
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

        identifier = _create_cache_id(
            font_identifiable_data,
            canvas_identifiable_data,
            text,
            position,
            foreground_color,
            background_color,
            bold,
            italic,
            underline,
            strikethrough,
            word_separator,
            canvas.get_size())

        result = self._memory_manager_instance.get(identifier)
        if result is None:
            start = _time.perf_counter()
            x, y = 0, 0
            surface = _pygame.Surface(
                canvas.get_size(),
                _pygame.SRCALPHA)

            pattern = "(\$\{[a-zA-Z =\()\0-9]+})|"+word_separator

            split_text = [token for token in _re.split(pattern, text) if token and not token.isspace()]

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
                        foreground_color_pattern_match = _re.match(
                            foreground_color_pattern,
                            syntax)

                        background_color_pattern = r'^cbg=\(([^()]+)\)$'
                        background_color_pattern_match = _re.match(
                            background_color_pattern,
                            syntax)

                        size_pattern = r'^sze=\(([^()]+)\)$'
                        size_pattern_match = _re.match(size_pattern, syntax)
                        if foreground_color_pattern_match:
                            raw_foreground_color = foreground_color_pattern_match.group(1)
                            foreground_color = _ColorConverter(raw_foreground_color).convert_format(
                                _Constants.RGBA)

                        elif background_color_pattern_match:
                            raw_background_color = background_color_pattern_match.group(1)
                            background_color = _ColorConverter(raw_background_color).convert_format(
                                _Constants.RGBA)

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
                                _Registry.do_anti_aliasing,
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
                        elif syntax in _Constants.TEXT_BASED_COLORS.keys():
                            foreground_color = _Constants.TEXT_BASED_COLORS[syntax]

                        elif (syntax.upper() in _Constants.TEXT_BASED_COLORS.keys() and
                                syntax != syntax.upper()):

                            background_color = _Constants.TEXT_BASED_COLORS[syntax.upper()]

                else:
                    rendered_word = font.render(
                        word+" ",
                        _Registry.do_anti_aliasing,
                        foreground_color)

                    if rendered_word.get_width() > surface.get_width():
                        word = word+" "
                        for letter in word:
                            rendered_word = font.render(
                                letter,
                                _Registry.do_anti_aliasing,
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
            end = _time.perf_counter()
            object_creation_time = end-start
            self._memory_manager_instance.add(
                surface,
                custom_id=identifier,
                object_creation_time=object_creation_time,
                recreatable_object=True)

        else:
            canvas.blit(result, defaults["position"])