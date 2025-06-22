# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

from libcpp.string cimport string

import os

# Declare the external C++ function
cdef extern from "PMMA_Core.hpp" namespace "CPP_General" nogil:
    void Set_PMMA_Location(string location) except + nogil
    void Set_Path_Separator(string separator) except + nogil

cdef class General:
    def __cinit__(self):
        print("Did you know you don't need to make an instance of this class in order to use it?")

    @staticmethod
    def set_pmma_location(path):
        cdef:
            string encoded_path = path.encode('utf-8')

        Set_PMMA_Location(encoded_path)

    @staticmethod
    def set_path_separator():
        cdef:
            string encoded_separator = str(os.sep).encode('utf-8')

        Set_Path_Separator(encoded_separator)
