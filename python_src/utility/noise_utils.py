import numpy as _numpy

def prefill_optimizer(x):
    x_array = _numpy.linspace(0, x, x)
    x_out_array = x_array
    y_array = _numpy.linspace(0, x, x)
    z_array = _numpy.linspace(0, x, x)

    _x, _y = _numpy.meshgrid(x_array, y_array)
    y_out_array = _numpy.stack((_x, _y), axis=-1)

    _x, _y, _z = _numpy.meshgrid(x_array, y_array, z_array)
    z_out_array = _numpy.stack((_x, _y, _z), axis=-1)

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