import atexit

cdef extern from "PMMA_Core.hpp" nogil:
    cdef void PMMA_Initialize()

    cdef void PMMA_Uninitialize()

def initialize():
    PMMA_Initialize()

def uninitialize():
    PMMA_Uninitialize()

atexit.register(uninitialize)