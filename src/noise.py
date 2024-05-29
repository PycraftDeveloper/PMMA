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
        self.seed = seed

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = raw_generate_2D_perlin_noise(
            x,
            y,
            self.math.get_function_fade(),
            self.math.get_function_hash2(),
            self.math.get_function_grad2(),
            self.math.get_function_lerp())
        return raw_ranger(noise, [-1, 1], range)

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = raw_generate_1D_perlin_noise(
            x,
            self.math.get_function_fade(),
            self.math.get_function_hash(),
            self.math.get_function_grad(),
            self.math.get_function_lerp())

        return raw_ranger(noise, [-2, 2], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed