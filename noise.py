from pmma.registry import Registry
from pmma.constants import Constants

from . import noise_utils

class Perlin(Registry):
    def generate_2D_perlin_noise(self, x, y, seed):
        if Registry.compile_math_functions:
            return noise_utils.generate_2D_perlin_noise(x, y, seed)
        else:
            return noise_utils.generate_2D_perlin_noise.py_func(x, y, seed)

    def generate_seed(self, number):
        return noise_utils.get_seed(number)