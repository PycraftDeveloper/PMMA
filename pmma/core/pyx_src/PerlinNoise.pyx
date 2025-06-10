# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

import random

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_PerlinNoise:
        CPP_PerlinNoise(const unsigned int seed) except + nogil

        inline float Noise1D(const float x) except + nogil
        inline float Noise2D(const float x, const float y) except + nogil
        inline float Noise3D(const float x, const float y, const float z) except + nogil

        inline void ArrayNoise1D(const float* values, const unsigned int length, float* out) except + nogil
        inline void ArrayNoise2D(const float (*values)[2], const unsigned int length, float* out) except + nogil
        inline void ArrayNoise3D(const float (*values)[3], const unsigned int length, float* out) except + nogil

        inline void RangeNoise1D(const float* x_range, const unsigned int length, float* out) except + nogil
        inline void RangeNoise2D(const float* x_range, const float* y_range, const unsigned int length, float* out) except + nogil
        inline void RangeNoise3D(const float* x_range, const float* y_range, const float* z_range, const unsigned int length, float* out) except + nogil


cdef class PerlinNoise:
    """
    Seed value must be positive integer in range 0 to 4294967295.
    """
    cdef:
        CPP_PerlinNoise* cpp_class_ptr
        unsigned int seed

    def __cinit__(self, seed = None):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_PerlinNoise(seed)

        self.seed = seed

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def noise_1d(self, float x):
        return self.cpp_class_ptr.Noise1D(x)

    def noise_2d(self, float x, float y):
        return self.cpp_class_ptr.Noise2D(x, y)

    def noise_3d(self, float x, float y, float z):
        return self.cpp_class_ptr.Noise3D(x, y, z)

    def array_noise_1d(self, values):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] values_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float* values_ptr
            float* out_ptr

            unsigned int length

        # Convert 'values' to numpy float32 contiguous array
        if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
            values_np = np.array(values, dtype=np.float32, order='C')
        else:
            values_np = values

        length = <unsigned int>values_np.shape[0]
        values_ptr = &values_np[0]

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

        self.cpp_class_ptr.ArrayNoise1D(values_ptr, length, out_ptr)

        if isinstance(values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    def array_noise_2d(self, values):
        cdef:
            np.ndarray[np.float32_t, ndim=2, mode='c'] values_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float (*values_ptr)[2]
            float* out_ptr

            unsigned int length

        # Convert 'values' to numpy float32 contiguous array
        if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
            values_np = np.array(values, dtype=np.float32, order='C')
        else:
            values_np = values

        length = <unsigned int>values_np.shape[0]
        values_ptr = <float (*)[2]> values_np.data

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

        self.cpp_class_ptr.ArrayNoise2D(values_ptr, length, out_ptr)

        if isinstance(values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    def array_noise_3d(self, values):
        cdef:
            np.ndarray[np.float32_t, ndim=3, mode='c'] values_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float (*values_ptr)[3]
            float* out_ptr

            unsigned int length

        # Convert 'values' to numpy float32 contiguous array
        if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
            values_np = np.array(values, dtype=np.float32, order='C')
        else:
            values_np = values

        length = <unsigned int>values_np.shape[0]
        values_ptr = <float (*)[3]> values_np.data

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

        self.cpp_class_ptr.ArrayNoise3D(values_ptr, length, out_ptr)

        if isinstance(values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    def range_noise_1d(self, x_range, length):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] x_range_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float* x_range_ptr
            float* out_ptr

        if not isinstance(x_range, np.ndarray) or x_range.dtype != np.float32 or not x_range.flags['C_CONTIGUOUS']:
            x_range_np = np.array(x_range, dtype=np.float32, order='C')
        else:
            x_range_np = x_range

        x_range_ptr = &x_range_np[0]

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

        self.cpp_class_ptr.RangeNoise1D(x_range_ptr, length, out_ptr)

        if isinstance(x_range, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    def range_noise_2d(self, x_range, y_range, length):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] x_range_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] y_range_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float* x_range_ptr
            const float* y_range_ptr
            float* out_ptr

        if not isinstance(x_range, np.ndarray) or x_range.dtype != np.float32 or not x_range.flags['C_CONTIGUOUS']:
            x_range_np = np.array(x_range, dtype=np.float32, order='C')
        else:
            x_range_np = x_range

        if not isinstance(y_range, np.ndarray) or y_range.dtype != np.float32 or not y_range.flags['C_CONTIGUOUS']:
            y_range_np = np.array(y_range, dtype=np.float32, order='C')
        else:
            y_range_np = y_range

        x_range_ptr = &x_range_np[0]
        y_range_ptr = &y_range_np[0]

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

        self.cpp_class_ptr.RangeNoise2D(x_range_ptr, y_range_ptr, length, out_ptr)

        if isinstance(x_range, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    def range_noise_3d(self, x_range, y_range, z_range, length):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] x_range_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] y_range_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] z_range_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float* x_range_ptr
            const float* y_range_ptr
            const float* z_range_ptr
            float* out_ptr

        if not isinstance(x_range, np.ndarray) or x_range.dtype != np.float32 or not x_range.flags['C_CONTIGUOUS']:
            x_range_np = np.array(x_range, dtype=np.float32, order='C')
        else:
            x_range_np = x_range

        if not isinstance(y_range, np.ndarray) or y_range.dtype != np.float32 or not y_range.flags['C_CONTIGUOUS']:
            y_range_np = np.array(y_range, dtype=np.float32, order='C')
        else:
            y_range_np = y_range

        if not isinstance(z_range, np.ndarray) or z_range.dtype != np.float32 or not z_range.flags['C_CONTIGUOUS']:
            z_range_np = np.array(z_range, dtype=np.float32, order='C')
        else:
            z_range_np = z_range

        x_range_ptr = &x_range_np[0]
        y_range_ptr = &y_range_np[0]
        z_range_ptr = &z_range_np[0]

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

        self.cpp_class_ptr.RangeNoise3D(x_range_ptr, y_range_ptr, z_range_ptr, length, out_ptr)

        if isinstance(x_range, np.ndarray):
            return out_np
        else:
            return out_np.tolist()