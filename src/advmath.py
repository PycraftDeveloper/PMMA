from pmma.src.registry import Registry

import pmma.src.utility.math_utils as math_utils

class Math:
    def get_function_hash(self):
        if Registry.compile_math_functions:
            if "raw_hash" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_hash"]:
                    return math_utils.raw_hash
                else:
                    return math_utils.raw_hash.py_func
            else:
                return math_utils.raw_hash
        else:
            return math_utils.raw_hash.py_func

    def hash(self, x):
        return self.get_function_hash()(x)

    def get_function_hash2(self):
        if Registry.compile_math_functions:
            if "raw_hash2" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_hash2"]:
                    return math_utils.raw_hash2
                else:
                    return math_utils.raw_hash2.py_func
            else:
                return math_utils.raw_hash2
        else:
            return math_utils.raw_hash2.py_func

    def hash2(self, x, y):
        return self.get_function_hash2()(x, y)

    def get_function_fade(self):
        if Registry.compile_math_functions:
            if "raw_fade" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_fade"]:
                    return math_utils.raw_fade
                else:
                    return math_utils.raw_fade.py_func
            else:
                return math_utils.raw_fade
        else:
            return math_utils.raw_fade.py_func

    def fade(self, x):
        return self.get_function_fade()(x)

    def get_function_lerp(self):
        if Registry.compile_math_functions:
            if "raw_lerp" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_lerp"]:
                    return math_utils.raw_lerp
                else:
                    return math_utils.raw_lerp.py_func
            else:
                return math_utils.raw_lerp
        else:
            return math_utils.raw_lerp.py_func

    def lerp(self, a, b, x):
        return self.get_function_lerp()(a, b, x)

    def get_function_grad(self):
        if Registry.compile_math_functions:
            if "raw_grad" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_grad"]:
                    return math_utils.raw_grad
                else:
                    return math_utils.raw_grad.py_func
            else:
                return math_utils.raw_grad
        else:
            return math_utils.raw_grad.py_func

    def grad(self, hash, x):
        return self.get_function_grad()(hash, x)

    def get_function_fast_grad(self):
        if Registry.compile_math_functions:
            if "raw_grad" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_fast_grad"]:
                    return math_utils.raw_fast_grad
                else:
                    return math_utils.raw_fast_grad.py_func
            else:
                return math_utils.raw_fast_grad
        else:
            return math_utils.raw_fast_grad.py_func

    def fast_grad(self, hash, x):
        return self.get_function_fast_grad()(hash, x)

    def get_function_grad2(self):
        if Registry.compile_math_functions:
            if "raw_grad2" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_grad2"]:
                    return math_utils.raw_grad2
                else:
                    return math_utils.raw_grad2.py_func
            else:
                return math_utils.raw_grad2
        else:
            return math_utils.raw_grad2.py_func

    def grad2(self, hash, x, y):
        return self.get_function_grad2()(hash, x, y)

    def get_function_fast_grad2(self):
        if Registry.compile_math_functions:
            if "raw_grad2" in Registry.custom_compiled_behavior.keys():
                if Registry.custom_compiled_behavior["raw_fast_grad2"]:
                    return math_utils.raw_fast_grad2
                else:
                    return math_utils.raw_fast_grad2.py_func
            else:
                return math_utils.raw_fast_grad2
        else:
            return math_utils.raw_fast_grad2.py_func

    def fast_grad2(self, hash, x, y):
        return self.get_function_fast_grad2()(hash, x, y)

    def get_function_overflow(self):
        return math_utils.raw_overflow

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
