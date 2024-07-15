import heapq
from libc.stdlib cimport malloc, free

cdef list set_mixer(dict parallel_functions, list concurrent_functions):
    cdef function_array = []
    for function in concurrent_functions:
        function_array.append((function, parallel_functions[function]["total_execution_time"]))

    return function_array

def laminator(dict parallel_functions, list concurrent_functions, int number_of_threads):
    function_array = set_mixer(parallel_functions, concurrent_functions)

    cdef list heap = []
    cdef list thread_function_array = []
    for i in range(number_of_threads):
        heap.append((0, i))
        thread_function_array.append([])

    # Transform the heap into a min-heap
    heapq.heapify(heap)

    # Sort the function array by execution times in descending order
    function_array.sort(key=lambda x: x[1], reverse=True)

    # Distribute the functions across the threads
    for function, time in function_array:
        exec_time, index = heapq.heappop(heap)
        thread_function_array[index].append(function)
        new_exec_time = exec_time + time
        heapq.heappush(heap, (new_exec_time, index))

    return thread_function_array
