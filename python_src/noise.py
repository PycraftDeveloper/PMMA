import random
import importlib

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.math_utils import *

class ExtendedPerlin():
    def __init__(self, seed=None, octaves=1, persistence=0.5):
        if Registry.cython_acceleration_available:
            self.extended_noise_module = importlib.import_module("pmma.bin.extended_perlin_noise")

        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed
        self.extended_noise = self.extended_noise_module.ExtendedPerlinNoise(self.seed, octaves, persistence)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed

class Perlin():
    def __init__(self, seed=None, octaves=1, persistence=0.5):
        if Registry.cython_acceleration_available:
            self.noise_module = importlib.import_module("pmma.bin.perlin_noise")
            self.extended_noise_module = importlib.import_module("pmma.bin.extended_perlin_noise")

        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed

        self.noise = self.noise_module.PerlinNoise(self.seed, octaves, persistence)
        self.extended_noise = self.extended_noise_module.ExtendedPerlinNoise(self.seed, octaves, persistence)

    def generate_1D_perlin_noise(self, x, range=[-1, 1]):
        noise = self.noise.fBM1D(x)

        return raw_ranger(noise, [-1.166227320654655, 0.30489170105612395], range)

    def generate_2D_perlin_noise(self, x, y, range=[-1, 1]):
        noise = self.noise.fBM2D(x, y)

        return raw_ranger(noise, [-0.5254378425377668, 0.3887421630840867], range)

    def generate_3D_perlin_noise(self, x, y, z, range=[-1, 1]):
        noise = self.noise.fBM3D(x, y, z)

        return raw_ranger(noise, [-0.511635154235906, 0.6931716092231993], range)


    def generate_1D_perlin_noise_from_array(self, array, range=[-1, 1]):
        noise = self.extended_noise.generate_fbm_1d(array)

        return raw_nparray_ranger(noise, [-0.5, 0.5], range)

    def generate_2D_perlin_noise_from_array(self, array, range=[-1, 1]):
        noise = self.extended_noise.generate_fbm_2d(array)

        return raw_nparray_ranger(noise, [-1, 1], range)

    def generate_3D_perlin_noise_from_array(self, array, range=[-1, 1]):
        noise = self.extended_noise.generate_fbm_3d(array)

        return raw_nparray_ranger(noise, [-1, 1], range)


    def generate_1D_perlin_noise_from_range(self, one_range, range=[-1, 1]):
        if len(one_range) == 1:
            array = numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            array = numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            array = numpy.linspace(one_range[0], one_range[1], one_range[2])

        noise = self.extended_noise.generate_fbm_1d(array)

        return raw_nparray_ranger(noise, [-0.5, 0.5], range)

    def generate_2D_perlin_noise_from_range(self, one_range, two_range, range=[-1, 1]):
        if len(one_range) == 1:
            x_array = numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            x_array = numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            x_array = numpy.linspace(one_range[0], one_range[1], one_range[2])

        if len(two_range) == 1:
            y_array = numpy.linspace(0, two_range[0], two_range[0])
        elif len(two_range) == 2:
            y_array = numpy.linspace(two_range[0], two_range[1], two_range[1])
        else:
            y_array = numpy.linspace(two_range[0], two_range[1], two_range[2])

        x, y = numpy.meshgrid(x_array, y_array)
        array = numpy.stack((x, y), axis=-1)

        noise = self.extended_noise.generate_fbm_2d(array)

        return raw_nparray_ranger(noise, [-1, 1], range)

    def generate_3D_perlin_noise_from_range(self, one_range, two_range, three_range, range=[-1, 1]):
        if len(one_range) == 1:
            x_array = numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            x_array = numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            x_array = numpy.linspace(one_range[0], one_range[1], one_range[2])

        if len(two_range) == 1:
            y_array = numpy.linspace(0, two_range[0], two_range[0])
        elif len(two_range) == 2:
            y_array = numpy.linspace(two_range[0], two_range[1], two_range[1])
        else:
            y_array = numpy.linspace(two_range[0], two_range[1], two_range[2])

        if len(three_range) == 1:
            z_array = numpy.linspace(0, three_range[0], three_range[0])
        elif len(three_range) == 2:
            z_array = numpy.linspace(three_range[0], three_range[1], three_range[1])
        else:
            z_array = numpy.linspace(three_range[0], three_range[1], three_range[2])

        x, y, z = numpy.meshgrid(x_array, y_array, z_array)
        array = numpy.stack((x, y, z), axis=-1)

        noise = self.extended_noise.generate_fbm_3d(array)

        return raw_nparray_ranger(noise, [-1, 1], range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed