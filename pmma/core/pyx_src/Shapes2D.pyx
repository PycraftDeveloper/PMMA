# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

import random, threading

import numpy as np
cimport numpy as np

import pmma.core.py_src.Utility as Utility

from NumberFormats cimport Color, CPP_ColorFormat, DisplayCoordinate, CPP_DisplayCoordinateFormat

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_RadialPolygonShape:
        CPP_DisplayCoordinateFormat* ShapeCentreFormat
        CPP_ColorFormat* ColorFormat

        inline void SetRadius(unsigned int in_radius) except + nogil
        inline void SetPointCount(unsigned int in_pointCount) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil

        void Render(float ShapeQuality) except + nogil

    cdef cppclass CPP_RectangleShape:
        CPP_DisplayCoordinateFormat* ShapeCentreFormat
        CPP_ColorFormat* ColorFormat

        inline void SetCentre(unsigned int* in_position) except + nogil
        inline void SetCornerRadius(unsigned int in_corner_radius) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil
        inline void SetSize(unsigned int* in_size) except + nogil

        void Render(float ShapeQuality) except + nogil

    cdef cppclass CPP_PixelShape:
        CPP_DisplayCoordinateFormat* ShapeCentreFormat
        CPP_ColorFormat* ColorFormat

        void Render() except + nogil

    cdef cppclass CPP_LineShape:
        CPP_ColorFormat* ColorFormat

        inline void SetRotation(float rotation) except + nogil
        inline void SetStartPosition(unsigned int* in_start_position) except + nogil
        inline void SetEndPosition(unsigned int* in_end_position) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil

        void Render(float ShapeQuality) except + nogil

    cdef cppclass CPP_PolygonShape:
        CPP_ColorFormat* ColorFormat

        inline void SetRotation(float rotation) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetPoints(unsigned int (*in_points)[2], unsigned int count) except + nogil
        inline void SetClosed(bool in_closed) except + nogil

        void Render(float ShapeQuality) except + nogil

    cdef cppclass CPP_ArcShape:
        CPP_DisplayCoordinateFormat* ShapeCentreFormat
        CPP_ColorFormat* ColorFormat

        inline void SetRotation(float rotation) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetStartAngle(float in_start_angle) except + nogil
        inline void SetEndAngle(float in_end_angle) except + nogil
        inline void SetPointCount(unsigned int in_point_count) except + nogil
        inline void SetRadius(unsigned int in_radius) except + nogil

        void Render(float ShapeQuality) except + nogil

    cdef cppclass CPP_EllipseShape:
        CPP_DisplayCoordinateFormat* ShapeCentreFormat
        CPP_ColorFormat* ColorFormat

        inline void SetPointCount(unsigned int in_point_count) except + nogil
        inline void SetWidth(unsigned int in_width) except + nogil
        inline void SetRotation(float rotation) except + nogil
        inline void SetSize(unsigned int* in_size) except + nogil

        void Render(float ShapeQuality) except + nogil

cdef class RadialPolygon:
    cdef:
        CPP_RadialPolygonShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_RadialPolygonShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    property shape_center:
        def __get__(self):
            self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

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
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_RectangleShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    property shape_center:
        def __get__(self):
            self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

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

    def set_corner_radius(self, corner_radius):
        self.cpp_class_ptr.SetCornerRadius(corner_radius)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

cdef class Pixel:
    cdef:
        CPP_PixelShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_PixelShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render()

    property shape_center:
        def __get__(self):
            self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

cdef class Line:
    cdef:
        CPP_LineShape* cpp_class_ptr
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_LineShape()

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

    def set_start(self, start_position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] start_position_np
            unsigned int* start_position_ptr

        if not isinstance(start_position, np.ndarray) or start_position.dtype != np.uint32 or not start_position.flags['C_CONTIGUOUS']:
            start_position_np = np.array(start_position, dtype=np.uint32, order='C')
        else:
            start_position_np = start_position

        start_position_ptr = <unsigned int*>&start_position_np[0]

        self.cpp_class_ptr.SetStartPosition(start_position_ptr)

    def set_end(self, end_position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] end_position_np
            unsigned int* end_position_ptr

        if not isinstance(end_position, np.ndarray) or end_position.dtype != np.uint32 or not end_position.flags['C_CONTIGUOUS']:
            end_position_np = np.array(end_position, dtype=np.uint32, order='C')
        else:
            end_position_np = end_position

        end_position_ptr = <unsigned int*>&end_position_np[0]

        self.cpp_class_ptr.SetEndPosition(end_position_ptr)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

cdef class PolygonShape:
    cdef:
        CPP_PolygonShape* cpp_class_ptr
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_PolygonShape()

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

    def set_points(self, points):
        cdef:
            np.ndarray[np.uint32_t, ndim=2, mode='c'] points_np
            unsigned int* points_ptr
            Py_ssize_t num_points

        # Ensure input is a C-contiguous NumPy array of shape (N, 2)
        if not isinstance(points, np.ndarray) or points.dtype != np.uint32 or not points.flags['C_CONTIGUOUS']:
            points_np = np.ascontiguousarray(points, dtype=np.uint32)
        else:
            points_np = points

        # Validate shape
        if points_np.ndim != 2 or points_np.shape[1] != 2:
            raise ValueError("Input array must have shape (N, 2)")

        num_points = points_np.shape[0]
        points_ptr = <unsigned int*> &points_np[0, 0]

        self.cpp_class_ptr.SetPoints(<unsigned int (*)[2]> points_ptr, num_points)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def set_closed(self, closed):
        self.cpp_class_ptr.SetClosed(closed);

cdef class Arc:
    cdef:
        CPP_ArcShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_ArcShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    property shape_center:
        def __get__(self):
            self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    def set_radius(self, radius):
        self.cpp_class_ptr.SetRadius(radius)

    def set_point_count(self, point_count):
        self.cpp_class_ptr.SetPointCount(point_count)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

    def set_start_angle(self, start_angle):
        self.cpp_class_ptr.SetStartAngle(start_angle)

    def set_end_angle(self, end_angle):
        self.cpp_class_ptr.SetEndAngle(end_angle)

cdef class Ellipse:
    cdef:
        CPP_EllipseShape* cpp_class_ptr
        DisplayCoordinate cpp_shape_center_format
        Color cpp_color_format

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_EllipseShape()

        self.cpp_shape_center_format = DisplayCoordinate()
        self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat

        self.cpp_color_format = Color()
        self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat

    def __dealloc__(self):
        del self.cpp_class_ptr

    def render(self):
        self.cpp_class_ptr.Render(0.27341772151898736)

    property shape_center:
        def __get__(self):
            self.cpp_shape_center_format.cpp_class_ptr = self.cpp_class_ptr.ShapeCentreFormat
            return self.cpp_shape_center_format

    property shape_color:
        def __get__(self):
            self.cpp_color_format.cpp_class_ptr = self.cpp_class_ptr.ColorFormat
            return self.cpp_color_format

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

    def set_point_count(self, point_count):
        self.cpp_class_ptr.SetPointCount(point_count)

    def set_width(self, width):
        self.cpp_class_ptr.SetWidth(width)

    def set_rotation(self, rotation):
        self.cpp_class_ptr.SetRotation(rotation)

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