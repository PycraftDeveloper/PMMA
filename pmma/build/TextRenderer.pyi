from typing import Union

from pmma.build.CoreTypes import Color, DisplayCoordinate

Numerical = Union[float, int]

class TextRenderer:
    position: DisplayCoordinate
    foreground_color: Color
    background_color: Color

    def set_use_in_line_formatting(self, use_in_line_formatting: bool) -> None: ...
    def get_use_in_line_formatting(self) -> bool: ...

    def set_text(self, text: str) -> None: ...
    def set_font(self, font: str) -> None: ...

    def set_size(self, size: Numerical) -> None: ...

    def render(self) -> None: ...