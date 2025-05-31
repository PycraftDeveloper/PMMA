# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

# Declare the external C++ function
cdef extern from "Display.hpp":
    void CW() nogil

def py_CW():
    return CW()
