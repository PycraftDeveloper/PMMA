# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

# Declare the external C++ function
cdef extern from "mywrapper.hpp":
    int multiply(int a, int b) nogil
    void CW()

# Python wrapper function
def py_multiply(int a, int b):
    return multiply(a, b)

def py_CW():
    return CW()
