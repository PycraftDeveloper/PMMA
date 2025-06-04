# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

import numpy as np
cimport numpy as np

# Declare the external C++ function
cdef extern from "libshared.h":
    cdef cppclass CPP_Display:
        CPP_Display() except + nogil

        void hello()

        void Create(unsigned int* NewSize, string NewCaption, string NewIcon, bool NewFullScreen, bool NewResizable, bool NewNoFrame, bool NewVsync, bool NewCentered, bool NewMaximized) except + nogil

        unsigned int GetWidth() except + nogil
        unsigned int GetHeight() except + nogil

        void GetSize(unsigned int* out) except + nogil

    CPP_Display* get_display_instance()
    void set_display_instance(CPP_Display*)

cdef class Display:
    cdef:
        CPP_Display* cpp_class_ptr
        bool using_numpy_arrays

    def __cinit__(self):
        cdef:
            CPP_Display* existing_instance

        self.cpp_class_ptr = new CPP_Display()

        existing_instance = get_display_instance()
        del existing_instance
        set_display_instance(self.cpp_class_ptr)

        self.using_numpy_arrays = False

    def __dealloc__(self):
        set_display_instance(NULL)

        del self.cpp_class_ptr

    def create(self, size=np.array([0, 0], dtype=np.uint32, order='C'), caption="PMMA Display", fullscreen=True, resizable=False, no_frame=False, vsync=True, icon="", centered=True, maximized=False):
        cdef:
            np.ndarray[np.uint32_t, ndim=1, mode='c'] size_np
            string encoded_caption = caption.encode('utf-8')
            string encoded_icon = icon.encode('utf-8')
            unsigned int* size_ptr


        if not isinstance(size, np.ndarray) or size.dtype != np.uint32 or not size.flags['C_CONTIGUOUS']:
            size_np = np.array(size, dtype=np.uint32, order='C')
            self.using_numpy_arrays = True
        else:
            size_np = size
            self.using_numpy_arrays = False

        size_ptr = <unsigned int*>&size_np[0]

        self.cpp_class_ptr.Create(size_ptr, encoded_caption, encoded_icon, fullscreen, resizable, no_frame, vsync, centered, maximized)

    def get_width(self):
        return self.cpp_class_ptr.GetWidth()

    def get_height(self):
        return self.cpp_class_ptr.GetHeight()

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
