from typing import Union, Iterable

import numpy as np
import numpy.typing as npt

from pmma.build.NumberFormats import Color

Numerical1D = Union[
    npt.NDArray[np.float32], # preferred
    npt.NDArray[np.float16],
    npt.NDArray[np.float64],
    npt.NDArray[np.int32], # preferred
    npt.NDArray[np.int8],
    npt.NDArray[np.int16],
    npt.NDArray[np.int64],
    Iterable[float],  # preferred
    Iterable[int],  # preferred
]

Numerical = Union[float, int]

class TextRenderer:
    foreground_color: Color
    background_color: Color

    def set_text(self, text: str) -> None: ...
    def set_font(self, font: str) -> None: ...

    def set_size(self, size: Numerical) -> None: ...

    def set_position(self, position: Numerical1D) -> None: ...

    def render(self) -> None: ...