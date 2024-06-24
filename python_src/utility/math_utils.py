import math

import numba
import pyrr
import numpy

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

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

def raw_nparray_ranger(value, old, new):
    value[value > old[1]] = old[1]
    value[value < old[0]] = old[0]

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