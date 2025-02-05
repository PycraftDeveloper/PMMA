# cython: language_level=3

import numpy as np
cimport numpy as cnp
from libc.math cimport sqrt

# Define the types for numpy arrays

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

# Clamping and mapping function for numpy arrays
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

# Compute the camera's orientation matrix
cpdef cnp.ndarray[double, ndim=2] raw_gl_look_at(cnp.ndarray[double, ndim=1] pos,
                                                 cnp.ndarray[double, ndim=1] target,
                                                 cnp.ndarray[double, ndim=1] up):
    """
    🟩 **R** -
    """
    cdef cnp.ndarray[double, ndim=1] x, y, z
    x, y, z = raw_compute_position(pos, target, up)

    translate = np.identity(4, dtype=np.double32)
    translate[3][0] = -pos[0]
    translate[3][1] = -pos[1]
    translate[3][2] = -pos[2]

    rotate = np.identity(4, dtype=np.double32)
    rotate[0][0] = x[0]  # -- X
    rotate[1][0] = x[1]
    rotate[2][0] = x[2]
    rotate[0][1] = y[0]  # -- Y
    rotate[1][1] = y[1]
    rotate[2][1] = y[2]
    rotate[0][2] = z[0]  # -- Z
    rotate[1][2] = z[1]
    rotate[2][2] = z[2]

    return rotate @ translate[:, np.newaxis]

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
    cdef cnp.ndarray[double, ndim=1] z = normalize(target - pos)
    cdef cnp.ndarray[double, ndim=1] x = normalize(np.cross(up, z))
    cdef cnp.ndarray[double, ndim=1] y = np.cross(z, x)
    return (x, y, z)

# Look at function
cpdef cnp.ndarray[double, ndim=2] raw_look_at(cnp.ndarray[double, ndim=1] camera_position,
                                             cnp.ndarray[double, ndim=1] camera_target,
                                             cnp.ndarray[double, ndim=1] up_vector):
    """
    🟩 **R** -
    """
    cdef cnp.ndarray[double, ndim=1] vector = camera_target - camera_position

    cdef double x = np.linalg.norm(vector)
    vector = vector / x

    cdef cnp.ndarray[double, ndim=1] vector2 = np.cross(up_vector, vector)
    vector2 /= np.linalg.norm(vector2)

    cdef cnp.ndarray[double, ndim=1] vector3 = np.cross(vector, vector2)

    return np.array([
        [vector2[0], vector3[0], vector[0], 0.0],
        [vector2[1], vector3[1], vector[1], 0.0],
        [vector2[2], vector3[2], vector[2], 0.0],
        [-np.dot(vector2, camera_position), -np.dot(vector3, camera_position), np.dot(vector, camera_position), 1.0]
    ], dtype=np.double32)

# Matrix multiplication function
cpdef cnp.ndarray[double, ndim=2] raw_multiply(cnp.ndarray[double, ndim=2] light_proj,
                                               cnp.ndarray[double, ndim=2] sun_light_look_at):
    """
    🟩 **R** -
    """
    return light_proj @ sun_light_look_at
