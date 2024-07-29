def laminator(function_array, number_of_threads):
    thread_function_array = []
    thread_execution_time_array = []
    for _ in range(number_of_threads):
        thread_function_array.append([])
        thread_execution_time_array.append(0)

    while function_array != []:
        min_execution_time_thread = min(thread_execution_time_array)
        min_execution_time_index = thread_execution_time_array.index(min_execution_time_thread)
        thread_function_array[min_execution_time_index].append(function_array[0][0])
        thread_execution_time_array[min_execution_time_index] += function_array[0][1]
        del function_array[0]

    return thread_execution_time_array

import random

funcs = []
N = 500
for _ in range(N):
    funcs.append([_, random.random()])

print(laminator(funcs, 3))