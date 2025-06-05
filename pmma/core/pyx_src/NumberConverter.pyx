# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import numpy as np
cimport numpy as np

cdef extern from "NumberConverter.hpp" nogil:
    cdef cppclass CPP_ColorConverter:
        inline void SetColor_RGBA(unsigned int* in_color) except + nogil
        inline void SetColor_rgba(float* in_color) except + nogil
        inline void SetColor_RGB(unsigned int* in_color) except + nogil
        inline void SetColor_rgb(float* in_color) except + nogil

        inline void GetColor_RGBA(unsigned int* out_color) except + nogil
        inline void GetColor_rgba(float* out_color) except + nogil
        inline void GetColor_RGB(unsigned int* out_color) except + nogil
        inline void GetColor_rgb(float* out_color) except + nogil

    cdef cppclass CPP_DisplayCoordinatesConverter:
        inline void SetCoordinates_Pixel(unsigned int* in_coordinates) except + nogil
        inline void SetCoordinates_Normalized(float* in_coordinates) except + nogil

        inline void GetCoordinates_Pixel(unsigned int* out_coordinates) except + nogil
        inline void GetCoordinates_Normalized(float* out_coordinates) except + nogil

    cdef cppclass CPP_AngleConverter:
        inline void SetAngle_Degrees(float in_angle) except + nogil
        inline void SetAngle_Radians(float in_angle) except + nogil

        inline float GetAngle_Degrees() except + nogil
        inline float GetAngle_Radians() except + nogil

    cdef cppclass CPP_DisplayScalarConverter:
        inline void SetScalar_Pixel(unsigned int in_scalar) except + nogil
        inline void SetScalar_Normalized(float in_scalar) except + nogil

        inline unsigned int GetScalar_Pixel() except + nogil
        inline float GetScalar_Normalized() except + nogil

    cdef cppclass CPP_ProportionConverter:
        inline void SetProportion_Percentage(float in_proportion) except + nogil
        inline void SetProportion_Decimal(float in_proportion) except + nogil

        inline float GetProportion_Percentage() except + nogil
        inline float GetProportion_Decimal() except + nogil

cdef class ColorConverter:
    cdef:
        CPP_ColorConverter* cpp_class_ptr
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ColorConverter()

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

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

    def get_color_RGBA(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(4, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_RGBA(out_color_ptr)

        if self.using_numpy_arrays:
            return out_color_np
        else:
            return out_color_np.tolist()

    def get_color_small_rgba(self):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(4, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_rgba(out_color_ptr)

        if self.using_numpy_arrays:
            return out_color_np
        else:
            return out_color_np.tolist()

    def get_color_RGB(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_color_np
            unsigned int* out_color_ptr

        out_color_np = np.empty(3, dtype=np.uint32, order='C')
        out_color_ptr = <unsigned int*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_RGB(out_color_ptr)

        if self.using_numpy_arrays:
            return out_color_np
        else:
            return out_color_np.tolist()

    def get_color_small_rgb(self):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_color_np
            float* out_color_ptr

        out_color_np = np.empty(3, dtype=np.float32, order='C')
        out_color_ptr = <float*>&out_color_np[0]

        self.cpp_class_ptr.GetColor_rgb(out_color_ptr)

        if self.using_numpy_arrays:
            return out_color_np
        else:
            return out_color_np.tolist()

cdef class DisplayCoordinatesConverter:
    cdef:
        CPP_DisplayCoordinatesConverter* cpp_class_ptr
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DisplayCoordinatesConverter()

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr

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

    def get_coordinates_pixel(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] out_coordinates_np
            unsigned int* out_coordinates_ptr

        out_coordinates_np = np.empty(2, dtype=np.uint32, order='C')
        out_coordinates_ptr = <unsigned int*>&out_coordinates_np[0]

        self.cpp_class_ptr.GetCoordinates_Pixel(out_coordinates_ptr)

        if self.using_numpy_arrays:
            return out_coordinates_np
        else:
            return out_coordinates_np.tolist()

    def get_coordinates_normalized(self):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_coordinates_np
            float* out_coordinates_ptr

        out_coordinates_np = np.empty(2, dtype=np.float32, order='C')
        out_coordinates_ptr = <float*>&out_coordinates_np[0]

        self.cpp_class_ptr.GetCoordinates_Normalized(out_coordinates_ptr)

        if self.using_numpy_arrays:
            return out_coordinates_np
        else:
            return out_coordinates_np.tolist()

cdef class AngleConverter:
    cdef:
        CPP_AngleConverter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_AngleConverter()

    def __dealloc__(self):
        del self.cpp_class_ptr

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

cdef class DisplayScalarConverter:
    cdef:
        CPP_DisplayScalarConverter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_DisplayScalarConverter()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def set_scalar_pixel(self, value):
        cdef unsigned int in_value = <unsigned int>value
        self.cpp_class_ptr.SetScalar_Pixel(in_value)

    def set_scalar_normalized(self, value):
        cdef float in_value = <float>value
        self.cpp_class_ptr.SetScalar_Normalized(in_value)

    def get_scalar_pixel(self):
        return self.cpp_class_ptr.GetScalar_Pixel()

    def get_scalar_normalized(self):
        return self.cpp_class_ptr.GetScalar_Normalized()

cdef class ProportionConverter:
    cdef:
        CPP_ProportionConverter* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ProportionConverter()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def set_proportion_percentage(self, value):
        self.cpp_class_ptr.SetProportion_Percentage(value)

    def set_proportion_decimal(self, value):
        self.cpp_class_ptr.SetProportion_Decimal(value)

    def get_proportion_percentage(self):
        return self.cpp_class_ptr.GetProportion_Percentage()

    def get_proportion_decimal(self):
        return self.cpp_class_ptr.GetProportion_Decimal()