import random

from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

from pmma.py_src.utility.math_utils import *

class Perlin():
    def __init__(self, seed=None):
        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = None

        return raw_ranger(noise, [-0.5008445989004566, 0.9999999987945568], range)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = None

        return raw_ranger(noise, [0.4871120631082581, 1.0561227977881837], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed