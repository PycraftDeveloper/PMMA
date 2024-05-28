from pmma.src.registry import Registry
from pmma.src.constants import Constants

from pmma.src.utility.math_utils import *
from pmma.src.utility.noise_utils import *

from pmma.src.advmath import Math

import time

class Benchmark:
    def __init__(self, n=100_000):
        self.n = n
        self.math = Math()

    def test_all(self):
        self.test_hash()
        self.test_fade()
        self.test_lerp()
        self.test_grad()
        self.test_extrapolate2()
        self.test_pythag()
        self.test_generate_2D_perlin_noise() # MUST BE DONE AFTER test_extrapolate2

    def test_hash(self):
        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            hash(iteration)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            hash.py_func(iteration)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["hash"] = total_compiled_time < total_raw_time

    def test_fade(self):
        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            fade(iteration)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            fade.py_func(iteration)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["fade"] = total_compiled_time < total_raw_time

    def test_lerp(self):
        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            lerp(iteration, 0, 1)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            lerp.py_func(iteration, 0, 1)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["lerp"] = total_compiled_time < total_raw_time

    def test_grad(self):
        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            grad(iteration, iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            grad.py_func(iteration, iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["grad"] = total_compiled_time < total_raw_time

    def test_extrapolate2(self):
        seed = raw_get_seed(0)
        raw_extrapolate2(seed, 0, 0, 0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_extrapolate2(seed, iteration, -iteration, iteration/2, -iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_extrapolate2.py_func(seed, iteration, -iteration, iteration/2, -iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["extrapolate2"] = total_compiled_time < total_raw_time

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

        Registry.custom_compiled_behavior["pythag"] = total_compiled_time < total_raw_time

    def test_generate_2D_perlin_noise(self): # slower when running test on other document with this optimization step, investigate - also strange error when running test do this first
        seed = raw_get_seed(0)
        compiled_extrapolate_function = raw_extrapolate2
        optimized_extrapolate_function = self.math.get_function_extrapolate2()
        raw_generate_2D_perlin_noise(compiled_extrapolate_function, 0, 0, seed)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_generate_2D_perlin_noise(compiled_extrapolate_function, iteration, iteration, seed)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_generate_2D_perlin_noise.py_func(optimized_extrapolate_function, iteration, iteration, seed)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["generate_2D_perlin_noise"] = total_compiled_time < total_raw_time