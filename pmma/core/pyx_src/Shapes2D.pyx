# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

import random, threading

import numpy as np
cimport numpy as np

import pmma.core.py_src.Utility as Utility

from CoreTypes cimport Color, CPP_Color, DisplayCoordinate, CPP_DisplayCoordinate

np.import_array()

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_RadialPolygonShape:
        CPP_DisplayCoordinate* ShapeCenterFormat
        CPP_Color* Color

        inline void SetRadius(unsigned int in_radius) except + nogil
        inline void SetPointCount(unsigned int in_pointCount) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil

        inline unsigned int GetRadius() except + nogil
        inline unsigned int GetPointCount() except + nogil
        inline unsigned int GetWidth() except + nogil
        inline float GetRotation() except + nogil

        void Render() except + nogil

    cdef cppclass CPP_RectangleShape:
        CPP_DisplayCoordinate* ShapeCenterFormat
        CPP_Color* Color

        inline void SetCornerRadius(unsigned int in_corner_radius) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil
        inline void SetSize(unsigned int* in_size) except + nogil

        inline unsigned int GetCornerRadius() except + nogil
        inline unsigned int GetWidth() except + nogil
        inline float GetRotation() except + nogil
        inline void GetSize(unsigned int* out_size) except + nogil

        void Render() except + nogil

    cdef cppclass CPP_PixelShape:
        CPP_DisplayCoordinate* ShapeCenterFormat
        CPP_Color* Color

        void Render() except + nogil

    cdef cppclass CPP_LineShape:
        CPP_DisplayCoordinate* ShapeStart
        CPP_DisplayCoordinate* ShapeEnd
        CPP_Color* Color

        inline void SetRotation(float rotation) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil

        inline unsigned int GetWidth() except + nogil
        inline float GetRotation() except + nogil

        void Render() except + nogil

    cdef cppclass CPP_PolygonShape:
        CPP_Color* Color

        inline void SetRotation(float rotation) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetPoints(unsigned int (*in_points)[2], unsigned int count) except + nogil
        inline void SetClosed(bool in_closed) except + nogil

        inline unsigned int GetWidth() except + nogil
        inline float GetRotation() except + nogil
        inline void GetPoints(unsigned int (*out_points)[2]) except + nogil
        inline bool GetClosed() except + nogil
        inline unsigned int GetPointCount() except + nogil

        void Render() except + nogil

    cdef cppclass CPP_ArcShape:
        CPP_DisplayCoordinate* ShapeCenterFormat
        CPP_Color* Color

        inline void SetRotation(float rotation) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetStartAngle(float in_start_angle) except + nogil
        inline void SetEndAngle(float in_end_angle) except + nogil
        inline void SetPointCount(unsigned int in_point_count) except + nogil
        inline void SetRadius(unsigned int in_radius) except + nogil

        inline float GetRotation() except + nogil
        inline unsigned int GetWidth() except + nogil
        inline float GetStartAngle() except + nogil
        inline float GetEndAngle() except + nogil
        inline unsigned int GetPointCount() except + nogil
        inline unsigned int GetRadius() except + nogil

        void Render() except + nogil

    cdef cppclass CPP_EllipseShape:
        CPP_DisplayCoordinate* ShapeCenterFormat
        CPP_Color* Color

        inline void SetPointCount(unsigned int in_point_count) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil
        inline void SetSize(unsigned int* in_size) except + nogil

        inline unsigned int GetPointCount() except + nogil
        inline unsigned int GetWidth() except + nogil
        inline float GetRotation() except + nogil
        inline void GetSize(unsigned int* out_size) except + nogil

        void Render() except + nogil

cdef class RadialPolygon:
    cdef:
        CPP_RadialPolygonShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_RadialPolygonShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.set_pointer(self.cpp_class_ptr.ShapeCenterFormat)

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_center:
        def __get__(self):
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

    def set_radius(self, radius):
        self.cpp_class_ptr.SetRadius(radius)

    def get_radius(self):
        return self.cpp_class_ptr.GetRadius()

    def set_point_count(self, point_count):
        self.cpp_class_ptr.SetPointCount(point_count)

    def get_point_count(self):
        return self.cpp_class_ptr.GetPointCount()

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def get_rotation(self):
        return self.cpp_class_ptr.GetRotation()

cdef class Rectangle:
    cdef:
        CPP_RectangleShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_RectangleShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.set_pointer(self.cpp_class_ptr.ShapeCenterFormat)

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_center:
        def __get__(self):
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

    def set_size(self, size):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            unsigned int* size_ptr

        if not isinstance(size, np.ndarray) or size.dtype != np.uint32 or not size.flags['C_CONTIGUOUS']:
            size_np = np.array(size, dtype=np.uint32, order='C')
            self.using_numpy_arrays = False
        else:
            size_np = size
            self.using_numpy_arrays = True

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.SetSize(size_ptr)

    def get_size(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            unsigned int* size_ptr

        size_np = np.empty(2, dtype=np.uint32, order='C')
        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.GetSize(size_ptr)

        if self.using_numpy_arrays:
            return size_np
        else:
            return size_np.tolist()

    def set_corner_radius(self, corner_radius):
        self.cpp_class_ptr.SetCornerRadius(corner_radius)

    def get_corner_radius(self):
        return self.cpp_class_ptr.GetCornerRadius()

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def get_rotation(self):
        return self.cpp_class_ptr.GetRotation()

cdef class Pixel:
    cdef:
        CPP_PixelShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_PixelShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.set_pointer(self.cpp_class_ptr.ShapeCenterFormat)

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_center:
        def __get__(self):
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

cdef class Line:
    cdef:
        CPP_LineShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_start
        DisplayCoordinate cpp_shape_end
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_LineShape()

        self.cpp_shape_start = DisplayCoordinate()
        self.cpp_shape_start.set_pointer(self.cpp_class_ptr.ShapeStart)

        self.cpp_shape_end = DisplayCoordinate()
        self.cpp_shape_end.set_pointer(self.cpp_class_ptr.ShapeEnd)

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

    property shape_start:
        def __get__(self):
            return self.cpp_shape_start

    property shape_end:
        def __get__(self):
            return self.cpp_shape_end

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def get_rotation(self):
        return self.cpp_class_ptr.GetRotation()

cdef class PolygonShape:
    cdef:
        CPP_PolygonShape* cpp_class_ptr
        Color cpp_color_format
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_PolygonShape()

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

    def set_points(self, points):
        cdef:
            np.ndarray[np.uint32_t, ndim=2, mode='c'] points_np
            unsigned int* points_ptr
            unsigned int num_points

        # Ensure input is a C-contiguous NumPy array of shape (N, 2)
        if not isinstance(points, np.ndarray) or points.dtype != np.uint32 or not points.flags['C_CONTIGUOUS']:
            points_np = np.ascontiguousarray(points, dtype=np.uint32)
            using_numpy_arrays = False
        else:
            points_np = points
            using_numpy_arrays = True

        # Validate shape
        if points_np.ndim != 2 or points_np.shape[1] != 2:
            raise ValueError("Input array must have shape (N, 2)")

        num_points = <unsigned int>points_np.shape[0]
        points_ptr = <unsigned int*> &points_np[0, 0]

        self.cpp_class_ptr.SetPoints(<unsigned int (*)[2]> points_ptr, num_points)

    def get_point_count(self):
        return self.cpp_class_ptr.GetPointCount()

    def get_points(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=2, mode='c'] points_np
            unsigned int (*points_ptr)[2]

        num_points = self.cpp_class_ptr.GetPointCount()
        points_np = np.empty((num_points, 2), dtype=np.uint32, order='C')
        points_ptr = <unsigned int (*)[2]> points_np.data

        self.cpp_class_ptr.GetPoints(points_ptr)

        if self.using_numpy_arrays:
            return points_np
        else:
            return points_np.tolist()

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def get_rotation(self):
        return self.cpp_class_ptr.GetRotation()

    def set_closed(self, closed):
        self.cpp_class_ptr.SetClosed(closed);

    def get_closed(self):
        return self.cpp_class_ptr.GetClosed()

cdef class Arc:
    cdef:
        CPP_ArcShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ArcShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.set_pointer(self.cpp_class_ptr.ShapeCenterFormat)

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    property shape_center:
        def __get__(self):
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

    def render(self):
        self.cpp_class_ptr.Render()

    def set_radius(self, radius):
        self.cpp_class_ptr.SetRadius(radius)

    def get_radius(self):
        return self.cpp_class_ptr.GetRadius()

    def set_point_count(self, point_count):
        self.cpp_class_ptr.SetPointCount(point_count)

    def get_point_count(self):
        return self.cpp_class_ptr.GetPointCount()

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def get_rotation(self):
        return self.cpp_class_ptr.GetRotation()

    def set_start_angle(self, start_angle):
        self.cpp_class_ptr.SetStartAngle(start_angle)

    def get_start_angle(self):
        return self.cpp_class_ptr.GetStartAngle()

    def set_end_angle(self, end_angle):
        self.cpp_class_ptr.SetEndAngle(end_angle)

    def get_end_angle(self):
        return self.cpp_class_ptr.GetEndAngle()

cdef class Ellipse:
    cdef:
        CPP_EllipseShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format
        bool using_numpy_arrays

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_EllipseShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.set_pointer(self.cpp_class_ptr.ShapeCenterFormat)

        self.cpp_color_format = Color()
        self.cpp_color_format.set_pointer(self.cpp_class_ptr.Color)

        self.using_numpy_arrays = False

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_center:
        def __get__(self):
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            return self.cpp_color_format

    def set_size(self, size):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            unsigned int* size_ptr

        if not isinstance(size, np.ndarray) or size.dtype != np.uint32 or not size.flags['C_CONTIGUOUS']:
            size_np = np.array(size, dtype=np.uint32, order='C')
            self.using_numpy_arrays = False
        else:
            size_np = size
            self.using_numpy_arrays = True

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.SetSize(size_ptr)

    def get_size(self):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            unsigned int* size_ptr

        size_np = np.empty(2, dtype=np.uint32, order='C')
        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.GetSize(size_ptr)

        if self.using_numpy_arrays:
            return size_np
        else:
            return size_np.tolist()

    def set_point_count(self, point_count):
        self.cpp_class_ptr.SetPointCount(point_count)

    def get_point_count(self):
        return self.cpp_class_ptr.GetPointCount()

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def get_rotation(self):
        return self.cpp_class_ptr.GetRotation()

# Complex shapes

cdef class Circle(RadialPolygon): # Define values to BLOCK
    def set_point_count(self, point_count):
        return

    def set_rotation(self, rotation):
        return

cdef class EquilateralTriangle(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(3)

    def set_point_count(self, point_count):
        return

cdef class RegularSquare(Rectangle): # Define values to BLOCK
    def set_size(self, size):
        super().set_size([size, size])

cdef class RegularPentagon(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(5)

    def set_point_count(self, point_count):
        return

cdef class RegularHexagon(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(6)

    def set_point_count(self, point_count):
        return

cdef class RegularHeptagon(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(7)

    def set_point_count(self, point_count):
        return

cdef class RegularOctagon(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(8)

    def set_point_count(self, point_count):
        return

cdef class RegularNonagon(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(9)

    def set_point_count(self, point_count):
        return

cdef class RegularDecagon(RadialPolygon): # Define values to BLOCK
    def __init__(self):
        super().__init__()

        super().set_point_count(10)

    def set_point_count(self, point_count):
        return