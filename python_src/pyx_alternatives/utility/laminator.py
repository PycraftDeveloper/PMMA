import heapq

def laminator(function_array, number_of_threads):
    # Initialize the heap and thread function arrays
    heap = [(0, i) for i in range(number_of_threads)]
    thread_function_array = [[] for _ in range(number_of_threads)]

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
    thread_execution_time_array = [time for time, index in sorted(heap, key=lambda x: x[1])]

    return thread_execution_time_array
