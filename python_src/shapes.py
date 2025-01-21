import math as _math
import time as _time
from gc import collect as _gc__collect

import pygame as _pygame
import moderngl as _moderngl
import numpy as _numpy

from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import DisplayCoordinatesConverter as _DisplayCoordinatesConverter
from pmma.python_src.number_converter import DisplayScalarConverter as _DisplayScalarConverter
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.number_converter import AngleConverter as _AngleConverter
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.advmath import Math as _Math
from pmma.python_src.events import WindowResized_EVENT as _WindowResized_EVENT

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.error_utils import ShapeRadiusNotSpecifiedError as _ShapeRadiusNotSpecifiedError
from pmma.python_src.utility.shape_utils import ShapeTemplate as _ShapeTemplate

class Line(_ShapeTemplate):
    """
    🟩 **R** -Draws a basic line.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._start = _DisplayCoordinatesConverter()
        self._end = _DisplayCoordinatesConverter()
        self._width = 1
        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._vertices_changed = True  # Mark vertices as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_line"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)

        self._resized_event = _WindowResized_EVENT()

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_start(self, start, start_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        start_input_type = type(start)
        if self._start.get_coordinate_set():
            if start_format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._start.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if start_input_type == _DisplayCoordinatesConverter:
                    start_coords = start.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    start_coords = [int(start[0]), int(start[1])]

                if start_coords[0] == original_coordinates[0] and start_coords[1] == original_coordinates[1]:
                    return

        self._vertices_changed = True
        if start_input_type != _DisplayCoordinatesConverter:
            self._start.set_coordinates(start, format=start_format)
        else:
            self._start = start

    def get_start(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._start is not None:
            return self._start.get_coordinates(format=format)

    def set_end(self, end, end_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        end_input_type = type(end)
        if self._start.get_coordinate_set():
            if end_format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._end.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if end_input_type == _DisplayCoordinatesConverter:
                    end_coords = end.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    end_coords = [int(end[0]), int(end[1])]

                if end_coords[0] == original_coordinates[0] and end_coords[1] == original_coordinates[1]:
                    return

        self._vertices_changed = True
        if end_input_type != _DisplayCoordinatesConverter:
            self._end.set_coordinates(end, format=end_format)
        else:
            self._end = end

    def get_end(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._end is not None:
            return self._end.get_coordinates(format=format)

    def set_width(self, width=1):
        """
        🟩 **R** -
        """
        if width <= 0:
            width = 1
        if width is None:
            width = 1
        self._width = width

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._width

    def _rotate_point_around_center(self, point, center, angle):
        """
        🟩 **R** - Rotates a 2D point around a given center by the given angle in radians, accounting for aspect ratio.

        :param point: A list or tuple representing the x and y coordinates (x, y)
        :param center: The center of rotation as (cx, cy)
        :param angle: The angle to rotate by, in radians.
        :return: The rotated point as a [x', y'] list.
        """
        # Get the aspect ratio (width/height)
        aspect_ratio = self._display.get_width() / self._display.get_height()

        # Scale the point and center coordinates to account for aspect ratio
        scaled_point = [point[0] * aspect_ratio, point[1]]
        scaled_center = [center[0] * aspect_ratio, center[1]]

        # Translate the point to the origin (relative to the center)
        translated_x = scaled_point[0] - scaled_center[0]
        translated_y = scaled_point[1] - scaled_center[1]

        # Apply 2D rotation matrix
        cos_angle = _numpy.cos(angle)
        sin_angle = _numpy.sin(angle)

        x_prime = cos_angle * translated_x - sin_angle * translated_y
        y_prime = sin_angle * translated_x + cos_angle * translated_y

        # Translate the point back to its original position (relative to the center)
        # Scale back the x-coordinate to remove aspect ratio effect
        return [x_prime / aspect_ratio + center[0], y_prime + center[1]]

    def _rotate_line(self, angle):
        """
        🟩 **R** - Rotates the line around its center by the given angle in radians.
        """
        # Get start and end points
        start_coords = self.get_start(format=_Constants.OPENGL_COORDINATES)
        end_coords = self.get_end(format=_Constants.OPENGL_COORDINATES)

        # Calculate the center of the line
        center_x = (start_coords[0] + end_coords[0]) / 2
        center_y = (start_coords[1] + end_coords[1]) / 2
        center = [center_x, center_y]

        # Rotate both start and end points around the center
        rotated_start = self._rotate_point_around_center(start_coords, center, angle)
        rotated_end = self._rotate_point_around_center(end_coords, center, angle)

        return [*rotated_start, *rotated_end]

    def _update_buffers(self):
        """
        🟩 **R** -
        """
        if self._vertices_changed:
            _Registry.number_of_render_updates += 1
            rotated_line_points = self._rotate_line(self._rotation.get_angle(format=_Constants.RADIANS))

            start_coords = rotated_line_points[:2]  # Start point (x1, y1)
            end_coords = rotated_line_points[2:]    # End point (x2, y2)

            # Calculate direction of the line
            direction = _numpy.array(end_coords) - _numpy.array(start_coords)
            direction_length = _numpy.linalg.norm(direction)
            direction_normalized = direction / direction_length

            x_ndc = 2.0 / self._display.get_width()  # Horizontal pixel size in NDC
            y_ndc = 2.0 / self._display.get_height()  # Vertical pixel size in NDC

            width = self._width * _numpy.array([x_ndc, y_ndc])

            normal = _numpy.array([-direction_normalized[1], direction_normalized[0]]) * width

            # Calculate the vertices of the line as a rectangle
            v1 = start_coords - normal
            v2 = start_coords + normal
            v3 = end_coords - normal
            v4 = end_coords + normal

            # Create the vertex array for two triangles representing the line
            vertices = _numpy.array([
                *v1, *v2, *v3,  # First triangle
                *v3, *v2, *v4   # Second triangle
            ], dtype='f4')

            if not self._vbo.get_created():
                self._vbo.create(vertices)
            else:
                self._vbo.update(vertices)

            self._vertices_changed = False  # Reset the flag

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

    def render(self):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._vertices_changed = True

        if self._color_changed or self._vertices_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Render the line
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class RadialPolygon(_ShapeTemplate):
    """
    🟩 **R** - Draws a radial polygon.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._point_count = None
        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._radius = _DisplayScalarConverter()
        self._inner_radius = _DisplayScalarConverter()
        self._center = _DisplayCoordinatesConverter()
        self._width = None
        self._vertices_changed = True  # Mark vertices as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_radial_polygon"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._position_changed = True
        self._initial_point_count = None

        self._resized_event = _WindowResized_EVENT()

    def _create_shape(self):
        """
        🟩 **R** -
        """
        if self._radius.get_point_set() is False:
            raise _ShapeRadiusNotSpecifiedError()

        if self._point_count is None:
            try:
                point_count = 1 + int((_Constants.TAU / _math.asin(1 / self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES))) * _Registry.shape_quality)
            except:
                point_count = 3
            if point_count < 3:
                point_count = 3
        else:
            point_count = self._point_count

        rotation = self._rotation.get_angle(_Constants.RADIANS)  # Get the current rotation angle

        angle_step = 2 * _math.pi / point_count
        angles = _numpy.arange(point_count) * angle_step + rotation

        # Get the outer and inner radii
        outer_radius = self._radius.get_point(_Constants.OPENGL_COORDINATES)

        if self._width is not None:
            self._inner_radius.set_point(max(self._radius.get_point() - self._width, 0))
            inner_radius = self._inner_radius.get_point(_Constants.OPENGL_COORDINATES) if self._width else 0
        else:
            inner_radius = 0

        # Calculate outer vertices as an array
        outer_vertices = _numpy.column_stack((outer_radius * _numpy.cos(angles),
                                        outer_radius * _numpy.sin(angles)))

        # Calculate inner vertices with a slight inward scaling as an array
        inner_vertices = _numpy.column_stack((inner_radius * _numpy.cos(angles) * 0.98,
                                        inner_radius * _numpy.sin(angles) * 0.98))

        # Interleave outer and inner vertices for the triangle strip pattern
        combined_vertices = _numpy.empty((2 * point_count + 2, 2), dtype='f4')
        combined_vertices[0:-2:2] = outer_vertices
        combined_vertices[1:-2:2] = inner_vertices

        # Close the shape by adding the first vertices again
        combined_vertices[-1] = inner_vertices[0]  # Append the first outer vertex to close the shape
        combined_vertices[-2] = outer_vertices[0]  # Append the first outer vertex to close the shape

        # The final array of vertices
        vertices = combined_vertices

        if self._initial_point_count == None or self._initial_point_count != point_count:
            self._initial_point_count = point_count
            self._vbo.quit()
            self._vbo.create(vertices)
        else:
            if self._vbo.get_created():
                self._vbo.update(vertices)
            else:
                self._vbo.create(vertices)

        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_radius(self, value, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(value) != _DisplayScalarConverter():
            self._radius.set_point(value, format=format)

    def get_radius(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._radius is not None:
            return self._radius.get_point(format=format)

    def set_point_count(self, point_count=None):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        self._point_count = point_count

    def get_point_count(self):
        """
        🟩 **R** -
        """
        return self._point_count

    def set_center(self, center, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        center_input_format = type(center)
        if self._center.get_coordinate_set():
            if format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._center.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if center_input_format == _DisplayCoordinatesConverter:
                    center_coords = center.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    center_coords = [int(center[0]), int(center[1])]

                if center_coords[0] == original_coordinates[0] and center_coords[1] == original_coordinates[1]:
                    return

        self._position_changed = True
        if center_input_format != _DisplayCoordinatesConverter:
            self._center.set_coordinates(center, format=format)
        else:
            self._center = center

    def get_center(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._center is not None:
            return self._center.get_coordinates(format=format)

    def set_width(self, width=None):
        """
        🟩 **R** -
        """
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._width

    def render(self):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._vertices_changed = True

        if self._color_changed or self._vertices_changed or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        if self._vertices_changed:
            self._create_shape()
            self._vertices_changed = False

        if self._position_changed:
            offset = self._center.get_coordinates(format=_Constants.OPENGL_COORDINATES)
            self._program.set_shader_variable('offset', offset)
            self._position_changed = False

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(_moderngl.TRIANGLE_STRIP)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Rectangle(_ShapeTemplate):
    """
    🟩 **R** - Draws a rectangle.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._position = _DisplayCoordinatesConverter()
        self._x_size = _DisplayScalarConverter()
        self._y_size = _DisplayScalarConverter()
        self._inner_radius = _DisplayScalarConverter()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._vertices_changed = True  # Mark vertices as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_rectangle"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._width = None
        self._position_changed = True

        self._resized_event = _WindowResized_EVENT()

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_width(self, width=None):
        """
        🟩 **R** -
        """
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._width

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_position(self, position, position_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        position_input_type = type(position)
        if self._position.get_coordinate_set():
            if position_format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._position.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if position_input_type == _DisplayCoordinatesConverter:
                    position_coords = position.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    position_coords = [int(position[0]), int(position[1])]

                if position_coords[0] == original_coordinates[0] and position_coords[1] == original_coordinates[1]:
                    return

        self._position_changed = True
        if position_input_type != _DisplayCoordinatesConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._position is not None:
            return self._position.get_coordinates(format=format)

    def set_size(self, size, size_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(size[0]) != _DisplayScalarConverter:
            self._x_size.set_point(size[0], format=size_format)
        else:
            self._x_size = size[0]

        if type(size[1]) != _DisplayScalarConverter:
            self._y_size.set_point(size[1], format=size_format)
        else:
            self._y_size = size[1]

    def get_size(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._x_size.get_point_set() and self._y_size.get_point_set():
            return [self._x_size.get_point(format=format), self._y_size.get_point(format=format)]

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

    def _update_buffers(self):
        """
        🟩 **R** - Calculate the vertices of the polygon based on the radius, center, point count, and rotation.
        """
        if self._vertices_changed:
            if self._position.get_coordinate_set() is False or self._x_size.get_point_set() is False or self._y_size.get_point_set() is False:
                return None

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

            _Registry.number_of_render_updates += 1

            # Unpack size and position
            x_size = self._x_size.get_point(_Constants.OPENGL_COORDINATES)
            y_size = self._y_size.get_point(_Constants.OPENGL_COORDINATES)
            half_outer_width = x_size / 2
            half_outer_height = y_size / 2
            x, y = (0, 0)

            self._inner_radius.set_point(self._width)
            border_width = self._inner_radius.get_point(format=_Constants.OPENGL_COORDINATES)

            half_inner_width = max(half_outer_width - border_width, 0)
            half_inner_height = max(half_outer_height - border_width, 0)

            offsets = _numpy.array([
                [-1, -1],  # Bottom-left
                [1, -1],   # Bottom-right
                [1, 1],    # Top-right
                [-1, 1]    # Top-left
            ])

            # Define the half-widths and half-heights as arrays for element-wise multiplication
            half_outer_size = _numpy.array([half_outer_width, half_outer_height])
            half_inner_size = _numpy.array([half_inner_width, half_inner_height])

            # Calculate the outer and inner vertices based on the offsets
            outer_vertices = _numpy.array([x, y]) + offsets * half_outer_size
            inner_vertices = _numpy.array([x, y]) + offsets * half_inner_size

            # Interleave the outer and inner vertices
            combined_vertices = _numpy.empty((outer_vertices.shape[0] * 2, 2), dtype=_numpy.float32)
            combined_vertices[0::2] = outer_vertices
            combined_vertices[1::2] = inner_vertices

            # Close the shape by adding the first vertices again
            combined_vertices = _numpy.vstack([combined_vertices, outer_vertices[0], inner_vertices[0]])

            # Apply rotation around the center
            rotation = self._rotation.get_angle(format=_Constants.RADIANS)
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            # Rotate each vertex around the center
            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], x, y, cos_theta, sin_theta) for v in combined_vertices], dtype='f4')

            self._vertices_changed = False  # Reset the flag

            if self._vbo.get_created() is False:
                self._vbo.create(rotated_vertices)
            else:
                self._vbo.update(rotated_vertices)

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

    def render(self):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._vertices_changed = True

        if self._color_changed or self._vertices_changed or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._position_changed:
            self._program.set_shader_variable('offset', self._position.get_coordinates(_Constants.OPENGL_COORDINATES))
            self._position_changed = False

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(_moderngl.TRIANGLE_STRIP)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Arc(_ShapeTemplate):
    """
    🟩 **R** - Draws an arc.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._radius = _DisplayScalarConverter()
        self._inner_radius = _DisplayScalarConverter()
        self._center = _DisplayCoordinatesConverter()
        self._start_angle = _AngleConverter()
        self._stop_angle = _AngleConverter()
        self._vertices_changed = True  # Mark vertices as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_arc"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._width = None
        self._position_changed = True
        self._initial_point_count = None

        self._resized_event = _WindowResized_EVENT()

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_width(self, width=1):
        """
        🟩 **R** -
        """
        if width <= 0:
            width = 1
        if width is None:
            width = 1
        self._width = width

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._width

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_start_angle(self, start_angle, angle_format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(start_angle) != _AngleConverter:
            self._start_angle.set_angle(start_angle, format=angle_format)

    def get_start_angle(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._start_angle is not None:
            return self._start_angle.get_angle(format=format)

    def set_stop_angle(self, stop_angle, angle_format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(stop_angle) != _AngleConverter:
            self._stop_angle.set_angle(stop_angle, format=angle_format)

    def get_stop_angle(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._stop_angle is not None:
            return self._stop_angle.get_angle(format=format)

    def set_center(self, center, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        center_input_type = type(center)
        if self._center.get_coordinate_set():
            if format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._center.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if center_input_type == _DisplayCoordinatesConverter:
                    center_coords = center.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    center_coords = [int(center[0]), int(center[1])]

                if center_coords[0] == original_coordinates[0] and center_coords[1] == original_coordinates[1]:
                    return

        self._position_changed = True
        if center_input_type != _DisplayCoordinatesConverter:
            self._center.set_coordinates(center, format=format)
        else:
            self._center = center

    def get_center(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._center is not None:
            return self._center.get_coordinates(format=format)

    def set_radius(self, value, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(value) != _DisplayScalarConverter():
            self._radius.set_point(value, format=format)

    def get_radius(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._radius is not None:
            return self._radius.get_point(format=format)

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

    def _update_buffers(self):
        """
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, radius, and width.
        """
        if self._vertices_changed:
            if self._center is None or self._radius is None or self._start_angle is None or self._stop_angle is None:
                return None  # Cannot proceed without these parameters

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

            _Registry.number_of_render_updates += 1

            center_x, center_y = [0, 0]
            start_angle = self._start_angle.get_angle(format=_Constants.RADIANS)
            stop_angle = self._stop_angle.get_angle(format=_Constants.RADIANS)
            outer_radius = self._radius.get_point(format=_Constants.OPENGL_COORDINATES)
            self._inner_radius.set_point(self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES) - self._width)
            inner_radius = self._inner_radius.get_point(format=_Constants.OPENGL_COORDINATES)  # Ensure inner radius is non-negative
            inner_radius = max(inner_radius, 0)

            # Determine the number of points to create smooth arcs for both inner and outer radii
            try:
                proportion_of_circle = abs(stop_angle - start_angle) / _Constants.TAU
                point_count = 1 + int(
                    ((_Constants.TAU / _math.asin(1 / self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES)))
                    * proportion_of_circle) * _Registry.shape_quality
                )
            except:
                point_count = 3

            if point_count < 3:
                point_count = 3

            # Generate angles for the arc
            angles = _numpy.linspace(start_angle, stop_angle, point_count)

            # Use broadcasting to calculate inner and outer vertices
            inner_vertices = _numpy.column_stack((
                center_x + inner_radius * _numpy.cos(angles),
                center_y + inner_radius * _numpy.sin(angles)
            )).astype('f4')

            outer_vertices = _numpy.column_stack((
                center_x + outer_radius * _numpy.cos(angles),
                center_y + outer_radius * _numpy.sin(angles)
            )).astype('f4')

            # Combine inner and outer vertices in a way suitable for TRIANGLE_STRIP
            vertices = _numpy.empty((2 * point_count, 2), dtype='f4')
            vertices[0::2] = outer_vertices
            vertices[1::2] = inner_vertices

            # Apply rotation if necessary
            rotation = self._rotation.get_angle(format=_Constants.RADIANS)
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)
            rotated_vertices = _numpy.array([
                self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta)
                for v in vertices
            ], dtype='f4')

            self._vertices_changed = False  # Reset the flag

            # Update VBO
            if self._initial_point_count == None or self._initial_point_count != point_count:
                self._initial_point_count = point_count
                self._vbo.quit()
                self._vbo.create(rotated_vertices)
            else:
                if self._vbo.get_created():
                    self._vbo.update(rotated_vertices)
                else:
                    self._vbo.create(rotated_vertices)

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

    def render(self):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._vertices_changed = True

        if self._color_changed or self._vertices_changed or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        self._update_buffers()

        if self._position_changed:
            self._program.set_shader_variable('offset', self._center.get_coordinates(format=_Constants.OPENGL_COORDINATES))
            self._position_changed = False

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Render the arc using GL_TRIANGLE_STRIP
        self._vao.render(_moderngl.TRIANGLE_STRIP)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end - start

class Ellipse(_ShapeTemplate):
    """
    🟩 **R** - Draws an ellipse.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._position = _DisplayCoordinatesConverter()
        self._outer_x_size = _DisplayScalarConverter()
        self._outer_y_size = _DisplayScalarConverter()
        self._rotation = _AngleConverter()
        self._inner_x_size = _DisplayScalarConverter()
        self._inner_y_size = _DisplayScalarConverter()
        self._vertices_changed = True  # Mark vertices as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_ellipse"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._math = _Math()
        self._width = None
        self._position_changed = True
        self._initial_point_count = None

        self._resized_event = _WindowResized_EVENT()

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_width(self, width=None):
        """
        🟩 **R** -
        """
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._width

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_position(self, position, position_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        position_input_type = type(position)
        if self._position.get_coordinate_set():
            if position_format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._position.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if position_input_type == _DisplayCoordinatesConverter:
                    position_coords = position.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    position_coords = [int(position[0]), int(position[1])]

                if position_coords[0] == original_coordinates[0] and position_coords[1] == original_coordinates[1]:
                    return

        self._position_changed = True
        if type(position) != _DisplayCoordinatesConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._position is not None:
            return self._position.get_coordinates(format=format)

    def set_size(self, size, size_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(size[0]) != _AngleConverter():
            self._outer_x_size.set_point(size[0], format=size_format)
        else:
            self._outer_x_size = size[0]

        if type(size[1]) != _AngleConverter():
            self._outer_y_size.set_point(size[1], format=size_format)
        else:
            self._outer_y_size = size[1]

    def get_size(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._outer_x_size.get_point_set() and self._outer_y_size.get_point_set():
            return [self._outer_x_size.get_coordinates(format=format), self._outer_y_size.get_coordinates(format=format)]

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

    def _update_buffers(self):
        """
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        if self._vertices_changed:
            if self._position.get_coordinate_set() is False or self._outer_x_size.get_point_set() is False or self._outer_y_size.get_point_set() is False:
                return None  # Cannot proceed without these parameters

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

            _Registry.number_of_render_updates += 1

            center_x, center_y = [0, 0]
            outer_size_x = self._outer_x_size.get_point(format=_Constants.OPENGL_COORDINATES)
            outer_size_y = self._outer_y_size.get_point(format=_Constants.OPENGL_COORDINATES)

            radius = self._math.pythag([self._outer_x_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES), self._outer_y_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES)])

            # Number of points to generate for the ellipse
            num_points = _Registry.shape_quality
            try:
                num_points = 1 + int((_Constants.TAU/_math.asin(1/radius))*_Registry.shape_quality)
            except:
                num_points = 3
            if num_points < 3:
                num_points = 3

            self._inner_x_size.set_point(self._outer_x_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES) - self._width*2)
            self._inner_y_size.set_point(self._outer_y_size.get_point(format=_Constants.CONVENTIONAL_COORDINATES) - self._width*2)

            inner_size_x = max(self._inner_x_size.get_point(format=_Constants.OPENGL_COORDINATES), 0)
            inner_size_y = max(self._inner_y_size.get_point(format=_Constants.OPENGL_COORDINATES), 0)

            # Generate points along the ellipse perimeter
            angles = _numpy.linspace(0, 2 * _numpy.pi, num_points)
            cos_angles = _numpy.cos(angles)
            sin_angles = _numpy.sin(angles)

            # Vectorized calculation for outer and inner vertices
            outer_vertices = _numpy.column_stack((center_x + (outer_size_x / 2) * cos_angles,
                                            center_y + (outer_size_y / 2) * sin_angles)).astype('f4')

            inner_vertices = _numpy.column_stack((center_x + (inner_size_x / 2) * cos_angles,
                                            center_y + (inner_size_y / 2) * sin_angles)).astype('f4')

            vertices = _numpy.empty((2 * num_points, 2), dtype='f4')
            vertices[0::2] = outer_vertices
            vertices[1::2] = inner_vertices

            # Apply rotation to each vertex if applicable
            rotation = self.get_rotation()
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

            self._vertices_changed = False  # Reset the flag

            if self._initial_point_count == None or self._initial_point_count != num_points:
                self._initial_point_count = num_points
                self._vbo.quit()
                self._vbo.create(rotated_vertices)
            else:
                if self._vbo.get_created():
                    self._vbo.update(rotated_vertices)
                else:
                    self._vbo.create(rotated_vertices)

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

    def render(self):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._vertices_changed = True

        if self._color_changed or self._vertices_changed or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        self._update_buffers()

        if self._position_changed:
            self._program.set_shader_variable('offset', self._position.get_coordinates(format=_Constants.OPENGL_COORDINATES))
            self._position_changed = False

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(_moderngl.TRIANGLE_STRIP)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Polygon(_ShapeTemplate):
    """
    🟩 **R** - Draws a polygon.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._points = []
        self._closed = True
        self._curved = False
        self._vertices_changed = True  # Mark vertices as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_polygon"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._math = _Math()
        self._width = None
        self._converted_inner_points = []

        self._resized_event = _WindowResized_EVENT()

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_curved(self, curved=False):
        """
        🟩 **R** -
        """
        self._curved = curved

    def get_curved(self):
        """
        🟩 **R** -
        """
        return self._curved

    def set_closed(self, closed=True):
        """
        🟩 **R** -
        """
        self._closed = closed

    def get_closed(self):
        """
        🟩 **R** -
        """
        return self._closed

    def set_points(self, points, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._vertices_changed = True
        self._points = []
        for point in points:
            if type(point) != _DisplayCoordinatesConverter:
                new_point = _DisplayCoordinatesConverter()
                new_point.set_coordinates(point, format=format)
                self._points.append(new_point)
            else:
                self._points.append(point)
            self._converted_inner_points.append(_DisplayCoordinatesConverter())

    def get_points(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        points = []
        for point in self._points:
            points.append(point.get_coordinates(format=format))
        return points

    def set_width(self, width=None):
        """
        🟩 **R** -
        """
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        """
        🟩 **R** -
        """
        return self._width

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

    def _update_buffers(self):
        """
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        if self._vertices_changed:
            if not self._points:
                return None  # No points to form the polygon

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

            _Registry.number_of_render_updates += 1

            outer_points = _numpy.array([p.get_coordinates(format=_Constants.OPENGL_COORDINATES) for p in self._points], dtype='f4')

            inner_points = []
            index = 0
            for p in self._points:
                coordinate = p.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                adjusted_x = coordinate[0] - self._width*2
                adjusted_y = coordinate[1] - self._width
                adjusted_point = [adjusted_x, adjusted_y]
                self._converted_inner_points[index].set_coordinates(adjusted_point, format=_Constants.CONVENTIONAL_COORDINATES)
                inner_points.append(self._converted_inner_points[index].get_coordinates(format=_Constants.OPENGL_COORDINATES))
                index += 1

            inner_points = _numpy.array(inner_points, dtype='f4')
            # Calculate center (average of points)
            center_x, center_y = _numpy.mean(outer_points, axis=0)

            vertices = _numpy.empty((2 * len(self._points), 2), dtype='f4')
            vertices[0::2] = outer_points
            vertices[1::2] = inner_points

            # Apply rotation
            rotation = self.get_rotation()
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

            # If closed, append the first vertex to close the loop
            if self._closed and len(rotated_vertices) > 1:
                extra_points = _numpy.array([rotated_vertices[0], rotated_vertices[1]], dtype='f4')
                rotated_vertices = _numpy.concatenate((rotated_vertices, extra_points))

            self._vertices_changed = False  # Reset the flag

            if self._vbo.get_created() is False:
                self._vbo.create(rotated_vertices)
            else:
                self._vbo.update(rotated_vertices)

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

    def render(self):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._vertices_changed = True

        if self._color_changed or self._vertices_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()

        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._closed is False and self._width is None:
            self._width = 1 # idk about this bit yet

        self._vao.render(_moderngl.TRIANGLE_STRIP)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Pixel(_ShapeTemplate):
    """
    🟩 **R** - Draws a Pixel.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._attributes.append(_Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._display = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]
        self._position = _DisplayCoordinatesConverter()
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_pixel"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._created_shape = False
        self._position_changed = True

        self._resized_event = _WindowResized_EVENT()

    def _create_shape(self):
        """
        🟩 **R** -
        """
        if self._vbo.get_created():
            self._vbo.update(_numpy.array([0, 0], dtype='f4'))
        else:
            self._vbo.create(_numpy.array([0, 0], dtype='f4'))

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_position(self, position, position_format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        position_input_type = type(position)
        if self._position.get_coordinate_set():
            if position_format == _Constants.CONVENTIONAL_COORDINATES:
                original_coordinates = self._position.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                if position_input_type == _DisplayCoordinatesConverter:
                    position_coords = position.get_coordinates(format=_Constants.CONVENTIONAL_COORDINATES)
                else:
                    position_coords = [int(position[0]), int(position[1])]

                if position_coords[0] == original_coordinates[0] and position_coords[1] == original_coordinates[1]:
                    return

        self._position_changed = True
        if type(position) != _DisplayCoordinatesConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._position is not None:
            return self._position.get_coordinates(format=format)

    def render(self, point_size=None, dynamic_rendering=True):
        """
        🟩 **R** -
        """
        start = _time.perf_counter()

        if dynamic_rendering:
            if self._position is None:
                self._logger.log_development("You didn't set a position for this shape. \
Therefore we not be rendering it to avoid any potential errors. This can be an effectively \
technique to 'prepare' a shape for rendering later on. This behavior can be controlled by \
setting the 'dynamic_rendering' key word argument to False. This message will only appear \
once to improve performance, but will continue to have an effect.")
                return None
            conventional_position = self.get_position(format=_Constants.CONVENTIONAL_COORDINATES)
            if conventional_position[0] < 0 or conventional_position[1] < 0:
                self._logger.log_development("Your position for this shape is off the \
screen, therefore as a performance improving feature we wont bother rendering it \
(because you wont see it). This behavior can be controlled by setting the \
'dynamic_rendering' key word argument to False. This message will only appear \
once to improve performance, but will continue to have an effect.")
                return None
            if conventional_position[0] > self._display.get_width() or conventional_position[1] > self._display.get_height():
                self._logger.log_development("Your position for this shape is off the \
screen, therefore as a performance improving feature we wont bother rendering it \
(because you wont see it). This behavior can be controlled by setting the \
'dynamic_rendering' key word argument to False. This message will only appear \
once to improve performance, but will continue to have an effect.")
                return None

        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._position_changed = True

        if self._color_changed or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()

        if self._created_shape is False:
            self._create_shape()
            self._created_shape = True

        if self._position_changed:
            offset = self._position.get_coordinates(format=_Constants.OPENGL_COORDINATES)
            self._program.set_shader_variable('offset', offset)
            self._position_changed = False

        if self._color_changed:
            self._program.set_shader_variable('color', self._color)
            self._color_changed = False  # Reset the flag

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

        self._vao.render(mode=_moderngl.POINTS)

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start