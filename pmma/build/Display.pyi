from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

Integer1D = Union[
    npt.NDArray[np.int_],
    Iterable[int],
]

class Display:
    def create(self, size: Integer1D=..., caption: str="PMMA Display", fullscreen: bool=True, resizable: bool=False, no_frame: bool=False, vsync: bool = True, icon: str="", centered: bool=True, maximized: bool=False) -> None: ...

    def get_width(self) -> int: ...
    def get_height(self) -> int: ...

    def get_size(self) -> Integer1D: ...