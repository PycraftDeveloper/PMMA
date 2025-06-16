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
    def __init__(self, seed: NoneInt=None, octaves: int=2, lacunarity: float=0.75, gain: float=1.0) -> None: ...

    def get_seed(self) -> int: ...
    def get_octaves(self) -> int: ...
    def get_lacunarity(self) -> float: ...
    def get_gain(self) -> float: ...

    def noise_1d(self, x: Numerical) -> float: ...
    def noise_2d(self, x: Numerical, y: Numerical) -> float: ...
    def noise_3d(self, x: Numerical, y: Numerical, z: Numerical) -> float: ...

    def array_noise_1d(self, values: Numerical1D) -> Numerical1D: ...
    def array_noise_2d(self, values: Numerical2D) -> Numerical2D: ...
    def array_noise_3d(self, values: Numerical3D) -> Numerical3D: ...

    def range_noise_1d(self, x_range: Numerical1D, length: Numerical) -> Numerical1D: ...
    def range_noise_2d(self, x_range: Numerical1D, y_range: Numerical1D, length: Numerical) -> Numerical1D: ...
    def range_noise_3d(self, x_range: Numerical1D, y_range: Numerical1D, z_range: Numerical1D, length: Numerical) -> Numerical1D: ...