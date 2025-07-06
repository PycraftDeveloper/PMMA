from typing import Union, Iterable

import numpy as np
import numpy.typing as npt

Numerical1D = Union[
    npt.NDArray[np.float_],
    npt.NDArray[np.int_],
    Iterable[float],
    Iterable[int],
]

Numerical = Union[float, int]

class TextRenderer:
    def set_text(self, text: str) -> None: ...
    def set_font(self, font: str) -> None: ...

    def set_size(self, size: Numerical) -> None: ...

    def set_foreground_color(self, color: Numerical1D) -> None: ...
    def set_background_color(self, color: Numerical1D) -> None: ...

    def set_position(self, position: Numerical1D) -> None: ...

    def render(self) -> None: ...