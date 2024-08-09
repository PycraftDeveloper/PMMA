from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

import pmma.python_src.utility.math_utils as math_utils

class Math:
    def __init__(self):
        Registry.pmma_object_instances[id(self)] = self
        self.shut_down = False

    def __del__(self):
        if self.shut_down is False:
            # do something
            pass

    def quit(self):
        self.__del__()
        self.shut_down = True

    def get_function_pythag(self):
        if Registry.compile_math_functions:
            if "raw_pythag" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_pythag"]:
                    return math_utils.raw_pythag
                else:
                    return math_utils.raw_pythag.py_func
            else:
                return math_utils.raw_pythag
        else:
            return math_utils.raw_pythag.py_func

    def pythag(self, points):
        return self.get_function_pythag()(points)

    def get_function_ranger(self):
        return math_utils.raw_ranger

    def ranger(self, value, old, new):
        return self.get_function_ranger()(value, old, new)

    def get_function_nparray_ranger(self):
        return math_utils.raw_nparray_ranger()

    def nparray_ranger(self, value, old, new):
        return self.get_function_nparray_ranger()(value, old, new)

    def get_function_gl_look_at(self):
        return math_utils.raw_gl_look_at

    def gl_look_at(self, eye, target, up):
        return self.get_function_gl_look_at()(eye, target, up)

    def get_function_compute_position(self):
        if Registry.compile_math_functions:
            if "raw_compute_position" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_compute_position"]:
                    return math_utils.raw_compute_position
                else:
                    return math_utils.raw_compute_position.py_func
            else:
                return math_utils.raw_compute_position
        else:
            return math_utils.raw_compute_position.py_func

    def compute_position(self, pos, target, up):
        return self.get_function_compute_position()(pos, target, up)

    def get_function_perspective_fov(self):
        if Registry.compile_math_functions:
            if "raw_perspective_fov" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_perspective_fov"]:
                    return math_utils.raw_perspective_fov
                else:
                    return math_utils.raw_perspective_fov.py_func
            else:
                return math_utils.raw_perspective_fov
        else:
            return math_utils.raw_perspective_fov.py_func

    def perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        return self.get_function_perspective_fov()(fov, aspect_ratio, near_plane, far_plane)

    def get_function_look_at(self):
        if Registry.compile_math_functions:
            if "raw_look_at" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_look_at"]:
                    return math_utils.raw_look_at
                else:
                    return math_utils.raw_look_at.py_func
            else:
                return math_utils.raw_look_at
        else:
            return math_utils.raw_look_at.py_func

    def look_at(self, camera_position, camera_target, up_vector):
        return self.get_function_look_at()(camera_position, camera_target, up_vector)

    def get_function_multiply(self):
        if Registry.compile_math_functions:
            if "raw_multiply" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_multiply"]:
                    return math_utils.raw_multiply
                else:
                    return math_utils.raw_multiply.py_func
            else:
                return math_utils.raw_multiply
        else:
            return math_utils.raw_multiply.py_func

    def multiply(self, a, b):
        return self.get_function_multiply()(a, b)
