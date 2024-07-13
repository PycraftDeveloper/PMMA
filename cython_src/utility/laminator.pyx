import heapq
from libc.stdlib cimport malloc, free

def laminator(list function_array, int number_of_threads):
    cdef list heap = [(0, i) for i in range(number_of_threads)]
    cdef list thread_function_array = [[] for _ in range(number_of_threads)]

    # Transform heap into a min-heap
    heapq.heapify(heap)

    # Sort the function array by execution times
    function_array.sort(key=lambda x: x[1], reverse=True)

    # Distribute the functions across the threads
    while function_array:
        exec_time, index = heapq.heappop(heap)
        function, time = function_array.pop()
        thread_function_array[index].append(function)
        new_exec_time = exec_time + time
        heapq.heappush(heap, (new_exec_time, index))

    # Extract the execution times from the heap
    cdef list thread_execution_time_array = [0] * number_of_threads
    for time, index in sorted(heap, key=lambda x: x[1]):
        thread_execution_time_array[index] = time

    return thread_execution_time_array
