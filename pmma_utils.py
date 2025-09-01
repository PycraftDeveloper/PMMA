# type: ignore

import time

from utils import *

def get_execution_time(function, *args, **kwargs):
    start_time = time.perf_counter()
    result = function(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return execution_time, result