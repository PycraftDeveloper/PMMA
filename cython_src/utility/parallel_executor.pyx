# parallel_executor.pyx
# cython: language_level=3
from cython.parallel import prange
import cython

cdef class ParallelExecutor:
    def __init__(self):
        pass

    @cython.cfunc
    @cython.exceptval(check=False)
    def run_compute_function(self, renderer, function):
        return function(renderer)

    cpdef list execute_batch_in_parallel(self, object renderer, list batch_functions):
        cdef int n = len(batch_functions)
        cdef object results = [None] * n

        # Running tasks in parallel using prange
        for i in prange(n, nogil=True):
            results[i] = self.run_compute_function(renderer, batch_functions[i])

        return results
