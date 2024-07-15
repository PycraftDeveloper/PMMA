import time
import importlib
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class ComputePipeline:
    def __init__(self, num_threads=None):
        if Registry.cython_acceleration_available:
            self.parallel_extension = importlib.import_module("pmma.bin.parallel_executor")
            self.laminator = importlib.import_module("pmma.bin.laminator")
            self.optimizer_extension = importlib.import_module("pmma.bin.pipeline_threads_ml")
        else:
            self.parallel_extension = importlib.import_module("pmma.python_src.pyx_alternatives.utility.parallel_executor")
            self.laminator = importlib.import_module("pmma.python_src.pyx_alternatives.utility.laminator")
            self.optimizer_extension = importlib.import_module("pmma.python_src.pyx_alternatives.utility.pipeline_threads_ml")

        self.parallel_executor = self.parallel_extension.ParallelExecutor()
        self.optimizer = self.optimizer_extension.RealTimeOptimizer()

        self.use_machine_learning = num_threads is None

        self.parallel_functions = {}
        self.series_functions = {}

        self.concurrent_functions = []
        self.series_functions = []
        self.num_threads = num_threads
        self.concurrent_functions_to_test = []
        self.concurrent_blocks = []
        self.previous_run_time = float("inf")
        self.created_initial_test_model = False

    def add_compute_function(self, func, parallel=False):
        if parallel:
            self.concurrent_functions_to_test.append(func)
            self.created_initial_test_model = False
        else:
            self.series_functions.append(func)

    def add_series_function(self, func):
        """Add a function to be executed in series."""
        self.series_functions.append(func)

    def change_num_threads(self, num_threads):
        """Change the number of threads used for concurrent functions."""
        self.use_machine_learning = num_threads is None
        self.num_threads = num_threads

    def perform_parallel_operation(self, num_threads):
        print(num_threads)
        if self.num_threads == 1:
            for func in self.concurrent_functions:
                start = time.perf_counter()
                result = func()
                end = time.perf_counter()
                total_execution_time = end-start
                self.parallel_functions[func] = {"result": result, "total_execution_time": self.parallel_functions[func]["total_execution_time"]+total_execution_time, "run_in_parallel": False}
        else:
            parallel_batches = self.laminator.laminator(self.parallel_functions, self.concurrent_functions, num_threads)

            self.parallel_functions = self.parallel_executor.execute_batch_in_parallel(parallel_batches, self.parallel_functions)

    def benchmark(self, n):
        start_time = time.time()
        self.perform_parallel_operation(n)
        end_time = time.time()
        return end_time - start_time

    def execute(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        overall_functions = {}

        if self.concurrent_functions != []:
            if self.created_initial_test_model is False and self.num_threads is None:
                self.created_initial_test_model = True
                self.optimizer.collect_initial_data(Constants.THREAD_COUNT, self.benchmark)
            if self.num_threads is None:
                num_threads = self.optimizer.predict_optimal_threads(Constants.THREAD_COUNT)
            else:
                num_threads = self.num_threads

            if self.num_threads is None:
                start_time_for_model_training = time.perf_counter()
            self.perform_parallel_operation(num_threads)
            if self.num_threads is None:
                end_time_for_model_training = time.perf_counter()
                total_time_for_model_training = end_time_for_model_training - start_time_for_model_training
                self.optimizer.update_model(num_threads, total_time_for_model_training)

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