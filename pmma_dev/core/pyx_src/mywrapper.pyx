# Declare the external C++ function
cdef extern from "mywrapper.hpp":
    int multiply(int a, int b)
    void CW()

# Python wrapper function
def py_multiply(int a, int b):
    return multiply(a, b)

def py_CW():
    return CW()
