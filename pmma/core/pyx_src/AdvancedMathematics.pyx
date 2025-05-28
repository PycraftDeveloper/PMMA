# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

cdef extern from "AdvancedMathematics.hpp":
    float CPP_PythagoreanDifference(const float x1, const float y1, const float x2, const float y2) nogil
    float CPP_PythagoreanDistance(const float x, const float y) nogil
    float CPP_SmoothStep(const float value) nogil
    float CPP_Ranger(const float value, const float* old_range, const float* new_range) nogil
    float CPP_ArrayRanger(float* value, const int length, const float* old_range, const float* new_range) nogil
    void CPP_ArrayNormalize(float* value) nogil
    void CPP_Cross(const float* a, const float* b, float* out) nogil
    void CPP_Subtract(const float* a, const float* b, float* out) nogil
    float CPP_Dot(const float* a, const float* b) nogil
    void CPP_LookAt(const float* eye, const float* target, const float* up, float* out) nogil
    void CPP_ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z) nogil
    void CPP_PerspectiveFOV(const float fov, const float aspect_ratio, const float near_plane, const float far_plane, float (*out)[4]) nogil

def PythagoreanDifference():
    pass

def PythagoreanDistance():
    pass

def SmoothStep():
    pass

def Ranger():
    pass

def ArrayRanger():
    pass

def ArrayNormalize():
    pass

def Cross():
    pass

def Subtract():
    pass

def Dot():
    pass

def LookAt():
    pass

def ComputePosition():
    pass

def PerspectiveFOV():
    pass