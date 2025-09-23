# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

import numpy as np
cimport numpy as np

from Logger cimport Logger

from NumberFormats cimport Color, CPP_ColorFormat, DisplayCoordinate, CPP_DisplayCoordinateFormat

np.import_array()

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_TextRenderer:
        CPP_ColorFormat* ForegroundColor
        CPP_ColorFormat* BackgroundColor

        inline void SetText(string NewText) except + nogil
        inline void SetFont(string NewFont) except + nogil

        inline void SetSize(unsigned int NewSize) except + nogil

        inline void SetPosition(unsigned int* NewPosition) except + nogil

        void Render() except + nogil

cdef class TextRenderer:
    cdef:
        CPP_TextRenderer* cpp_class_ptr
        Logger logger
        Color cpp_foreground_color
        Color cpp_background_color

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_TextRenderer()
        self.logger = Logger()

        self.logger.internal_log_debug(
            29,
            (
                "The TextRenderer API is currently still in development "
                "and is likely to change as we continue to refine this "
                "area of the API in PMMA 5.1."),
            False
        )

        self.cpp_foreground_color = Color()
        self.cpp_foreground_color.set_pointer(self.cpp_class_ptr.ForegroundColor)

        self.cpp_background_color = Color()
        self.cpp_background_color.set_pointer(self.cpp_class_ptr.BackgroundColor)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    property foreground_color:
        def __get__(self):
            return self.cpp_foreground_color

    property background_color:
        def __get__(self):
            return self.cpp_background_color

    def set_text(self, text):
        cdef string encoded_text = text.encode("utf-8")
        self.cpp_class_ptr.SetText(encoded_text)

    def set_font(self, font):
        cdef string encoded_font = font.encode('utf-8')
        self.cpp_class_ptr.SetFont(encoded_font)

    def set_size(self, size):
        self.cpp_class_ptr.SetSize(size)

    def set_position(self, position):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] position_np
            unsigned int* position_ptr

        if not isinstance(position, np.ndarray) or position.dtype != np.uint32 or not position.flags['C_CONTIGUOUS']:
            position_np = np.array(position, dtype=np.uint32, order='C')
        else:
            position_np = position

        position_ptr = <unsigned int*>&position_np[0]

        self.cpp_class_ptr.SetPosition(position_ptr)

    def render(self):
        self.cpp_class_ptr.Render()