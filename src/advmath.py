from pmma.src.registry import Registry

import pmma.src.utility.math_utils as math_utils

class Math:
    def get_function_linear_interpolation(self):
        if Registry.compile_math_functions and ("linear_interpolation" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["linear_interpolation"]):
            return math_utils.linear_interpolation
        else:
            return math_utils.linear_interpolation.py_func

    def linear_interpolation(self, a, b, x):
        return self.get_function_linear_interpolation()(a, b, x)

    def get_function_cosine_interpolation(self):
        if Registry.compile_math_functions and ("cosine_interpolation" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["cosine_interpolation"]):
            return math_utils.cosine_interpolation
        else:
            return math_utils.cosine_interpolation.py_func

    def cosine_interpolation(self, a, b, x):
        return self.get_function_cosine_interpolation()(a, b, x)

    def get_function_cubic_interpolation(self):
        if Registry.compile_math_functions and ("cubic_interpolation" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["cubic_interpolation"]):
            return math_utils.cubic_interpolation
        else:
            return math_utils.cubic_interpolation.py_func

    def cubic_interpolation(self, a, b, c, d, x):
        return self.get_function_cubic_interpolation()(a, b, c, d, x)

    def get_function_fade(self):
        if Registry.compile_math_functions and ("fade" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["fade"]):
            return math_utils.fade
        else:
            return math_utils.fade.py_func

    def fade(self, t):
        return self.get_function_fade()(t)

    def get_function_extrapolate2(self):
        if Registry.compile_math_functions and ("extrapolate2" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["extrapolate2"]):
            return math_utils.extrapolate2
        else:
            return math_utils.extrapolate2.py_func

    def extrapolate2(self, perm, xsb, ysb, dx, dy):
        return self.get_function_extrapolate2()(perm, xsb, ysb, dx, dy)

    def get_function_overflow(self):
        return math_utils.overflow

    def get_function_pythag(self):
        if Registry.compile_math_functions and ("pythag" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["pythag"]):
            return math_utils.pythag
        else:
            return math_utils.pythag.py_func

    def pythag(self, points):
        return self.get_function_pythag()(points)

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
        if Registry.compile_math_functions and ("compute_position" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["compute_position"]):
            return math_utils.compute_position
        else:
            return math_utils.compute_position.py_func

    def compute_position(self, pos, target, up):
        return self.get_function_compute_position()(pos, target, up)

    def get_function_perspective_fov(self):
        if Registry.compile_math_functions and ("perspective_fov" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["perspective_fov"]):
            return math_utils.perspective_fov
        else:
            return math_utils.perspective_fov.py_func

    def perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        return self.get_function_perspective_fov()(fov, aspect_ratio, near_plane, far_plane)

    def get_function_look_at(self):
        if Registry.compile_math_functions and ("look_at" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["look_at"]):
            return math_utils.look_at
        else:
            return math_utils.look_at.py_func

    def look_at(self, camera_position, camera_target, up_vector):
        return self.get_function_look_at()(camera_position, camera_target, up_vector)

    def get_function_multiply(self):
        if Registry.compile_math_functions and ("multiply" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["multiply"]):
            return math_utils.multiply
        else:
            return math_utils.multiply.py_func

    def multiply(self, a, b):
        return self.get_function_multiply()(a, b)
