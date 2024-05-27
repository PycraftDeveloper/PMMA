from pmma.src.registry import Registry
from pmma.src.constants import Constants

from pmma.src.utility.math_utils import *
from pmma.src.utility.noise_utils import *

import time

class Benchmark:
    def __init__(self, n=100_000):
        self.n = n

    def test_all(self):
        self.test_linear_interpolation()
        self.test_cosine_interpolation()
        self.test_cubic_interpolation()
        self.test_fade()
        self.test_extrapolate2()
        self.test_pythag()

    def test_linear_interpolation(self):
        linear_interpolation(0, 0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            linear_interpolation(iteration, -iteration, iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            linear_interpolation.py_func(iteration, -iteration, iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["linear_interpolation"] = total_compiled_time > total_raw_time

    def test_cosine_interpolation(self):
        cosine_interpolation(0, 0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            cosine_interpolation(iteration, -iteration, iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            cosine_interpolation.py_func(iteration, -iteration, iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["cosine_interpolation"] = total_compiled_time > total_raw_time

    def test_cubic_interpolation(self):
        cubic_interpolation(0, 0, 0, 0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            cubic_interpolation(iteration, -iteration, iteration/2, -iteration/2, iteration/4)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            cubic_interpolation(iteration, -iteration, iteration/2, -iteration/2, iteration/4)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["cubic_interpolation"] = total_compiled_time > total_raw_time

    def test_fade(self):
        fade(0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            fade(iteration)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            fade(iteration)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["fade"] = total_compiled_time > total_raw_time

    def test_extrapolate2(self):
        seed = get_seed(0)
        extrapolate2(seed, 0, 0, 0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            extrapolate2(seed, iteration, -iteration, iteration/2, -iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            extrapolate2(seed, iteration, -iteration, iteration/2, -iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["extrapolate2"] = total_compiled_time > total_raw_time

    def test_pythag(self):
        pythag([0, 0, 0])

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            pythag([float(iteration), iteration/2, iteration/4])
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            pythag([float(iteration), iteration/2, iteration/4])
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["pythag"] = total_compiled_time > total_raw_time