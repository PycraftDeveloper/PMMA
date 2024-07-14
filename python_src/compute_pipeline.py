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

        self.parallel_functions = {}
        self.series_functions = {}

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
        overall_functions = {}

        if self.concurrent_functions != []:
            if self.num_threads == 1:
                for func in self.concurrent_functions:
                    start = time.perf_counter()
                    result = func[0]()
                    end = time.perf_counter()
                    total_execution_time = end-start
                    self.parallel_functions[func] = {"result": result, "total_execution_time": self.parallel_functions[function]["total_execution_time"]+total_execution_time, "run_in_parallel": False}
            else:
                s = time.perf_counter()
                parallel_batches = self.laminator.laminator(self.parallel_functions, self.concurrent_functions, self.num_threads)
                e = time.perf_counter()
                print(f"Time to create parallel batches: {e-s}")

                self.parallel_functions = self.parallel_executor.execute_batch_in_parallel(parallel_batches, self.parallel_functions)

        for func in self.concurrent_functions_to_test:
            start = time.perf_counter()
            result = func()
            end = time.perf_counter()
            total_execution_time = end - start
            self.parallel_functions[func] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}
            self.concurrent_functions.append(func)

        self.concurrent_functions_to_test = []

        # Execute series functions
        for func in self.series_functions:
            start = time.perf_counter()
            result = func()
            end = time.perf_counter()
            total_execution_time = end - start
            self.series_functions[func] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}

        overall_functions.update(self.series_functions)
        overall_functions.update(self.parallel_functions)

        return overall_functions