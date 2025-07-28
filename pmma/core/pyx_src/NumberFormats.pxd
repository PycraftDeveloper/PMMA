# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_ColorFormat:
        CPP_ColorFormat() except + nogil

        inline void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except + nogil

        inline void GenerateRandomColor() except + nogil
        inline void GeneratePerlinColor(float value) except + nogil
        inline void GenerateFractalBrownianMotionColor(float value) except + nogil

        inline void SetColor_RGBA(unsigned int* in_color) except + nogil
        inline void SetColor_rgba(float* in_color) except + nogil
        inline void SetColor_RGB(unsigned int* in_color) except + nogil
        inline void SetColor_rgb(float* in_color) except + nogil

        inline void GetColor_RGBA(unsigned int* out_color) except + nogil
        inline void GetColor_rgba(float* out_color) except + nogil
        inline void GetColor_RGB(unsigned int* out_color) except + nogil
        inline void GetColor_rgb(float* out_color) except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

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

    cdef cppclass CPP_AngleFormat:
        CPP_AngleFormat() except + nogil

        void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except +

        inline void GenerateRandomAngle() except + nogil
        inline void GeneratePerlinAngle(float value) except + nogil
        inline void GenerateFractalBrownianMotionAngle(float value) except + nogil

        inline void SetAngle_Degrees(float in_angle) except + nogil
        inline void SetAngle_Radians(float in_angle) except + nogil

        inline float GetAngle_Degrees() except + nogil
        inline float GetAngle_Radians() except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

    cdef cppclass CPP_ProportionFormat:
        CPP_ProportionFormat() except + nogil

        void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except +

        inline void GenerateRandomProportion() except + nogil
        inline void GeneratePerlinProportion(float value) except + nogil
        inline void GenerateFractalBrownianMotionProportion(float value) except + nogil

        inline void SetProportion_Percentage(float in_proportion) except + nogil
        inline void SetProportion_Decimal(float in_proportion) except + nogil

        inline float GetProportion_Percentage() except + nogil
        inline float GetProportion_Decimal() except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

cdef class Color:
    cdef CPP_ColorFormat* cpp_class_ptr
    cdef bool using_numpy_arrays

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)
    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)
    cpdef void generate_random_color(self)
    cpdef void generate_color_from_perlin_noise(self, float value)
    cpdef void generate_color_from_fractal_brownian_motion(self, float value)
    cpdef void set_color_RGBA(self, in_color)
    cpdef void set_color_small_rgba(self, in_color)
    cpdef void set_color_RGB(self, in_color)
    cpdef void set_color_small_rgb(self, in_color)
    cpdef get_color_RGBA(self, bint detect_format=*)
    cpdef get_color_small_rgba(self, bint detect_format=*)
    cpdef get_color_RGB(self, bint detect_format=*)
    cpdef get_color_small_rgb(self, bint detect_format=*)

cdef class DisplayCoordinate:
    cdef CPP_DisplayCoordinateFormat* cpp_class_ptr
    cdef bool using_numpy_arrays

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)
    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)
    cpdef void generate_random_display_coordinate(self)
    cpdef void generate_display_coordinate_from_perlin_noise(self, float value)
    cpdef void generate_display_coordinate_from_fractal_brownian_motion(self, float value)
    cpdef get_display_coordinate(self, bint detect_format=*)
    cpdef void set_display_coordinate(self, in_display_coordinate)

cdef class Angle:
    cdef CPP_AngleFormat* cpp_class_ptr

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)
    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)
    cpdef void generate_random_angle(self)
    cpdef void generate_angle_from_perlin_noise(self, float value)
    cpdef void generate_angle_from_fractal_brownian_motion(self, float value)
    cpdef void set_angle_degrees(self, float value)
    cpdef void set_angle_radians(self, float value)
    cpdef get_angle_degrees(self)
    cpdef get_angle_radians(self)

cdef class Proportion:
    cdef CPP_ProportionFormat* cpp_class_ptr

    cpdef void configure(self, seed=?, octaves=?, lacunarity=?, gain=?)
    cpdef unsigned int get_seed(self)
    cpdef unsigned int get_octaves(self)
    cpdef float get_lacunarity(self)
    cpdef float get_gain(self)
    cpdef bint get_set(self)
    cpdef void generate_random_proportion(self)
    cpdef void generate_proportion_from_perlin_noise(self, float value)
    cpdef void generate_proportion_from_fractal_brownian_motion(self, float value)
    cpdef void set_proportion_percentage(self, float value)
    cpdef void set_proportion_decimal(self, float value)
    cpdef get_proportion_percentage(self)
    cpdef get_proportion_decimal(self)

cdef class LinkedProportion(Proportion):
    cdef object linked_class
    cdef object attr_name

    cpdef void generate_random_proportion(self)
    cpdef void generate_proportion_from_perlin_noise(self, float value)
    cpdef void generate_proportion_from_fractal_brownian_motion(self, float value)
    cpdef void set_proportion_percentage(self, float value)
    cpdef void set_proportion_decimal(self, float value)