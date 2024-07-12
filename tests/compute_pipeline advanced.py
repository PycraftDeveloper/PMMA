import threading
import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
import time

class ComputePipeline:
    def __init__(self, num_threads=2):
        self.concurrent_functions = []
        self.series_functions = []
        self.num_threads = num_threads
        self.concurrent_functions_to_test = []

    def add_compute_function(self, func, parallel=False):
        if parallel:
            self.concurrent_functions_to_test.append(func)
        else:
            self.series_functions.append(func)

    def _add_concurrent_function(self, func, estimated_time):
        """Add a function to be executed concurrently."""
        self.concurrent_functions.append((func, estimated_time))

    def add_series_function(self, func):
        """Add a function to be executed in series."""
        self.series_functions.append(func)

    def execute(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        results = []

        # Group concurrent functions into blocks
        concurrent_blocks = self._group_functions(self.concurrent_functions, self.num_threads)

        # Execute concurrent function blocks
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = [executor.submit(self._execute_block, block) for block in concurrent_blocks]
            for future in futures:
                results.extend(future.result())

        for func in self.concurrent_functions_to_test:
            start = time.perf_counter()
            results.append(func())
            end = time.perf_counter()
            total_execution_time = end - start
            self._add_concurrent_function(func, total_execution_time)

        self.concurrent_functions_to_test = []

        # Execute series functions
        for func in self.series_functions:
            results.append((func, func()))

        return results

    def _group_functions(self, functions, num_groups):
        """Group functions into blocks based on estimated execution time."""
        functions.sort(key=lambda x: x[1], reverse=True)  # Sort by estimated time descending
        blocks = [[] for _ in range(num_groups)]
        block_times = [0] * num_groups

        for func, estimated_time in functions:
            # Find the block with the minimum total time
            min_index = block_times.index(min(block_times))
            blocks[min_index].append(func)
            block_times[min_index] += estimated_time

        return blocks

    def _execute_block(self, block):
        """Execute a block of functions."""
        results = []
        for func in block:
            results.append(func())
        return results

# Example usage:

def timed_function(duration, name):
    def inner_function():
        print(f"Running {name} for {duration} seconds")
        time.sleep(duration)
        return f"Result of {name}"
    return inner_function

executor = ComputePipeline(num_threads=3)
executor.add_concurrent_function(timed_function(2, "func1"))
executor.add_concurrent_function(timed_function(1, "func2"))
executor.add_concurrent_function(timed_function(3, "func3"))
executor.add_concurrent_function(timed_function(1, "func4"))
executor.add_concurrent_function(timed_function(4, "func5"))
executor.add_series_function(timed_function(2, "func6"))

start = time.perf_counter()
results = executor.execute()
end = time.perf_counter()
print(end-start)
print(results)

start = time.perf_counter()
results = executor.execute()
end = time.perf_counter()
print(end-start)
print(results)