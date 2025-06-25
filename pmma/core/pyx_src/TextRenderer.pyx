# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

import numpy as np
cimport numpy as np

import pmma.core.py_src.Utility as Utility

cdef extern from "PMMA_Core.hpp":
    cdef cppclass CPP_TextRenderer:
        CPP_TextRenderer(string& font_path, int font_height) except +

        void begin() except +
        void end() except +
        void drawText(string& text, float* pos, float scale, float* color) except +

cdef class TextRenderer:
    cdef:
        CPP_TextRenderer* cpp_class_ptr

    def __cinit__(self, font_path, font_height):
        cdef:
            string encoded_font_path = font_path.encode('utf-8')
        self.cpp_class_ptr = new CPP_TextRenderer(encoded_font_path, font_height)

    def __dealloc__(self):
        del self.cpp_class_ptr

    @Utility.require_render_thread
    def begin(self):
        self.cpp_class_ptr.begin()

    @Utility.require_render_thread
    def end(self):
        self.cpp_class_ptr.end()

    @Utility.require_render_thread
    def drawText(self, text, pos, scale, color):
        cdef:
            string encoded_text = text.encode('utf-8')

            np.ndarray[np.float32_t, ndim=1, mode='c'] position_np
            float* pos_ptr

            np.ndarray[np.float32_t, ndim=1, mode='c'] color_np
            float* color_ptr

        if not isinstance(pos, np.ndarray) or pos.dtype != np.float32 or not pos.flags['C_CONTIGUOUS']:
            position_np = np.array(pos, dtype=np.float32, order='C')
        else:
            position_np = pos

        pos_ptr = <float*>&position_np[0]

        if not isinstance(color, np.ndarray) or color.dtype != np.float32 or not color.flags['C_CONTIGUOUS']:
            color_np = np.array(color, dtype=np.float32, order='C')
        else:
            color_np = color

        color_ptr = <float*>&color_np[0]

        self.cpp_class_ptr.drawText(encoded_text, pos_ptr, scale, color_ptr)