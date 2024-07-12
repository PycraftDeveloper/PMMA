import asyncio
import time

class FunctionExecutor:
    def __init__(self, num_threads=2):
        self.concurrent_functions = []
        self.series_functions = []
        self.num_threads = num_threads

    def add_concurrent_function(self, func, estimated_time):
        """Add a function to be executed concurrently."""
        self.concurrent_functions.append((func, estimated_time))

    def add_series_function(self, func):
        """Add a function to be executed in series."""
        self.series_functions.append(func)

    def _group_functions(self, functions, num_groups):
        """Group functions into blocks based on estimated execution time."""
        functions.sort(key=lambda x: x[1], reverse=True)  # Sort by estimated time descending
        blocks = [[] for _ in range(num_groups)]
        block_times = [0] * num_groups

        for func, estimated_time in functions:
            # Find the block with the minimum total time
            min_index = block_times.index(min(block_times))
            blocks[min_index].append(func)
            block_times[min_index] += estimated_time

        return blocks

    async def _execute_block(self, block):
        """Execute a block of functions."""
        results = []
        tasks = [asyncio.to_thread(func) for func in block]
        for task in asyncio.as_completed(tasks):
            results.append(await task)
        return results

    async def execute_async(self):
        """Execute all functions, concurrent functions in threads and series functions in order."""
        results = []

        # Group concurrent functions into blocks
        concurrent_blocks = self._group_functions(self.concurrent_functions, self.num_threads)

        # Execute concurrent function blocks
        concurrent_tasks = [self._execute_block(block) for block in concurrent_blocks]
        concurrent_results = await asyncio.gather(*concurrent_tasks)
        for block_result in concurrent_results:
            results.extend(block_result)

        # Execute series functions
        for func in self.series_functions:
            results.append(func())

        return results

    def execute(self):
        """Wrapper to run the async execute method."""
        return asyncio.run(self.execute_async())

# Example usage:

def timed_function(duration, name):
    def inner_function():
        print(f"Running {name} for {duration} seconds")
        time.sleep(duration)
        return f"Result of {name}"
    return inner_function

executor = FunctionExecutor(num_threads=2)
executor.add_concurrent_function(timed_function(2, "func1"), estimated_time=2)
executor.add_concurrent_function(timed_function(1, "func2"), estimated_time=1)
executor.add_concurrent_function(timed_function(3, "func3"), estimated_time=3)
executor.add_concurrent_function(timed_function(1, "func4"), estimated_time=1)
executor.add_concurrent_function(timed_function(4, "func5"), estimated_time=4)
executor.add_series_function(timed_function(2, "func6"))

results = executor.execute()
print(results)


"""
New approach
============

Run each compute function first to determine exec speed.
Then, store function and corresponding exec speed in arrays.
Index 0 gives (function, exec) pair.

Use this, and N threads to split the array into N parts of
roughly equal time complexity.

Then compute these in batches somehow. Threads/ThreadExecutorPool/Async not sure as yet.
"""