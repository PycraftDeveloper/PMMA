# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import random

import numpy as np
cimport numpy as np

from NumberFormats cimport CPP_ColorFormat, Color, CPP_DisplayCoordinateFormat, DisplayCoordinate

cdef class Color:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ColorFormat()

        self.using_numpy_arrays = False
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_ColorFormat* cpp_class_ptr):
        self.cpp_class_ptr = cpp_class_ptr
        self.owns_cpp_class_ptr = False

    cpdef void configure(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr.Configure(seed, octaves, lacunarity, gain)

    cpdef unsigned int get_seed(self):
        return self.cpp_class_ptr.GetSeed()

    cpdef unsigned int get_octaves(self):
        return self.cpp_class_ptr.GetOctaves()

    cpdef float get_lacunarity(self):
        return self.cpp_class_ptr.GetFrequency()

    cpdef float get_gain(self):
        return self.cpp_class_ptr.GetAmplitude()

    cpdef bint get_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_from_random(self, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFromRandom(generate_alpha)

    cpdef void generate_from_perlin_noise(self, float value, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFromPerlinNoise(value, generate_alpha)

    cpdef void generate_from_fractal_brownian_motion(self, float value, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFromFractalBrownianMotion(value, generate_alpha)

    cpdef void set_RGBA(self, in_color):
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

        self.cpp_class_ptr.Set_RGBA(in_color_ptr)

    cpdef void set_rgba(self, in_color):
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

        self.cpp_class_ptr.Set_rgba(in_color_ptr)

    cpdef void set_RGB(self, in_color):
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

        self.cpp_class_ptr.Set_RGB(in_color_ptr)

    cpdef void set_rgb(self, in_color):
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

        self.cpp_class_ptr.Set_rgb(in_color_ptr)

    cpdef get_RGBA(self, bint detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(4, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_class_ptr.Get_RGBA(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    cpdef get_rgba(self, bint detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(4, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_class_ptr.Get_rgba(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    cpdef get_RGB(self, bint detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(3, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_class_ptr.Get_RGB(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    cpdef get_rgb(self, bint detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(3, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_class_ptr.Get_rgb(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

cdef class DisplayCoordinate:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DisplayCoordinateFormat()
        self.using_numpy_arrays = False
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_DisplayCoordinateFormat* cpp_class_ptr):
        self.cpp_class_ptr = cpp_class_ptr
        self.owns_cpp_class_ptr = False

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

    cpdef bint get_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_from_random(self):
        self.cpp_class_ptr.GenerateFromRandom()

    cpdef void generate_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GenerateFromPerlinNoise(value)

    cpdef void generate_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFromFractalBrownianMotion(value)

    cpdef get_coords(self, bint detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_coordinate_np
            unsigned int* out_coordinate_ptr

        out_coordinate_np = np.empty(2, dtype=np.uint32, order='C')
        out_coordinate_ptr = <unsigned int*>&out_coordinate_np[0]
        self.cpp_class_ptr.Get(out_coordinate_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_coordinate_np
            else:
                return out_coordinate_np.tolist()
        else:
            return out_coordinate_np

    cpdef void set_coords(self, in_display_coordinate):
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
        self.cpp_class_ptr.Set(in_coordinate_ptr)

cdef class Angle:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_AngleFormat()
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_AngleFormat* cpp_class_ptr):
        self.cpp_class_ptr = cpp_class_ptr
        self.owns_cpp_class_ptr = False

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

    cpdef bint get_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_from_random(self):
        self.cpp_class_ptr.GenerateFromRandom()

    cpdef void generate_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GenerateFromPerlinNoise(value)

    cpdef void generate_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFromFractalBrownianMotion(value)

    cpdef void set_degrees(self, float value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.Set_Degrees(in_value)

    cpdef void set_radians(self, float value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.Set_Radians(in_value)

    cpdef get_degrees(self):
        return self.cpp_class_ptr.Get_Degrees()

    cpdef get_radians(self):
        return self.cpp_class_ptr.Get_Radians()

cdef class Proportion:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ProportionFormat()
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_ProportionFormat* cpp_class_ptr):
        self.cpp_class_ptr = cpp_class_ptr
        self.owns_cpp_class_ptr = False

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

    cpdef bint get_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_from_random(self):
        self.cpp_class_ptr.GenerateFromRandom()

    cpdef void generate_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GenerateFromPerlinNoise(value)

    cpdef void generate_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFromFractalBrownianMotion(value)

    cpdef void set_percentage(self, float value):
        self.cpp_class_ptr.Set_Percentage(value)

    cpdef void set_decimal(self, float value):
        self.cpp_class_ptr.Set_Decimal(value)

    cpdef get_percentage(self):
        return self.cpp_class_ptr.Get_Percentage()

    cpdef get_decimal(self):
        return self.cpp_class_ptr.Get_Decimal()

cdef class LinkedProportion(Proportion):
    def __cinit__(self, linked_class, attr_name):
        super().__init__()

    def __init__(self, linked_class, attr_name):
        self.linked_class = linked_class
        self.attr_name = attr_name

    cpdef void generate_from_random(self):
        super().GenerateFromRandom()
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_perlin_noise(self, float value):
        super().GenerateFromPerlinNoise(value)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_fractal_brownian_motion(self, float value):
        super().GenerateFromFractalBrownianMotion(value)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void set_percentage(self, float value):
        super().Set_Percentage(value)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void set_decimal(self, float value):
        super().Set_Decimal(value)
        setattr(self.linked_class, self.attr_name, value)