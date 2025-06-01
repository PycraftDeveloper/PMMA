from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

Integer1D = Union[
    npt.NDArray[np.int_],
    Iterable[int],
]

class Display:
    def create(self, Size: Integer1D, Caption: str) -> str: ...

    def get_width(self) -> int: ...
    def get_height(self) -> int: ...