
import time

from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

from pmma.py_src.utility.math_utils import *

class Benchmark:
    def __init__(self, n=100_000):
        self.n = n

    def test_all(self):
        self.test_pythag()

    def test_pythag(self):
        raw_pythag([0, 0, 0])

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_pythag([float(iteration), iteration/2, iteration/4])
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_pythag.py_func([float(iteration), iteration/2, iteration/4])
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_pythag"] = total_compiled_time < total_raw_time