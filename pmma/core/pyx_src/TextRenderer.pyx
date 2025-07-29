# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_TextRenderer:
        inline void SetText(string NewText) except + nogil
        inline void SetFont(string NewFont) except + nogil

        inline void SetSize(unsigned int NewSize) except + nogil

        inline void SetForegroundColor(float* NewColor) except + nogil
        inline void SetBackgroundColor(float* NewColor) except + nogil

        inline void SetPosition(unsigned int* NewPosition) except + nogil

        void Render() except + nogil

cdef class TextRenderer:
    cdef:
        CPP_TextRenderer* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_TextRenderer()

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    def set_text(self, text):
        cdef string encoded_text = text.encode("utf-8")
        self.cpp_class_ptr.SetText(encoded_text)

    def set_font(self, font):
        cdef string encoded_font = font.encode('utf-8')
        self.cpp_class_ptr.SetFont(encoded_font)

    def set_size(self, size):
        self.cpp_class_ptr.SetSize(size)

    def set_foreground_color(self, color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] color_np
            float* color_ptr

        if not isinstance(color, np.ndarray) or color.dtype != np.float32 or not color.flags['C_CONTIGUOUS']:
            color_np = np.array(color, dtype=np.float32, order='C')
        else:
            color_np = color

        color_ptr = <float*>&color_np[0]

        self.cpp_class_ptr.SetForegroundColor(color_ptr)

    def set_background_color(self, color):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] color_np
            float* color_ptr

        if not isinstance(color, np.ndarray) or color.dtype != np.float32 or not color.flags['C_CONTIGUOUS']:
            color_np = np.array(color, dtype=np.float32, order='C')
        else:
            color_np = color

        color_ptr = <float*>&color_np[0]

        self.cpp_class_ptr.SetBackgroundColor(color_ptr)

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