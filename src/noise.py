import random

from pmma.src.registry import Registry
from pmma.src.constants import Constants

from pmma.src.utility.noise_utils import *
from pmma.src.utility.math_utils import *

from pmma.src.advmath import Math

class Perlin():
    def __init__(self, seed=None):
        if seed is None:
            seed = random.randint(0, 1000000)
        self.math = Math()
        self.seed_value = seed
        self.seed = raw_get_seed(seed)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        if Registry.compile_math_functions and ("generate_2D_perlin_noise" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["generate_2D_perlin_noise"]):
            noise = raw_generate_2D_perlin_noise(raw_extrapolate2, x, y, self.seed)
        else:
            noise = raw_generate_2D_perlin_noise.py_func(self.math.get_function_extrapolate2(), x, y, self.seed)
        return raw_ranger(noise, [-1, 1], range)

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = raw_generate_1D_perlin_noise(
            x,
            self.math.get_function_fade(),
            self.math.get_function_hash(),
            self.math.get_function_grad(),
            self.math.get_function_lerp())

        return raw_ranger(noise, [-1, 1], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed

    def get_seed_value(self):
        return self.seed_value