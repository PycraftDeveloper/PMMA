# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_SpaceKeyEvent:
        bool GetPressed() except + nogil

cdef class SpaceKeyEvent:
    cdef:
        CPP_SpaceKeyEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_SpaceKeyEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_pressed(self):
        return self.cpp_class_ptr.GetPressed()