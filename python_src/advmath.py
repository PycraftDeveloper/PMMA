from gc import collect as _gc__collect
import importlib as _importlib

from numpy import array as _numpy__array
from numpy import float64 as _numpy__float64

from pmma.python_src.utility.registry_utils import Registry as _Registry
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

        if _Registry.cython_acceleration_available:
            self._math_module = _importlib.import_module(
                "pmma.bin.math_utils")

        else:
            self._math_module = _importlib.import_module(
                "pmma.python_src.pyx_alternatives.utility.math_utils")

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def get_function_smooth_step(self):
        return self._math_module.raw_smooth_step

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
        return self._math_module.raw_pythag

    def pythag(self, points):
        """
        **R** - Calculates the pythagorean distance between two points.

        Parameters:
            points (list) - A list containing two tuples, each representing a point in 3D space.

        Returns:
            distance (float) - The calculated pythagorean distance between the two points.
        """
        if type(points) in [list, tuple]:
            points = _numpy__array(points, dtype=_numpy__float64)
        return self.get_function_pythag()(points)

    def get_function_ranger(self):
        return self._math_module.raw_ranger

    def ranger(self, value, old, new):
        return self.get_function_ranger()(value, old, new)

    def get_function_nparray_ranger(self):
        return self._math_module.raw_nparray_ranger

    def nparray_ranger(self, value, old, new):
        return self.get_function_nparray_ranger()(value, old, new)

    def get_function_gl_look_at(self):
        return self._math_module.raw_gl_look_at

    def gl_look_at(self, eye, target, up):
        return self.get_function_gl_look_at()(eye, target, up)

    def get_function_compute_position(self):
        return self._math_module.raw_compute_position

    def compute_position(self, pos, target, up):
        return self.get_function_compute_position()(pos, target, up)

    def get_function_perspective_fov(self):
        return self._math_module.raw_perspective_fov

    def perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        return self.get_function_perspective_fov()(fov, aspect_ratio, near_plane, far_plane)

    def get_function_look_at(self):
        return self._math_module.raw_look_at

    def look_at(self, camera_position, camera_target, up_vector):
        return self.get_function_look_at()(camera_position, camera_target, up_vector)

    def get_function_multiply(self):
        return self._math_module.raw_multiply

    def multiply(self, a, b):
        return self.get_function_multiply()(a, b)
