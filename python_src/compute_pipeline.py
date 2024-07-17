import time
import importlib
import inspect

import numpy

from pmma.python_src.scalable_compute_core import ScalableCompute

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class ComputePipeline:
    def __init__(self):
        if Constants.COMPUTE_CORE_OBJECT in Registry.pmma_module_spine.keys():
            self.compute_core = Registry.pmma_module_spine[Constants.COMPUTE_CORE_OBJECT]
        else:
            self.compute_core = ScalableCompute()
            Registry.pmma_module_spine[Constants.COMPUTE_CORE_OBJECT] = self.compute_core

        if Registry.cython_acceleration_available:
            self.__laminator = importlib.import_module("pmma.bin.laminator")
        else:
            self.__laminator = importlib.import_module("pmma.python_src.pyx_alternatives.utility.laminator")

        self.__parallel_functions = {}
        self.__series_functions = {}

        self.__function_array = []

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

        if parallel:
            if len(self.__function_array) == 0:
                self.__function_array.append([func])
            else:
                last_item = self.__function_array[-1]
                if type(last_item) == list:
                    self.__function_array[-1].append(func)
                else:
                    self.__function_array.append([func])

        else:
            self.__function_array.append(func)

    def __perform_parallel_operation(self, function_array):
        parallel_batches = self.__laminator.laminator(self.__parallel_functions, function_array, Constants.CORE_COUNT)

        print("Here")

        self.compute_core.execute(parallel_batches)

        print("There")
        self.__parallel_functions = self.compute_core.get_results_data()

    def execute(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        overall_functions = {}

        for element in self.__function_array:
            if callable(element):
                start = time.perf_counter()
                result = element()
                end = time.perf_counter()
                total_execution_time = end - start
                self.__series_functions[element] = {"result": result, "total_execution_time": total_execution_time, "run_in_parallel": False}
            else:
                self.__perform_parallel_operation(element)

        overall_functions.update(self.__series_functions)
        overall_functions.update(self.__parallel_functions)

        return overall_functions