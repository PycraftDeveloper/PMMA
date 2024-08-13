Math (``pmma.Math``)
=======
    
    🟩 **R** - A standalone class that extends the range of built-in mathematical operations to expose all of the advanced mathematical operations used within PMMA.
    This class also currently uses Numba for JIT (just-in-time) compilation (in no-python mode) as required.
    
    Required 3rd-party modules: Numba, Numpy and Pyrr.
    

Create
+++++++

..py:method:: pmma.Math() -> pmma.Math

Methods
+++++++

..py:method: Math.quit() -> None
    
    Exit function.
    

..py:method: Math.get_function_pythag() -> Callable
    
    🟩 **R** - Exposes either the raw Python pythagoras function in PMMA's utility library, or the JIT function with the same operation.
    This depends on the state of PMMA's registry entry: ``Registry.custom_compiled_behavior["raw_pythag"]``.
    For more information on this behavior, check out the Registry section, or look at the welcome page.
    
    Returns:
        Pythag function (Callable) - The requested function.
        

..py:method: Math.pythag(points: Callable[[Union[List[float], Tuple[float, ...]]], float]) -> float
    
    **R** - Calculates the pythagorean distance between two points.
    
        Arguments:
        points (Callable[[Union[List[float], Tuple[float, ...]]], float]) - A list containing two tuples, each representing a point in 3D space.
        
    Returns:
        distance (float) - The calculated pythagorean distance between the two points.
        

..py:method: Math.get_function_ranger() -> None

..py:method: Math.ranger() -> None

..py:method: Math.get_function_nparray_ranger() -> None

..py:method: Math.nparray_ranger() -> None

..py:method: Math.get_function_gl_look_at() -> None

..py:method: Math.gl_look_at() -> None

..py:method: Math.get_function_compute_position() -> None

..py:method: Math.compute_position() -> None

..py:method: Math.get_function_perspective_fov() -> None

..py:method: Math.perspective_fov() -> None

..py:method: Math.get_function_look_at() -> None

..py:method: Math.look_at() -> None

..py:method: Math.get_function_multiply() -> None

..py:method: Math.multiply() -> None

