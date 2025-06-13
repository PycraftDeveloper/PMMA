from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

Numerical1D = Union[
    npt.NDArray[np.float_],
    npt.NDArray[np.int_],
    Iterable[float],
    Iterable[int],
]

class TextEvent:
    def __init__(self) -> None: ...

    def get_text(self) -> str: ...

    def get_enabled(self) -> bool: ...

    def set_enabled(self, value: bool) -> None: ...

    def clear_text(self) -> None: ...

class MouseEvent:
    def __init__(self) -> None: ...

    def get_position(self, using_numpy: bool=True) -> Numerical1D: ...

    def get_delta(self, using_numpy: bool=True) -> Numerical1D: ...

    def get_delta_toggle(self, using_numpy: bool=True) -> Numerical1D: ...