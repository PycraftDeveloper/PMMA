from typing import Union, Iterable

import numpy as np
import numpy.typing as npt

Numerical = Union[float, int]
NoneInt = Union[None, int]

Numerical1D = Union[
    npt.NDArray[np.float_],
    npt.NDArray[np.int_],
    Iterable[float],
    Iterable[int],
]

Numerical2D = Union[
    npt.NDArray[np.float_],
    npt.NDArray[np.int_],
    Iterable[Iterable[float]],
    Iterable[Iterable[int]],
]

Numerical3D = Union[
    npt.NDArray[np.float_],
    npt.NDArray[np.int_],
    Iterable[Iterable[float]],
    Iterable[Iterable[int]],
]

class FractalBrownianMotion:
    def __init__(self, octaves: int, lacunarity: float, gain: float, seed: NoneInt = None, ) -> None: ...

    def get_seed(self) -> int: ...
    def get_octaves(self) -> int: ...
    def get_lacunarity(self) -> float: ...
    def get_gain(self) -> float: ...

    def noise1D(self, x: Numerical) -> float: ...
    def noise2D(self, x: Numerical, y: Numerical) -> float: ...
    def noise3D(self, x: Numerical, y: Numerical, z: Numerical) -> float: ...

    def array_noise1D(self, values: Numerical1D) -> Numerical1D: ...
    def array_noise2D(self, values: Numerical2D) -> Numerical2D: ...
    def array_noise3D(self, values: Numerical3D) -> Numerical3D: ...

    def range_noise1D(self, x_range: Numerical1D, length: Numerical) -> Numerical1D: ...
    def range_noise2D(self, x_range: Numerical1D, y_range: Numerical1D, length: Numerical) -> Numerical1D: ...
    def range_noise3D(self, x_range: Numerical1D, y_range: Numerical1D, z_range: Numerical1D, length: Numerical) -> Numerical1D: ...