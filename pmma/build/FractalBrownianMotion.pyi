from typing import Union, Iterable

import numpy as np
import numpy.typing as npt

Numerical = Union[float, int]
NoneInt = Union[None, int]

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

Numerical2D = Union[
    npt.NDArray[np.float32], # preferred
    npt.NDArray[np.float16],
    npt.NDArray[np.float64],
    npt.NDArray[np.int32], # preferred
    npt.NDArray[np.int8],
    npt.NDArray[np.int16],
    npt.NDArray[np.int64],
    Iterable[Iterable[float]],  # preferred
    Iterable[Iterable[int]],  # preferred
]

Numerical3D = Union[
    npt.NDArray[np.float32], # preferred
    npt.NDArray[np.float16],
    npt.NDArray[np.float64],
    npt.NDArray[np.int32], # preferred
    npt.NDArray[np.int8],
    npt.NDArray[np.int16],
    npt.NDArray[np.int64],
    Iterable[Iterable[Iterable[float]]],  # preferred
    Iterable[Iterable[Iterable[int]]],  # preferred
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