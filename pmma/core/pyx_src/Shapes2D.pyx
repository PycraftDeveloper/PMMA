# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

import random, threading

import numpy as np
cimport numpy as np

import pmma.core.py_src.Utility as Utility

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_RadialPolygonShape:
        inline void SetColor(float* in_color, unsigned int size) except + nogil
        inline void SetCentre(unsigned int* in_position) except + nogil
        inline void SetRadius(unsigned int in_radius) except + nogil
        inline void SetPointCount(unsigned int in_pointCount) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil

        void Render(float ShapeQuality) except + nogil

    cdef cppclass CPP_RectangleShape:
        inline void SetColor(float* in_color, unsigned int size) except + nogil
        inline void SetCentre(unsigned int* in_position) except + nogil
        inline void SetCornerRadius(unsigned int in_corner_radius) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil
        inline void SetSize(unsigned int* in_size) except + nogil

        void Render(float ShapeQuality) except + nogil

cdef class RadialPolygon:
    cdef:
        CPP_RadialPolygonShape* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_RadialPolygonShape()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    def set_centre(self, position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] position_np
            unsigned int* position_ptr

        if not isinstance(position, np.ndarray) or position.dtype != np.uint32 or not position.flags['C_CONTIGUOUS']:
            position_np = np.array(position, dtype=np.uint32, order='C')
        else:
            position_np = position

        position_ptr = <unsigned int*>&position_np[0]

        self.cpp_class_ptr.SetCentre(position_ptr)

    def set_color(self, color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] color_np
            float* color_ptr

        if not isinstance(color, np.ndarray) or color.dtype != np.uint32 or not color.flags['C_CONTIGUOUS']:
            color_np = np.array(color, dtype=np.float32, order='C')
        else:
            color_np = color

        color_ptr = <float*>&color_np[0]

        self.cpp_class_ptr.SetColor(color_ptr, 4)

    def set_radius(self, radius):
        self.cpp_class_ptr.SetRadius(radius)

    def set_point_count(self, point_count):
        self.cpp_class_ptr.SetPointCount(point_count)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

cdef class Rectangle:
    cdef:
        CPP_RectangleShape* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_RectangleShape()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    def set_centre(self, position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] position_np
            unsigned int* position_ptr

        if not isinstance(position, np.ndarray) or position.dtype != np.uint32 or not position.flags['C_CONTIGUOUS']:
            position_np = np.array(position, dtype=np.uint32, order='C')
        else:
            position_np = position

        position_ptr = <unsigned int*>&position_np[0]

        self.cpp_class_ptr.SetCentre(position_ptr)

    def set_size(self, size):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            unsigned int* size_ptr

        if not isinstance(size, np.ndarray) or size.dtype != np.uint32 or not size.flags['C_CONTIGUOUS']:
            size_np = np.array(size, dtype=np.uint32, order='C')
        else:
            size_np = size

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.SetSize(size_ptr)

    def set_color(self, color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] color_np
            float* color_ptr

        if not isinstance(color, np.ndarray) or color.dtype != np.uint32 or not color.flags['C_CONTIGUOUS']:
            color_np = np.array(color, dtype=np.float32, order='C')
        else:
            color_np = color

        color_ptr = <float*>&color_np[0]

        self.cpp_class_ptr.SetColor(color_ptr, 4)

    def set_corner_radius(self, corner_radius):
        self.cpp_class_ptr.SetCornerRadius(corner_radius)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)