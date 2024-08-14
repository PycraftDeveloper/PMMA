import random
import importlib
import threading
import gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.utility.math_utils import *

def prefill_optimizer(x):
    x_array = numpy.linspace(0, x, x)
    x_out_array = x_array
    y_array = numpy.linspace(0, x, x)
    z_array = numpy.linspace(0, x, x)

    _x, _y = numpy.meshgrid(x_array, y_array)
    y_out_array = numpy.stack((_x, _y), axis=-1)

    _x, _y, _z = numpy.meshgrid(x_array, y_array, z_array)
    z_out_array = numpy.stack((_x, _y, _z), axis=-1)

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

class Perlin:
    def __init__(
            self,
            seed=None,
            octaves=1,
            persistence=0.5,
            do_prefill=None,
            number_of_single_samples=10_000):

        initialize(self)

        self.attributes = []

        if Registry.cython_acceleration_available:
            self.noise_module = importlib.import_module(
                "pmma.bin.perlin_noise")

            self.extended_noise_module = importlib.import_module(
                "pmma.bin.extended_perlin_noise")

        else:
            self.noise_module = importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.perlin_noise")

            self.extended_noise_module = importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.extended_perlin_noise")

        if seed is None:
            seed = random.randint(0, 1000000)
        self.seed = seed

        self.noise = self.noise_module.PerlinNoise(
            self.seed,
            octaves,
            persistence)

        self.extended_noise = self.extended_noise_module.ExtendedPerlinNoise(
            self.seed,
            octaves,
            persistence)

        if do_prefill is None:
            self.do_prefill = not NoiseIntermediary.prefill
        else:
            self.do_prefill = do_prefill

        if self.do_prefill:
            self.prefill_thread = threading.Thread(
                target=self.prefill,
                args=(number_of_single_samples,))

            self.prefill_thread.daemon = True
            NoiseIntermediary.prefill = True
            self.prefill_thread.start()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def prefill(self, number_of_single_samples):
        try:
            for x in range(1, number_of_single_samples):
                self.generate_1D_perlin_noise(x/100, prefill=True)
                self.generate_2D_perlin_noise(x/100, -x/100, prefill=True)
                self.generate_3D_perlin_noise(x/100, -x/100, x/100, prefill=True)

            x = 10
            x_array, y_array, z_array = prefill_optimizer(x)

            self.generate_1D_perlin_noise_from_array(x_array, prefill=True)

            self.generate_2D_perlin_noise_from_array(y_array, prefill=True)

            self.generate_3D_perlin_noise_from_array(z_array, prefill=True)

            self.generate_1D_perlin_noise_from_range([x], prefill=True)
            self.generate_2D_perlin_noise_from_range([x], [x], prefill=True)
            self.generate_3D_perlin_noise_from_range([x], [x], [x], prefill=True)
        except Exception as error:
            print(error)

    def generate_1D_perlin_noise(self, x, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        noise = self.noise.fBM1D(x)

        if noise > NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]:
            NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"] = noise
        if noise < NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"]:
            NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"] = noise

        return raw_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"],
                NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]],
            new_range)

    def generate_2D_perlin_noise(self, x, y, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        noise = self.noise.fBM2D(x, y)

        if noise > NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"]:
            NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"] = noise
        if noise < NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"]:
            NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"] = noise

        return raw_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"],
                NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"]],
            new_range)

    def generate_3D_perlin_noise(self, x, y, z, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        noise = self.noise.fBM3D(x, y, z)

        if noise > NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"]:
            NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"] = noise
        if noise < NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"]:
            NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"] = noise

        return raw_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"],
                NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"]],
            new_range)


    def generate_1D_perlin_noise_from_array(self, array, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        noise = self.extended_noise.generate_fbm_1d(array)

        if noise.max() > NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"]:
            NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"]:
            NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"] = noise.min()

        return raw_nparray_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"],
                NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]],
            new_range)

    def generate_2D_perlin_noise_from_array(self, array, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        noise = self.extended_noise.generate_fbm_2d(array)

        if noise.max() > NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"]:
            NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"]:
            NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"] = noise.min()

        return raw_nparray_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"],
                NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"]],
            new_range)

    def generate_3D_perlin_noise_from_array(self, array, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        noise = self.extended_noise.generate_fbm_3d(array)

        if noise.max() > NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"]:
            NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"]:
            NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"] = noise.min()

        return raw_nparray_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"],
                NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"]],
            new_range)


    def generate_1D_perlin_noise_from_range(self, one_range, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

        if len(one_range) == 1:
            array = numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            array = numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            array = numpy.linspace(one_range[0], one_range[1], one_range[2])

        noise = self.extended_noise.generate_fbm_1d(array)

        if noise.max() > NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"]:
            NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"]:
            NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"] = noise.min()

        return raw_nparray_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"],
                NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"]],
            new_range)

    def generate_2D_perlin_noise_from_range(self, one_range, two_range, new_range=[-1, 1], prefill=False):
        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

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

        if noise.max() > NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"]:
            NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"]:
            NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"] = noise.min()

        return raw_nparray_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"],
                NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"]],
            new_range)

    def generate_3D_perlin_noise_from_range(
            self,
            one_range,
            two_range,
            three_range,
            new_range=[-1, 1],
            prefill=False):

        if not prefill:
            if self.do_prefill and self.prefill_thread.is_alive():
                self.prefill_thread.join()

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

        if noise.max() > NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"]:
            NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"]:
            NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"] = noise.min()

        return raw_nparray_ranger(
            noise,
            [
                NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"],
                NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"]],
            new_range)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self.seed