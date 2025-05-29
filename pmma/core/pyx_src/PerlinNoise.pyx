# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

import random

cdef extern from "PerlinNoise.hpp":
    cdef cppclass CPP_PerlinNoise:
        CPP_PerlinNoise(unsigned int seed) nogil
        float CPP_Noise1D(float x) nogil
        float CPP_Noise2D(float x, float y) nogil
        float CPP_Noise3D(float x, float y, float z) nogil

cdef class PerlinNoise:
    """
    Seed value must be positive integer in range 0 to 4294967295.
    """
    cdef CPP_PerlinNoise* cpp_class_ptr

    def __cinit__(self, unsigned int seed = 0xFFFFFFFF):
        if seed == 0xFFFFFFFF:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value
        self.cpp_class_ptr = new CPP_PerlinNoise(seed)

    def __dealloc__(self):
        del self.cpp_class_ptr

    def noise1D(self, float x):
        return self.cpp_class_ptr.CPP_Noise1D(x)

    def noise2D(self, float x, float y):
        return self.cpp_class_ptr.CPP_Noise2D(x, y)

    def noise3D(self, float x, float y, float z):
        return self.cpp_class_ptr.CPP_Noise3D(x, y, z)