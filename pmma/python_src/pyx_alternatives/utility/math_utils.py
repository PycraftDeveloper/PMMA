from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

class AdvancedMathIntermediary:
    def __init__(self):
        self._numpy__module = _ModuleManager.import_module("numpy")

    # Cubic smoothstep function for acceleration/deceleration
    def raw_smooth_step(self, t):
        """
        🟩 **R** -
        """
        return t * t * (3 - 2 * t)

    # Clamping and mapping function
    def raw_ranger(self, value, old, new):
        """
        🟩 **R** -
        """
        # Ensure value is within bounds of the 'old' range
        if value > old[1]:
            value = old[1]
        elif value < old[0]:
            value = old[0]

        # Check if 'old' and 'new' lists are identical
        if old[0] == new[0] and old[1] == new[1]:
            return value

        old_range = old[1] - old[0]
        new_range = new[1] - new[0]

        if old_range == 0:
            old_range = self._numpy__module.finfo(float).tiny

        new_value = (((value - old[0]) * new_range) / old_range) + new[0]
        return new_value

    # Clamping and mapping function for numpy arrays
    def raw_nparray_ranger(self, value, old, new):
        """
        🟩 **R** -
        """
        value[value > old[1]] = old[1]
        value[value < old[0]] = old[0]

        if self._numpy__module.array_equal(old, new):
            return value

        old_range = old[1] - old[0]
        new_range = new[1] - new[0]

        if old_range == 0:
            old_range = self._numpy__module.finfo(float).tiny

        new_value = (((value - old[0]) * new_range) / old_range) + new[0]
        return new_value

    # Compute the camera's orientation matrix
    def raw_gl_look_at(self, pos, target, up):
        """
        🟩 **R** -
        """
        x, y, z = self.raw_compute_position(pos, target, up)

        translate = self._numpy__module.identity(4, dtype=self._numpy__module.double32)
        translate[3][0] = -pos[0]
        translate[3][1] = -pos[1]
        translate[3][2] = -pos[2]

        rotate = self._numpy__module.identity(4, dtype=self._numpy__module.double32)
        rotate[0][0] = x[0]  # -- X
        rotate[1][0] = x[1]
        rotate[2][0] = x[2]
        rotate[0][1] = y[0]  # -- Y
        rotate[1][1] = y[1]
        rotate[2][1] = y[2]
        rotate[0][2] = z[0]  # -- Z
        rotate[1][2] = z[1]
        rotate[2][2] = z[2]

        return rotate @ translate[:, self._numpy__module.newaxis]

    # Compute the norm and direction
    def raw_pythag(self, points):
        """
        🟩 **R** -
        """
        sum = 0
        for point in points:
            sum += point ** 2
        return sum ** 0.5

    # Function to normalize a vector
    def normalize(self, v):
        """
        🟩 **R** -
        """
        norm = self._numpy__module.dot(v, v) ** 0.5  # Compute the norm manually
        if norm == 0:
            return v
        return v / norm

    # Function to compute the camera's basis vectors
    def raw_compute_position(self, pos, target, up):
        """
        🟩 **R** -
        """
        z = self.normalize(target - pos)
        x = self.normalize(self._numpy__module.cross(up, z))
        y = self._numpy__module.cross(z, x)
        return (x, y, z)

    # Look at function
    def raw_look_at(self, camera_position, camera_target, up_vector):
        """
        🟩 **R** -
        """
        vector = camera_target - camera_position

        x = self._numpy__module.linalg.norm(vector)
        vector = vector / x

        vector2 = self._numpy__module.cross(up_vector, vector)
        vector2 /= self._numpy__module.linalg.norm(vector2)

        vector3 = self._numpy__module.cross(vector, vector2)

        return self._numpy__module.array([
            [vector2[0], vector3[0], vector[0], 0.0],
            [vector2[1], vector3[1], vector[1], 0.0],
            [vector2[2], vector3[2], vector[2], 0.0],
            [-self._numpy__module.dot(vector2, camera_position), -self._numpy__module.dot(vector3, camera_position), self._numpy__module.dot(vector, camera_position), 1.0]
        ], dtype=self._numpy__module.double32)

    # Matrix multiplication function
    def raw_multiply(self, light_proj, sun_light_look_at):
        """
        🟩 **R** -
        """
        return light_proj @ sun_light_look_at
