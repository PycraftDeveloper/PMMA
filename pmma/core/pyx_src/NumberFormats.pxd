# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libc.stdint cimport uint8_t
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_ColorFormat:
        CPP_ColorFormat() except + nogil

        inline void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except + nogil

        inline void GenerateFromRandom(bool GenerateAlpha) except + nogil
        inline void GenerateFrom1DPerlinNoise(float value, bool GenerateAlpha) except + nogil
        inline void GenerateFrom1DFractalBrownianMotion(float value, bool GenerateAlpha) except + nogil
        inline void GenerateFrom2DPerlinNoise(float value_one, float value_two, bool GenerateAlpha) except + nogil
        inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two, bool GenerateAlpha) except + nogil
        inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_two, bool GenerateAlpha) except + nogil
        inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_two, bool GenerateAlpha) except + nogil

        inline void Set_RGBA(uint8_t* in_color) except + nogil
        inline void Set_RGB(uint8_t* in_color) except + nogil

        inline void Get_RGBA(uint8_t* out_color) except + nogil
        inline void Get_RGB(uint8_t* out_color) except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

    cdef cppclass CPP_DisplayCoordinateFormat:
        CPP_DisplayCoordinateFormat() except +

        void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except +

        void GenerateFromRandom() except +
        void GenerateFrom1DPerlinNoise(float value) except +
        void GenerateFrom2DPerlinNoise(float value_one, float value_two) except +
        void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) except +
        void GenerateFrom1DFractalBrownianMotion(float value) except +
        void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) except +
        void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) except +

        void Get(unsigned int* out_coordinate) except +
        void Set(unsigned int* in_coordinate) except +

        unsigned int GetSeed() except +
        unsigned int GetOctaves() except +
        float GetFrequency() except +
        float GetAmplitude() except +
        bool GetSet() except +

    cdef cppclass CPP_AngleFormat:
        CPP_AngleFormat() except + nogil

        void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except +

        inline void GenerateFromRandom() except + nogil
        inline void GenerateFrom1DPerlinNoise(float value) except + nogil
        inline void GenerateFrom2DPerlinNoise(float value_one, float value_two) except + nogil
        inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) except + nogil
        inline void GenerateFrom1DFractalBrownianMotion(float value) except + nogil
        inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) except + nogil
        inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) except + nogil

        inline void Set_Degrees(float in_angle) except + nogil
        inline void Set_Radians(float in_angle) except + nogil

        inline float Get_Degrees() except + nogil
        inline float Get_Radians() except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

    cdef cppclass CPP_ProportionFormat:
        CPP_ProportionFormat() except + nogil

        void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except +

        inline void GenerateFromRandom() except + nogil
        inline void GenerateFrom1DPerlinNoise(float value) except + nogil
        inline void GenerateFrom2DPerlinNoise(float value_one, float value_two) except + nogil
        inline void GenerateFrom3DPerlinNoise(float value_one, float value_two, float value_three) except + nogil
        inline void GenerateFrom1DFractalBrownianMotion(float value) except + nogil
        inline void GenerateFrom2DFractalBrownianMotion(float value_one, float value_two) except + nogil
        inline void GenerateFrom3DFractalBrownianMotion(float value_one, float value_two, float value_three) except + nogil

        inline void Set_Percentage(float in_proportion) except + nogil
        inline void Set_Decimal(float in_proportion) except + nogil

        inline float Get_Percentage() except + nogil
        inline float Get_Decimal() except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

cdef class Color:
    cdef CPP_ColorFormat* cpp_class_ptr
    cdef bool using_numpy_arrays
    cdef bool owns_cpp_class_ptr

    cdef void set_pointer(self, CPP_ColorFormat* cpp_class_ptr)

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)

    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)

    cpdef void generate_from_random(self, bool generate_alpha=?)

    cpdef void generate_from_1D_perlin_noise(self, float value, bool generate_alpha=?)
    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two, bool generate_alpha=?)
    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three, bool generate_alpha=?)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value, bool generate_alpha=?)
    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two, bool generate_alpha=?)
    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three, bool generate_alpha=?)

    cpdef void set_RGBA_array(self, in_color)
    cpdef void set_RGB_array(self, in_color)
    cpdef get_RGBA_array(self, bint detect_format=*)
    cpdef get_RGB_array(self, bint detect_format=*)

    cpdef void set_RGBA(self, uint8_t r, uint8_t g, uint8_t b, uint8_t a)
    cpdef void set_RGB(self, uint8_t r, uint8_t g, uint8_t b)
    cpdef tuple get_RGBA(self)
    cpdef tuple get_RGB(self)

cdef class DisplayCoordinate:
    cdef CPP_DisplayCoordinateFormat* cpp_class_ptr
    cdef bool using_numpy_arrays
    cdef bool owns_cpp_class_ptr

    cdef void set_pointer(self, CPP_DisplayCoordinateFormat* cpp_class_ptr)

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)

    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)

    cpdef void generate_from_random(self)

    cpdef void generate_from_1D_perlin_noise(self, float value)
    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two)
    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value)
    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two)
    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three)

    cpdef get_coord_array(self, bint detect_format=*)
    cpdef void set_coord_array(self, in_coord)

    cpdef tuple get_coord(self)
    cpdef void set_coord(self, unsigned int x, unsigned int y)

cdef class Angle:
    cdef CPP_AngleFormat* cpp_class_ptr
    cdef bool owns_cpp_class_ptr

    cdef void set_pointer(self, CPP_AngleFormat* cpp_class_ptr)

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)

    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)

    cpdef void generate_from_random(self)

    cpdef void generate_from_1D_perlin_noise(self, float value)
    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two)
    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value)
    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two)
    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three)

    cpdef void set_degrees(self, float value)
    cpdef void set_radians(self, float value)
    cpdef get_degrees(self)
    cpdef get_radians(self)

cdef class Proportion:
    cdef CPP_ProportionFormat* cpp_class_ptr
    cdef bool owns_cpp_class_ptr

    cdef void set_pointer(self, CPP_ProportionFormat* cpp_class_ptr)

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)

    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)

    cpdef void generate_from_random(self)

    cpdef void generate_from_1D_perlin_noise(self, float value)
    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two)
    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value)
    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two)
    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three)

    cpdef void set_percentage(self, float value)
    cpdef void set_decimal(self, float value)
    cpdef get_percentage(self)
    cpdef get_decimal(self)

cdef class LinkedProportion(Proportion):
    cdef object linked_class
    cdef object attr_name

    cpdef void generate_from_random(self)

    cpdef void generate_from_1D_perlin_noise(self, float value)
    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two)
    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value)
    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two)
    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three)

    cpdef void set_percentage(self, float value)
    cpdef void set_decimal(self, float value)