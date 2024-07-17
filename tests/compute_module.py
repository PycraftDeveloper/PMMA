# compute_module.py
import multiprocessing

class MyClass:
    def __init__(self):
        pass

    def compute(self):
        """compute stuff"""
        pass

    def render(self):
        """render stuff"""
        pass

def worker(func):
    func()

def execute_compute_functions(funcs):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(worker, funcs)
