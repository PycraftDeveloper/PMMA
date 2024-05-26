from pmma.src.registry import Registry

import pmma.src.utility.math_utils as math_utils

class Math:
    def get_function_extrapolate2(self):
        if Registry.compile_math_functions:
            return math_utils.extrapolate2
        else:
            return math_utils.extrapolate2.py_func

    def extrapolate2(self, perm, xsb, ysb, dx, dy):
        return self.get_function_extrapolate2()(perm, xsb, ysb, dx, dy)

    def extrapolate(self, perm, xsb, dx):
        return self.get_function_extrapolate()(perm, xsb, dx)

    def get_function_extrapolate(self):
        if Registry.compile_math_functions:
            return math_utils.extrapolate
        else:
            return math_utils.extrapolate.py_func

    def get_function_overflow(self):
        return math_utils.overflow

    def pythag(self, *args):
        return math_utils.pythag(*args)

    def overflow(self, x):
        return self.function_overflow()(x)

    def get_function_ranger(self):
        return math_utils.ranger

    def ranger(self, value, old, new):
        return self.get_function_ranger()(value, old, new)

    def get_function_gl_look_at(self):
        return math_utils.gl_look_at

    def gl_look_at(self, eye, target, up):
        return self.get_function_gl_look_at()(eye, target, up)

    def get_function_compute_position(self):
        if Registry.compile_math_functions:
            return math_utils.compute_position
        else:
            return math_utils.compute_position.py_func

    def compute_position(self, pos, target, up):
        return self.get_function_compute_position()(pos, target, up)

    def get_function_perspective_fov(self):
        if Registry.compile_math_functions:
            return math_utils.perspective_fov
        else:
            return math_utils.perspective_fov.py_func

    def perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        return self.get_function_perspective_fov()(fov, aspect_ratio, near_plane, far_plane)

    def get_function_look_at(self):
        if Registry.compile_math_functions:
            return math_utils.look_at
        else:
            return math_utils.look_at.py_func

    def look_at(self, camera_position, camera_target, up_vector):
        return self.get_function_look_at()(camera_position, camera_target, up_vector)

    def get_function_multiply(self):
        if Registry.compile_math_functions:
            return math_utils.multiply
        else:
            return math_utils.multiply.py_func

    def multiply(self, a, b):
        return self.get_function_multiply()(a, b)
