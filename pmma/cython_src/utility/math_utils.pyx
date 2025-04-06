# cython: language_level=3

import numpy as np
cimport numpy as cnp
from libc.math cimport sqrt
from libc.math cimport tan

# Cubic smoothstep function for acceleration/deceleration
cpdef double raw_smooth_step(double t):
    """
    🟩 **R** -
    """
    return t * t * (3 - 2 * t)

# Clamping and mapping function
cpdef double raw_ranger(double value, list old, list new):
    """
    🟩 **R** -
    """
    cdef double old_range, new_range, new_value

    # Ensure value is within bounds of the 'old' range
    if value > old[1]:
        value = old[1]
    elif value < old[0]:
        value = old[0]

    # Check if 'old' and 'new' lists are identical
    if old[0] == new[0] and old[1] == new[1]:
        return value

    old_range = old[1] - old[0]
    new_range = new[1] - new[0]

    if old_range == 0:
        old_range = np.finfo(float).tiny

    new_value = (((value - old[0]) * new_range) / old_range) + new[0]
    return new_value

cpdef cnp.ndarray[double, ndim=1] raw_nparray_ranger(cnp.ndarray[double, ndim=1] value, cnp.ndarray[double, ndim=1] old, cnp.ndarray[double, ndim=1] new):
    """
    🟩 **R** -
    """
    value[value > old[1]] = old[1]
    value[value < old[0]] = old[0]

    if np.array_equal(old, new):
        return value

    old_range = old[1] - old[0]
    new_range = new[1] - new[0]

    if old_range == 0:
        old_range = np.finfo(float).tiny

    new_value = (((value - old[0]) * new_range) / old_range) + new[0]
    return new_value

cpdef cnp.ndarray[double, ndim=2] raw_look_at(cnp.ndarray[double, ndim=1] camera_pos,
               cnp.ndarray[double, ndim=1] target,
               cnp.ndarray[double, ndim=1] up):
    """
    🟩 **R** -
    """
    cdef double[:] f = camera_pos - target
    cdef double norm = sqrt(f[0]**2 + f[1]**2 + f[2]**2)
    f[0] /= norm
    f[1] /= norm
    f[2] /= norm

    cdef double[:] s = np.cross(up, f)
    norm = sqrt(s[0]**2 + s[1]**2 + s[2]**2)
    s[0] /= norm
    s[1] /= norm
    s[2] /= norm

    cdef double[:] u = np.cross(f, s)

    cdef cnp.ndarray[double, ndim=2] mat = np.identity(4, dtype=np.double)

    mat[0, 0] = s[0]; mat[0, 1] = s[1]; mat[0, 2] = s[2]; mat[0, 3] = -s[0]*camera_pos[0] - s[1]*camera_pos[1] - s[2]*camera_pos[2]
    mat[1, 0] = u[0]; mat[1, 1] = u[1]; mat[1, 2] = u[2]; mat[1, 3] = -u[0]*camera_pos[0] - u[1]*camera_pos[1] - u[2]*camera_pos[2]
    mat[2, 0] = f[0]; mat[2, 1] = f[1]; mat[2, 2] = f[2]; mat[2, 3] = -f[0]*camera_pos[0] - f[1]*camera_pos[1] - f[2]*camera_pos[2]

    return mat

# Compute the norm and direction
cpdef double raw_pythag(cnp.ndarray[double, ndim=1] points):
    """
    🟩 **R** -
    """
    cdef double sum = 0
    for point in points:
        sum += point ** 2
    return sqrt(sum)

# Function to normalize a vector
cdef inline cnp.ndarray[double, ndim=1] normalize(cnp.ndarray[double, ndim=1] v):
    """
    🟩 **R** -
    """
    cdef double norm = sqrt(np.dot(v, v))  # Compute the norm manually
    if norm == 0:
        return v
    return v / norm

# Function to compute the camera's basis vectors
cpdef tuple raw_compute_position(cnp.ndarray[double, ndim=1] pos,
                                cnp.ndarray[double, ndim=1] target,
                                cnp.ndarray[double, ndim=1] up):
    """
    🟩 **R** -
    """
    cdef cnp.ndarray[double, ndim=1] z = normalize(pos - target)
    cdef cnp.ndarray[double, ndim=1] x = normalize(np.cross(up, z))
    cdef cnp.ndarray[double, ndim=1] y = np.cross(z, x)
    return (x, y, z)

# Matrix multiplication function
cpdef cnp.ndarray[double, ndim=2] raw_multiply(cnp.ndarray[double, ndim=2] light_proj,
                                            cnp.ndarray[double, ndim=2] sun_light_look_at):
    """
    🟩 **R** -
    """
    return light_proj @ sun_light_look_at

cpdef cnp.ndarray[double, ndim=2] raw_perspective_fov(double fov, double aspect_ratio, double near_plane, double far_plane):
    """
    🟩 **R** -
    """

    cdef double f = 1.0 / tan(fov * 0.5)
    cdef double nf = 1.0 / (near_plane - far_plane)

    # Create a 4x4 matrix using NumPy
    cdef cnp.ndarray[cnp.double_t, ndim=2] mat = np.zeros((4, 4), dtype=np.double)

    mat[0, 0] = f / aspect_ratio
    mat[0, 1] = mat[0, 2] = mat[0, 3] = 0.0

    mat[1, 0] = 0.0
    mat[1, 1] = f
    mat[1, 2] = mat[1, 3] = 0.0

    mat[2, 0] = mat[2, 1] = 0.0
    mat[2, 2] = (far_plane + near_plane) * nf
    mat[2, 3] = (2.0 * far_plane * near_plane) * nf

    mat[3, 0] = mat[3, 1] = 0.0
    mat[3, 2] = -1.0
    mat[3, 3] = 0.0

    return mat