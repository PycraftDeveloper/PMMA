# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

import numpy as np
cimport numpy as np
from libc.stdlib cimport malloc, free

cdef extern from "AdvancedMathematics.hpp":
    float CPP_PythagoreanDifference(const float x1, const float y1, const float x2, const float y2) nogil
    float CPP_PythagoreanDistance(const float x, const float y) nogil
    float CPP_SmoothStep(const float value) nogil
    float CPP_Ranger(const float value, const float* old_range, const float* new_range) nogil
    void CPP_ArrayRanger(float* value, const int length, const float* old_range, const float* new_range) nogil
    void CPP_ArrayNormalize(float* value) nogil
    void CPP_Cross(const float* a, const float* b, float* out) nogil
    void CPP_Subtract(const float* a, const float* b, float* out) nogil
    float CPP_Dot(const float* a, const float* b) nogil
    void CPP_LookAt(const float* eye, const float* target, const float* up, float* out) nogil
    void CPP_ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z) nogil
    void CPP_PerspectiveFOV(const float fov, const float aspect_ratio, const float near_plane, const float far_plane, float (*out)[4]) nogil

def IndividualPythagoreanDifference(x1, y1, x2, y2):
    return CPP_PythagoreanDifference(x1, y1, x2, y2)

def PointPythagoreanDifference(point1, point2):
    return CPP_PythagoreanDifference(point1[0], point1[1], point2[0], point2[1])

def IndividualPythagoreanDistance(x, y):
    return CPP_PythagoreanDistance(x, y)

def PointPythagoreanDistance(point):
    return CPP_PythagoreanDistance(point[0], point[1])

def SmoothStep(value):
    return CPP_SmoothStep(value)

def Ranger(float value, old_range, new_range):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] old_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] new_np
        const float* old_ptr
        const float* new_ptr

    # Convert old_range to contiguous numpy array of float32 if not already
    if not isinstance(old_range, np.ndarray) or old_range.dtype != np.float32 or not old_range.flags['C_CONTIGUOUS']:
        old_np = np.array(old_range, dtype=np.float32, order='C')
    else:
        old_np = old_range

    # Same for new_range
    if not isinstance(new_range, np.ndarray) or new_range.dtype != np.float32 or not new_range.flags['C_CONTIGUOUS']:
        new_np = np.array(new_range, dtype=np.float32, order='C')
    else:
        new_np = new_range

    old_ptr = <const float*> &old_np[0]
    new_ptr = <const float*> &new_np[0]

    return CPP_Ranger(value, old_ptr, new_ptr)

def ArrayRanger(values, old_range, new_range):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] values_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] old_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] new_np
        float* values_ptr
        const float* old_ptr
        const float* new_ptr
        int length

    # Convert 'values' to numpy float32 contiguous array
    if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
        values_np = np.array(values, dtype=np.float32, order='C')
    else:
        values_np = values

    length = values_np.shape[0]
    values_ptr = &values_np[0]

    # Convert old_range and new_range as before
    if not isinstance(old_range, np.ndarray) or old_range.dtype != np.float32 or not old_range.flags['C_CONTIGUOUS']:
        old_np = np.array(old_range, dtype=np.float32, order='C')
    else:
        old_np = old_range

    if not isinstance(new_range, np.ndarray) or new_range.dtype != np.float32 or not new_range.flags['C_CONTIGUOUS']:
        new_np = np.array(new_range, dtype=np.float32, order='C')
    else:
        new_np = new_range

    old_ptr = &old_np[0]
    new_ptr = &new_np[0]

    # Call C++ function, modifies values_np in place
    CPP_ArrayRanger(values_ptr, length, old_ptr, new_ptr)

    # If input was a numpy array, it's modified in place already.
    # If input was a list, we return the new numpy array with modifications.
    if isinstance(values, np.ndarray):
        return values_np
    else:
        return values_np.tolist()

def ArrayNormalize(values):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] values_np
        float* values_ptr

    # Convert 'values' to numpy float32 contiguous array
    if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
        values_np = np.array(values, dtype=np.float32, order='C')
    else:
        values_np = values

    values_ptr = &values_np[0]

    CPP_ArrayNormalize(values_ptr)

    if isinstance(values, np.ndarray):
        return values_np
    else:
        return values_np.tolist()

def Cross(first_values, second_values):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] first_values_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] second_values_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] out_np = np.empty(3, dtype=np.float32, order='C')
        const float* first_values_ptr
        const float* second_values_ptr
        float* out_ptr = &out_np[0]

    if not isinstance(first_values, np.ndarray) or first_values.dtype != np.float32 or not first_values.flags['C_CONTIGUOUS']:
        first_values_np = np.array(first_values, dtype=np.float32, order='C')
    else:
        first_values_np = first_values

    if not isinstance(second_values, np.ndarray) or second_values.dtype != np.float32 or not second_values.flags['C_CONTIGUOUS']:
        second_values_np = np.array(second_values, dtype=np.float32, order='C')
    else:
        second_values_np = second_values

    first_values_ptr = &first_values_np[0]
    second_values_ptr = &second_values_np[0]

    CPP_Cross(first_values_ptr, second_values_ptr, out_ptr)

    if isinstance(first_values, np.ndarray):
        return out_np
    else:
        return out_np.tolist()

def Subtract(first_values, second_values):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] first_values_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] second_values_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] out_np = np.empty(3, dtype=np.float32, order='C')
        const float* first_values_ptr
        const float* second_values_ptr
        float* out_ptr = &out_np[0]

    if not isinstance(first_values, np.ndarray) or first_values.dtype != np.float32 or not first_values.flags['C_CONTIGUOUS']:
        first_values_np = np.array(first_values, dtype=np.float32, order='C')
    else:
        first_values_np = first_values

    if not isinstance(second_values, np.ndarray) or second_values.dtype != np.float32 or not second_values.flags['C_CONTIGUOUS']:
        second_values_np = np.array(second_values, dtype=np.float32, order='C')
    else:
        second_values_np = second_values

    first_values_ptr = &first_values_np[0]
    second_values_ptr = &second_values_np[0]

    CPP_Subtract(first_values_ptr, second_values_ptr, out_ptr)

    if isinstance(first_values, np.ndarray):
        return out_np
    else:
        return out_np.tolist()

def Dot(first_values, second_values):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] first_values_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] second_values_np
        const float* first_values_ptr
        const float* second_values_ptr

    if not isinstance(first_values, np.ndarray) or first_values.dtype != np.float32 or not first_values.flags['C_CONTIGUOUS']:
        first_values_np = np.array(first_values, dtype=np.float32, order='C')
    else:
        first_values_np = first_values

    if not isinstance(second_values, np.ndarray) or second_values.dtype != np.float32 or not second_values.flags['C_CONTIGUOUS']:
        second_values_np = np.array(second_values, dtype=np.float32, order='C')
    else:
        second_values_np = second_values

    first_values_ptr = &first_values_np[0]
    second_values_ptr = &second_values_np[0]

    return CPP_Dot(first_values_ptr, second_values_ptr)

def LookAt(eye, target, up):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] eye_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] target_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] up_np
        np.ndarray[np.float32_t, ndim=2, mode='c'] out_np = np.empty((4, 4), dtype=np.float32, order='C')
        const float* eye_ptr
        const float* target_ptr
        const float* up_ptr
        float* out_ptr = <float*> out_np.data

    if not isinstance(eye, np.ndarray) or eye.dtype != np.float32 or not eye.flags['C_CONTIGUOUS']:
        eye_np = np.array(eye, dtype=np.float32, order='C')
    else:
        eye_np = eye

    if not isinstance(target, np.ndarray) or target.dtype != np.float32 or not target.flags['C_CONTIGUOUS']:
        target_np = np.array(target, dtype=np.float32, order='C')
    else:
        target_np = target

    if not isinstance(up, np.ndarray) or up.dtype != np.float32 or not up.flags['C_CONTIGUOUS']:
        up_np = np.array(up, dtype=np.float32, order='C')
    else:
        up_np = up

    eye_ptr = &eye_np[0]
    target_ptr = &target_np[0]
    up_ptr = &up_np[0]

    CPP_LookAt(eye_ptr, target_ptr, up_ptr, out_ptr)

    if isinstance(eye, np.ndarray):
        return out_np
    else:
        return out_np.tolist()

def ComputePosition(position, target, up):
    cdef:
        np.ndarray[np.float32_t, ndim=1, mode='c'] position_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] target_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] up_np
        np.ndarray[np.float32_t, ndim=1, mode='c'] x_out_np = np.empty(3, dtype=np.float32, order='C')
        np.ndarray[np.float32_t, ndim=1, mode='c'] y_out_np = np.empty(3, dtype=np.float32, order='C')
        np.ndarray[np.float32_t, ndim=1, mode='c'] z_out_np = np.empty(3, dtype=np.float32, order='C')
        const float* position_ptr
        const float* target_ptr
        const float* up_ptr
        float* x_out_ptr = &x_out_np[0]
        float* y_out_ptr = &y_out_np[0]
        float* z_out_ptr = &z_out_np[0]

    if not isinstance(position, np.ndarray) or position.dtype != np.float32 or not position.flags['C_CONTIGUOUS']:
        position_np = np.array(position, dtype=np.float32, order='C')
    else:
        position_np = position

    if not isinstance(target, np.ndarray) or target.dtype != np.float32 or not target.flags['C_CONTIGUOUS']:
        target_np = np.array(target, dtype=np.float32, order='C')
    else:
        target_np = target

    if not isinstance(up, np.ndarray) or up.dtype != np.float32 or not up.flags['C_CONTIGUOUS']:
        up_np = np.array(up, dtype=np.float32, order='C')
    else:
        up_np = up

    position_ptr = &position_np[0]
    target_ptr = &target_np[0]
    up_ptr = &up_np[0]

    CPP_ComputePosition(position_ptr, target_ptr, up_ptr, x_out_ptr, y_out_ptr, z_out_ptr)

    if isinstance(position, np.ndarray):
        return x_out_np, y_out_np, z_out_np
    else:
        return x_out_np.tolist(), y_out_np.tolist(), z_out_np.tolist()

def PerspectiveFOV(FOV, aspect_ratio, near_plane, far_plane):
    cdef:
        np.ndarray[np.float32_t, ndim=2, mode='c'] out_np = np.empty((4, 4), dtype=np.float32, order='C')
        float (*out_ptr)[4]

    out_ptr = <float (*)[4]> out_np.data

    CPP_PerspectiveFOV(FOV, aspect_ratio, near_plane, far_plane, out_ptr)

    return out_np