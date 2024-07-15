import heapq

def set_mixer(parallel_functions, concurrent_functions):
    function_array = []
    for function in concurrent_functions:
        if not function in parallel_functions:
            total_execution_time = 0
        else:
            total_execution_time = parallel_functions[function]["total_execution_time"]
        function_array.append((function, total_execution_time))

    return function_array

def laminator(parallel_functions, concurrent_functions, number_of_threads):
    function_array = set_mixer(parallel_functions, concurrent_functions)

    heap = []
    thread_function_array = []
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
