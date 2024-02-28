from pmma.src.registry import Registry

from pmma.src.utility.noise_utils import *
from pmma.src.utility.math_utils import *

class Perlin(Registry):
    def __init__(self, seed):
        self.seed_value = seed
        self.seed = get_seed(seed)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        if Registry.compile_math_functions:
            noise = generate_2D_perlin_noise(extrapolate2,x, y, self.seed)
        else:
            noise = generate_2D_perlin_noise.py_func(extrapolate2.py_func, x, y, self.seed)
        return ranger(noise, [-1, 1], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed

    def get_seed_value(self):
        return self.seed_value