import threading
import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class ComputePipeline:
    def __init__(self, num_threads=None):
        if num_threads is None:
            num_threads = 0
            self.experiment_using_threads = True
            self.average_number_of_threads = []
        else:
            self.experiment_using_threads = False

        self.concurrent_functions = []
        self.series_functions = []
        self.num_threads = num_threads
        self.concurrent_functions_to_test = []
        self.concurrent_blocks = []
        self.saved_number_of_threads = self.num_threads
        self.previous_run_time = float("inf")

    def add_compute_function(self, func, parallel=False):
        if parallel:
            self.concurrent_functions_to_test.append(func)
        else:
            self.series_functions.append(func)

    def _add_concurrent_function(self, func, estimated_time):
        """Add a function to be executed concurrently."""
        self.concurrent_functions.append((func, estimated_time))
        self.concurrent_blocks = []

    def add_series_function(self, func):
        """Add a function to be executed in series."""
        self.series_functions.append(func)

    def change_num_threads(self, num_threads):
        """Change the number of threads used for concurrent functions."""
        if num_threads is None:
            num_threads = 0
            self.experiment_using_threads = True
            self.average_number_of_threads = []
        else:
            self.experiment_using_threads = False
        self.num_threads = num_threads
        self.concurrent_blocks = []

    def request_experimental_thread_evaluation(self):
        self.experiment_using_threads = True
        self.average_number_of_threads = []

    def execute(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        results = []

        if self.concurrent_functions != []:
            if self.experiment_using_threads:
                self.num_threads += 1
                self.concurrent_blocks = []
                # Group concurrent functions into blocks
                if self.concurrent_blocks == [] or self.saved_number_of_threads != self.num_threads:
                    self.concurrent_blocks = self._group_functions(self.concurrent_functions, self.num_threads)
                    self.saved_number_of_threads = self.num_threads

                # Execute concurrent function blocks
                start = time.perf_counter()
                if self.num_threads == 1:
                    results.extend(self._execute_block(self.concurrent_blocks[0]))
                else:
                    with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
                        futures = [executor.submit(self._execute_block, block) for block in self.concurrent_blocks]
                        for future in futures:
                            results.extend(future.result())
                end = time.perf_counter()
                if end-start <= self.previous_run_time:
                    self.previous_run_time = end-start
                else:
                    self.num_threads -= 1

                self.average_number_of_threads.append(self.num_threads)
                if len(self.average_number_of_threads) > 100:
                    average = sum(self.average_number_of_threads)/len(self.average_number_of_threads)
                    print(average, self.num_threads)
                    if average > self.num_threads-0.5 and average < self.num_threads+0.5:
                        self.experiment_using_threads = False
            else:
                # Group concurrent functions into blocks
                if self.concurrent_blocks == [] or self.saved_number_of_threads != self.num_threads:
                    self.concurrent_blocks = self._group_functions(self.concurrent_functions, self.num_threads)
                    self.saved_number_of_threads = self.num_threads

                # Execute concurrent function blocks
                if self.num_threads == 1:
                    results.extend(self._execute_block(self.concurrent_blocks[0]))
                else:
                    with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
                        futures = [executor.submit(self._execute_block, block) for block in self.concurrent_blocks]
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