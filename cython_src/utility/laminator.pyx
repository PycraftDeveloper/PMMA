import heapq
from libc.stdlib cimport malloc, free

cdef tuple set_mixer(dict parallel_functions, list concurrent_functions, int number_of_threads):
    cdef function_array = []
    for function in concurrent_functions:
        if not function in parallel_functions:
            total_execution_time = 0
        else:
            total_execution_time = parallel_functions[function]["total_execution_time"]
        function_array.append((function, total_execution_time))

    cdef list chunk_array = []
    cdef list time_array = []
    for i in range(number_of_threads):
        chunk_array.append([])
        time_array.append(0)

    return function_array, chunk_array, time_array

def laminator(dict parallel_functions, list concurrent_functions, int number_of_threads):
    function_array, chunk_array, time_array = set_mixer(parallel_functions, concurrent_functions, number_of_threads)

    # Distribute the functions across the threads
    for function, time in function_array:
        minimum_time = min(time_array)
        minimum_time_index = time_array.index(minimum_time)
        chunk_array[minimum_time_index].append(function)
        time_array[minimum_time_index] += time

    return chunk_array
