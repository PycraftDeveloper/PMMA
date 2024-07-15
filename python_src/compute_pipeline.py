import time
import importlib

import numpy

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
        self.optimizer = []

        self.use_machine_learning = num_threads is None

        self.parallel_functions = {}
        self.series_functions = {}

        self.function_array = []

        self.num_threads = num_threads
        self.trained = False

    def add(self, func, parallel=False):
        self.trained = False
        if parallel:
            if len(self.function_array) == 0:
                self.function_array.append([func])
                self.optimizer.append(
                    {
                        "model": self.optimizer_extension.RealTimeOptimizer(),
                        "context": numpy.array([]),
                        "use_model": True,
                        "threads": 1})
            else:
                last_item = self.function_array[-1]
                if callable(last_item):
                    self.function_array.append([func])
                    self.optimizer.append(
                    {
                        "model": self.optimizer_extension.RealTimeOptimizer(),
                        "context": numpy.array([]),
                        "use_model": True,
                        "threads": 1})
                else:
                    self.function_array[-1].append(func)
        else:
            self.function_array.append(func)

    def change_num_threads(self, num_threads):
        """Change the number of threads used for concurrent functions."""
        self.use_machine_learning = num_threads is None
        self.num_threads = num_threads

    def perform_parallel_operation(self, function_array, num_threads):
        if num_threads == 1:
            for func in function_array:
                start = time.perf_counter()
                result = func()
                end = time.perf_counter()
                total_execution_time = end-start
                if func in self.parallel_functions:
                    self.parallel_functions[func] = {"result": result, "total_execution_time": self.parallel_functions[func]["total_execution_time"]+total_execution_time, "run_in_parallel": False}
                else:
                    self.parallel_functions[func] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}
        else:
            parallel_batches = self.laminator.laminator(self.parallel_functions, function_array, num_threads)

            self.parallel_functions = self.parallel_executor.execute_batch_in_parallel(parallel_batches, self.parallel_functions)

    def benchmark(self, function_array, n):
        start_time = time.time()
        self.perform_parallel_operation(function_array, n)
        end_time = time.time()
        return end_time - start_time

    def train(self):
        if self.use_machine_learning:
            self.trained = True
            segment = 0
            for element in self.function_array:
                if not callable(element):
                    self.optimizer[segment]["model"].collect_initial_data(Constants.THREAD_COUNT, self.benchmark, element)
                    segment += 1

    def execute(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        overall_functions = {}

        segment = 0
        for element in self.function_array:
            if callable(element):
                start = time.perf_counter()
                result = element()
                end = time.perf_counter()
                total_execution_time = end - start
                self.series_functions[element] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}
            else:
                if self.trained is False:
                    self.train()

                if self.num_threads is None:
                    if self.optimizer[segment]["use_model"]:
                        num_threads = self.optimizer[segment]["model"].predict_optimal_threads(Constants.THREAD_COUNT)
                        self.optimizer[segment]["threads"] = num_threads
                    else:
                        num_threads = self.optimizer[segment]["threads"]
                else:
                    num_threads = self.num_threads

                if self.num_threads is None:
                    start_time_for_model_training = time.perf_counter()
                self.perform_parallel_operation(element, num_threads)
                if self.num_threads is None:
                    end_time_for_model_training = time.perf_counter()
                    total_time_for_model_training = end_time_for_model_training - start_time_for_model_training
                    if self.optimizer[segment]["use_model"]:
                        self.optimizer[segment]["model"].update_model(num_threads, total_time_for_model_training)

                    context = self.optimizer[segment]["context"]
                    if len(context) > 100:
                        standard_deviation = numpy.std(context)
                        mean = numpy.mean(context)
                        self.optimizer[segment]["context"] = self.optimizer[segment]["context"][1:]

                        self.optimizer[segment]["use_model"] = not (total_time_for_model_training < mean + 2*standard_deviation and total_time_for_model_training > mean - 2*standard_deviation)
                    else:
                        self.optimizer[segment]["use_model"] = True

                    self.optimizer[segment]["context"] = numpy.append(total_time_for_model_training, self.optimizer[segment]["context"])

                segment += 1

        overall_functions.update(self.series_functions)
        overall_functions.update(self.parallel_functions)

        return overall_functions