# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

from Logger cimport Logger

from CoreTypes cimport Color, CPP_ColorFormat, DisplayCoordinate, CPP_DisplayCoordinateFormat

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_TextRenderer:
        CPP_DisplayCoordinateFormat* Position
        CPP_ColorFormat* ForegroundColor
        CPP_ColorFormat* BackgroundColor

        inline void SetText(string NewText) except + nogil
        inline void SetFont(string NewFont) except + nogil

        inline void SetSize(unsigned int NewSize) except + nogil

        void Render() except + nogil

cdef class TextRenderer:
    cdef:
        CPP_TextRenderer* cpp_class_ptr
        DisplayCoordinate cpp_position
        Color cpp_foreground_color
        Color cpp_background_color

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_TextRenderer()

        self.cpp_position = DisplayCoordinate()
        self.cpp_position.set_pointer(self.cpp_class_ptr.Position)

        self.cpp_foreground_color = Color()
        self.cpp_foreground_color.set_pointer(self.cpp_class_ptr.ForegroundColor)

        self.cpp_background_color = Color()
        self.cpp_background_color.set_pointer(self.cpp_class_ptr.BackgroundColor)

    def __dealloc__(self):
        del self.cpp_class_ptr
        self.cpp_class_ptr = NULL

    property position:
        def __get__(self):
            return self.cpp_position

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

    def render(self):
        self.cpp_class_ptr.Render()