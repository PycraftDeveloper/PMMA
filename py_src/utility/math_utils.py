from ctypes import c_int64

import math

from pmma.py_src.registry import Registry

import numba
import pyrr
import numpy

from pmma.py_src.constants import Constants

GRADIENTS2 = Constants.GRADIENTS2

@numba.njit(fastmath=True, cache=True)
def raw_hash(x):
    # A simple hash function for our purposes
    x = ((x >> 13) ^ x) * 15731
    x = (x * x * 789221 + 1376312589)
    return x & 0xFFFFFFFF

@numba.njit(fastmath=True, cache=True)
def raw_fade(t):
    # Perlin's fade function
    return t * t * t * (t * (t * 6 - 15) + 10)

@numba.njit(fastmath=True, cache=True)
def raw_lerp(a, b, t):
    # Linear interpolation
    return a + t * (b - a)

@numba.njit(fastmath=True, cache=True)
def raw_grad(hash, x):
    """Calculate gradient vector and dot product with distance vector."""
    g = hash & 15
    grad = 1 + (g & 7)  # Gradient is one of 1, 2, ..., 8
    if g & 8:
        grad = -grad  # And a random sign for the gradient
    return grad * x

@numba.njit(fastmath=True, cache=True)
def raw_fast_grad(hash, x):
    # Calculate gradient
    return (hash & 1) * 2 - 1 * x

@numba.njit(fastmath=True, cache=True)
def raw_grad2(hash, x, y):
    """Calculate the dot product of the distance and gradient vectors."""
    g = hash & 7  # There are 8 possible gradients
    if g == 0: u, v = 1, 1
    elif g == 1: u, v = -1, 1
    elif g == 2: u, v = 1, -1
    elif g == 3: u, v = -1, -1
    elif g == 4: u, v = 1, 0
    elif g == 5: u, v = -1, 0
    elif g == 6: u, v = 0, 1
    else: u, v = 0, -1
    return u * x + v * y

@numba.njit(fastmath=True, cache=True)
def raw_fast_grad2(hash, x, y):
    # Calculate gradient based on hash
    h = hash & 3
    u = x if h & 2 == 0 else -x
    v = y if h & 1 == 0 else -y
    return u + v

@numba.njit(fastmath=True, cache=True)
def raw_hash2(x, y):
    # A simple hash function for our purposes
    return (x * 73856093 ^ y * 19349663) & 0xFFFFFFFF

def raw_overflow(x):
    return c_int64(x).value

def raw_ranger(value, old, new):
    if value > old[1]:
        value = old[1]
    elif value < old[0]:
        value = old[0]

    if old == new:
        return value
    else:
        old_range = (old[1] - old[0])
        new_range = (new[1] - new[0])
        new_value = (((value - old[0]) * new_range) / old_range) + new[0]
        return new_value

def raw_gl_look_at(pos, target, up):
    x, y, z = raw_compute_position(
        pos, target, up)

    translate = pyrr.Matrix44.identity(dtype="f4")
    translate[3][0] = -pos.x
    translate[3][1] = -pos.y
    translate[3][2] = -pos.z

    rotate = pyrr.Matrix44.identity(dtype="f4")
    rotate[0][0] = x[0]  # -- X
    rotate[1][0] = x[1]
    rotate[2][0] = x[2]
    rotate[0][1] = y[0]  # -- Y
    rotate[1][1] = y[1]
    rotate[2][1] = y[2]
    rotate[0][2] = z[0]  # -- Z
    rotate[1][2] = z[1]
    rotate[2][2] = z[2]

    return rotate * translate[:, numpy.newaxis]

@numba.njit(fastmath=True, cache=True)
def raw_pythag(points):
    sum = 0
    for point in points:
        sum += point ** 2
    return sum ** 0.5

@numba.njit(fastmath=True, cache=True)
def raw_compute_position(pos, target, up):
    def normalize(v):
        norm = numpy.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    z = normalize(pos - target)
    x = normalize(numpy.cross(normalize(up), z))
    y = numpy.cross(z, x)
    return x, y, z

@numba.njit(fastmath=True, cache=True)
def raw_perspective_fov(fov, aspect_ratio, near_plane, far_plane):
    num = 1.0 / math.tan(fov / 2.0)
    num9 = num / aspect_ratio
    return numpy.array([
        [num9, 0.0, 0.0, 0.0],
        [0.0, num, 0.0, 0.0],
        [0.0, 0.0, far_plane / (near_plane - far_plane), -1.0],
        [0.0, 0.0, (near_plane * far_plane) /
            (near_plane - far_plane), 0.0]
    ], dtype="f4")

@numba.njit(fastmath=True, cache=True)
def raw_look_at(camera_position, camera_target, up_vector):
    vector = camera_target - camera_position

    x = numpy.linalg.norm(vector)
    vector = vector / x

    vector2 = numpy.cross(up_vector, vector)
    vector2 /= numpy.linalg.norm(vector2)

    vector3 = numpy.cross(vector, vector2)
    return numpy.array([
        [vector2[0], vector3[0], vector[0], 0.0],
        [vector2[1], vector3[1], vector[1], 0.0],
        [vector2[2], vector3[2], vector[2], 0.0],
        [-numpy.dot(vector2, camera_position), -numpy.dot(
            vector3, camera_position), numpy.dot(vector, camera_position), 1.0]
    ], dtype="f4")

@numba.njit(fastmath=True, cache=True)
def raw_multiply(light_proj, sun_light_look_at):
    return light_proj * sun_light_look_at