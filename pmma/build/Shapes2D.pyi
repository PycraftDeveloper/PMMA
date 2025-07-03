from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

Numerical1D = Union[
    npt.NDArray[np.float_],
    npt.NDArray[np.int_],
    Iterable[float],
    Iterable[int],
]

Numerical = Union[
    Iterable[float],
    Iterable[int],
]

class RadialPolygon:
    def __init__(self) -> None: ...

    def render(self) -> None: ...

    def set_centre(self, position: Numerical1D) -> None: ...
    def set_color(self, color: Numerical1D) -> None: ...
    def set_radius(self, radius: int) -> None: ...
    def set_point_count(self, point_count: int) -> None: ...
    def set_width(self, width: int) -> None: ...
    def set_rotation(self, rotation: Numerical) -> None: ...