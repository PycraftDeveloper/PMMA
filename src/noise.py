import random

from pmma.src.registry import Registry
from pmma.src.constants import Constants

from pmma.src.utility.noise_utils import *
from pmma.src.utility.math_utils import *

from pmma.src.advmath import Math

class Perlin():
    def __init__(self, seed=None):
        self.permutation = np.arange(256, dtype=int)
        if seed is None:
            seed = random.randint(0, 1000000)
        np.random.seed(seed)
        self.math = Math()
        self.seed = seed
        np.random.shuffle(self.permutation)
        self.permutation = np.stack([self.permutation, self.permutation]).flatten()

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = raw_generate_1D_perlin_noise(
            x,
            self.permutation,
            self.math.get_function_fade(),
            self.math.get_function_grad(),
            self.math.get_function_lerp())

        return raw_ranger(noise, [-0.5008445989004566, 0.9999999987945568], range)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = raw_generate_2D_perlin_noise(
            x,
            y,
            self.permutation,
            self.math.get_function_fade(),
            self.math.get_function_grad2(),
            self.math.get_function_lerp())

        return raw_ranger(noise, [0.4871120631082581, 1.0561227977881837], range)

    def generate_seedless_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = raw_generate_seedless_1D_perlin_noise(
            x,
            self.math.get_function_fade(),
            self.math.get_function_hash(),
            self.math.get_function_fast_grad(),
            self.math.get_function_lerp())

        return raw_ranger(noise, [0, 2], range)

    def generate_seedless_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = raw_generate_seedless_2D_perlin_noise(
            x,
            y,
            self.math.get_function_fade(),
            self.math.get_function_hash2(),
            self.math.get_function_fast_grad2(),
            self.math.get_function_lerp())
        return raw_ranger(noise, [-0.5011956148034188, 0.5011956153536878], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed