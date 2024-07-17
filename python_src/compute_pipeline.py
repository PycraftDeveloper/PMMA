import time
import importlib
import inspect

import numpy

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class ComputePipeline:
    def __init__(self, num_threads=1):
        if Registry.cython_acceleration_available:
            self.__parallel_extension = importlib.import_module("pmma.bin.parallel_executor")
            self.__laminator = importlib.import_module("pmma.bin.laminator")
            self.__optimizer_extension = importlib.import_module("pmma.bin.pipeline_threads_ml")
        else:
            self.__parallel_extension = importlib.import_module("pmma.python_src.pyx_alternatives.utility.parallel_executor")
            self.__laminator = importlib.import_module("pmma.python_src.pyx_alternatives.utility.laminator")
            self.__optimizer_extension = importlib.import_module("pmma.python_src.pyx_alternatives.utility.pipeline_threads_ml")

        self.__parallel_executor = self.__parallel_extension.ParallelExecutor()
        self.__optimizer = []

        self.__use_machine_learning = num_threads is None

        self.__parallel_functions = {}
        self.__series_functions = {}

        self.__function_array = []

        self.__num_threads = num_threads
        self.__trained = False

    def __function_intermediary(self, param):
        if callable(param) and not inspect.isclass(param):
            # If param is a callable (function or bound method), return it directly
            return param
        elif inspect.isclass(param):
            # If param is a class, instantiate it
            instance = param()
            if hasattr(instance, 'compute') and callable(getattr(instance, 'compute')):
                return instance.compute
            else:
                raise ValueError("Class does not have a callable 'compute' method")
        elif isinstance(param, object):
            # If param is an instance of a class, check for a callable 'compute' method
            if hasattr(param, 'compute') and callable(getattr(param, 'compute')):
                return param.compute
            else:
                raise ValueError("Instance does not have a callable 'compute' method")
        else:
            raise ValueError("Unsupported parameter type")

    def add(self, func, parallel=False):
        func = self.__function_intermediary(func)

        self.__trained = False
        if parallel:
            if len(self.__function_array) == 0:
                self.__function_array.append([func])
                self.__optimizer.append(
                    {
                        "model": self.__optimizer_extension.RealTimeOptimizer(),
                        "context": numpy.array([]),
                        "use_model": True,
                        "threads": 1})
            else:
                last_item = self.__function_array[-1]
                if callable(last_item):
                    self.__function_array.append([func])
                    self.__optimizer.append(
                    {
                        "model": self.__optimizer_extension.RealTimeOptimizer(),
                        "context": numpy.array([]),
                        "use_model": True,
                        "threads": 1})
                else:
                    self.__function_array[-1].append(func)
        else:
            self.__function_array.append(func)

    def change_num_threads(self, num_threads):
        """Change the number of threads used for concurrent functions."""
        self.__use_machine_learning = num_threads is None
        self.__num_threads = num_threads

    def __perform_parallel_operation(self, function_array, num_threads):
        if num_threads == 1:
            for func in function_array:
                start = time.perf_counter()
                result = func()
                end = time.perf_counter()
                total_execution_time = end-start
                if func in self.__parallel_functions:
                    self.__parallel_functions[func] = {"result": result, "total_execution_time": self.__parallel_functions[func]["total_execution_time"]+total_execution_time, "run_in_parallel": False}
                else:
                    self.__parallel_functions[func] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}
        else:
            parallel_batches = self.__laminator.laminator(self.__parallel_functions, function_array, num_threads)

            self.__parallel_functions = self.__parallel_executor.execute_batch_in_parallel(parallel_batches, self.__parallel_functions)

    def __benchmark(self, __function_array, n):
        start_time = time.time()
        self.__perform_parallel_operation(__function_array, n)
        end_time = time.time()
        return end_time - start_time

    def train(self):
        if self.__use_machine_learning:
            self.__trained = True
            segment = 0
            for element in self.__function_array:
                if not callable(element):
                    self.__optimizer[segment]["model"].collect_initial_data(Constants.THREAD_COUNT, self.__benchmark, element)
                    segment += 1

    def execute(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        overall_functions = {}

        segment = 0
        for element in self.__function_array:
            if callable(element):
                start = time.perf_counter()
                result = element()
                end = time.perf_counter()
                total_execution_time = end - start
                self.__series_functions[element] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}
            else:
                if self.__trained is False:
                    self.train()

                if self.__num_threads is None:
                    if self.__optimizer[segment]["use_model"]:
                        num_threads = self.__optimizer[segment]["model"].predict_optimal_threads(Constants.THREAD_COUNT)
                        self.__optimizer[segment]["threads"] = num_threads
                    else:
                        num_threads = self.__optimizer[segment]["threads"]
                else:
                    num_threads = self.__num_threads

                if self.__num_threads is None:
                    start_time_for_model_training = time.perf_counter()
                self.__perform_parallel_operation(element, num_threads)
                if self.__num_threads is None:
                    end_time_for_model_training = time.perf_counter()
                    total_time_for_model_training = end_time_for_model_training - start_time_for_model_training
                    if self.__optimizer[segment]["use_model"]:
                        self.__optimizer[segment]["model"].update_model(num_threads, total_time_for_model_training)
                        self.__optimizer[segment]["context"] = numpy.append(total_time_for_model_training, self.__optimizer[segment]["context"])

                    context = self.__optimizer[segment]["context"]
                    if len(context) > 100:
                        standard_deviation = numpy.std(context)
                        mean = numpy.mean(context)
                        self.__optimizer[segment]["context"] = self.__optimizer[segment]["context"][1:]

                        self.__optimizer[segment]["use_model"] = not (total_time_for_model_training < mean + 2*standard_deviation and total_time_for_model_training > mean - 2*standard_deviation)
                    else:
                        self.__optimizer[segment]["use_model"] = True

                segment += 1

        overall_functions.update(self.__series_functions)
        overall_functions.update(self.__parallel_functions)

        return overall_functions