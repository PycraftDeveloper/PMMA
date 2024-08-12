
Math (``pmma.Math``)
=======

Object
++++++
.. py:class:: Math

    🟩 **R** - A standalone class that extends the range of built-in mathematical operations to expose all of the advanced mathematical operations used within PMMA.
    This class also currently uses Numba for JIT (just-in-time) compilation (in no-python mode) as required.
    
    Required 3rd-party modules: Numba, Numpy and Pyrr.
  
Methods
++++++
.. py:method:: Math.quit() -> NYD:

.. py:method:: Math.get_function_pythag() -> NYD:

    🟩 **R** - Exposes either the raw Python pythagoras function in PMMA's utility library, or the JIT function with the same operation.
    This depends on the state of PMMA's registry entry: ``Registry.custom_compiled_behavior["raw_pythag"]``.
    For more information on this behavior, check out the Registry section, or look at the welcome page.
  
.. py:method:: Math.pythag(points) -> NYD:

.. py:method:: Math.get_function_ranger() -> NYD:

.. py:method:: Math.ranger(value, old, new) -> NYD:

.. py:method:: Math.get_function_nparray_ranger() -> NYD:

.. py:method:: Math.nparray_ranger(value, old, new) -> NYD:

.. py:method:: Math.get_function_gl_look_at() -> NYD:

.. py:method:: Math.gl_look_at(eye, target, up) -> NYD:

.. py:method:: Math.get_function_compute_position() -> NYD:

.. py:method:: Math.compute_position(pos, target, up) -> NYD:

.. py:method:: Math.get_function_perspective_fov() -> NYD:

.. py:method:: Math.perspective_fov(fov, aspect_ratio, near_plane, far_plane) -> NYD:

.. py:method:: Math.get_function_look_at() -> NYD:

.. py:method:: Math.look_at(camera_position, camera_target, up_vector) -> NYD:

.. py:method:: Math.get_function_multiply() -> NYD:

.. py:method:: Math.multiply(a, b) -> NYD:
