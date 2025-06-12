# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "PMMA_Core.hpp" nogil:
    cdef cppclass CPP_TextEvent:
        string GetText() except + nogil

        void SetEnabled(bool NewIsEnabled) except + nogil
        bool GetEnabled() except + nogil

        void ClearText() except + nogil

cdef class TextEvent:
    cdef:
        CPP_TextEvent* cpp_class_ptr

    def __cinit__(self):
        self.cpp_class_ptr = new CPP_TextEvent()

    def __dealloc__(self):
        del self.cpp_class_ptr

    def get_text(self):
        cdef string cpp_str = self.cpp_class_ptr.GetText()
        return cpp_str.c_str().decode("utf-8")

    def get_enabled(self):
        return self.cpp_class_ptr.GetEnabled()

    def set_enabled(self, value):
        self.cpp_class_ptr.SetEnabled(value)

    def clear_text(self):
        self.cpp_class_ptr.ClearText()