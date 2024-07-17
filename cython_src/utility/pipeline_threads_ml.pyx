# distutils: language = c++
import time
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np

try:
    from sklearnex import patch_sklearn

    # Patch scikit-learn to use Intel optimized versions
    patch_sklearn()
except:
    pass

cdef class RealTimeOptimizer:
    cdef object scaler
    cdef object model
    cdef bint initial_data_collected
    cdef object data
    cdef object X
    cdef object y

    def __init__(self):
        self.scaler = StandardScaler()
        self.model = SGDRegressor()
        self.initial_data_collected = False
        self.data = None
        self.X = None
        self.y = None

    def collect_initial_data(self, int max_n, object benchmark_function, list function_array):
        cdef list data = []
        for n in range(1, max_n + 1):
            elapsed_time = benchmark_function(function_array, n)
            data.append((n, elapsed_time))
        self.data = pd.DataFrame(data, columns=['threads', 'time'])
        self.X = self.data[['threads']]
        self.y = self.data['time']

        # Scale the features
        self.scaler.fit(self.X)
        X_scaled = self.scaler.transform(self.X)

        self.model.fit(X_scaled, self.y)
        self.initial_data_collected = True

    def update_model(self, int n, float elapsed_time):
        new_data = pd.DataFrame([[n, elapsed_time]], columns=['threads', 'time'])
        self.data = pd.concat([self.data, new_data], ignore_index=True)
        self.X = self.data[['threads']]
        self.y = self.data['time']

        # Scale the new data
        X_scaled = self.scaler.transform(self.X)

        self.model.partial_fit(X_scaled, self.y)

    def predict_optimal_threads(self, int max_n):
        X_new = np.arange(1, max_n + 1).reshape(-1, 1)

        # Ensure X_new is a DataFrame to match the fitted scaler's expectations
        X_new_df = pd.DataFrame(X_new, columns=['threads'])

        # Scale the new data
        X_new_scaled = self.scaler.transform(X_new_df)

        y_pred = self.model.predict(X_new_scaled)
        optimal_threads = X_new[np.argmin(y_pred)]
        return optimal_threads[0]