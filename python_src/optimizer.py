import time

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.utility.math_utils import *

class Benchmark:
    def __init__(self, n=None):
        self.attributes = []

        if n is None:
            if Registry.power_saving_mode:
                n = 1_000
            else:
                n = 10_000

        self.n = n

        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def test_all(self):
        self.test_pythag()

    def test_pythag(self):
        raw_pythag([0, 0, 0])

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_pythag([
                float(iteration),
                iteration/2,
                iteration/4])

            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_pythag.py_func([
                float(iteration),
                iteration/2,
                iteration/4])

            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_pythag"] = total_compiled_time < total_raw_time