import random as _random
import importlib as _importlib
import threading as _threading
from gc import collect as _gc__collect
from traceback import format_exc as _traceback__format_exc
import time as _time

import numpy as _numpy
from numpy import array as _numpy__array
from numpy import float64 as _numpy__float64

from pmma.python_src.advmath import Math as _advmath__Math

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.noise_utils import NoiseIntermediary as _NoiseIntermediary
from pmma.python_src.utility.noise_utils import prefill_optimizer as _prefill_optimizer
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.general_utils import random_real_number as _random_real_number

class Perlin:
    def __init__(
            self,
            seed=None,
            octaves=1,
            persistence=0.5,
            do_prefill=None):

        _initialize(self)

        if _Registry.cython_acceleration_available:
            self._noise_module = _importlib.import_module(
                "pmma.bin.perlin_noise")

            self._extended_noise_module = _importlib.import_module(
                "pmma.bin.extended_perlin_noise")

        else:
            self._noise_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.perlin_noise")

            self._extended_noise_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.extended_perlin_noise")

        if seed is None:
            seed = _random.randint(0, 1000000)
        self._seed = seed

        self._noise = self._noise_module.PerlinNoise(
            self._seed,
            octaves,
            persistence)

        self._extended_noise = self._extended_noise_module.ExtendedPerlinNoise(
            self._seed,
            octaves,
            persistence)

        if do_prefill is None:
            self._do_prefill = not _NoiseIntermediary.prefill
        else:
            self._do_prefill = do_prefill

        self._math = _advmath__Math()

        if self._do_prefill:
            self._prefill_thread = _threading.Thread(
                target=self.prefill)
            self._prefill_thread.name = "PerlinNoise:Prefill_Thread"

            self._prefill_thread.daemon = True
            _NoiseIntermediary.prefill = True
            self._prefill_thread.start()

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def prefill(self):
        try:
            _Registry.perlin_noise_prefill_single_samples = 0
            x_samples = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            for _ in range(0, 10):
                for _ in range(100):
                    _Registry.perlin_noise_prefill_single_samples += 1
                    x = _random_real_number()
                    self.generate_1D_perlin_noise(x/100)
                    self.generate_2D_perlin_noise(x/100, -x/100)
                    self.generate_3D_perlin_noise(x/100, -x/100, x/100)
                _time.sleep(1/45)

            x = x_samples[0]
            del x_samples[0]
            _Registry.perlin_noise_prefill_array_samples += 1
            x_array, y_array, z_array = _prefill_optimizer(x)

            self.generate_1D_perlin_noise_from_array(x_array)

            self.generate_2D_perlin_noise_from_array(y_array)

            self.generate_3D_perlin_noise_from_array(z_array)

            self.generate_1D_perlin_noise_from_range([x])
            self.generate_2D_perlin_noise_from_range([x], [x])
            self.generate_3D_perlin_noise_from_range([x], [x], [x])

            while _Registry.in_game_loop is False or _Registry.power_saving_mode:
                for _ in range(100):
                    _Registry.perlin_noise_prefill_single_samples += 1
                    x = _random_real_number()
                    self.generate_1D_perlin_noise(x/100)
                    self.generate_2D_perlin_noise(x/100, -x/100)
                    self.generate_3D_perlin_noise(x/100, -x/100, x/100)

                if x_samples != []:
                    x = x_samples[0]
                    del x_samples[0]
                    _Registry.perlin_noise_prefill_array_samples += 1
                    x_array, y_array, z_array = _prefill_optimizer(x)

                    self.generate_1D_perlin_noise_from_array(x_array)

                    self.generate_2D_perlin_noise_from_array(y_array)

                    self.generate_3D_perlin_noise_from_array(z_array)

                    self.generate_1D_perlin_noise_from_range([x])
                    self.generate_2D_perlin_noise_from_range([x], [x])
                    self.generate_3D_perlin_noise_from_range([x], [x], [x])
                _time.sleep(1/30)
        except Exception as error:
            print(error)
            print(_traceback__format_exc())

    def generate_1D_perlin_noise(self, x, new_range=[-1, 1]):
        noise = self._noise.fBM1D(x)

        if noise > _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"] = noise
        if noise < _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"] = noise

        return self._math.ranger(
            noise,
            _numpy__array([
                    _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["min"],
                    _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise"]["max"]],
                dtype=_numpy__float64),
            _numpy__array(new_range, dtype=_numpy__float64))

    def generate_2D_perlin_noise(self, x, y, new_range=[-1, 1]):
        noise = self._noise.fBM2D(x, y)

        if noise > _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"] = noise
        if noise < _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"] = noise

        return self._math.ranger(
            noise,
            _numpy__array([
                    _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["min"],
                    _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise"]["max"]],
                dtype=_numpy__float64),
            _numpy__array(new_range, dtype=_numpy__float64))

    def generate_3D_perlin_noise(self, x, y, z, new_range=[-1, 1]):
        noise = self._noise.fBM3D(x, y, z)

        if noise > _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"] = noise
        if noise < _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"] = noise

        return self._math.ranger(
            noise,
            _numpy__array([
                    _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["min"],
                    _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise"]["max"]],
                dtype=_numpy__float64),
            _numpy__array(new_range, dtype=_numpy__float64))


    def generate_1D_perlin_noise_from_array(self, array, new_range=[-1, 1]):
        noise = self._extended_noise.generate_fbm_1d(array)

        if noise.max() > _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"] = noise.min()

        function_range_as_numpy_array = _numpy__array([
                _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["min"],
                _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_array"]["max"]],
            dtype=_numpy__float64)
        desired_range_as_numpy_array = _numpy__array(new_range, dtype=_numpy__float64)

        return self._math.nparray_ranger(
            noise,
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

    def generate_2D_perlin_noise_from_array(self, array, new_range=[-1, 1]):
        noise = self._extended_noise.generate_fbm_2d(array)

        if noise.max() > _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"] = noise.min()

        function_range_as_numpy_array = _numpy__array([
                _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["min"],
                _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_array"]["max"]],
            dtype=_numpy__float64)
        desired_range_as_numpy_array = _numpy__array(new_range, dtype=_numpy__float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def generate_3D_perlin_noise_from_array(self, array, new_range=[-1, 1]):
        noise = self._extended_noise.generate_fbm_3d(array)

        if noise.max() > _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"] = noise.max()
        if noise.min() < _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"] = noise.min()

        function_range_as_numpy_array = _numpy__array([
                _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["min"],
                _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_array"]["max"]],
            dtype=_numpy__float64)
        desired_range_as_numpy_array = _numpy__array(new_range, dtype=_numpy__float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def generate_1D_perlin_noise_from_range(self, one_range, new_range=[-1, 1]):
        if len(one_range) == 1:
            array = _numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            array = _numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            array = _numpy.linspace(one_range[0], one_range[1], one_range[2])

        noise = self._extended_noise.generate_fbm_1d(array)

        if noise.max() > _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"] = noise.min()

        function_range_as_numpy_array = _numpy__array([
                _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["min"],
                _NoiseIntermediary.noise_ranges["generate_1D_perlin_noise_from_range"]["max"]],
            dtype=_numpy__float64)
        desired_range_as_numpy_array = _numpy__array(new_range, dtype=_numpy__float64)

        return self._math.nparray_ranger(
            noise, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

    def generate_2D_perlin_noise_from_range(self, one_range, two_range, new_range=[-1, 1]):
        if len(one_range) == 1:
            x_array = _numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            x_array = _numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            x_array = _numpy.linspace(one_range[0], one_range[1], one_range[2])

        if len(two_range) == 1:
            y_array = _numpy.linspace(0, two_range[0], two_range[0])
        elif len(two_range) == 2:
            y_array = _numpy.linspace(two_range[0], two_range[1], two_range[1])
        else:
            y_array = _numpy.linspace(two_range[0], two_range[1], two_range[2])

        x, y = _numpy.meshgrid(x_array, y_array)
        array = _numpy.stack((x, y), axis=-1)

        noise = self._extended_noise.generate_fbm_2d(array)

        if noise.max() > _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"] = noise.min()

        function_range_as_numpy_array = _numpy__array([
                _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["min"],
                _NoiseIntermediary.noise_ranges["generate_2D_perlin_noise_from_range"]["max"]],
            dtype=_numpy__float64)
        desired_range_as_numpy_array = _numpy__array(new_range, dtype=_numpy__float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def generate_3D_perlin_noise_from_range(
            self,
            one_range,
            two_range,
            three_range,
            new_range=[-1, 1]):

        if len(one_range) == 1:
            x_array = _numpy.linspace(0, one_range[0], one_range[0])
        elif len(one_range) == 2:
            x_array = _numpy.linspace(one_range[0], one_range[1], one_range[1])
        else:
            x_array = _numpy.linspace(one_range[0], one_range[1], one_range[2])

        if len(two_range) == 1:
            y_array = _numpy.linspace(0, two_range[0], two_range[0])
        elif len(two_range) == 2:
            y_array = _numpy.linspace(two_range[0], two_range[1], two_range[1])
        else:
            y_array = _numpy.linspace(two_range[0], two_range[1], two_range[2])

        if len(three_range) == 1:
            z_array = _numpy.linspace(0, three_range[0], three_range[0])
        elif len(three_range) == 2:
            z_array = _numpy.linspace(three_range[0], three_range[1], three_range[1])
        else:
            z_array = _numpy.linspace(three_range[0], three_range[1], three_range[2])

        x, y, z = _numpy.meshgrid(x_array, y_array, z_array)
        array = _numpy.stack((x, y, z), axis=-1)

        noise = self._extended_noise.generate_fbm_3d(array)

        if noise.max() > _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"]:
            _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"] = noise.max()
        if noise.min() < _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"]:
            _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"] = noise.min()

        function_range_as_numpy_array = _numpy__array([
                _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["min"],
                _NoiseIntermediary.noise_ranges["generate_3D_perlin_noise_from_range"]["max"]],
            dtype=_numpy__float64)
        desired_range_as_numpy_array = _numpy__array(new_range, dtype=_numpy__float64)

        flattened_array = noise.flatten()

        range_adjusted_array = self._math.nparray_ranger(
            flattened_array, # flatten 'n' squish
            function_range_as_numpy_array,
            desired_range_as_numpy_array)

        return range_adjusted_array.reshape(noise.shape)

    def set_seed(self, seed):
        self.__init__(seed)

    def get_seed(self):
        return self._seed