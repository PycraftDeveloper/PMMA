from pmma.src.registry import Registry

import pmma.src.utility.math_utils as math_utils

class Math:
    def get_function_hash(self):
        if Registry.compile_math_functions and ("hash" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["hash"]):
            return math_utils.hash
        else:
            return math_utils.hash.py_func

    def hash(self, x):
        return self.get_function_hash()(x)

    def get_function_fade(self):
        if Registry.compile_math_functions and ("fade" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["fade"]):
            return math_utils.fade
        else:
            return math_utils.fade.py_func

    def fade(self, x):
        return self.get_function_fade()(x)

    def get_function_lerp(self):
        if Registry.compile_math_functions and ("lerp" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["lerp"]):
            return math_utils.lerp
        else:
            return math_utils.lerp.py_func

    def lerp(self, a, b, x):
        return self.get_function_lerp()(a, b, x)

    def get_function_grad(self):
        if Registry.compile_math_functions and ("grad" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["grad"]):
            return math_utils.grad
        else:
            return math_utils.grad.py_func

    def grad(self, hash, x):
        return self.get_function_grad()(hash, x)

    def get_function_extrapolate2(self):
        if Registry.compile_math_functions and ("extrapolate2" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["extrapolate2"]):
            return math_utils.raw_extrapolate2
        else:
            return math_utils.raw_extrapolate2.py_func

    def extrapolate2(self, perm, xsb, ysb, dx, dy):
        return self.get_function_extrapolate2()(perm, xsb, ysb, dx, dy)

    def get_function_overflow(self):
        return math_utils.raw_overflow

    def get_function_pythag(self):
        if Registry.compile_math_functions and ("pythag" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["pythag"]):
            return math_utils.raw_pythag
        else:
            return math_utils.raw_pythag.py_func

    def pythag(self, points):
        return self.get_function_pythag()(points)

    def overflow(self, x):
        return self.get_function_overflow()(x)

    def get_function_ranger(self):
        return math_utils.raw_ranger

    def ranger(self, value, old, new):
        return self.get_function_ranger()(value, old, new)

    def get_function_gl_look_at(self):
        return math_utils.raw_gl_look_at

    def gl_look_at(self, eye, target, up):
        return self.get_function_gl_look_at()(eye, target, up)

    def get_function_compute_position(self):
        if Registry.compile_math_functions and ("compute_position" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["compute_position"]):
            return math_utils.raw_compute_position
        else:
            return math_utils.raw_compute_position.py_func

    def compute_position(self, pos, target, up):
        return self.get_function_compute_position()(pos, target, up)

    def get_function_perspective_fov(self):
        if Registry.compile_math_functions and ("perspective_fov" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["perspective_fov"]):
            return math_utils.raw_perspective_fov
        else:
            return math_utils.raw_perspective_fov.py_func

    def perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        return self.get_function_perspective_fov()(fov, aspect_ratio, near_plane, far_plane)

    def get_function_look_at(self):
        if Registry.compile_math_functions and ("look_at" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["look_at"]):
            return math_utils.raw_look_at
        else:
            return math_utils.raw_look_at.py_func

    def look_at(self, camera_position, camera_target, up_vector):
        return self.get_function_look_at()(camera_position, camera_target, up_vector)

    def get_function_multiply(self):
        if Registry.compile_math_functions and ("multiply" in Registry.custom_compiled_behavior.keys() and Registry.custom_compiled_behavior["multiply"]):
            return math_utils.raw_multiply
        else:
            return math_utils.raw_multiply.py_func

    def multiply(self, a, b):
        return self.get_function_multiply()(a, b)
