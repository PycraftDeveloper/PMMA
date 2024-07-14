import heapq
from libc.stdlib cimport malloc, free

def laminator(dict parallel_functions, list concurrent_functions, int number_of_threads):
    cdef function_array = []
    for key in parallel_functions.keys():
        if key in concurrent_functions:
            function_array.append((key, parallel_functions[key]["total_execution_time"]))

    cdef list heap = [(0, i) for i in range(number_of_threads)]
    cdef list thread_function_array = [[] for _ in range(number_of_threads)]

    # Transform the heap into a min-heap
    heapq.heapify(heap)

    # Sort the function array by execution times in descending order
    function_array.sort(key=lambda x: x[1], reverse=True)

    # Distribute the functions across the threads
    while function_array:
        exec_time, index = heapq.heappop(heap)
        function, time = function_array.pop(0)  # pop the function with the highest time
        thread_function_array[index].append(function)
        new_exec_time = exec_time + time
        heapq.heappush(heap, (new_exec_time, index))

    return thread_function_array
