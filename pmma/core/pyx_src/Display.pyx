# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

# Declare the external C++ function
cdef extern from "Display.hpp":
    cdef cppclass CPP_Display:
        CPP_Display() except + nogil

        void Create(unsigned int Width, unsigned int Height) except + nogil

        unsigned int GetWidth() except + nogil
        unsigned int GetHeight() except + nogil


cdef class Display:
    cdef CPP_Display* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Display()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def Create(self, Width, Height):
        self.cpp_class_ptr.Create(Width, Height)

    def GetWidth(self):
        return self.cpp_class_ptr.GetWidth()

    def GetHeight(self):
        return self.cpp_class_ptr.GetHeight()