# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libc.stdint cimport uint8_t

import random

import numpy as np
cimport numpy as np

from CoreTypes cimport CPP_Color, Color, CPP_DisplayCoordinate, DisplayCoordinate

np.import_array()

cdef class Color:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Color()

        self.using_numpy_arrays = False
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_Color* cpp_class_ptr):
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

    cpdef void generate_from_1D_perlin_noise(self, float value, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFrom1DPerlinNoise(value, generate_alpha)

    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFrom2DPerlinNoise(value_one, value_two, generate_alpha)

    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFrom3DPerlinNoise(value_one, value_two, value_three, generate_alpha)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFrom1DFractalBrownianMotion(value, generate_alpha)

    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFrom2DFractalBrownianMotion(value_one, value_two, generate_alpha)

    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three, bool generate_alpha=True):
        self.cpp_class_ptr.GenerateFrom3DFractalBrownianMotion(value_one, value_two, value_three, generate_alpha)

    cpdef void set_color_name(self, color_name):
        cdef:
            string cpp_color_name

        cpp_color_name = color_name.encode('utf-8')
        self.cpp_class_ptr.Set_ColorName(cpp_color_name)

    cpdef void set_RGBA_array(self, in_color):
        cdef:
            np.ndarray[np.uint8_t, ndim=1, mode='c'] in_color_np
            uint8_t* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.uint8 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.uint8, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <uint8_t*>&in_color_np[0]

        self.cpp_class_ptr.Set_RGBA(in_color_ptr)

    cpdef void set_RGB_array(self, in_color):
        cdef:
            np.ndarray[np.uint8_t, ndim=1, mode='c'] in_color_np
            uint8_t* in_color_ptr

        if not isinstance(in_color, np.ndarray) or in_color.dtype != np.uint8 or not in_color.flags['C_CONTIGUOUS']:
            in_color_np = np.array(in_color, dtype=np.uint8, order='C')
            self.using_numpy_arrays = True
        else:
            in_color_np = in_color
            self.using_numpy_arrays = False

        in_color_ptr = <uint8_t*>&in_color_np[0]

        self.cpp_class_ptr.Set_RGB(in_color_ptr)

    cpdef get_RGBA_array(self, bint detect_format=True):
        cdef:
            np.ndarray[np.uint8_t, ndim=1, mode='c'] out_color_np
            uint8_t* out_color_ptr

        out_color_np = np.empty(4, dtype=np.uint8, order='C')
        out_color_ptr = <uint8_t*>&out_color_np[0]

        self.cpp_class_ptr.Get_RGBA(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    cpdef get_RGB_array(self, bint detect_format=True):
        cdef:
            np.ndarray[np.uint8_t, ndim=1, mode='c'] out_color_np
            uint8_t* out_color_ptr

        out_color_np = np.empty(3, dtype=np.uint8, order='C')
        out_color_ptr = <uint8_t*>&out_color_np[0]

        self.cpp_class_ptr.Get_RGB(out_color_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_color_np
            else:
                return out_color_np.tolist()
        else:
            return out_color_np

    cpdef void set_RGBA(self, uint8_t r, uint8_t g, uint8_t b, uint8_t a):
        cdef uint8_t color[4]
        color[0] = r
        color[1] = g
        color[2] = b
        color[3] = a
        self.cpp_class_ptr.Set_RGBA(&color[0])

    cpdef void set_RGB(self, uint8_t r, uint8_t g, uint8_t b):
        cdef uint8_t color[3]
        color[0] = r
        color[1] = g
        color[2] = b
        self.cpp_class_ptr.Set_RGB(&color[0])

    cpdef tuple get_RGBA(self):
        cdef uint8_t color[4]
        self.cpp_class_ptr.Get_RGBA(&color[0])
        return color[0], color[1], color[2], color[3]

    cpdef tuple get_RGB(self):
        cdef uint8_t color[3]
        self.cpp_class_ptr.Get_RGB(&color[0])
        return color[0], color[1], color[2]

cdef class DisplayCoordinate:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DisplayCoordinate()
        self.using_numpy_arrays = False
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_DisplayCoordinate* cpp_class_ptr):
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

    cpdef void set_centered(self):
        self.cpp_class_ptr.SetCentered()

    cpdef void generate_from_random(self):
        self.cpp_class_ptr.GenerateFromRandom()

    cpdef void generate_from_1D_perlin_noise(self, float value):
        self.cpp_class_ptr.GenerateFrom1DPerlinNoise(value)

    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two):
        self.cpp_class_ptr.GenerateFrom2DPerlinNoise(value_one, value_two)

    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three):
        self.cpp_class_ptr.GenerateFrom3DPerlinNoise(value_one, value_two, value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFrom1DFractalBrownianMotion(value)

    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two):
        self.cpp_class_ptr.GenerateFrom2DFractalBrownianMotion(value_one, value_two)

    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three):
        self.cpp_class_ptr.GenerateFrom3DFractalBrownianMotion(value_one, value_two, value_three)

    cpdef get_coord_array(self, bint detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_coordinate_np
            float* out_coordinate_ptr

        out_coordinate_np = np.empty(2, dtype=np.float32, order='C')
        out_coordinate_ptr = <float*>&out_coordinate_np[0]
        self.cpp_class_ptr.Get(out_coordinate_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_coordinate_np
            else:
                return out_coordinate_np.tolist()
        else:
            return out_coordinate_np

    cpdef void set_coord_array(self, in_coord):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] in_coordinate_np
            float* in_coordinate_ptr

        if not isinstance(in_coord, np.ndarray) or in_coord.dtype != np.float32 or not in_coord.flags['C_CONTIGUOUS']:
            in_coordinate_np = np.array(in_coord, dtype=np.float32, order='C')
            self.using_numpy_arrays = True
        else:
            in_coordinate_np = in_coord
            self.using_numpy_arrays = False

        in_coordinate_ptr = <float*>&in_coordinate_np[0]
        self.cpp_class_ptr.Set(in_coordinate_ptr)

    cpdef tuple get_coord(self):
        cdef float coords[2]
        self.cpp_class_ptr.Get(&coords[0])
        return coords[0], coords[1]

    cpdef void set_coord(self, float x, float y):
        cdef float coords[2]
        coords[0] = x
        coords[1] = y
        self.cpp_class_ptr.Set(&coords[0])

cdef class Angle:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Angle()
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_Angle* cpp_class_ptr):
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

    cpdef void generate_from_1D_perlin_noise(self, float value):
        self.cpp_class_ptr.GenerateFrom1DPerlinNoise(value)

    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two):
        self.cpp_class_ptr.GenerateFrom2DPerlinNoise(value_one, value_two)

    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three):
        self.cpp_class_ptr.GenerateFrom3DPerlinNoise(value_one, value_two, value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFrom1DFractalBrownianMotion(value)

    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two):
        self.cpp_class_ptr.GenerateFrom2DFractalBrownianMotion(value_one, value_two)

    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three):
        self.cpp_class_ptr.GenerateFrom3DFractalBrownianMotion(value_one, value_two, value_three)

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
        self.cpp_class_ptr = new CPP_Proportion()
        self.owns_cpp_class_ptr = True

    def __dealloc__(self):
        if self.owns_cpp_class_ptr:
            del self.cpp_class_ptr
            self.cpp_class_ptr = NULL

    cdef void set_pointer(self, CPP_Proportion* cpp_class_ptr):
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

    cpdef void generate_from_1D_perlin_noise(self, float value):
        self.cpp_class_ptr.GenerateFrom1DPerlinNoise(value)

    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two):
        self.cpp_class_ptr.GenerateFrom2DPerlinNoise(value_one, value_two)

    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three):
        self.cpp_class_ptr.GenerateFrom3DPerlinNoise(value_one, value_two, value_three)

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFrom1DFractalBrownianMotion(value)

    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two):
        self.cpp_class_ptr.GenerateFrom2DFractalBrownianMotion(value_one, value_two)

    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three):
        self.cpp_class_ptr.GenerateFrom3DFractalBrownianMotion(value_one, value_two, value_three)

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

    cpdef void generate_from_1D_perlin_noise(self, float value):
        super().GenerateFrom1DPerlinNoise(value)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_2D_perlin_noise(self, float value_one, float value_two):
        super().GenerateFrom2DPerlinNoise(value_one, value_two)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_3D_perlin_noise(self, float value_one, float value_two, float value_three):
        super().GenerateFrom3DPerlinNoise(value_one, value_two, value_three)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_1D_fractal_brownian_motion(self, float value):
        super().GenerateFrom1DFractalBrownianMotion(value)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_2D_fractal_brownian_motion(self, float value_one, float value_two):
        super().GenerateFrom2DFractalBrownianMotion(value_one, value_two)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void generate_from_3D_fractal_brownian_motion(self, float value_one, float value_two, float value_three):
        super().GenerateFrom3DFractalBrownianMotion(value_one, value_two, value_three)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void set_percentage(self, float value):
        super().Set_Percentage(value)
        setattr(self.linked_class, self.attr_name, super().get_decimal())

    cpdef void set_decimal(self, float value):
        super().Set_Decimal(value)
        setattr(self.linked_class, self.attr_name, value)