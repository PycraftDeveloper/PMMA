import concurrent.futures
import os
import time
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np
import random

# Worker function to simulate some work
def worker_function(data):
    time.sleep(random.random())
    return data * data

# Function to benchmark a given number of threads
def benchmark(n):
    with concurrent.futures.ThreadPoolExecutor(max_workers=n) as executor:
        start_time = time.time()
        futures = [executor.submit(worker_function, i) for i in range(10)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        end_time = time.time()
        return end_time - start_time

# Real-time learning class
class RealTimeOptimizer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = SGDRegressor()
        self.initial_data_collected = False

    def collect_initial_data(self, max_n):
        data = []
        for n in range(1, max_n + 1):
            elapsed_time = benchmark(n)
            data.append((n, elapsed_time))
        self.data = pd.DataFrame(data, columns=['threads', 'time'])
        self.X = self.data[['threads']]
        self.y = self.data['time']

        # Scale the features
        self.scaler.fit(self.X)
        X_scaled = self.scaler.transform(self.X)

        self.model.fit(X_scaled, self.y)
        self.initial_data_collected = True

    def update_model(self, n, elapsed_time):
        new_data = pd.DataFrame([[n, elapsed_time]], columns=['threads', 'time'])
        self.data = pd.concat([self.data, new_data], ignore_index=True)
        self.X = self.data[['threads']]
        self.y = self.data['time']

        # Scale the new data
        X_scaled = self.scaler.transform(self.X)

        self.model.partial_fit(X_scaled, self.y)

    def predict_optimal_threads(self, max_n):
        X_new = np.arange(1, max_n + 1).reshape(-1, 1)

        # Scale the new data
        X_new_scaled = self.scaler.transform(X_new)

        y_pred = self.model.predict(X_new_scaled)
        optimal_threads = X_new[np.argmin(y_pred)]
        return optimal_threads[0]

# Main execution
if __name__ == "__main__":
    max_threads = os.cpu_count() * 2
    optimizer = RealTimeOptimizer()

    # Collect initial data
    optimizer.collect_initial_data(max_threads)

    # Real-time optimization loop
    for cycle in range(10):  # Run 10 cycles for demonstration
        optimal_threads = optimizer.predict_optimal_threads(max_threads)
        print(f"Cycle {cycle + 1}: Predicted optimal number of threads: {optimal_threads}")
        elapsed_time = benchmark(optimal_threads)
        print(f"Cycle {cycle + 1}: Elapsed time with {optimal_threads} threads: {elapsed_time:.2f} seconds")
        optimizer.update_model(optimal_threads, elapsed_time)
