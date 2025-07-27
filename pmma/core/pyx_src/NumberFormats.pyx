# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import random

import numpy as np
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
        CPP_DisplayCoordinateFormat() except + nogil

        inline void Configure(unsigned int new_seed, unsigned int new_octaves, float new_frequency, float new_amplitude) except + nogil

        inline void GenerateRandomDisplayCoordinate() except + nogil
        inline void GeneratePerlinDisplayCoordinate(float value) except + nogil
        inline void GenerateFractalBrownianMotionDisplayCoordinate(float value) except + nogil

        inline void GetDisplayCoordinate(unsigned int* out_coordinate) except + nogil
        void SetDisplayCoordinate(unsigned int* in_coordinate) except + nogil

        inline unsigned int GetSeed() except + nogil
        inline unsigned int GetOctaves() except + nogil
        inline float GetFrequency() except + nogil
        inline float GetAmplitude() except + nogil
        inline bool GetSet() except + nogil

    cdef cppclass CPP_AngleFormat:
        CPP_AngleFormat(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

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
        CPP_ProportionFormat(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

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
    cdef:
        CPP_ColorFormat* cpp_class_ptr
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ColorFormat()

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def configure(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr.Configure(seed, octaves, lacunarity, gain)

    def get_seed(self):
        return self.cpp_class_ptr.GetSeed()

    def get_octaves(self):
        return self.cpp_class_ptr.GetOctaves()

    def get_lacunarity(self):
        return self.cpp_class_ptr.GetFrequency()

    def get_gain(self):
        return self.cpp_class_ptr.GetAmplitude()

    def get_color_set(self):
        return self.self.cpp_class_ptr.GetSet()

    def generate_random_color(self):
        self.cpp_class_ptr.GenerateRandomColor()

    def generate_color_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinColor(value)

    def generate_color_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionColor(value)

    def set_color_RGBA(self, in_color):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] in_color_np
            unsigned int* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.uint32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <unsigned int*>&in_color_np[0]

        self.cpp_class_ptr.SetColor_RGBA(in_color_ptr)

    def set_color_small_rgba(self, in_color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] in_color_np
            float* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.float32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.float32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <float*>&in_color_np[0]

        self.cpp_class_ptr.SetColor_rgba(in_color_ptr)

    def set_color_RGB(self, in_color):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] in_color_np
            unsigned int* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.uint32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <unsigned int*>&in_color_np[0]

        self.cpp_class_ptr.SetColor_RGB(in_color_ptr)

    def set_color_small_rgb(self, in_color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] in_color_np
            float* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.float32 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.float32, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <float*>&in_color_np[0]

        self.cpp_class_ptr.SetColor_rgb(in_color_ptr)

    def get_color_RGBA(self, detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(4, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_RGBA(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    def get_color_small_rgba(self, detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(4, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_rgba(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    def get_color_RGB(self, detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(3, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_RGB(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    def get_color_small_rgb(self, detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(3, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_rgb(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

cdef class DisplayCoordinate:
    cdef:
        CPP_DisplayCoordinateFormat* cpp_class_ptr
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DisplayCoordinateFormat()

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def configure(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr.Configure(seed, octaves, lacunarity, gain)

    def get_seed(self):
        return self.cpp_class_ptr.GetSeed()

    def get_octaves(self):
        return self.cpp_class_ptr.GetOctaves()

    def get_lacunarity(self):
        return self.cpp_class_ptr.GetFrequency()

    def get_gain(self):
        return self.cpp_class_ptr.GetAmplitude()

    def get_display_coordinate_set(self):
        return self.self.cpp_class_ptr.GetSet()

    def generate_random_display_coordinate(self):
        self.cpp_class_ptr.GenerateRandomDisplayCoordinate()

    def generate_display_coordinate_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinDisplayCoordinate(value)

    def generate_display_coordinate_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionDisplayCoordinate(value)

    def get_display_coordinate(self, detect_format=True):
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

    def set_display_coordinate(self, in_display_coordinate):
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

cdef class Angle:
    cdef:
        CPP_AngleFormat* cpp_class_ptr

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_AngleFormat(seed, octaves, lacunarity, gain)

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.cpp_class_ptr.GetSeed()

    def get_octaves(self):
        return self.cpp_class_ptr.GetOctaves()

    def get_lacunarity(self):
        return self.cpp_class_ptr.GetFrequency()

    def get_gain(self):
        return self.cpp_class_ptr.GetAmplitude()

    def get_angle_set(self):
        return self.self.cpp_class_ptr.GetSet()

    def generate_random_angle(self):
        self.cpp_class_ptr.GenerateRandomAngle()

    def generate_angle_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinAngle(value)

    def generate_angle_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionAngle(value)

    def set_angle_degrees(self, value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetAngle_Degrees(in_value)

    def set_angle_radians(self, value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetAngle_Radians(in_value)

    def get_angle_degrees(self):
        return self.cpp_class_ptr.GetAngle_Degrees()

    def get_angle_radians(self):
        return self.cpp_class_ptr.GetAngle_Radians()

cdef class Proportion:
    cdef:
        CPP_ProportionFormat* cpp_class_ptr

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_ProportionFormat(seed, octaves, lacunarity, gain)

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.cpp_class_ptr.GetSeed()

    def get_octaves(self):
        return self.cpp_class_ptr.GetOctaves()

    def get_lacunarity(self):
        return self.cpp_class_ptr.GetFrequency()

    def get_gain(self):
        return self.cpp_class_ptr.GetAmplitude()

    def get_proportion_set(self):
        return self.self.cpp_class_ptr.GetSet()

    def generate_random_proportion(self):
        self.cpp_class_ptr.GenerateRandomProportion()

    def generate_proportion_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinProportion(value)

    def generate_proportion_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionProportion(value)

    def set_proportion_percentage(self, value):
        self.cpp_class_ptr.SetProportion_Percentage(value)

    def set_proportion_decimal(self, value):
        self.cpp_class_ptr.SetProportion_Decimal(value)

    def get_proportion_percentage(self):
        return self.cpp_class_ptr.GetProportion_Percentage()

    def get_proportion_decimal(self):
        return self.cpp_class_ptr.GetProportion_Decimal()

cdef class LinkedProportion(Proportion):
    cdef:
        object linked_class
        object attr_name

    def __cinit__(self, linked_class, attr_name, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        super().__init__(seed, octaves, lacunarity, gain)

    def __init__(self, linked_class, attr_name, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        self.linked_class = linked_class
        self.attr_name = attr_name

    def generate_random_proportion(self):
        super().generate_random_proportion()
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    def generate_proportion_from_perlin_noise(self, value):
        super().GeneratePerlinProportion(value)
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    def generate_proportion_from_fractal_brownian_motion(self, value):
        super().GenerateFractalBrownianMotionProportion(value)
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    def set_proportion_percentage(self, value):
        super().SetProportion_Percentage(value)
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    def set_proportion_decimal(self, value):
        super().SetProportion_Decimal(value)
        setattr(self.linked_class, self.attr_name, value)