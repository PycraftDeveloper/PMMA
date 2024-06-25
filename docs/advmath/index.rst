
Advanced-Mathematics (``pmma.Math``)
=======

Object
++++++

.. py:class:: Math

    🟩 A standalone class that extends the range of built-in mathematical operations to expose all of the advanced mathematical operations used within PMMA.
    This class also currently uses Numba for JIT (just-in-time) compilation (in no-python mode) as required.

    Required 3rd-party modules: Numba, Numpy and Pyrr.

Methods
++++++
.. py:method:: Math.get_function_pythag() -> Callable[[Union[List[float], Tuple[float, ...]]], float]:

    🟩 Exposes either the raw Python pythagoras function in PMMA's utility library, or the JIT function with the same operation.
    This depends on the state of PMMA's registry entry: ``Registry.custom_compiled_behavior["raw_pythag"]``.
    For more information on this behavior, check out the Registry section, or look at the welcome page.

.. py:method:: Math.pythag(points: Union[List[float], Tuple[float, ...]]) -> float:

    return float

.. py:method:: Math.get_function_ranger() -> Callable[[float, Union[List[float], Tuple[float, ...]], Union[List[float], Tuple[float, ...]]], float]:

    return function

.. py:method:: Math.ranger(value: float, old: Union[List[float], Tuple[float, ...]], new: Union[List[float], Tuple[float, ...]]) -> float

    return float

.. py:method:: Math.get_function_nparray_ranger() -> Callable[[numpy.ndarray, Union[List[float], Tuple[float, ...]], Union[List[float], Tuple[float, ...]]], numpy.ndarray]:

    return function

.. py:method:: Math.nparray_ranger(value, old, new)

    return numpy_array

.. py:method:: Math.get_function_gl_look_at

    return function

.. py:method:: Math.gl_look_at(eye, target, up)

    return /

.. py:method:: Math.get_function_compute_position

    return function

.. py:method:: Math.compute_position(pos, target, up)

    return /

.. py:method:: Math.get_function_perspective_fov

    return function

.. py:method:: Math.perspective_fov(fov, aspect_ratio, near_plane, far_plane)

    return /

.. py:method:: Math.get_function_look_at

    return function

.. py:method:: Math.look_at(camera_position, camera_target, up_vector)

    return /

.. py:method:: Math.get_function_multiply

    return function

.. py:method:: Math.multiply(a, b)

    return /
