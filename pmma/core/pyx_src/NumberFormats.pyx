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

    def __dealloc__(self):
        del self.cpp_class_ptr

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

    cpdef void generate_random_color(self):
        self.cpp_class_ptr.GenerateRandomColor()

    cpdef void generate_color_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GeneratePerlinColor(value)

    cpdef void generate_color_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionColor(value)

    cpdef void set_color_RGBA(self, in_color):
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

    cpdef void set_color_small_rgba(self, in_color):
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

    cpdef void set_color_RGB(self, in_color):
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

    cpdef void set_color_small_rgb(self, in_color):
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

    cpdef get_color_RGBA(self, bint detect_format=True):
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

    cpdef get_color_small_rgba(self, bint detect_format=True):
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

    cpdef get_color_RGB(self, bint detect_format=True):
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

    cpdef get_color_small_rgb(self, bint detect_format=True):
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

    cpdef bint get_set(self):
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

cdef class Angle:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_AngleFormat()

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

    cpdef bint get_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_random_angle(self):
        self.cpp_class_ptr.GenerateRandomAngle()

    cpdef void generate_angle_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GeneratePerlinAngle(value)

    cpdef void generate_angle_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionAngle(value)

    cpdef void set_angle_degrees(self, float value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetAngle_Degrees(in_value)

    cpdef void set_angle_radians(self, float value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetAngle_Radians(in_value)

    cpdef get_angle_degrees(self):
        return self.cpp_class_ptr.GetAngle_Degrees()

    cpdef get_angle_radians(self):
        return self.cpp_class_ptr.GetAngle_Radians()

cdef class Proportion:
    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ProportionFormat()

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

    cpdef bint get_set(self):
        return self.cpp_class_ptr.GetSet()

    cpdef void generate_random_proportion(self):
        self.cpp_class_ptr.GenerateRandomProportion()

    cpdef void generate_proportion_from_perlin_noise(self, float value):
        self.cpp_class_ptr.GeneratePerlinProportion(value)

    cpdef void generate_proportion_from_fractal_brownian_motion(self, float value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionProportion(value)

    cpdef void set_proportion_percentage(self, float value):
        self.cpp_class_ptr.SetProportion_Percentage(value)

    cpdef void set_proportion_decimal(self, float value):
        self.cpp_class_ptr.SetProportion_Decimal(value)

    cpdef get_proportion_percentage(self):
        return self.cpp_class_ptr.GetProportion_Percentage()

    cpdef get_proportion_decimal(self):
        return self.cpp_class_ptr.GetProportion_Decimal()

cdef class LinkedProportion(Proportion):
    def __cinit__(self, linked_class, attr_name):
        super().__init__()

    def __init__(self, linked_class, attr_name):
        self.linked_class = linked_class
        self.attr_name = attr_name

    cpdef void generate_random_proportion(self):
        super().generate_random_proportion()
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    cpdef void generate_proportion_from_perlin_noise(self, float value):
        super().GeneratePerlinProportion(value)
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    cpdef void generate_proportion_from_fractal_brownian_motion(self, float value):
        super().GenerateFractalBrownianMotionProportion(value)
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    cpdef void set_proportion_percentage(self, float value):
        super().SetProportion_Percentage(value)
        setattr(self.linked_class, self.attr_name, super().get_proportion_decimal())

    cpdef void set_proportion_decimal(self, float value):
        super().SetProportion_Decimal(value)
        setattr(self.linked_class, self.attr_name, value)