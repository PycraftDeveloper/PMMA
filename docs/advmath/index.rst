
Advanced-Mathematics (``pmma.Math``)
=======

Object
++++++

.. py:class:: Math

    🟩 A standalone class that extends the range of built-in mathematical operations to expose all of the advanced mathematical operations used within PMMA. This class also currently uses Numba for JIT (just-in-time) compilation (in no-python mode) as required. Required 3rd-party modules: Numba, Numpy and Pyrr.

Methods
++++++
def get_function_pythag
    return function

def pythag (points)
    return float

def get_function_ranger
    return function

def ranger (value, old, new)
    return float

def get_function_nparray_ranger
    return function

def nparray_ranger (value, old, new)
    return numpy_array

def get_function_gl_look_at
    return function

def gl_look_at (eye, target, up)
    return /

def get_function_compute_position
    return function

def compute_position (pos, target, up)
    return /

def get_function_perspective_fov
    return function

def perspective_fov (fov, aspect_ratio, near_plane, far_plane)
    return /

def get_function_look_at
    return function

def look_at (camera_position, camera_target, up_vector)
    return /

def get_function_multiply
    return function

def multiply (a, b)
    return /
