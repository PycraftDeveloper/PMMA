import time as _time
import gc as _gc

from pmma.python_src.registry import Registry

import pmma.python_src.utility.math_utils as _math_utils
from pmma.python_src.utility.general_utils import initialize as _initialize

class Benchmark:
    def __init__(self, n=None):
        _initialize(self)

        if n is None:
            if Registry.power_saving_mode:
                n = 1_000
            else:
                n = 10_000

        self._n = n

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def test_all(self):
        self.test_pythag()

    def test_pythag(self):
        _math_utils.raw_pythag([0, 0, 0])

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self._n):
            start = _time.perf_counter()
            _math_utils.raw_pythag([
                float(iteration),
                iteration/2,
                iteration/4])

            end = _time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self._n):
            start = _time.perf_counter()
            _math_utils.raw_pythag.py_func([
                float(iteration),
                iteration/2,
                iteration/4])

            end = _time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_pythag"] = total_compiled_time < total_raw_time