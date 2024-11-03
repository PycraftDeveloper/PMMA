from pyrr import Matrix44 as _pyrr__Matrix44
from numpy import newaxis as _numpy__newaxis
from numpy import linalg as _numpy__linalg
from numpy import cross as _numpy__cross
from numpy import array as _numpy__array
from numpy import dot as _numpy__dot
from numpy import finfo as _numpy__finfo

def raw_smooth_step(t):
    # Cubic smoothstep function for acceleration/deceleration
    return t * t * (3 - 2 * t)

def raw_ranger(value, old, new):
    if value > old[1]:
        value = old[1]
    elif value < old[0]:
        value = old[0]

    comparing_two_arrays = (old == new)
    if comparing_two_arrays.all():
        return value
    else:
        old_range = (old[1] - old[0])
        new_range = (new[1] - new[0])
        if old_range == 0:
            old_range = _numpy__finfo(float).tiny
        new_value = (((value - old[0]) * new_range) / old_range) + new[0]
        return new_value

def raw_nparray_ranger(value, old, new):
    value[value > old[1]] = old[1]
    value[value < old[0]] = old[0]

    comparing_two_arrays = (old == new)
    if comparing_two_arrays.all():
        return value
    else:
        old_range = (old[1] - old[0])
        new_range = (new[1] - new[0])
        if old_range == 0:
            old_range = _numpy__finfo(float).tiny
        new_value = (((value - old[0]) * new_range) / old_range) + new[0]
        return new_value

def raw_gl_look_at(pos, target, up):
    x, y, z = raw_compute_position(
        pos, target, up)

    translate = _pyrr__Matrix44.identity(dtype="f4")
    translate[3][0] = -pos.x
    translate[3][1] = -pos.y
    translate[3][2] = -pos.z

    rotate = _pyrr__Matrix44.identity(dtype="f4")
    rotate[0][0] = x[0]  # -- X
    rotate[1][0] = x[1]
    rotate[2][0] = x[2]
    rotate[0][1] = y[0]  # -- Y
    rotate[1][1] = y[1]
    rotate[2][1] = y[2]
    rotate[0][2] = z[0]  # -- Z
    rotate[1][2] = z[1]
    rotate[2][2] = z[2]

    return rotate * translate[:, _numpy__newaxis]

def raw_pythag(points):
    sum = 0
    for point in points:
        sum += point ** 2
    return sum ** 0.5

def raw_compute_position(pos, target, up):
    def normalize(v):
        norm = _numpy__linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    z = normalize(pos - target)
    x = normalize(_numpy__cross(normalize(up), z))
    y = _numpy__cross(z, x)
    return x, y, z

def raw_look_at(camera_position, camera_target, up_vector):
    vector = camera_target - camera_position

    x = _numpy__linalg.norm(vector)
    vector = vector / x

    vector2 = _numpy__cross(up_vector, vector)
    vector2 /= _numpy__linalg.norm(vector2)

    vector3 = _numpy__cross(vector, vector2)
    return _numpy__array([
        [vector2[0], vector3[0], vector[0], 0.0],
        [vector2[1], vector3[1], vector[1], 0.0],
        [vector2[2], vector3[2], vector[2], 0.0],
        [-_numpy__dot(vector2, camera_position), -_numpy__dot(
            vector3, camera_position), _numpy__dot(vector, camera_position), 1.0]
    ], dtype="f4")

def raw_multiply(light_proj, sun_light_look_at):
    return light_proj * sun_light_look_at