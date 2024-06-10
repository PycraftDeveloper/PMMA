import random

from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

from pmma.py_src.utility.math_utils import *

from pmma.bin.perlin_noise import PerlinNoise

class Perlin():
    def __init__(self, seed=None, octaves=1, persistence=0.5):
        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed
        self.noise = PerlinNoise(self.seed, octaves, persistence)

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = self.noise.fBM1D(x)

        return noise#raw_ranger(noise, [-0.5008445989004566, 0.9999999987945568], range)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = self.noise.fBM2D(x, y)

        return noise#raw_ranger(noise, [0.4871120631082581, 1.0561227977881837], range)

    def generate_3D_perlin_noise(self, x, y, z, range=[-1, 1]):
        noise = self.noise.fBM3D(x, y, z)

        return noise#raw_ranger(noise, [0.4871120631082581, 1.0561227977881837], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed