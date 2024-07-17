import multiprocessing
import time

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

def job_worker_function(queue, event):
    while True:
        try:
            x = queue.get()
            if event.get() == "Start":
                data, results_data = x  # This will block until there is data in the queue
                if data is None:
                    print("Worker received shutdown signal.")
                    break
                for function in data:
                    start = time.perf_counter()
                    result = function()
                    end = time.perf_counter()
                    total_execution_time = end - start
                    if function in results_data:
                        results_data[function] = {
                            "result": result,
                            "total_execution_time": results_data[function]["total_execution_time"] + total_execution_time,
                            "run_in_parallel": True
                        }
                    else:
                        results_data[function] = {
                            "result": result,
                            "total_execution_time": total_execution_time,
                            "run_in_parallel": True
                        }

                queue.put(results_data)
                event.put("Done")
        except Exception as e:
            print(f"Error in worker: {e}")

class ScalableCompute:
    def __init__(self, number_of_jobs=Constants.CORE_COUNT):
        self.__number_of_jobs = number_of_jobs
        self.__jobs = []
        self.__queues = []
        self.__results_data = {}
        self.__events = []

        for _ in range(self.__number_of_jobs):
            queue = multiprocessing.Queue()
            event = multiprocessing.Queue()
            process = multiprocessing.Process(target=job_worker_function, args=(queue, event,))
            process.start()
            self.__jobs.append(process)
            self.__queues.append(queue)
            self.__events.append(event)

    def execute(self, blocked_data):
        if len(blocked_data) > self.__number_of_jobs:
            raise ValueError("Too many blocks for available processes!")
        elif len(blocked_data) == self.__number_of_jobs:
            print("Perfect!")
        else:
            print("Adjustment needed")

        for i in range(len(blocked_data)):
            self.__queues[i].put((blocked_data[i], self.__results_data))
            self.__events[i].put("Start")

        for i in range(len(self.__jobs)):
            while self.__events[i].get() == "Start":
                self.__events[i].put("Start")
            results_data = self.__queues[i].get()
            print(results_data)
            self.__results_data.update(results_data)

    def get_results_data(self):
        return self.__results_data
