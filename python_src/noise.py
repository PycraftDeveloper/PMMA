import random
import importlib

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.math_utils import *

class ExtendedPerlin():
    def __init__(self, seed=None, octaves=1, persistence=0.5):
        if Registry.cython_acceleration_available:
            self.extended_noise_module = __import__("pmma.bin.extended_perlin_noise")
        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed
        self.noise = self.extended_noise_module.PerlinNoise(self.seed, octaves, persistence)

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = self.noise.generate_fbm_1d(x)

        return noise # for now

    def generate_2D_perlin_noise(self, x, range=[-1, 1]):
        noise = self.noise.generate_fbm_2d(x)

        return noise # for now

    def generate_3D_perlin_noise(self, x, range=[-1, 1]):
        noise = self.noise.generate_fbm_2d(x)

        return noise # for now

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed

class Perlin():
    def __init__(self, seed=None, octaves=1, persistence=0.5):
        if Registry.cython_acceleration_available:
            self.noise_module = importlib.import_module("pmma.bin.perlin_noise")
        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed
        self.noise = self.noise_module.PerlinNoise(self.seed, octaves, persistence)

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = self.noise.fBM1D(x)

        return raw_ranger(noise, [-1.166227320654655, 0.30489170105612395], range)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = self.noise.fBM2D(x, y)

        return raw_ranger(noise, [-0.5254378425377668, 0.3887421630840867], range)

    def generate_3D_perlin_noise(self, x, y, z, range=[-1, 1]):
        noise = self.noise.fBM3D(x, y, z)

        return raw_ranger(noise, [-0.511635154235906, 0.6931716092231993], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed