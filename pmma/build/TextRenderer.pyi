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
    def __cinit__(self, font_path: str, font_height: Numerical) -> None: ...

    def begin(self) -> None: ...

    def end(self) -> None: ...

    def drawText(self, text: str, pos: Numerical1D, scale: Numerical, color: Numerical1D) -> None: ...