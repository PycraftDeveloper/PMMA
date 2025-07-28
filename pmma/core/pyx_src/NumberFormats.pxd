# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_DisplayCoordinateFormat:
        CPP_DisplayCoordinateFormat() except +
        void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except +
        void GenerateRandomDisplayCoordinate() except +
        void GeneratePerlinDisplayCoordinate(float value) except +
        void GenerateFractalBrownianMotionDisplayCoordinate(float value) except +
        void GetDisplayCoordinate(unsigned int* out_coordinate) except +
        void SetDisplayCoordinate(unsigned int* in_coordinate) except +
        unsigned int GetSeed() except +
        unsigned int GetOctaves() except +
        float GetFrequency() except +
        float GetAmplitude() except +
        bool GetSet() except +

cdef class DisplayCoordinate:
    cdef CPP_DisplayCoordinateFormat* cpp_class_ptr
    cdef bool using_numpy_arrays

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)
    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_display_coordinate_set(self)
    cpdef void generate_random_display_coordinate(self)
    cpdef void generate_display_coordinate_from_perlin_noise(self, float value)
    cpdef void generate_display_coordinate_from_fractal_brownian_motion(self, float value)
    cpdef get_display_coordinate(self, bint detect_format=*)
    cpdef void set_display_coordinate(self, in_display_coordinate)
