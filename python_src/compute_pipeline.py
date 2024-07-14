import threading
import time
import importlib
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
import random

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class ComputePipeline:
    def __init__(self, num_threads=None):
        if Registry.cython_acceleration_available:
            self.parallel_extension = importlib.import_module("pmma.bin.parallel_executor")
            self.laminator = importlib.import_module("pmma.bin.laminator")
        else:
            self.parallel_extension = importlib.import_module("pmma.python_src.pyx_alternatives.utility.parallel_executor")
            self.laminator = importlib.import_module("pmma.python_src.pyx_alternatives.utility.laminator")

        self.parallel_executor = self.parallel_extension.ParallelExecutor()

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
            if self.num_threads == 1:
                for func in self.concurrent_functions:
                    results.append(func[0]())
            else:
                parallel_batches = self.laminator.laminator(self.concurrent_functions.copy(), self.num_threads)

                results += self.parallel_executor.execute_batch_in_parallel(parallel_batches)

        for func in self.concurrent_functions_to_test:
            start = time.perf_counter()
            results.append(func())
            end = time.perf_counter()
            total_execution_time = end - start
            self.concurrent_functions.append((func, total_execution_time))

        self.concurrent_functions_to_test = []

        # Execute series functions
        for func in self.series_functions:
            results.append((func, func()))

        return results