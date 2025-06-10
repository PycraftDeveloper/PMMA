# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import random

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_ColorConverter:
        CPP_ColorConverter(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

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

    cdef cppclass CPP_DisplayCoordinatesConverter:
        CPP_DisplayCoordinatesConverter(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

        inline void GenerateRandomCoordinates() except + nogil

        inline void GeneratePerlinCoordinates(float value) except + nogil

        inline void GenerateFractalBrownianMotionCoordinates(float value) except + nogil

        inline void SetCoordinates_Pixel(unsigned int* in_coordinates) except + nogil
        inline void SetCoordinates_Normalized(float* in_coordinates) except + nogil

        inline void GetCoordinates_Pixel(unsigned int* out_coordinates) except + nogil
        inline void GetCoordinates_Normalized(float* out_coordinates) except + nogil

    cdef cppclass CPP_AngleConverter:
        CPP_AngleConverter(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

        inline void GenerateRandomAngle() except + nogil

        inline void GeneratePerlinAngle(float value) except + nogil

        inline void GenerateFractalBrownianMotionAngle(float value) except + nogil

        inline void SetAngle_Degrees(float in_angle) except + nogil
        inline void SetAngle_Radians(float in_angle) except + nogil

        inline float GetAngle_Degrees() except + nogil
        inline float GetAngle_Radians() except + nogil

    cdef cppclass CPP_DisplayScalarConverter:
        CPP_DisplayScalarConverter(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

        inline void GenerateRandomScalar() except + nogil

        inline void GeneratePerlinScalar(float value) except + nogil

        inline void GenerateFractalBrownianMotionScalar(float value) except + nogil

        inline void SetScalar_Pixel(unsigned int in_scalar) except + nogil
        inline void SetScalar_Normalized(float in_scalar) except + nogil

        inline unsigned int GetScalar_Pixel() except + nogil
        inline float GetScalar_Normalized() except + nogil

    cdef cppclass CPP_ProportionConverter:
        CPP_ProportionConverter(unsigned int seed, unsigned int octaves, float frequency, float amplitude) except + nogil

        inline void GenerateRandomProportion() except + nogil

        inline void GeneratePerlinProportion(float value) except + nogil

        inline void GenerateFractalBrownianMotionProportion(float value) except + nogil

        inline void SetProportion_Percentage(float in_proportion) except + nogil
        inline void SetProportion_Decimal(float in_proportion) except + nogil

        inline float GetProportion_Percentage() except + nogil
        inline float GetProportion_Decimal() except + nogil

cdef class ColorConverter:
    cdef:
        CPP_ColorConverter* cpp_class_ptr
        bool using_numpy_arrays

        unsigned int seed
        unsigned int octaves
        float lacunarity
        float gain

        bool is_color_set

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_ColorConverter(seed, octaves, lacunarity, gain)

        self.using_numpy_arrays = False
        self.is_color_set = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def get_octaves(self):
        return self.octaves

    def get_lacunarity(self):
        return self.lacunarity

    def get_gain(self):
        return self.gain

    def get_color_set(self):
        return self.is_color_set

    def generate_random_color(self):
        self.cpp_class_ptr.GenerateRandomColor()
        self.is_color_set = True

    def generate_color_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinColor(value)
        self.is_color_set = True

    def generate_color_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionColor(value)
        self.is_color_set = True

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
        self.is_color_set = True

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
        self.is_color_set = True

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
        self.is_color_set = True

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
        self.is_color_set = True

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

cdef class DisplayCoordinatesConverter:
    cdef:
        CPP_DisplayCoordinatesConverter* cpp_class_ptr
        bool using_numpy_arrays

        unsigned int seed
        unsigned int octaves
        float lacunarity
        float gain

        bool is_coordinates_set

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_DisplayCoordinatesConverter(seed, octaves, lacunarity, gain)

        self.using_numpy_arrays = False
        self.is_coordinates_set = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def get_octaves(self):
        return self.octaves

    def get_lacunarity(self):
        return self.lacunarity

    def get_gain(self):
        return self.gain

    def get_coordinates_set(self):
        return self.is_coordinates_set

    def generate_random_coordinates(self):
        self.cpp_class_ptr.GenerateRandomCoordinates()
        self.is_coordinates_set = True

    def generate_coordinates_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinCoordinates(value)
        self.is_coordinates_set = True

    def generate_coordinates_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionCoordinates(value)
        self.is_coordinates_set = True

    def set_coordinates_pixel(self, in_coordinates):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] in_coordinates_np
            unsigned int* in_coordinates_ptr

        if not isinstance(in_coordinates, np.ndarray) or in_coordinates.dtype != np.uint32 or not in_coordinates.flags['C_CONTIGUOUS']:
            in_coordinates_np = np.array(in_coordinates, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            in_coordinates_np = in_coordinates
            self.using_numpy_arrays = False

        in_coordinates_ptr = <unsigned int*>&in_coordinates_np[0]

        self.cpp_class_ptr.SetCoordinates_Pixel(in_coordinates_ptr)
        self.is_coordinates_set = True

    def set_coordinates_normalized(self, in_coordinates):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] in_coordinates_np
            float* in_coordinates_ptr

        if not isinstance(in_coordinates, np.ndarray) or in_coordinates.dtype != np.float32 or not in_coordinates.flags['C_CONTIGUOUS']:
            in_coordinates_np = np.array(in_coordinates, dtype=np.float32, order='C')
            self.using_numpy_arrays = True
        else:
            in_coordinates_np = in_coordinates
            self.using_numpy_arrays = False

        in_coordinates_ptr = <float*>&in_coordinates_np[0]

        self.cpp_class_ptr.SetCoordinates_Normalized(in_coordinates_ptr)
        self.is_coordinates_set = True

    def get_coordinates_pixel(self, detect_format=True):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_coordinates_np
            unsigned int* out_coordinates_ptr

        out_coordinates_np = np.empty(2, dtype=np.uint32, order='C')
        out_coordinates_ptr = <unsigned int*>&out_coordinates_np[0]

        self.cpp_class_ptr.GetCoordinates_Pixel(out_coordinates_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_coordinates_np
            else:
                return out_coordinates_np.tolist()
        else:
            return out_coordinates_np

    def get_coordinates_normalized(self, detect_format=True):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_coordinates_np
            float* out_coordinates_ptr

        out_coordinates_np = np.empty(2, dtype=np.float32, order='C')
        out_coordinates_ptr = <float*>&out_coordinates_np[0]

        self.cpp_class_ptr.GetCoordinates_Normalized(out_coordinates_ptr)

        if detect_format:
            if self.using_numpy_arrays:
                return out_coordinates_np
            else:
                return out_coordinates_np.tolist()
        else:
            return out_coordinates_np

cdef class AngleConverter:
    cdef:
        CPP_AngleConverter* cpp_class_ptr

        unsigned int seed
        unsigned int octaves
        float lacunarity
        float gain

        bool is_angle_set

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_AngleConverter(seed, octaves, lacunarity, gain)

        self.is_angle_set = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def get_octaves(self):
        return self.octaves

    def get_lacunarity(self):
        return self.lacunarity

    def get_gain(self):
        return self.gain

    def get_angle_set(self):
        return self.is_angle_set

    def generate_random_angle(self):
        self.cpp_class_ptr.GenerateRandomAngle()
        self.is_angle_set = True

    def generate_angle_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinAngle(value)
        self.is_angle_set = True

    def generate_angle_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionAngle(value)
        self.is_angle_set = True

    def set_angle_degrees(self, value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetAngle_Degrees(in_value)
        self.is_angle_set = True

    def set_angle_radians(self, value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetAngle_Radians(in_value)
        self.is_angle_set = True

    def get_angle_degrees(self):
        return self.cpp_class_ptr.GetAngle_Degrees()

    def get_angle_radians(self):
        return self.cpp_class_ptr.GetAngle_Radians()

cdef class DisplayScalarConverter:
    cdef:
        CPP_DisplayScalarConverter* cpp_class_ptr

        unsigned int seed
        unsigned int octaves
        float lacunarity
        float gain

        bool is_scalar_set

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_DisplayScalarConverter(seed, octaves, lacunarity, gain)

        self.is_scalar_set = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def get_octaves(self):
        return self.octaves

    def get_lacunarity(self):
        return self.lacunarity

    def get_gain(self):
        return self.gain

    def get_scalar_set(self):
        return self.is_scalar_set

    def generate_random_scalar(self):
        self.cpp_class_ptr.GenerateRandomScalar()
        self.is_scalar_set = True

    def generate_scalar_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinScalar(value)
        self.is_scalar_set = True

    def generate_scalar_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionScalar(value)
        self.is_scalar_set = True

    def set_scalar_pixel(self, value):
        cdef unsigned int in_value = <unsigned int>value
        self.cpp_class_ptr.SetScalar_Pixel(in_value)
        self.is_scalar_set = True

    def set_scalar_normalized(self, value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetScalar_Normalized(in_value)
        self.is_scalar_set = True

    def get_scalar_pixel(self):
        return self.cpp_class_ptr.GetScalar_Pixel()

    def get_scalar_normalized(self):
        return self.cpp_class_ptr.GetScalar_Normalized()

cdef class ProportionConverter:
    cdef:
        CPP_ProportionConverter* cpp_class_ptr

        unsigned int seed
        unsigned int octaves
        float lacunarity
        float gain

        bool is_proportion_set

    def __cinit__(self, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_ProportionConverter(seed, octaves, lacunarity, gain)

        self.is_proportion_set = False

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def get_octaves(self):
        return self.octaves

    def get_lacunarity(self):
        return self.lacunarity

    def get_gain(self):
        return self.gain

    def get_proportion_set(self):
        return self.is_proportion_set

    def generate_random_proportion(self):
        self.cpp_class_ptr.GenerateRandomProportion()
        self.is_proportion_set = True

    def generate_proportion_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinProportion(value)
        self.is_proportion_set = True

    def generate_proportion_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionProportion(value)
        self.is_proportion_set = True

    def set_proportion_percentage(self, value):
        self.cpp_class_ptr.SetProportion_Percentage(value)
        self.is_proportion_set = True

    def set_proportion_decimal(self, value):
        self.cpp_class_ptr.SetProportion_Decimal(value)
        self.is_proportion_set = True

    def get_proportion_percentage(self):
        return self.cpp_class_ptr.GetProportion_Percentage()

    def get_proportion_decimal(self):
        return self.cpp_class_ptr.GetProportion_Decimal()

cdef class LinkedProportionConverter:
    cdef:
        CPP_ProportionConverter* cpp_class_ptr

        unsigned int seed
        unsigned int octaves
        float lacunarity
        float gain

        bool is_proportion_set

        object linked_class
        object attr_name

    def __cinit__(self, linked_class, attr_name, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        if seed == None:
            seed = random.randint(0, 0xFFFFFFFF) # 0 and max 32 bit int value

        self.cpp_class_ptr = new CPP_ProportionConverter(seed, octaves, lacunarity, gain)

        self.is_proportion_set = False

    def __init__(self, linked_class, attr_name, seed=None, octaves=2, lacunarity=0.75, gain=1.0):
        self.linked_class = linked_class
        self.attr_name = attr_name

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_seed(self):
        return self.seed

    def get_octaves(self):
        return self.octaves

    def get_lacunarity(self):
        return self.lacunarity

    def get_gain(self):
        return self.gain

    def get_proportion_set(self):
        return self.is_proportion_set

    def generate_random_proportion(self):
        self.cpp_class_ptr.GenerateRandomProportion()
        self.is_proportion_set = True
        setattr(self.linked_class, self.attr_name, self.get_proportion_decimal())

    def generate_proportion_from_perlin_noise(self, value):
        self.cpp_class_ptr.GeneratePerlinProportion(value)
        self.is_proportion_set = True
        setattr(self.linked_class, self.attr_name, self.get_proportion_decimal())

    def generate_proportion_from_fractal_brownian_motion(self, value):
        self.cpp_class_ptr.GenerateFractalBrownianMotionProportion(value)
        self.is_proportion_set = True
        setattr(self.linked_class, self.attr_name, self.get_proportion_decimal())

    def set_proportion_percentage(self, value):
        self.cpp_class_ptr.SetProportion_Percentage(value)
        self.is_proportion_set = True
        setattr(self.linked_class, self.attr_name, self.get_proportion_decimal())

    def set_proportion_decimal(self, value):
        self.cpp_class_ptr.SetProportion_Decimal(value)
        self.is_proportion_set = True
        setattr(self.linked_class, self.attr_name, value)

    def get_proportion_percentage(self):
        return self.cpp_class_ptr.GetProportion_Percentage()

    def get_proportion_decimal(self):
        return self.cpp_class_ptr.GetProportion_Decimal()