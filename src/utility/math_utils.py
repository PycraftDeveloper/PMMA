from ctypes import c_int64

import math

from pmma.src.registry import Registry

import numba
import pyrr
import numpy

from pmma.src.constants import Constants

GRADIENTS2 = Constants.GRADIENTS2

@numba.njit(fastmath=True, cache=True)
def raw_linear_interpolation(a, b, x):
    return a + x * (b - a)

@numba.njit(fastmath=True, cache=True)
def raw_cosine_interpolation(a, b, x):
    x2 = (1 - math.cos(x * math.pi)) / 2
    return a * (1 - x2) + b * x2

@numba.njit(fastmath=True, cache=True)
def raw_cubic_interpolation(v0, v1, v2, v3, x):
    p = (v3 - v2) - (v0 - v1)
    q = (v0 - v1) - p
    r = v2 - v0
    s = v1
    return p * x**3 + q * x**2 + r * x + s

@numba.njit(fastmath=True, cache=True)
def raw_fade(x):
    # useful only for linear interpolation
    return (6 * x**5) - (15 * x**4) + (10 * x**3)

@numba.njit(fastmath=True, cache=True)
def raw_extrapolate2(perm, xsb, ysb, dx, dy):
    index = perm[(perm[xsb & 0xFF] + ysb) & 0xFF] & 0x0E
    g1, g2 = GRADIENTS2[index : index + 2]
    return g1 * dx + g2 * dy

def raw_overflow(x):
    return c_int64(x).value

def raw_ranger(value, old, new):
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