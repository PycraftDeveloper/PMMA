# parallel_executor.pyx
# cython: language_level=3
from concurrent.futures import ThreadPoolExecutor, as_completed
import cython

cdef class ParallelExecutor:
    def __init__(self):
        pass

    #@cython.cfunc
    #@cython.exceptval(check=False)
    def run_compute_function(self, list functions):
        results = []
        for function in functions:
            results.append(function())
        return results

    cpdef list execute_batch_in_parallel(self, list batch_functions):
        cdef int n = len(batch_functions)
        cdef list results = [None] * n
        cdef list futures = []

        with ThreadPoolExecutor() as executor:
            for batch_number in range(n):
                futures.append(executor.submit(self.run_compute_function, batch_functions[batch_number]))

            for future in as_completed(futures):
                results += future.result()

        return results
