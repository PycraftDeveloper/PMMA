# parallel_executor.pyx
# cython: language_level=3
from concurrent.futures import ThreadPoolExecutor, as_completed
import cython
import time

cdef class ParallelExecutor:
    cdef dict parallel_functions
    def __init__(self):
        self.parallel_functions = None

    @cython.cfunc
    @cython.exceptval(check=False)
    def run_compute_function(self, list functions):
        for function in functions:
            start = time.perf_counter()
            result = function()
            end = time.perf_counter()
            total_execution_time = end-start
            self.parallel_functions[function] = {"result": result, "total_execution_time": self.parallel_functions[function]["total_execution_time"]+total_execution_time, "run_in_parallel": True}

    cpdef dict execute_batch_in_parallel(self, list batch_functions, dict parallel_functions):
        self.parallel_functions = parallel_functions
        cdef int n = len(batch_functions)
        cdef list futures = []

        with ThreadPoolExecutor() as executor:
            for batch_number in range(n):
                futures.append(executor.submit(self.run_compute_function, batch_functions[batch_number]))

        return self.parallel_functions