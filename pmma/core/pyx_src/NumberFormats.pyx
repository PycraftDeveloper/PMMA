# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

import random
import numpy as np
cimport numpy as np

from libcpp cimport bool
from NumberFormats cimport CPP_DisplayCoordinateFormat, DisplayCoordinate

cdef class DisplayCoordinate:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DisplayCoordinateFormat()
        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    cpdef void configure(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed is None:
            seed = random.randint(0, 0xFFFFFFFF)
        self.cpp_class_ptr.Configure(seed, octaves, lacunarity, gain)

    cpdef unsigned int get_seed(self):
        return self.cpp_class_ptr.GetSeed()

    cpdef unsigned int get_octaves(self):
        return self.cpp_class_ptr.GetOctaves()

    cpdef float get_lacunarity(self):
        return self.cpp_class_ptr.GetFrequency()

    cpdef float get_gain(self):
        return self.cpp_class_ptr.GetAmplitude()

    cpdef bint get_display_coordinate_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_random_display_coordinate(self):
        self.cpp_class_ptr.GenerateRandomDisplayCoordinate()

    cpdef void generate_display_coordinate_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GeneratePerlinDisplayCoordinate(value)

    cpdef void generate_display_coordinate_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionDisplayCoordinate(value)

    cpdef get_display_coordinate(self, bint detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_coordinate_np
            unsigned int* out_coordinate_ptr

        out_coordinate_np = np.empty(2, dtype=np.uint32, order='C')
        out_coordinate_ptr = <unsigned int*>&out_coordinate_np[0]
        self.cpp_class_ptr.GetDisplayCoordinate(out_coordinate_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_coordinate_np
            else:
                return out_coordinate_np.tolist()
        else:
            return out_coordinate_np

    cpdef void set_display_coordinate(self, in_display_coordinate):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] in_coordinate_np
            unsigned int* in_coordinate_ptr

        if not isinstance(in_display_coordinate, np.ndarray) or in_display_coordinate.dtype != np.uint32 or not in_display_coordinate.flags['C_CONTIGUOUS']:
            in_coordinate_np = np.array(in_display_coordinate, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            in_coordinate_np = in_display_coordinate
            self.using_numpy_arrays = False

        in_coordinate_ptr = <unsigned int*>&in_coordinate_np[0]
        self.cpp_class_ptr.SetDisplayCoordinate(in_coordinate_ptr)
