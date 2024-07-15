# parallel_executor.pyx
# cython: language_level=3
from concurrent.futures import ThreadPoolExecutor
import time

class ParallelExecutor:
    def __init__(self):
        self.parallel_functions = None

    def run_compute_function(self, functions):
        for function in functions:
            start = time.perf_counter()
            result = function()
            end = time.perf_counter()
            total_execution_time = end-start
            if function in self.parallel_functions:
                self.parallel_functions[function] = {"result": result, "total_execution_time": self.parallel_functions[function]["total_execution_time"]+total_execution_time, "run_in_parallel": True}
            else:
                self.parallel_functions[function] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": True}

    def execute_batch_in_parallel(self, batch_functions, parallel_functions):
        self.parallel_functions = parallel_functions
        n = len(batch_functions)
        futures = []

        with ThreadPoolExecutor() as executor:
            for batch_number in range(n-1):
                futures.append(executor.submit(self.run_compute_function, batch_functions[batch_number]))

            self.run_compute_function(batch_functions[n-1])

        return self.parallel_functions