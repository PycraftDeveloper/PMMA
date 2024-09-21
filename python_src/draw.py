import math as _math
import time as _time
import gc as _gc

import pygame as _pygame
import pyglet as _pyglet
import moderngl as _moderngl
import numpy as _numpy

from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.constants import Constants
from pmma.python_src.number_converter import CoordinateConverter as _CoordinateConverter
from pmma.python_src.number_converter import PointConverter as _PointConverter
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.number_converter import AngleConverter as _AngleConverter
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.advmath import Math as _Math

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.error_utils import ShapeRadiusNotSpecifiedError as _ShapeRadiusNotSpecifiedError

class Line:
    """
    Draws a basic line.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        self._start = _CoordinateConverter()
        self._end = _CoordinateConverter()
        self._width = 1
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_line"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_rotation(self, rotation, format=Constants.RADIANS):
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=Constants.RADIANS):
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_start(self, start, start_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(start) != _CoordinateConverter:
            self._start.set_coordinates(start, format=start_format)
        else:
            self._start = start

    def get_start(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._start is not None:
            return self._start.get_coordinates(format=format)

    def set_end(self, end, end_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(end) != _CoordinateConverter:
            self._end.set_coordinates(end, format=end_format)
        else:
            self._end = end

    def get_end(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._end is not None:
            return self._end.get_coordinates(format=format)

    def set_color(self, color, format=Constants.RGB):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color.set_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.get_color(format=format)

    def set_width(self, width=1):
        if width <= 0:
            width = 1
        if width is None:
            width = 1
        self._width = width

    def get_width(self):
        return self._width

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def _rotate_point_around_center(self, point, center, angle):
        """
        Rotates a 2D point around a given center by the given angle in radians.

        :param point: A list or tuple representing the x and y coordinates (x, y)
        :param center: The center of rotation as (cx, cy)
        :param angle: The angle to rotate by, in radians.
        :return: The rotated point as a [x', y'] list.
        """
        # Translate the point to the origin (relative to the center)
        translated_x = point[0] - center[0]
        translated_y = point[1] - center[1]

        # Apply 2D rotation matrix
        cos_angle = _numpy.cos(angle)
        sin_angle = _numpy.sin(angle)

        x_prime = cos_angle * translated_x - sin_angle * translated_y
        y_prime = sin_angle * translated_x + cos_angle * translated_y

        # Translate the point back to its original position (relative to the center)
        return [x_prime + center[0], y_prime + center[1]]

    def _rotate_line(self, angle):
        """
        Rotates the line around its center by the given angle in radians.
        """
        # Get start and end points
        start_coords = self.get_start(format=Constants.OPENGL_COORDINATES)
        end_coords = self.get_end(format=Constants.OPENGL_COORDINATES)

        # Calculate the center of the line
        center_x = (start_coords[0] + end_coords[0]) / 2
        center_y = (start_coords[1] + end_coords[1]) / 2
        center = [center_x, center_y]

        # Rotate both start and end points around the center
        rotated_start = self._rotate_point_around_center(start_coords, center, angle)
        rotated_end = self._rotate_point_around_center(end_coords, center, angle)

        return [*rotated_start, *rotated_end]

    def _update_buffers(self):
        # This method is used to update the VBO with new vertex data if vertices have changed
        if self._vertices_changed:
            _Registry.number_of_render_updates += 1
            rotated_line_points = self._rotate_line(self._rotation.get_angle(format=Constants.RADIANS))

            # Convert vertices to a numpy array (float32 type for ModernGL compatibility)
            vertices = _numpy.array([
                *rotated_line_points
            ], dtype='f4')  # 'f4' means float32

            if self._vbo.get_created() is False:
                self._vbo.create(vertices)
            else:
                self._vbo.update(vertices)

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio())

            self._vertices_changed = False  # Reset the flag

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
            self._color_changed = False  # Reset the flag

    def render(self):
        start = _time.perf_counter()

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Set line width
        _Registry.context.line_width = self._width # unreliable

        # Render the line
        self._vao.render(mode=_moderngl.LINES)

        _Registry.context.line_width = 1 # unreliable

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class RadialPolygon:
    """
    Draws a radial polygon.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        self._point_count = None
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._radius = _PointConverter()
        self._center = _CoordinateConverter()
        self._width = None
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_radial_polygon"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._created_shape = False

    def _create_shape(self):
        if self._radius.get_point_set() is False:
            raise _ShapeRadiusNotSpecifiedError()

        if self._point_count is None:
            try:
                point_count = 1 + int((Constants.TAU/_math.asin(1/self._radius.get_point(format=Constants.CONVENTIONAL_COORDINATES)))*_Registry.shape_quality)
            except ValueError:
                point_count = 3
            if point_count < 3:
                point_count = 3
        else:
            point_count = self._point_count

        angle_step = 2 * _math.pi / point_count
        vertices = []

        rotation = self._rotation.get_angle(Constants.RADIANS)  # Get the current rotation angle

        center = [0, 0]
        radius = self._radius.get_point(Constants.OPENGL_COORDINATES)

        for i in range(point_count):
            angle = i * angle_step + rotation
            x = center[0] + radius * _math.cos(angle)
            y = center[1] + radius * _math.sin(angle)
            vertices.append([x, y])

        vertices = _numpy.array(vertices, dtype='f4')

        if self._vbo.get_created():
            self._vbo.update(vertices)
        else:
            self._vbo.create(vertices)

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_rotation(self, rotation, format=Constants.RADIANS):
        self._vertices_changed = True
        self._created_shape = False
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=Constants.RADIANS):
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_radius(self, value, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        self._created_shape = False
        if type(value) != _PointConverter():
            self._radius.set_point(value, format=format)

    def get_radius(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._radius is not None:
            return self._radius.get_point(format=format)

    def set_color(self, color, format=Constants.RGB):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color.set_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.get_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def set_point_count(self, point_count=None):
        self._vertices_changed = True
        self._point_count = point_count

    def get_point_count(self):
        return self._point_count

    def set_center(self, centre, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(centre) != _CoordinateConverter:
            self._center.set_coordinates(centre, format=format)
        else:
            self._center = centre

    def get_center(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._center is not None:
            return self._center.get_coordinates(format=format)

    def set_width(self, width=None):
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        return self._width

    def render(self):
        start = _time.perf_counter()

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        if self._created_shape is False:
            self._create_shape()
            self._created_shape = True

        if self._vertices_changed:
            offset = self._center.get_coordinates(format=Constants.OPENGL_COORDINATES)
            self._program.set_shader_variable('offset', offset)
            self._vertices_changed = False

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
            self._color_changed = False  # Reset the flag

        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio())

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._width != None:
            mode = _moderngl.LINE_STRIP
            _Registry.context.line_width = self._width # unreliable
        else:
            mode = _moderngl.TRIANGLE_FAN

        self._vao.render(mode)

        _Registry.context.line_width = 1 # unreliable

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Rectangle:
    """
    Draws a rectangle.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._position = _CoordinateConverter()
        self._size = _CoordinateConverter()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_rectangle"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._width = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_width(self, width=None):
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        return self._width

    def set_rotation(self, rotation, format=Constants.RADIANS):
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=Constants.RADIANS):
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(position) != _CoordinateConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.get_coordinates(format=format)

    def set_size(self, size, size_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(size) != _CoordinateConverter():
            self._size.set_coordinates(size, format=size_format)

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._size is not None:
            return self._size.get_coordinates(format=format)

    def set_color(self, color, format=Constants.RGB):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color.set_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.get_color(format=format)

    def _rotate_point(self, x, y, cx, cy, cos_theta, sin_theta):
        dx = x - cx
        dy = y - cy
        return [
            cx + dx * cos_theta - dy * sin_theta,
            cy + dx * sin_theta + dy * cos_theta
        ]

    def _update_buffers(self):
        """
        Calculate the vertices of the polygon based on the radius, center, point count, and rotation.
        """
        if self._vertices_changed:
            if self._position is None or self._size is None:
                return None  # Cannot proceed without these

            _Registry.number_of_render_updates += 1

            # Unpack size and position
            size = self._size.get_coordinates(Constants.OPENGL_COORDINATES)
            half_width = size[0] / 2
            half_height = size[1] / 2
            cx, cy = self._position.get_coordinates(Constants.OPENGL_COORDINATES)

            # Define the unrotated rectangle vertices relative to the center
            vertices = _numpy.array([
                [cx - half_width, cy - half_height],  # Bottom-left
                [cx + half_width, cy - half_height],  # Bottom-right
                [cx + half_width, cy + half_height],  # Top-right
                [cx - half_width, cy + half_height],  # Top-left
            ], dtype='f4')

            # Apply rotation around the center
            rotation = self._rotation.get_angle(format=Constants.RADIANS)
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            # Rotate each vertex around the center
            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], cx, cy, cos_theta, sin_theta) for v in vertices], dtype='f4')

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio())

            self._vertices_changed = False  # Reset the flag

            if self._vbo.get_created() is False:
                self._vbo.create(rotated_vertices)
            else:
                self._vbo.update(rotated_vertices)

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
            self._color_changed = False  # Reset the flag

    def render(self):
        start = _time.perf_counter()

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._width != None:
            mode = _moderngl.LINE_LOOP
            _Registry.context.line_width = self._width # unreliable
        else:
            mode = _moderngl.TRIANGLE_FAN

        self._vao.render(mode)

        _Registry.context.line_width = 1 # unreliable

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Arc:
    """
    Draws am arc.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._radius = _PointConverter()
        self._center = _CoordinateConverter()
        self._start_angle = _AngleConverter()
        self._stop_angle = _AngleConverter()
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_arc"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._width = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_width(self, width=1):
        if width <= 0:
            width = 1
        if width is None:
            width = 1
        self._width = width

    def get_width(self):
        return self._width

    def set_rotation(self, rotation, format=Constants.RADIANS):
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=Constants.RADIANS):
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_start_angle(self, start_angle, angle_format=Constants.RADIANS):
        self._vertices_changed = True
        if type(start_angle) != _AngleConverter:
            self._start_angle.set_angle(start_angle, format=angle_format)

    def get_start_angle(self, format=Constants.RADIANS):
        if self._start_angle is not None:
            return self._start_angle.get_angle(format=format)

    def set_stop_angle(self, stop_angle, angle_format=Constants.RADIANS):
        self._vertices_changed = True
        if type(stop_angle) != _AngleConverter:
            self._stop_angle.set_angle(stop_angle, format=angle_format)

    def get_stop_angle(self, format=Constants.RADIANS):
        if self._stop_angle is not None:
            return self._stop_angle.get_angle(format=format)

    def set_center(self, centre, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(centre) != _CoordinateConverter:
            self._center.set_coordinates(centre, format=format)
        else:
            self._center = centre

    def get_center(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._center is not None:
            return self._center.get_coordinates(format=format)

    def set_radius(self, value, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(value) != _PointConverter():
            self._radius.set_point(value, format=format)

    def get_radius(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._radius is not None:
            return self._radius.get_point(format=format)

    def set_color(self, color, format=Constants.RGB):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color.set_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.get_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def _rotate_point(self, x, y, cx, cy, cos_theta, sin_theta):
        dx = x - cx
        dy = y - cy
        return [
            cx + dx * cos_theta - dy * sin_theta,
            cy + dx * sin_theta + dy * cos_theta
        ]

    def _update_buffers(self):
        """
        Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        if self._vertices_changed:
            if self._center is None or self._radius is None or self._start_angle is None or self._stop_angle is None:
                return None  # Cannot proceed without these parameters

            _Registry.number_of_render_updates += 1

            center_x, center_y = self._center.get_coordinates(format=Constants.OPENGL_COORDINATES)
            start_angle = self._start_angle.get_angle(format=Constants.RADIANS)
            stop_angle = self._stop_angle.get_angle(format=Constants.RADIANS)
            radius = self._radius.get_point(format=Constants.OPENGL_COORDINATES)

            # Number of points to generate for the arc
            try:
                proportion_of_circle = abs(stop_angle - start_angle) / Constants.TAU
                point_count = 1 + int(((Constants.TAU/_math.asin(1/self._radius.get_point(format=Constants.CONVENTIONAL_COORDINATES)))*proportion_of_circle)*_Registry.shape_quality)
            except ValueError:
                point_count = 3
            if point_count < 3:
                point_count = 3

            # Generate points along the arc
            angles = _numpy.linspace(start_angle, stop_angle, point_count)
            vertices = _numpy.array([[center_x + radius * _numpy.cos(angle), center_y + radius * _numpy.sin(angle)] for angle in angles], dtype='f4')

            # Apply rotation to each vertex if applicable
            rotation = self._rotation.get_angle(format=Constants.RADIANS)
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio())

            self._vertices_changed = False  # Reset the flag

            if self._vbo.get_created() is False:
                self._vbo.create(rotated_vertices)
            else:
                self._vbo.update(rotated_vertices)

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
            self._color_changed = False  # Reset the flag

    def render(self):
        start = _time.perf_counter()

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        _Registry.context.line_width = self._width # unreliable

        # Draw the polygon using triangle fan (good for convex shapes)
        self._vao.render(_moderngl.LINE_STRIP)

        _Registry.context.line_width = 1 # unreliable

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Ellipse:
    """
    Draws an ellipse.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._position = _CoordinateConverter()
        self._size = _CoordinateConverter()
        self._rotation = _AngleConverter()
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_ellipse"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._math = _Math()
        self._width = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_width(self, width=None):
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        return self._width

    def set_rotation(self, rotation, format=Constants.RADIANS):
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=Constants.RADIANS):
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(position) != _CoordinateConverter:
            self._position.set_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.get_coordinates(format=format)

    def set_size(self, size, size_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(size) != _CoordinateConverter():
            self._size.set_coordinates(size, format=size_format)

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._size is not None:
            return self._size.get_coordinates(format=format)

    def set_color(self, color, format=Constants.RGB):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color.set_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.get_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def _rotate_point(self, x, y, cx, cy, cos_theta, sin_theta):
        dx = x - cx
        dy = y - cy
        return [
            cx + dx * cos_theta - dy * sin_theta,
            cy + dx * sin_theta + dy * cos_theta
        ]

    def _update_buffers(self):
        """
        Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        if self._vertices_changed:
            if self._position is None or self._size is None:
                return None  # Cannot proceed without these parameters

            _Registry.number_of_render_updates += 1

            center_x, center_y = self._position.get_coordinates(format=Constants.OPENGL_COORDINATES)
            size_x, size_y = self._size.get_coordinates(format=Constants.OPENGL_COORDINATES)

            radius = self._math.pythag(self._size.get_coordinates(format=Constants.CONVENTIONAL_COORDINATES))

            # Number of points to generate for the ellipse
            num_points = _Registry.shape_quality
            try:
                num_points = 1 + int((Constants.TAU/_math.asin(1/radius))*_Registry.shape_quality)
            except ValueError:
                num_points = 3
            if num_points < 3:
                num_points = 3

            # Generate points along the ellipse perimeter
            angles = _numpy.linspace(0, 2 * _numpy.pi, num_points)
            vertices = _numpy.array([[center_x + (size_x / 2) * _numpy.cos(angle), center_y + (size_y / 2) * _numpy.sin(angle)] for angle in angles], dtype='f4')

            # Apply rotation to each vertex if applicable
            rotation = self.get_rotation()
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio())

            self._vertices_changed = False  # Reset the flag

            if self._vbo.get_created() is False:
                self._vbo.create(rotated_vertices)
            else:
                self._vbo.update(rotated_vertices)

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
            self._color_changed = False  # Reset the flag

    def render(self):
        start = _time.perf_counter()

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._width != None:
            mode = _moderngl.LINE_STRIP
            _Registry.context.line_width = self._width # unreliable
        else:
            mode = _moderngl.TRIANGLE_FAN

        self._vao.render(mode)

        _Registry.context.line_width = 1 # unreliable

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Polygon:
    """
    Draws a polygon.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._points = []
        self._closed = True
        self._curved = False
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_polygon"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._math = _Math()
        self._width = None

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_rotation(self, rotation, format=Constants.RADIANS):
        self._vertices_changed = True
        if type(rotation) != _AngleConverter:
            self._rotation.set_angle(rotation, format=format)
        else:
            self._rotation = rotation

    def get_rotation(self, format=Constants.RADIANS):
        if self._rotation is not None:
            return self._rotation.get_angle(format=format)

    def set_curved(self, curved=False):
        self._curved = curved

    def get_curved(self):
        return self._curved

    def set_closed(self, closed=True):
        self._closed = closed

    def get_closed(self):
        return self._closed

    def set_points(self, points, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        self._points = []
        for point in points:
            if type(point) != _CoordinateConverter:
                new_point = _CoordinateConverter()
                new_point.set_coordinates(point, format=format)
                self._points.append(new_point)
            else:
                self._points.append(point)

    def get_points(self, format=Constants.CONVENTIONAL_COORDINATES):
        points = []
        for point in self._points:
            points.append(point.get_coordinates(format=format))
        return points

    def set_color(self, color, format=Constants.RGB):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color.set_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.get_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def set_width(self, width=None):
        if width <= 0:
            width = None
        self._width = width

    def get_width(self):
        return self._width

    def _rotate_point(self, x, y, cx, cy, cos_theta, sin_theta):
        dx = x - cx
        dy = y - cy
        return [
            cx + dx * cos_theta - dy * sin_theta,
            cy + dx * sin_theta + dy * cos_theta
        ]

    def _update_buffers(self):
        """
        Calculate the vertices for the arc based on start_angle, stop_angle, center, and radius.
        """
        if self._vertices_changed:
            if not self._points:
                return None  # No points to form the polygon

            _Registry.number_of_render_updates += 1

            points = _numpy.array([p.get_coordinates(format=Constants.OPENGL_COORDINATES) for p in self._points], dtype='f4')

            # Calculate center (average of points)
            center_x, center_y = _numpy.mean(points, axis=0)

            # Apply rotation
            rotation = self.get_rotation()
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in points], dtype='f4')

            # If closed, append the first vertex to close the loop
            if self._closed and len(rotated_vertices) > 1:
                rotated_vertices = _numpy.append(rotated_vertices, [rotated_vertices[0]], axis=0)

            self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio())

            self._vertices_changed = False  # Reset the flag

            if self._vbo.get_created() is False:
                self._vbo.create(rotated_vertices)
            else:
                self._vbo.update(rotated_vertices)

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
            self._color_changed = False  # Reset the flag

    def render(self):
        start = _time.perf_counter()

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._closed is False and self._width is None:
            self._width = 1

        if self._width != None:
            mode = _moderngl.LINE_LOOP if self._closed else _moderngl.LINE_STRIP
            _Registry.context.line_width = self._width # unreliable
        else:
            mode = _moderngl.TRIANGLE_FAN

        self._vao.render(mode)

        _Registry.context.line_width = 1 # unreliable

        end = _time.perf_counter()
        _Registry.total_time_spent_drawing += end-start

class Pixel:
    """
    Draws a Pixel.
    """
    def __init__(self):
        _initialize(self)

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._color = _ColorConverter()
        if Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            self._surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        else:
            self._surface = None
        self._position = _CoordinateConverter()
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_pixel"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._created_shape = False

    def _create_shape(self):
        if self._vbo.get_created():
            self._vbo.update(_numpy.array([0, 0], dtype='f4'))
        else:
            self._vbo.create(_numpy.array([0, 0], dtype='f4'))

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        if type(position) != _CoordinateConverter:
            self._vertices_changed = self._position.set_coordinates(position, format=position_format)
        else:
            self._vertices_changed = self._position.set_coordinates(position.get_coordinates(format=position_format))

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.get_coordinates(format=format)

    def set_color(self, color, format=Constants.RGB):
        if type(color) != _ColorConverter:
            self._color_changed = self._color.set_color(color, format=format)
        else:
            self._color_changed = self._color.set_color(color.get_color(format=format))

    def get_color(self, format=Constants.RGB):
        if self._color is not None:
            return self._color.get_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def render(self, point_size=None, dynamic_rendering=True):
        start = _time.perf_counter()

        if dynamic_rendering:
            if self._position is None:
                self._logger.log_development("You didn't set a position for this shape. \
Therefore we not be rendering it to avoid any potential errors. This can be an effectively \
technique to 'prepare' a shape for rendering later on. This behavior can be controlled by \
setting the 'dynamic_rendering' key word argument to False. This message will only appear \
once to improve performance, but will continue to have an effect.")
                return None
            conventional_position = self.get_position(format=Constants.CONVENTIONAL_COORDINATES)
            if conventional_position[0] < 0 or conventional_position[1] < 0:
                self._logger.log_development("Your position for this shape is off the \
screen, therefore as a performance improving feature we wont bother rendering it \
(because you wont see it). This behavior can be controlled by setting the \
'dynamic_rendering' key word argument to False. This message will only appear \
once to improve performance, but will continue to have an effect.")
                return None
            if conventional_position[0] > self._surface.get_width() or conventional_position[1] > self._surface.get_height():
                self._logger.log_development("Your position for this shape is off the \
screen, therefore as a performance improving feature we wont bother rendering it \
(because you wont see it). This behavior can be controlled by setting the \
'dynamic_rendering' key word argument to False. This message will only appear \
once to improve performance, but will continue to have an effect.")
                return None

        self._surface.update_attempted_render_calls(1)

        if self._color_changed or self._vertices_changed:
            self._surface.set_refresh_optimization_override(True)

        if self._surface.get_clear_called_but_skipped():
            return None

        self._surface.get_2D_hardware_accelerated_surface()

        if self._created_shape is False:
            self._create_shape()
            self._created_shape = True

        if self._vertices_changed:
            offset = self._position.get_coordinates(format=Constants.OPENGL_COORDINATES)
            self._program.set_shader_variable('offset', offset)
            self._vertices_changed = False

        if self._color_changed:
            color = self._color.get_color(format=Constants.SMALL_RGBA)
            self._program.set_shader_variable('color', color)
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