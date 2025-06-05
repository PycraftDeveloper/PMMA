from libcpp cimport bool
from libcpp.string cimport string

import numpy as np
cimport numpy as np

cdef extern from "Display.hpp":  # adjust namespace if needed
    cdef cppclass CPP_Display:
        CPP_Display() except + nogil

        void Create(unsigned int* NewSize, string NewCaption, string NewIcon, bool NewFullScreen, bool NewResizable, bool NewNoFrame, bool NewVsync, bool NewCentered, bool NewMaximized) except + nogil

        unsigned int GetWidth() except + nogil
        unsigned int GetHeight() except + nogil

        void GetSize(unsigned int* out) except + nogil
