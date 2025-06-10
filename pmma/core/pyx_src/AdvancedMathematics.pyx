# cython: boundscheck=False, wraparound=False, cdivision=True, nonecheck=False, initializedcheck=False

import numpy as np
cimport numpy as np

cdef extern from "PMMA_Core.hpp" namespace "CPP_AdvancedMathematics" nogil:
    float PythagoreanDifference(const float x1, const float y1, const float x2, const float y2) except + nogil
    float PythagoreanDistance(const float x, const float y) except + nogil
    float SmoothStep(const float value) except + nogil
    float Ranger(const float value, const float* old_range, const float* new_range) except + nogil
    void ArrayRanger(const float* value, const unsigned int length, const float* old_range, const float* new_range, float* out) except + nogil
    void ArrayNormalize(const float* value, float* out) except + nogil
    void Cross(const float* a, const float* b, float* out) except + nogil
    void Subtract(const float* a, const float* b, float* out) except + nogil
    float Dot(const float* a, const float* b) except + nogil
    void LookAt(const float* eye, const float* target, const float* up, float* out) except + nogil
    void ComputePosition(const float* position, const float* target, const float* up, float* out_x, float* out_y, float* out_z) except + nogil
    void PerspectiveFOV(const float fov, const float aspect_ratio, const float near_plane, const float far_plane, float (*out)[4]) except + nogil

cdef class AdvancedMathematics:
    def __cinit__(self):
        print("Did you know you don't need to make an instance of this class in order to use it?")

    @staticmethod
    def individual_pythagorean_difference(x1, y1, x2, y2):
        return PythagoreanDifference(x1, y1, x2, y2)

    @staticmethod
    def point_pythagorean_difference(point1, point2):
        return PythagoreanDifference(point1[0], point1[1], point2[0], point2[1])

    @staticmethod
    def individual_pythagorean_distance(x, y):
        return PythagoreanDistance(x, y)

    @staticmethod
    def point_pythagorean_distance(point):
        return PythagoreanDistance(point[0], point[1])

    @staticmethod
    def smooth_step(value):
        return SmoothStep(value)

    @staticmethod
    def ranger(value, old_range, new_range):
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

        old_ptr = &old_np[0]
        new_ptr = &new_np[0]

        return Ranger(value, old_ptr, new_ptr)

    @staticmethod
    def array_ranger(values, old_range, new_range):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] values_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] old_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] new_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np
            const float* values_ptr
            const float* old_ptr
            const float* new_ptr
            float* out_ptr

            unsigned int length

        # Convert 'values' to numpy float32 contiguous array
        if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
            values_np = np.array(values, dtype=np.float32, order='C')
        else:
            values_np = values

        length = <unsigned int>values_np.shape[0]
        values_ptr = &values_np[0]

        out_np = np.empty(length, dtype=np.float32, order='C')
        out_ptr = &out_np[0]

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

        # Call C++ function
        ArrayRanger(values_ptr, length, old_ptr, new_ptr, out_ptr)

        if isinstance(values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    @staticmethod
    def array_normalize(values):
        cdef:
            np.ndarray[np.float32_t, ndim=1, mode='c'] values_np
            np.ndarray[np.float32_t, ndim=1, mode='c'] out_np = np.empty(3, dtype=np.float32, order='C')
            const float* values_ptr
            float* out_ptr = &out_np[0]

        # Convert 'values' to numpy float32 contiguous array
        if not isinstance(values, np.ndarray) or values.dtype != np.float32 or not values.flags['C_CONTIGUOUS']:
            values_np = np.array(values, dtype=np.float32, order='C')
        else:
            values_np = values

        values_ptr = &values_np[0]

        ArrayNormalize(values_ptr, out_ptr)

        if isinstance(values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    @staticmethod
    def cross(first_values, second_values):
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

        Cross(first_values_ptr, second_values_ptr, out_ptr)

        if isinstance(first_values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    @staticmethod
    def subtract(first_values, second_values):
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

        Subtract(first_values_ptr, second_values_ptr, out_ptr)

        if isinstance(first_values, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    @staticmethod
    def dot(first_values, second_values):
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

        return Dot(first_values_ptr, second_values_ptr)

    @staticmethod
    def look_at(eye, target, up):
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

        LookAt(eye_ptr, target_ptr, up_ptr, out_ptr)

        if isinstance(eye, np.ndarray):
            return out_np
        else:
            return out_np.tolist()

    @staticmethod
    def compute_position(position, target, up):
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

        ComputePosition(position_ptr, target_ptr, up_ptr, x_out_ptr, y_out_ptr, z_out_ptr)

        if isinstance(position, np.ndarray):
            return x_out_np, y_out_np, z_out_np
        else:
            return x_out_np.tolist(), y_out_np.tolist(), z_out_np.tolist()

    @staticmethod
    def perspective_fov(FOV, aspect_ratio, near_plane, far_plane):
        cdef:
            np.ndarray[np.float32_t, ndim=2, mode='c'] out_np = np.empty((4, 4), dtype=np.float32, order='C')
            float (*out_ptr)[4]

        out_ptr = <float (*)[4]> out_np.data

        PerspectiveFOV(FOV, aspect_ratio, near_plane, far_plane, out_ptr)

        return out_np