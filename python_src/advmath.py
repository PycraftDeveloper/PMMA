from gc import collect as _gc__collect

from pmma.python_src.utility.registry_utils import Registry as _Registry
import pmma.python_src.utility.math_utils as _math_utils
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class Math:
    """
    🟩 **R** - A standalone class that extends the range of built-in mathematical operations to expose all of the advanced mathematical operations used within PMMA.
    This class also currently uses Numba for JIT (just-in-time) compilation (in no-python mode) as required.

    Required 3rd-party modules: Numba, Numpy and Pyrr.
    """
    def __init__(self):
        """
        Constructor for the Math class.
        """
        _initialize(self)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_function_smooth_step(self):
        return _math_utils.raw_smooth_step

    def smooth_step(self, value):
        return self.get_function_smooth_step()(value)

    def get_function_pythag(self):
        """
        🟩 **R** - Exposes either the raw Python pythagoras function in PMMA's utility library, or the JIT function with the same operation.
        This depends on the state of PMMA's registry entry: ``_Registry.custom_compiled_behavior["raw_pythag"]``.
        For more information on this behavior, check out the Registry section, or look at the welcome page.

        Returns:
            Pythag function (Callable) - The requested function.
        """
        if _Registry.compile_math_functions:
            if "raw_pythag" in _Registry.custom_compiled_behavior.keys():
                if _Registry.custom_compiled_behavior["raw_pythag"]:
                    return _math_utils.raw_pythag
                else:
                    return _math_utils.raw_pythag.py_func
            else:
                return _math_utils.raw_pythag
        else:
            return _math_utils.raw_pythag.py_func

    def pythag(self, points):
        """
        **R** - Calculates the pythagorean distance between two points.

        Parameters:
            points (list) - A list containing two tuples, each representing a point in 3D space.

        Returns:
            distance (float) - The calculated pythagorean distance between the two points.
        """
        return self.get_function_pythag()(points)

    def get_function_ranger(self):
        return _math_utils.raw_ranger

    def ranger(self, value, old, new):
        return self.get_function_ranger()(value, old, new)

    def get_function_nparray_ranger(self):
        return _math_utils.raw_nparray_ranger()

    def nparray_ranger(self, value, old, new):
        return self.get_function_nparray_ranger()(value, old, new)

    def get_function_gl_look_at(self):
        return _math_utils.raw_gl_look_at

    def gl_look_at(self, eye, target, up):
        return self.get_function_gl_look_at()(eye, target, up)

    def get_function_compute_position(self):
        if _Registry.compile_math_functions:
            if "raw_compute_position" in _Registry.custom_compiled_behavior.keys():
                if _Registry.custom_compiled_behavior["raw_compute_position"]:
                    return _math_utils.raw_compute_position
                else:
                    return _math_utils.raw_compute_position.py_func
            else:
                return _math_utils.raw_compute_position
        else:
            return _math_utils.raw_compute_position.py_func

    def compute_position(self, pos, target, up):
        return self.get_function_compute_position()(pos, target, up)

    def get_function_perspective_fov(self):
        if _Registry.compile_math_functions:
            if "raw_perspective_fov" in _Registry.custom_compiled_behavior.keys():
                if _Registry.custom_compiled_behavior["raw_perspective_fov"]:
                    return _math_utils.raw_perspective_fov
                else:
                    return _math_utils.raw_perspective_fov.py_func
            else:
                return _math_utils.raw_perspective_fov
        else:
            return _math_utils.raw_perspective_fov.py_func

    def perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        return self.get_function_perspective_fov()(fov, aspect_ratio, near_plane, far_plane)

    def get_function_look_at(self):
        if _Registry.compile_math_functions:
            if "raw_look_at" in _Registry.custom_compiled_behavior.keys():
                if _Registry.custom_compiled_behavior["raw_look_at"]:
                    return _math_utils.raw_look_at
                else:
                    return _math_utils.raw_look_at.py_func
            else:
                return _math_utils.raw_look_at
        else:
            return _math_utils.raw_look_at.py_func

    def look_at(self, camera_position, camera_target, up_vector):
        return self.get_function_look_at()(camera_position, camera_target, up_vector)

    def get_function_multiply(self):
        if _Registry.compile_math_functions:
            if "raw_multiply" in _Registry.custom_compiled_behavior.keys():
                if _Registry.custom_compiled_behavior["raw_multiply"]:
                    return _math_utils.raw_multiply
                else:
                    return _math_utils.raw_multiply.py_func
            else:
                return _math_utils.raw_multiply
        else:
            return _math_utils.raw_multiply.py_func

    def multiply(self, a, b):
        return self.get_function_multiply()(a, b)
