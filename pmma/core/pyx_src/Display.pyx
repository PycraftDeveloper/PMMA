# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

import numpy as np
cimport numpy as np

# Declare the external C++ function
cdef extern from "Display.hpp":
    cdef cppclass CPP_Display:
        CPP_Display() except + nogil

        void Create(unsigned int* Size, char* Caption) except + nogil

        unsigned int GetWidth() except + nogil
        unsigned int GetHeight() except + nogil


cdef class Display:
    cdef CPP_Display* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_Display()

    def __dealloc__(self):
        #self.cpp_class_ptr.Destructor()
        del self.cpp_class_ptr # shouldn't this call the CPP_Display destructor?

    def create(self, size, caption="PMMA Display"):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            bytes caption_bytes = caption.encode('utf-8')
            char* caption_ptr = caption_bytes
            unsigned int* size_ptr

        if not isinstance(size, np.ndarray) or size.dtype != np.uint32 or not size.flags['C_CONTIGUOUS']:
            size_np = np.array(size, dtype=np.uint32, order='C')
        else:
            size_np = size

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.Create(size_ptr, caption_ptr)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def get_height(self):
        return self.cpp_class_ptr.GetHeight()