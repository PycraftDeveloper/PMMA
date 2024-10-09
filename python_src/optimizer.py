import time as _time
from gc import collect as _gc__collect
import importlib as _importlib

from numpy import array as _numpy__array
from numpy import float32 as _numpy__float32

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Benchmark:
    def __init__(self, n=None):
        _initialize(self)

        if n is None:
            if _Registry.power_saving_mode:
                n = 1_000
            else:
                n = 10_000

        self._n = n

        self._compiled_math_module = _importlib.import_module(
            "pmma.bin.math_utils")

        self._native_math_module = _importlib.import_module(
            "pmma.python_src.pyx_alternatives.utility.math_utils")

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def test_all(self):
        self.test_pythag()

    def test_pythag(self):
        self._compiled_math_module.raw_pythag(_numpy__array([0, 0, 0], dtype=_numpy__float32))

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self._n):
            start = _time.perf_counter()
            self._compiled_math_module.raw_pythag(_numpy__array([
                    float(iteration),
                    iteration/2,
                    iteration/4],
                dtype=_numpy__float32))

            end = _time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self._n):
            start = _time.perf_counter()
            self._native_math_module.raw_pythag(_numpy__array([
                    float(iteration),
                    iteration/2,
                    iteration/4],
                dtype=_numpy__float32))

            end = _time.perf_counter()
            total_raw_time += end - start

        _Registry.custom_compiled_behavior["raw_pythag"] = total_compiled_time < total_raw_time