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
        self.test_hash2()
        self.test_fade()
        self.test_lerp()
        self.test_grad()
        self.test_grad2()
        self.test_pythag()

    def test_hash(self):
        raw_hash(0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_hash(iteration)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_hash.py_func(iteration)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_hash"] = total_compiled_time < total_raw_time

    def test_hash2(self):
        raw_hash2(0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_hash2(iteration, -iteration)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_hash2.py_func(iteration, -iteration)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_hash2"] = total_compiled_time < total_raw_time

    def test_fade(self):
        raw_fade(0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_fade(iteration)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_fade.py_func(iteration)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_fade"] = total_compiled_time < total_raw_time

    def test_lerp(self):
        raw_lerp(0, 0, 1)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_lerp(iteration, 0, 1)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_lerp.py_func(iteration, 0, 1)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_lerp"] = total_compiled_time < total_raw_time

    def test_grad(self):
        raw_grad(0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_grad(iteration, iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_grad.py_func(iteration, iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_grad"] = total_compiled_time < total_raw_time

    def test_grad2(self):
        raw_grad2(0, 0, 0)

        total_compiled_time = 0
        total_raw_time = 0
        for iteration in range(self.n):
            start = time.perf_counter()
            raw_grad2(iteration, -iteration, iteration/2)
            end = time.perf_counter()
            total_compiled_time += end - start

        for iteration in range(self.n):
            start = time.perf_counter()
            raw_grad2.py_func(iteration, -iteration, iteration/2)
            end = time.perf_counter()
            total_raw_time += end - start

        Registry.custom_compiled_behavior["raw_grad2"] = total_compiled_time < total_raw_time

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