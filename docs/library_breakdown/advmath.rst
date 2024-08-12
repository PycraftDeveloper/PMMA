Advanced-Mathematics (``pmma.Math``)
=======

Object
++++++

.. py:class:: Math

    🟩 **R** - A standalone class that extends the range of built-in mathematical operations to expose all of the advanced mathematical operations used within PMMA.
    This class also currently uses Numba for JIT (just-in-time) compilation (in no-python mode) as required.

    Required 3rd-party modules: Numba, Numpy and Pyrr.

Methods
++++++
.. py:method:: Math.get_function_pythag() -> Callable[[Union[List[float], Tuple[float, ...]]], float]:

    🟩 **R** - Exposes either the raw Python pythagoras function in PMMA's utility library, or the JIT function with the same operation.
    This depends on the state of PMMA's registry entry: ``Registry.custom_compiled_behavior["raw_pythag"]``.
    For more information on this behavior, check out the Registry section, or look at the welcome page.

.. py:method:: Math.pythag(points: Union[List[float], Tuple[float, ...]]) -> float:

    🟩 **RN** - Performs the Pythagorean Theorem over a set of points. This isn't limited to sets of a set size, so works for n-dimensions.

.. py:method:: Math.get_function_ranger() -> Callable[[float, Union[List[float], Tuple[float, ...]], Union[List[float], Tuple[float, ...]]], float]:

    🟩 **R** - Exposes the raw Python range function in PMMA's utility library.

.. py:method:: Math.ranger(value: float, old: Union[List[float], Tuple[float, ...]], new: Union[List[float], Tuple[float, ...]]) -> float:

    🟩 **R** - Allows for a value within a range to be converted to a new range through linear interpolation.

.. py:method:: Math.get_function_nparray_ranger() -> Callable[[numpy.ndarray, Union[List[float], Tuple[float, ...]], Union[List[float], Tuple[float, ...]]], numpy.ndarray]:

    🟩 **R** -

.. py:method:: Math.nparray_ranger(value: numpy.ndarray, old: Union[List[float], Tuple[float, ...]], new: Union[List[float], Tuple[float, ...]]) -> numpy.ndarray:

    🟩 **R** -

.. py:method:: Math.get_function_gl_look_at() -> Callable[[numpy.ndarray, numpy.ndarray, numpy.ndarray], numpy.ndarray]:

    🟩 **R** -

.. py:method:: Math.gl_look_at(eye: numpy.ndarray, target: numpy.ndarray, up: numpy.ndarray) -> numpy.ndarray:

    🟩 **R** -

.. py:method:: Math.get_function_compute_position() -> Callable[[numpy.ndarray, numpy.ndarray, numpy.ndarray], numpy.ndarray]:

    🟩 **R** -

.. py:method:: Math.compute_position(eye: numpy.ndarray, target: numpy.ndarray, up: numpy.ndarray) -> numpy.ndarray:

    🟩 **RN** -

.. py:method:: Math.get_function_perspective_fov() -> Callable[[float, float, float, float], numpy.ndarray]:

    🟩 **R** -

.. py:method:: Math.perspective_fov(fov: float, aspect_ratio: float, near_plane: float, far_plane: float) -> numpy.ndarray:

    🟩 **RN** -

.. py:method:: Math.get_function_look_at() -> Callable[[numpy.ndarray, numpy.ndarray, numpy.ndarray], numpy.ndarray]:

    🟩 **R** -

.. py:method:: Math.look_at(camera_position: numpy.ndarray, camera_target: numpy.ndarray, up_vector: numpy.ndarray) -> numpy.ndarray:

    🟩 **RN** -

.. py:method:: Math.get_function_multiply() -> Callable[[numpy.ndarray, numpy.ndarray], numpy.ndarray]:

    🟨 **R** -

.. py:method:: Math.multiply(a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:

    🟨 **RN** -
