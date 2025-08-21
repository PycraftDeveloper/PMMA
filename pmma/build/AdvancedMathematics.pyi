from typing import Iterable, Union

import numpy as np
import numpy.typing as npt

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

Float1D = Union[npt.NDArray[np.float32], Iterable[float]]

Numerical = Union[float, int]

class AdvancedMathematics:
    @staticmethod
    def lerp(x1: float, x2: float, duration: float, current_duration: float) -> float: ...

    @staticmethod
    def individual_pythagorean_difference(x1: Numerical, y1: Numerical, x2: Numerical, y2: Numerical) -> float: ...

    @staticmethod
    def point_pythagorean_difference(point1: Numerical1D, point2: Numerical1D) -> float: ...

    @staticmethod
    def individual_pythagorean_distance(x: Numerical, y: Numerical) -> float: ...

    @staticmethod
    def point_pythagorean_distance(point: Numerical1D) -> float: ...

    @staticmethod
    def smooth_step(value: Numerical) -> float: ...

    @staticmethod
    def ranger(value: Numerical, old_range: Numerical1D, new_range: Numerical1D) -> float: ...

    @staticmethod
    def array_ranger(values: Numerical1D, old_range: Numerical1D, new_range: Numerical1D) -> Numerical1D: ...

    @staticmethod
    def array_normalize(values: Numerical) -> Numerical1D: ...

    @staticmethod
    def cross(first_values: Numerical1D, second_values: Numerical1D) -> Numerical1D: ...

    @staticmethod
    def subtract(first_values: Numerical1D, second_values: Numerical1D) -> Numerical1D: ...

    @staticmethod
    def dot(first_values: Numerical1D, second_values: Numerical1D) -> float: ...

    @staticmethod
    def look_at(eye: Numerical1D, target: Numerical1D, up: Numerical1D) -> Numerical1D: ...

    @staticmethod
    def compute_position(position: Numerical1D, target: Numerical1D, up: Numerical1D) -> Numerical1D: ...

    @staticmethod
    def perspective_fov(FOV: Numerical, aspect_ratio: Numerical, near_plane: Numerical, far_plane: Numerical) -> Numerical1D: ...