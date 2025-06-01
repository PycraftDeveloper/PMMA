from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

Integer1D = Union[
    npt.NDArray[np.int_],
    Iterable[int],
]

def create(Size: Integer1D, Caption: str) -> str: ...

def get_width() -> int: ...
def get_height() -> int: ...