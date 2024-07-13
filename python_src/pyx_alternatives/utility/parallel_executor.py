class ParallelExecutor:
    def __init__(self):
        pass

    def run_compute_function(self, renderer, function):
        return function(renderer)

    def execute_batch_in_parallel(self, renderer, batch_functions):
        n = len(batch_functions)
        results = [None] * n

        # Running tasks in parallel using range
        for i in range(n, nogil=True):
            results[i] = self.run_compute_function(renderer, batch_functions[i])

        return results