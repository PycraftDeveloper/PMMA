from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants
from pmma.python_src.utility.registry_utils import Registry as _Registry

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class ShapeTemplate:
    """
    🟩 **R** -
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._pygame__module = _ModuleManager.import_module("pygame")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._number_converter__module = _ModuleManager.import_module("pmma.python_src.number_converter")
        self._events__module = _ModuleManager.import_module("pmma.python_src.events")

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")
        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")

        if not _InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT)
            from pmma.python_src.utility.shape_geometry_utils import ShapeGeometryManager as _ShapeGeometryManager
            _ShapeGeometryManager()

        self._logger = self._logging_utils__module.InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            self._pygame__module.init()

        self._color_changed = True
        self._fill_color_manager = self._number_converter__module.ColorConverter()
        self._display = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT]

        self._resized_event = self._events__module.WindowResized_EVENT()

        self._geometry_created = False

        _Registry.shape_count += 1

        self.old_shape_identifier = None

        self._color_data = None
        self._vertex_data = None
        self._offset_data = self._numpy__module.array([0, 0], dtype=self._numpy__module.float32)

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        if type(color) == self._number_converter__module.ColorConverter:
            color = color.get_color(format=_Constants.RGBA)
            format = _Constants.RGBA

        if self._fill_color_manager.get_color_set():
            original_color = self._fill_color_manager.get_color(format=_Constants.RGBA)
            self._fill_color_manager.set_color(color, format=format)
            if self._numpy__module.any(self._fill_color_manager.get_color(format=_Constants.RGBA) != original_color):
                self._color_changed = True
            else:
                self._color_changed = False
                self._fill_color_manager.set_color(original_color, format=_Constants.RGBA)
        else:
            self._color_changed = True
            self._fill_color_manager.set_color(color, format=format)

        if self._color_changed:
            self._color_data = self._fill_color_manager.get_color(format=_Constants.SMALL_RGBA)

    def get_color_set(self):
        """
        🟩 **R** -
        """
        return self._fill_color_manager.get_color_set()

    def get_color(self, format):
        """
        🟩 **R** -
        """
        if self._fill_color_manager.get_color_set():
            return self._fill_color_manager.get_color(format=format)

    def set_seed(self, seed):
        self._fill_color_manager.set_seed(seed)

    def get_seed(self):
        return self._fill_color_manager.get_seed()

    def set_red_seed(self, seed=None):
        self._fill_color_manager.set_red_seed(seed)

    def set_green_seed(self, seed=None):
        self._fill_color_manager.set_green_seed(seed)

    def set_blue_seed(self, seed=None):
        self._fill_color_manager.set_blue_seed(seed)

    def set_alpha_seed(self, seed=None):
        self._fill_color_manager.set_alpha_seed(seed)

    def get_red_seed(self):
        return self._fill_color_manager.get_red_seed()

    def get_green_seed(self):
        return self._fill_color_manager.get_green_seed()

    def get_blue_seed(self):
        return self._fill_color_manager.get_blue_seed()

    def get_alpha_seed(self):
        return self._fill_color_manager.get_alpha_seed()

    def generate_random_color(
            self,
            color_range=[0, 255],
            generate_alpha=True,
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._color_changed = True

        if generate_alpha is False:
            alpha_color_range = [255, 255]

        self._color_data = self._fill_color_manager.generate_random_color(
            format=_Constants.SMALL_RGBA,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def generate_color_from_perlin_noise(
            self,
            value=None,
            generate_alpha=True,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        """
        🟩 **R** -
        """
        self._color_changed = True

        if generate_alpha is False:
            alpha_color_range = [255, 255]

        self._color_data = self._fill_color_manager.generate_color_from_perlin_noise(
            value=value,
            format=_Constants.SMALL_RGBA,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            _Registry.shape_count -= 1

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

class LineUtils:
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._math__module = _ModuleManager.import_module("math")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

    def _internal_render(self, color_changed, geometry_created):
        """
        🟩 **R** -
        """
        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if color_changed:
            self._program.set_shader_variable('color', self._color_data)

        if geometry_created is False:
            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio())
            self._vbo.set_data(self._vertex_data)

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Render the line
        self._vao.render(mode=self._moderngl__module.TRIANGLE_STRIP)

    def _rotate_point_around_center(self, point, center, angle):
        """
        🟩 **R** - Rotates a 2D point around a given center by the given angle in radians, accounting for aspect ratio.

        :param point: A list or tuple representing the x and y coordinates (x, y)
        :param center: The center of rotation as (cx, cy)
        :param angle: The angle to rotate by, in radians.
        :return: The rotated point as a [x', y'] list.
        """
        # Scale the point and center coordinates to account for aspect ratio
        scaled_point = [point[0], point[1]]
        scaled_center = [center[0], center[1]]

        # Translate the point to the origin (relative to the center)
        translated_x = scaled_point[0] - scaled_center[0]
        translated_y = scaled_point[1] - scaled_center[1]

        # Apply 2D rotation matrix
        cos_angle = self._math__module.cos(angle)
        sin_angle = self._math__module.sin(angle)

        x_prime = cos_angle * translated_x - sin_angle * translated_y
        y_prime = sin_angle * translated_x + cos_angle * translated_y

        # Translate the point back to its original position (relative to the center)
        # Scale back the x-coordinate to remove aspect ratio effect
        return [x_prime + center[0], y_prime + center[1]]

    def _rotate_line(self, angle, start_coords, end_coords):
        """
        🟩 **R** - Rotates the line around its center by the given angle in radians.
        """
        # Calculate the center of the line
        center_x = (start_coords[0] + end_coords[0]) / 2
        center_y = (start_coords[1] + end_coords[1]) / 2
        center = [center_x, center_y]

        # Rotate both start and end points around the center
        rotated_start = self._rotate_point_around_center(start_coords, center, angle)
        rotated_end = self._rotate_point_around_center(end_coords, center, angle)

        return [*rotated_start, *rotated_end]

    def _create_geometry(self):
        """
        🟩 **R** -
        """
        rotation_in_radians = self._rotation.get_angle(format=_Constants.RADIANS)
        start_coords = self.get_start(format=_Constants.OPENGL_COORDINATES)
        start_coords = [start_coords[0] * self._display.get_aspect_ratio(), start_coords[1]]
        end_coords = self.get_end(format=_Constants.OPENGL_COORDINATES)
        end_coords = [end_coords[0] * self._display.get_aspect_ratio(), end_coords[1]]

        identifier = self._internal_general_utils.create_cache_id(
            rotation_in_radians,
            tuple(start_coords),
            tuple(end_coords),
            self._width)

        cached_data = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].line_cache(self.old_shape_identifier, identifier)

        if cached_data is not None:
            vertices = cached_data
        else:
            rotated_line_points = self._rotate_line(rotation_in_radians, start_coords, end_coords)

            start_coords = rotated_line_points[:2]  # Start point (x1, y1)
            end_coords = rotated_line_points[2:]    # End point (x2, y2)

            # Calculate direction of the line
            direction = self._numpy__module.array(end_coords) - self._numpy__module.array(start_coords)
            direction_length = self._numpy__module.linalg.norm(direction)
            direction_normalized = direction / direction_length

            x_ndc = 2.0 / self._display.get_width() * self._display.get_aspect_ratio()  # Horizontal pixel size in NDC
            y_ndc = 2.0 / self._display.get_height()  # Vertical pixel size in NDC

            width = self._width * self._numpy__module.array([x_ndc, y_ndc])

            normal = self._numpy__module.array([-direction_normalized[1], direction_normalized[0]]) * width

            # Calculate the vertices of the line as a rectangle
            v1 = start_coords - normal
            v2 = start_coords + normal
            v3 = end_coords - normal
            v4 = end_coords + normal

            # Create the vertex array for two triangles representing the line
            vertices = self._numpy__module.array([
                *v1, *v2, *v3,  # First triangle
                *v3, *v2, *v4   # Second triangle
            ], dtype='f4')

            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_line(identifier, vertices)

        self.old_shape_identifier = identifier
        self._vertex_data = vertices

class RadialPolygonUtils:
    """
    🟩 **R** -
    """
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._numpy__module = _ModuleManager.import_module("numpy")
        self._math__module = _ModuleManager.import_module("math")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

    def _internal_render(self, color_changed, position_changed, geometry_created):
        """
        🟩 **R** -
        """
        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if color_changed:
            self._program.set_shader_variable('color', self._color_data)

        if position_changed:
            self._program.set_shader_variable('offset', self._offset_data)

        if geometry_created is False:
            self._vbo.set_data(self._vertex_data)
            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio())

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(self._moderngl__module.TRIANGLE_STRIP)

    def _create_geometry(self):
        """
        🟩 **R** -
        """
        radius = self._radius.get_point(_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(_Constants.RADIANS)  # Get the current rotation angle

        if self._point_count is None:
            try:
                point_count = 1 + int((_Constants.TAU / self._math__module.asin(1 / self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES))) * _Registry.shape_quality)
            except:
                point_count = 3
        else:
            point_count = self._point_count

        if point_count < 3:
            point_count = 3

        identifier = self._internal_general_utils.create_cache_id(radius, rotation, self._width, point_count)

        cached_data = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].radial_polygon_cache(self.old_shape_identifier, identifier)

        if cached_data is not None:
            vertices = cached_data
        else:
            angle_step = 2 * self._math__module.pi / point_count
            angles = self._numpy__module.arange(point_count) * angle_step + rotation

            # Get the outer and inner radii
            outer_radius = radius

            if self._width is not None:
                self._inner_radius.set_point(max(self._radius.get_point() - self._width, 0))
                inner_radius = self._inner_radius.get_point(_Constants.OPENGL_COORDINATES) if self._width else 0
            else:
                inner_radius = 0

            # Calculate outer vertices as an array
            outer_vertices = self._numpy__module.column_stack((outer_radius * self._numpy__module.cos(angles),
                                            outer_radius * self._numpy__module.sin(angles)))

            # Calculate inner vertices with a slight inward scaling as an array
            inner_vertices = self._numpy__module.column_stack((inner_radius * self._numpy__module.cos(angles) * 0.98,
                                            inner_radius * self._numpy__module.sin(angles) * 0.98))

            # Interleave outer and inner vertices for the triangle strip pattern
            combined_vertices = self._numpy__module.empty((2 * point_count + 2, 2), dtype='f4')
            combined_vertices[0:-2:2] = outer_vertices
            combined_vertices[1:-2:2] = inner_vertices

            # Close the shape by adding the first vertices again
            combined_vertices[-1] = inner_vertices[0]  # Append the first outer vertex to close the shape
            combined_vertices[-2] = outer_vertices[0]  # Append the first outer vertex to close the shape

            # The final array of vertices
            vertices = combined_vertices.flatten()

            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_radial_polygon(identifier, vertices)

        self.old_shape_identifier = identifier
        self._vertex_data = vertices

class RectangleUtils:
    """
    🟩 **R** -
    """
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._math__module = _ModuleManager.import_module("math")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

    def _internal_render(self, color_changed, position_changed, geometry_created):
        """
        🟩 **R** -
        """
        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if color_changed:
            self._program.set_shader_variable('color', self._color_data)

        if position_changed:
            self._program.set_shader_variable('offset', self._offset_data)

        if geometry_created is False:
            self._vbo.set_data(self._vertex_data)
            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio())

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(self._moderngl__module.TRIANGLE_STRIP)

    def _arc(self, cx, cy, start_angle, end_angle, r, segments):
        """
        🟩 **R** -
        """
        arc_vertices = []
        for angle in self._numpy__module.linspace(start_angle, end_angle, segments):
            px = cx + r * self._math__module.cos(angle)
            py = cy + r * self._math__module.sin(angle)
            arc_vertices.append((px, py))
        return arc_vertices

    def _generate_corner(self, cx, cy, start_angle, end_angle, outer_radius, inner_radius, segments):
        """
        🟩 **R** -
        """
        outer_arc = self._arc(cx, cy, start_angle, end_angle, outer_radius, segments)
        inner_arc = self._arc(cx, cy, start_angle, end_angle, inner_radius, segments)
        return zip(outer_arc, inner_arc)

    def _create_geometry(self):
        """
        🟩 **R** - Calculate the vertices of the polygon based on the radius, center, point count, and rotation.
        """
        x_size = self._x_size.get_point(_Constants.OPENGL_COORDINATES)
        y_size = self._y_size.get_point(_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)
        width = self._width.get_point(_Constants.OPENGL_COORDINATES)
        if width == 0:
            width = max(x_size / 2, y_size / 2)
        corner_radius = self._corner_radius.get_point(_Constants.OPENGL_COORDINATES)
        normal_corner_radius = self._corner_radius.get_point(_Constants.CONVENTIONAL_COORDINATES)
        corner_radius = min(corner_radius, x_size / 2, y_size / 2)
        width = min(width, x_size / 2, y_size / 2)

        identifier = self._internal_general_utils.create_cache_id(x_size, y_size, width, rotation, corner_radius)

        cached_data = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].rectangle_cache(self.old_shape_identifier, identifier)

        if cached_data is not None:
            vertices = cached_data
        else:
            if normal_corner_radius == 1:  # Skip rounded corners when the radius is effectively 1 or 0
                # Generate a simple rectangle without rounded corners
                combined_vertices = self._numpy__module.array([
                    (-x_size / 2, -y_size / 2),  # Bottom-left corner
                    (x_size / 2, -y_size / 2),   # Bottom-right corner
                    (-x_size / 2, y_size / 2),   # Top-left corner
                    (x_size / 2, y_size / 2),    # Top-right corner
                ], dtype="f4")
            else:
                try:
                    minimum_radius = min(
                        normal_corner_radius,
                        self._x_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES) / 2,
                        self._y_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES) / 2)

                    segments = 1 + int((_Constants.TAU / self._math__module.asin(1 / minimum_radius)) * _Registry.shape_quality)
                    segments //= 4
                except:
                    segments = 3
                if segments < 3:
                    segments = 3

                vertices = []

                # Outer and inner rectangle dimensions
                outer_radius = corner_radius
                inner_radius = corner_radius - width
                outer_width = x_size
                outer_height = y_size

                # Bottom-left corner
                bl_corners = self._generate_corner(
                    -outer_width / 2 + outer_radius,
                    -outer_height / 2 + outer_radius,
                    self._math__module.pi, 1.5 * self._math__module.pi,
                    outer_radius,
                    inner_radius,
                    segments)
                # Bottom-right corner
                br_corners = self._generate_corner(
                    outer_width / 2 - outer_radius,
                    -outer_height / 2 + outer_radius,
                    1.5 * self._math__module.pi,
                    2 * self._math__module.pi,
                    outer_radius,
                    inner_radius,
                    segments)
                # Top-right corner
                tr_corners = self._generate_corner(
                    outer_width / 2 - outer_radius,
                    outer_height / 2 - outer_radius,
                    0,
                    0.5 * self._math__module.pi,
                    outer_radius,
                    inner_radius,
                    segments)
                # Top-left corner
                tl_corners = self._generate_corner(
                    -outer_width / 2 + outer_radius,
                    outer_height / 2 - outer_radius,
                    0.5 * self._math__module.pi,
                    self._math__module.pi,
                    outer_radius,
                    inner_radius,
                    segments)

                # Combine all corners and edges in triangle strip order
                for outer, inner in bl_corners:
                    vertices.extend([outer, inner])
                for outer, inner in br_corners:
                    vertices.extend([outer, inner])
                for outer, inner in tr_corners:
                    vertices.extend([outer, inner])
                for outer, inner in tl_corners:
                    vertices.extend([outer, inner])

                # Close the shape by connecting the last and first vertices
                vertices.append(vertices[0])  # Outer vertex
                vertices.append(vertices[1])  # Inner vertex

                combined_vertices = self._numpy__module.array(vertices, dtype='f4')

            # Apply rotation around the center
            if rotation % self._math__module.pi != 0:
                cos_theta = self._math__module.cos(rotation)
                sin_theta = self._math__module.sin(rotation)

                # Rotation matrix
                rotation_matrix = self._numpy__module.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]], dtype='f4')

                # Apply rotation in a vectorized way
                vertices = combined_vertices @ rotation_matrix.T
                vertices = vertices.flatten()
            else:
                vertices = combined_vertices.flatten()

            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_rectangle(identifier, vertices)

        self._geometry_created = True  # Reset the flag
        self.old_shape_identifier = identifier
        self._vertex_data = vertices

class ArcUtils:
    """
    🟩 **R** -
    """
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._math__module = _ModuleManager.import_module("math")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

    def _internal_render(self, color_changed, position_changed, geometry_created):
        """
        🟩 **R** -
        """
        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if color_changed:
            self._program.set_shader_variable('color', self._color_data)

        if position_changed:
            self._program.set_shader_variable('offset', self._offset_data)

        if geometry_created is False:
            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio())
            # Update VBO
            self._vbo.set_data(self._vertex_data)

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Render the arc using GL_TRIANGLE_STRIP
        self._vao.render(self._moderngl__module.TRIANGLE_STRIP)

    def _create_geometry(self):
        """
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, radius, and width.
        """
        if self._radius is None or self._start_angle is None or self._stop_angle is None:
            return None  # Cannot proceed without these parameters

        start_angle = self._start_angle.get_angle(format=_Constants.RADIANS)
        stop_angle = self._stop_angle.get_angle(format=_Constants.RADIANS)
        outer_radius = self._radius.get_point(format=_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)

        identifier = self._internal_general_utils.create_cache_id(start_angle, stop_angle, outer_radius, rotation, self._width)

        cached_data = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].arc_cache(self.old_shape_identifier, identifier)

        if cached_data is not None:
            rotated_vertices = cached_data
        else:
            center_x, center_y = [0, 0]

            if self._width is not None:
                self._inner_radius.set_point(max(self._radius.get_point() - self._width, 0))
                inner_radius = self._inner_radius.get_point(_Constants.OPENGL_COORDINATES) if self._width else 0
            else:
                inner_radius = 0

            '''self._inner_radius.set_point(self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES) - self._width)
            inner_radius = self._inner_radius.get_point(format=_Constants.OPENGL_COORDINATES)  # Ensure inner radius is non-negative
            inner_radius = max(inner_radius, 0)'''

            # Determine the number of points to create smooth arcs for both inner and outer radii
            try:
                proportion_of_circle = abs(stop_angle - start_angle) / _Constants.TAU
                point_count = 1 + int(
                    ((_Constants.TAU / self._math__module.asin(1 / self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES)))
                    * proportion_of_circle) * _Registry.shape_quality
                )
            except:
                point_count = 3

            if point_count < 3:
                point_count = 3

            # Generate angles for the arc
            angles = self._numpy__module.linspace(start_angle, stop_angle, point_count)

            # Use broadcasting to calculate inner and outer vertices
            inner_vertices = self._numpy__module.column_stack((
                center_x + inner_radius * self._numpy__module.cos(angles),
                center_y + inner_radius * self._numpy__module.sin(angles)
            )).astype('f4')

            outer_vertices = self._numpy__module.column_stack((
                center_x + outer_radius * self._numpy__module.cos(angles),
                center_y + outer_radius * self._numpy__module.sin(angles)
            )).astype('f4')

            # Combine inner and outer vertices in a way suitable for TRIANGLE_STRIP
            vertices = self._numpy__module.empty((2 * point_count, 2), dtype='f4')
            vertices[0::2] = outer_vertices
            vertices[1::2] = inner_vertices

            # Apply rotation around the center
            if rotation % self._math__module.pi != 0:
                cos_theta = self._math__module.cos(rotation)
                sin_theta = self._math__module.sin(rotation)

                # Rotation matrix
                rotation_matrix = self._numpy__module.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]], dtype='f4')

                # Apply rotation in a vectorized way
                vertices = vertices @ rotation_matrix.T
                rotated_vertices = vertices.flatten()
            else:
                rotated_vertices = vertices.flatten()

            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_arc(identifier, rotated_vertices)

        self._geometry_created = True  # Reset the flag
        self.old_shape_identifier = identifier
        self._vertex_data = rotated_vertices

class EllipseUtils:
    """
    🟩 **R** -
    """
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._math__module = _ModuleManager.import_module("math")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._advmath__module = _ModuleManager.import_module("pmma.python_src.advmath")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

        self._math = self._advmath__module.Math()

    def _internal_render(self, color_changed, position_changed, geometry_created):
        """
        🟩 **R** -
        """
        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if color_changed:
            self._program.set_shader_variable('color', self._color_data)

        if position_changed:
            self._program.set_shader_variable('offset', self._offset_data)

        if geometry_created is False:
            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio())
            self._vbo.set_data(self._vertex_data)

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(self._moderngl__module.TRIANGLE_STRIP)

    def _rotate_point(self, x, y, cx, cy, cos_theta, sin_theta):
        """
        🟩 **R** -
        """
        dx = x - cx
        dy = y - cy
        return [
            cx + dx * cos_theta - dy * sin_theta,
            cy + dx * sin_theta + dy * cos_theta
        ]

    def _create_geometry(self):
        """
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        outer_size_x = self._outer_x_size.get_point(format=_Constants.OPENGL_COORDINATES)
        outer_size_y = self._outer_y_size.get_point(format=_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)

        if self._width is None:
            width = max(self._outer_x_size.get_point(), self._outer_y_size.get_point())
        else:
            width = self._width

        identifier = self._internal_general_utils.create_cache_id(
            outer_size_x,
            outer_size_y,
            width,
            rotation)

        cached_data = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].ellipse_cache(self.old_shape_identifier, identifier)

        if cached_data is not None:
            rotated_vertices = cached_data
        else:
            center_x, center_y = [0, 0]

            radius = self._math.pythag([self._outer_x_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES), self._outer_y_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES)])

            # Number of points to generate for the ellipse
            num_points = _Registry.shape_quality
            try:
                num_points = 1 + int((_Constants.TAU/self._math__module.asin(1/radius))*_Registry.shape_quality)
            except:
                num_points = 3
            if num_points < 3:
                num_points = 3

            self._inner_x_size.set_point(self._outer_x_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES) - width*2)
            self._inner_y_size.set_point(self._outer_y_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES) - width*2)

            inner_size_x = max(self._inner_x_size.get_point(format=_Constants.OPENGL_COORDINATES), 0)
            inner_size_y = max(self._inner_y_size.get_point(format=_Constants.OPENGL_COORDINATES), 0)

            # Generate points along the ellipse perimeter
            angles = self._numpy__module.linspace(0, 2 * self._numpy__module.pi, num_points)
            cos_angles = self._numpy__module.cos(angles)
            sin_angles = self._numpy__module.sin(angles)

            # Vectorized calculation for outer and inner vertices
            outer_vertices = self._numpy__module.column_stack((center_x + (outer_size_x / 2) * cos_angles,
                                            center_y + (outer_size_y / 2) * sin_angles)).astype('f4')

            inner_vertices = self._numpy__module.column_stack((center_x + (inner_size_x / 2) * cos_angles,
                                            center_y + (inner_size_y / 2) * sin_angles)).astype('f4')

            vertices = self._numpy__module.empty((2 * num_points, 2), dtype='f4')
            vertices[0::2] = outer_vertices
            vertices[1::2] = inner_vertices

            # Apply rotation around the center
            if rotation % self._math__module.pi != 0:
                cos_theta = self._math__module.cos(rotation)
                sin_theta = self._math__module.sin(rotation)

                # Rotation matrix
                rotation_matrix = self._numpy__module.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]], dtype='f4')

                # Apply rotation in a vectorized way
                vertices = vertices @ rotation_matrix.T
                rotated_vertices = vertices.flatten()
            else:
                rotated_vertices = vertices.flatten()

            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_ellipse(identifier, rotated_vertices)

        self._geometry_created = True  # Reset the flag
        self.old_shape_identifier = identifier
        self._vertex_data = rotated_vertices

class PolygonUtils:
    """
    🟩 **R** -
    """
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._math__module = _ModuleManager.import_module("math")
        self._numpy__module = _ModuleManager.import_module("numpy")

        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")

        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

    def _internal_render(self, color_changed, geometry_created):
        """
        🟩 **R** -
        """
        self._display.get_2D_hardware_accelerated_surface()

        # Update VBO with any changes to vertices or colors
        if color_changed:
            self._program.set_shader_variable('color', self._color_data)

        if geometry_created is False:
            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio())
            self._vbo.set_data(self._vertex_data)

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._closed is False and self._width is None:
            self._width = 1 # idk about this bit yet

        self._vao.render(self._moderngl__module.TRIANGLE_STRIP)

    def _rotate_point(self, x, y, cx, cy, cos_theta, sin_theta):
        """
        🟩 **R** -
        """
        dx = x - cx
        dy = y - cy
        return [
            self._display.get_aspect_ratio() * (cx + dx * cos_theta - dy * sin_theta),
            cy + dx * sin_theta + dy * cos_theta
        ]

    def _create_geometry(self):
        """
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        if not self._points:
            return None  # No points to form the polygon

        outer_points = self._numpy__module.array([p.get_coordinates(format=_Constants.OPENGL_COORDINATES) for p in self._points], dtype='f4')
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)

        if self._width is None:
            width = 1
        else:
            width = self._width

        identifier = self._internal_general_utils.create_cache_id(
            outer_points.tobytes(),
            rotation,
            width)

        cached_data = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].polygon_cache(self.old_shape_identifier, identifier)

        if cached_data is not None:
            rotated_vertices = cached_data
        else:
            inner_points = []
            index = 0
            for p in self._points:
                coordinate = p.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                adjusted_x = coordinate[0] - width
                adjusted_y = coordinate[1] - width
                adjusted_point = [adjusted_x, adjusted_y]
                self._converted_inner_points[index].set_coordinates(adjusted_point, format=_Constants.CONVENTIONAL_COORDINATES)
                inner_points.append(self._converted_inner_points[index].get_coordinates(format=_Constants.OPENGL_COORDINATES))
                index += 1

            inner_points = self._numpy__module.array(inner_points, dtype='f4')
            # Calculate center (average of points)
            center_x, center_y = self._numpy__module.mean(outer_points, axis=0)

            vertices = self._numpy__module.empty((2 * len(self._points), 2), dtype='f4')
            vertices[0::2] = outer_points
            vertices[1::2] = inner_points

            if rotation % self._math__module.pi == 0:
                # Apply rotation
                cos_theta = self._numpy__module.cos(rotation)
                sin_theta = self._numpy__module.sin(rotation)

                rotated_vertices = self._numpy__module.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

                # If closed, append the first vertex to close the loop
                if self._closed and len(rotated_vertices) > 1:
                    extra_points = self._numpy__module.array([rotated_vertices[0], rotated_vertices[1]], dtype='f4')
                    rotated_vertices = self._numpy__module.concatenate((rotated_vertices, extra_points))

                rotated_vertices = rotated_vertices.flatten()
            else:
                rotated_vertices = vertices.flatten()

            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_polygon(identifier, rotated_vertices)

        self._geometry_created = True  # Reset the flag
        self.old_shape_identifier = identifier
        self._vertex_data = rotated_vertices

class PixelUtils:
    """
    🟩 **R** -
    """
    def __init__(self):
        super().__init__()

        self._moderngl__module = _ModuleManager.import_module("moderngl")
        self._numpy__module = _ModuleManager.import_module("numpy")

    def _internal_render(self, color_changed, position_changed, point_size=None):
        """
        🟩 **R** -
        """
        if self._position is None:
            return None

        conventional_position = self.get_position(format=_Constants.CONVENTIONAL_COORDINATES)
        if conventional_position[0] < 0 or conventional_position[1] < 0:
            return None

        if conventional_position[0] > self._display.get_width() or conventional_position[1] > self._display.get_height():
            return None

        self._display.update_attempted_render_calls(1)

        if color_changed or position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        if point_size is None:
            if _Registry.do_anti_aliasing:
                self._logger.log_development("When using anti-aliasing we need to slightly \
increase the point size to ensure that it is rendered visibly onscreen. That is why sometimes \
your single pixel might appear like a 2x2 instead of 1x1 pixels wide. This behavior can be \
forced back to 1 by using the 'point_size' key word argument to this method call, however \
we generally don't recommend this without good reason.")
                if _Registry.anti_aliasing_level > 8:
                    self._logger.log_development("You are using an anti-aliasing level of \
more than 8. When using high anti-aliasing samples we automatically increase the pixel size \
slightly to ensure that it is still visible. However in testing we where not able to exceed \
an anti-aliasing level of 8, you have here so we cannot guarantee that the pixel will be \
visible. If the pixel cannot be found then adjust the point size parameter to this method \
call to larger than 2.")
                _Registry.context.point_size = 2
            else:
                _Registry.context.point_size = 1
        else:
            _Registry.context.point_size = point_size
            self._logger.log_development("You have specified a custom point size. This should \
only really be used to fix any potential problems with anti-aliasing and small pixels being \
simply 'aliased-away'. You can use this to make points appear larger, however its generally \
recommended to do this in the shader it's self with: `gl_PointSize`.")

        self._vao.render(mode=self._moderngl__module.POINTS)

    def _create_geometry(self):
        """
        🟩 **R** -
        """
        if _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_pixel_exists():
            vertices = _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_pixel()
        else:
            vertices = self._numpy__module.array([0, 0], dtype='f4')
            _Registry.pmma_module_spine[_InternalConstants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_pixel(vertices)

        self._vbo.set_data(vertices)