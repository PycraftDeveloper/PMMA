import math as _math
import time as _time
import gc as _gc

import pygame as _pygame
import pyglet as _pyglet
import moderngl as _moderngl
import numpy as _numpy

from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import ColorBufferObject as _ColorBufferObject
from pmma.python_src.opengl import IndexBufferObject as _IndexBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.constants import Constants
from pmma.python_src.general import *
from pmma.python_src.number_converter import CoordinateConverter as _CoordinateConverter
from pmma.python_src.number_converter import PointConverter as _PointConverter
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.number_converter import AngleConverter as _AngleConverter
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

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

        self._color = None
        self._start = None
        self._end = None
        self._width = 1
        self._surface = None
        self._vertices_changed = True  # Mark vertices as changed initially
        self._color_changed = True  # Mark color as changed initially
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_line"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()

    def set_start(self, start, start_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(start) != _CoordinateConverter:
            self._start = _CoordinateConverter()
            self._start.input_coordinates(start, format=start_format)
        else:
            self._start = start

    def get_start(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._start is not None:
            return self._start.output_coordinates(format=format)

    def set_end(self, end, end_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(end) != _CoordinateConverter:
            self._end = _CoordinateConverter()
            self._end.input_coordinates(end, format=end_format)
        else:
            self._end = end

    def get_end(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._end is not None:
            return self._end.output_coordinates(format=format)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def set_width(self, width=1):
        self._width = width

    def get_width(self):
        return self._width

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def _update_buffers(self):
        # This method is used to update the VBO with new vertex data if vertices have changed
        if self._vertices_changed:
            start_coords = self.get_start(format=Constants.OPENGL_COORDINATES)
            end_coords = self.get_end(format=Constants.OPENGL_COORDINATES)

            # Convert vertices to a numpy array (float32 type for ModernGL compatibility)
            vertices = _numpy.array([
                *start_coords,  # Start position
                *end_coords  # End position
            ], dtype='f4')  # 'f4' means float32

            if self._vbo.get_created() is False:
                self._vbo.create(vertices)
            else:
                self._vbo.update(vertices)

            self._program.get_program()['aspect_ratio'].value = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_aspect_ratio()

            self._vertices_changed = False  # Reset the flag

        if self._color_changed:
            color = self.get_color(format=Constants.SMALL_RGBA)
            self._program.get_program()['color'].value = tuple(color)  # Set uniform color in the shader
            self._color_changed = False  # Reset the flag

    def render(self):
        _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        self._update_buffers()

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Set line width
        _Registry.context.line_width = self.get_width() # unreliable

        # Render the line
        self._vao.render(mode=_moderngl.LINES)

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

        self._color = None
        self._point_count = None
        self._surface = None
        self._radius = None
        self._center = None
        self._width = None
        self._radius = None

    def set_radius(self, value, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(value) != _PointConverter():
            self._radius = _PointConverter()
            self._radius.input_point(value, format=format)

    def get_radius(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._radius is not None:
            return self._radius.output_point(format=format)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def set_point_count(self, point_count=None):
        self._vertices_changed = True
        if self._point_count is None:
            self._point_count = 1 + int((Constants.TAU/_math.asin(1/self._radius))*_Registry.shape_quality)
        self._point_count = point_count

    def get_point_count(self):
        return self._point_count

    def set_center(self, centre, format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(centre) != _CoordinateConverter:
            self._center = _CoordinateConverter()
            self._center.input_coordinates(centre, format=format)
        else:
            self._center = centre

    def get_center(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._center is not None:
            return self._center.output_coordinates(format=format)

    def set_width(self, width=None):
        self._width = width

    def get_width(self):
        return self._width

    def render(self):
        print("Not yet finished!!!")

class Rect:
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

        self._color = None
        self._surface = None
        self._position = None
        self._size = None

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(position) != _CoordinateConverter:
            self._position = _CoordinateConverter()
            self._position.input_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.output_coordinates(format=format)

    def set_size(self, size, size_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(size) != _PointConverter():
            self._size = _PointConverter()
            self._size.input_point(size, format=size_format)

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._size is not None:
            return self._size.output_point(format=format)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def render(self):
        print("Not yet finished!!!")

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

        self._color = None
        self._surface = None
        self._position = None
        self._size = None
        self._start_angle = None
        self._stop_angle = None

    def set_start_angle(self, start_angle, angle_format=Constants.RADIANS):
        self._vertices_changed = True
        if type(start_angle) != _AngleConverter:
            self._start_angle = _AngleConverter()
            self._start_angle.set_angle(start_angle, format=angle_format)

    def get_start_angle(self, format=Constants.RADIANS):
        if self._start_angle is not None:
            return self._start_angle.get_angle(format=format)

    def set_stop_angle(self, stop_angle, angle_format=Constants.RADIANS):
        self._vertices_changed = True
        if type(stop_angle) != _AngleConverter:
            self._stop_angle = _AngleConverter()
            self._stop_angle.set_angle(stop_angle, format=angle_format)

    def get_stop_angle(self, format=Constants.RADIANS):
        if self._stop_angle is not None:
            return self._stop_angle.get_angle(format=format)

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(position) != _CoordinateConverter:
            self._position = _CoordinateConverter()
            self._position.input_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.output_coordinates(format=format)

    def set_size(self, size, size_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(size) != _PointConverter():
            self._size = _PointConverter()
            self._size.input_point(size, format=size_format)

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._size is not None:
            return self._size.output_point(format=format)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def render(self):
        print("Not yet finished!!!")

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

        self._color = None
        self._surface = None
        self._position = None
        self._size = None

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(position) != _CoordinateConverter:
            self._position = _CoordinateConverter()
            self._position.input_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.output_coordinates(format=format)

    def set_size(self, size, size_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(size) != _PointConverter():
            self._size = _PointConverter()
            self._size.input_point(size, format=size_format)

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._size is not None:
            return self._size.output_point(format=format)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def render(self):
        print("Not yet finished!!!")

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

        self._color = None
        self._surface = None
        self._points = []
        self._closed = True
        self._curved = False

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
                new_point.input_coordinates(point, format=format)
                self._points.append(new_point)
            else:
                self._points.append(point)

    def get_points(self, format=Constants.CONVENTIONAL_COORDINATES):
        points = []
        for point in self._points:
            points.append(point.output_coordinates(format=format))
        return points

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def render(self):
        print("Not yet finished!!!")

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

        self._color = None
        self._surface = None
        self._position = None

    def set_position(self, position, position_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(position) != _CoordinateConverter:
            self._position = _CoordinateConverter()
            self._position.input_coordinates(position, format=position_format)
        else:
            self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if self._position is not None:
            return self._position.output_coordinates(format=format)

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _ColorConverter:
            self._color = _ColorConverter()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        if self._color is not None:
            return self._color.output_color(format=format)

    def set_surface(self, surface=None):
        if surface is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            surface = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._surface = surface

    def get_surface(self):
        return self._surface

    def render(self):
        print("Not yet finished!!!")