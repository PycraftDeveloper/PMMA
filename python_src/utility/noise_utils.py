import numpy

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

def prefill_optimizer(x):
    x_array = numpy.linspace(0, x, x)
    x_out_array = x_array
    y_array = numpy.linspace(0, x, x)
    z_array = numpy.linspace(0, x, x)

    _x, _y = numpy.meshgrid(x_array, y_array)
    y_out_array = numpy.stack((_x, _y), axis=-1)

    _x, _y, _z = numpy.meshgrid(x_array, y_array, z_array)
    z_out_array = numpy.stack((_x, _y, _z), axis=-1)

    return x_out_array, y_out_array, z_out_array

class NoiseIntermediary:
    prefill = False
    noise_ranges = {
        "generate_1D_perlin_noise": {"min": 2, "max": -2},
        "generate_2D_perlin_noise": {"min": 2, "max": -2},
        "generate_3D_perlin_noise": {"min": 2, "max": -2},
        "generate_1D_perlin_noise_from_array": {"min": 2, "max": -2},
        "generate_2D_perlin_noise_from_array": {"min": 2, "max": -2},
        "generate_3D_perlin_noise_from_array": {"min": 2, "max": -2},
        "generate_1D_perlin_noise_from_range": {"min": 2, "max": -2},
        "generate_2D_perlin_noise_from_range": {"min": 2, "max": -2},
        "generate_3D_perlin_noise_from_range": {"min": 2, "max": -2},
    }