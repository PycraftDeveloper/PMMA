from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

class AdvancedMathIntermediary:
    def __init__(self):
        self._math__module = _ModuleManager.import_module("math")
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
    def raw_look_at(self, camera_pos, target, up):
        """
        🟩 **R** -
        """
        f = self._numpy__module.array(camera_pos, dtype=self._numpy__module.double) - self._numpy__module.array(target, dtype=self._numpy__module.double)
        f /= self._numpy__module.linalg.norm(f)

        s = self._numpy__module.cross(up, f)
        s /= self._numpy__module.linalg.norm(s)

        u = self._numpy__module.cross(f, s)

        mat = self._numpy__module.identity(4, dtype=self._numpy__module.float64)
        mat[0, :3] = s
        mat[1, :3] = u
        mat[2, :3] = f
        mat[0, 3] = -self._numpy__module.dot(s, camera_pos)
        mat[1, 3] = -self._numpy__module.dot(u, camera_pos)
        mat[2, 3] = -self._numpy__module.dot(f, camera_pos)

        return mat

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
        z = self.normalize(pos - target)
        x = self.normalize(self._numpy__module.cross(up, z))
        y = self._numpy__module.cross(z, x)
        return (x, y, z)

    # Matrix multiplication function
    def raw_multiply(self, light_proj, sun_light_look_at):
        """
        🟩 **R** -
        """
        return light_proj @ sun_light_look_at

    def raw_perspective_fov(self, fov, aspect_ratio, near_plane, far_plane):
        """
        🟩 **R** -
        """
        f = 1.0 / self._math__module.tan(fov * 0.5)

        nf = 1.0 / (near_plane - far_plane)

        return [
            [f / aspect_ratio, 0.0, 0.0, 0.0],
            [0.0, f, 0.0, 0.0],
            [0.0, 0.0, (far_plane + near_plane) * nf, (2 * far_plane * near_plane) * nf],
            [0.0, 0.0, -1.0, 0.0]
        ]
