import math as _math
import time as _time
import gc as _gc

import pygame as _pygame
import pygame.gfxdraw as _gfxdraw
import pyglet as _pyglet

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.constants import Constants
from pmma.python_src.color import Color as _Color
from pmma.python_src.general import *
from pmma.python_src.coordinate import Coordinate as _Coordinate

from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

class Line:
    """
    Draws a line.
    """
    def __init__(
            self,
            color=None,
            color_format=Constants.AUTODETECT,
            start=None,
            start_format=Constants.CONVENTIONAL_COORDINATES,
            end=None,
            end_format=Constants.CONVENTIONAL_COORDINATES,
            width=1,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=color_format)
        else:
            self._color = color

        if type(start) != _Coordinate:
            self._start = _Coordinate()
            self._start.input_coordinates(start, format=start_format)
        else:
            self._start = start

        if type(end) != _Coordinate:
            self._end = _Coordinate()
            self._end.input_coordinates(end, format=end_format)
        else:
            self._end = end

        self._width = width
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_start(self, start, start_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(start) != _Coordinate:
            self._start = _Coordinate()
            self._start.input_coordinates(start, format=start_format)
        else:
            self._start = start

    def get_start(self, format=Constants.CONVENTIONAL_COORDINATES):
        return self._start.output_coordinates(format=format)

    def set_end(self, end, end_format=Constants.CONVENTIONAL_COORDINATES):
        self._vertices_changed = True
        if type(end) != _Coordinate:
            self._end = _Coordinate()
            self._end.input_coordinates(end, format=end_format)
        else:
            self._end = end

    def get_end(self, format=Constants.CONVENTIONAL_COORDINATES):
        return self._end.output_coordinates(format=format)

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None #returnable

class Lines:
    def __init__(
            self,
            color=None,
            points=None,
            width=1,
            closed=False,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._points = points
        self._width = width
        self._closed = closed
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_points(self, points):
        self._vertices_changed = True
        self._points = points

    def get_points(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._points

        coordinate_converter = _Coordinate()
        points = []
        for point in self._points:
            coordinate_converter.input_coordinates(point)
            points.append(coordinate_converter.output_coordinates(format=format))
        return points

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_closed(self, closed):
        self._vertices_changed = True
        self._closed = closed

    def get_closed(self):
        return self._closed

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None #returnable

class AdvancedPolygon:
    def __init__(
            self,
            color=None,
            centre=None,
            radius=None,
            number_of_sides=None,
            rotation_angle=0,
            width=0,
            wire_frame=False,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._center = centre
        self._radius = radius
        self._number_of_sides = number_of_sides
        self._rotation_angle = rotation_angle
        self._width = width
        self._wire_frame = wire_frame
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_center(self, centre):
        self._vertices_changed = True
        self._center = centre

    def get_center(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._center

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._center)
        return coordinate_converter.output_coordinates(format=format)

    def set_radius(self, radius):
        self._vertices_changed = True
        self._radius = radius

    def get_radius(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._radius
        elif format == Constants.OPENGL_COORDINATES:
            return self._radius / (self._canvas.get_height() / 2)

    def set_number_of_sides(self, number_of_sides):
        self._vertices_changed = True
        self._number_of_sides = number_of_sides

    def get_number_of_sides(self):
        return self._number_of_sides

    def set_rotation_angle(self, rotation_angle):
        self._vertices_changed = True
        self._rotation_angle = rotation_angle

    def get_rotation_angle(self):
        return self._rotation_angle

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_wire_frame(self, wire_frame):
        self._wire_frame = wire_frame

    def get_wire_frame(self):
        return self._wire_frame

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None #returnable

class RotatedRect: # https://stackoverflow.com/a/73855696
    """
    Draw a rectangle, centered at x, y.
    All credit to Tim Swast for this function!

    Arguments:
    x (int/float):
        The x coordinate of the center of the shape.
    y (int/float):
        The y coordinate of the center of the shape.
    radius (int/float):
        The radius of the rectangle.
    height (int/float):
        The height of the rectangle.
    color (str):
        Name of the fill color, in HTML format.
    """
    def __init__(
            self,
            color=None,
            center_of_rect=None,
            radius=None,
            height=None,
            rotation_angle=0,
            width=0,
            canvas=None):
        """
        Draw a rectangle, centered at x, y.
        All credit to Tim Swast for this function!

        Arguments:
        x (int/float):
            The x coordinate of the center of the shape.
        y (int/float):
            The y coordinate of the center of the shape.
        radius (int/float):
            The radius of the rectangle.
        height (int/float):
            The height of the rectangle.
        color (str):
            Name of the fill color, in HTML format.
        """
        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._center_of_rect = center_of_rect
        self._radius = radius
        self._height = height
        self._rotation_angle = rotation_angle
        self._width = width
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_center_of_rect(self, center_of_rect):
        self._vertices_changed = True
        self._center_of_rect = center_of_rect

    def get_center_of_rect(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._center_of_rect

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._center_of_rect)
        return coordinate_converter.output_coordinates(format=format)

    def set_radius(self, radius):
        self._vertices_changed = True
        self._radius = radius

    def get_radius(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._radius
        elif format == Constants.OPENGL_COORDINATES:
            return self._radius / (self._canvas.get_height() / 2)

    def set_height(self, height):
        self._vertices_changed = True
        self._height = height

    def get_height(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._height
        elif format == Constants.OPENGL_COORDINATES:
            return self._height / (self._canvas.get_height() / 2) # not sure if this this right.

    def set_rotation_angle(self, rotation_angle):
        self._rotation_angle = rotation_angle

    def get_rotation_angle(self):
        return self._rotation_angle

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        """
        Draw a rectangle, centered at x, y.
        All credit to Tim Swast for this function!

        Arguments:
        x (int/float):
            The x coordinate of the center of the shape.
        y (int/float):
            The y coordinate of the center of the shape.
        radius (int/float):
            The radius of the rectangle.
        height (int/float):
            The height of the rectangle.
        color (str):
            Name of the fill color, in HTML format.
        """
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1
        x, y = self._center_of_rect
        points = []

        # The distance from the center of the rectangle to
        # one of the corners is the same for each corner.
        radius = _math.sqrt((self._height / 2)**2 + (radius / 2)**2)

        # Get the angle to one of the corners with respect
        # to the x-axis.
        angle = _math.atan2(self._height / 2, radius / 2)

        # Transform that angle to reach each corner of the rectangle.
        angles = [angle, -angle + _math.pi, angle + _math.pi, -angle]

        # Convert rotation from degrees to radians.
        rot_radians = (_math.pi / 180) * self._rotation_angle

        # Calculate the coordinates of each point.
        for angle in angles:
            y_offset = -1 * radius * _math.sin(angle + rot_radians)
            x_offset = radius * _math.cos(angle + rot_radians)
            points.append((x + x_offset, y + y_offset))

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None# returnable

class Rect:
    def __init__(
            self,
            color=None,
            position=None,
            size=None,
            width=0,
            border_radius=-1,
            border_top_left_radius=-1,
            border_top_right_radius=-1,
            border_bottom_left_radius=-1,
            border_bottom_right_radius=-1,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._position = position
        self._size = size
        self._width = width
        self._border_radius = border_radius
        self._border_top_left_radius = border_top_left_radius
        self._border_top_right_radius = border_top_right_radius
        self._border_bottom_left_radius = border_bottom_left_radius
        self._border_bottom_right_radius = border_bottom_right_radius
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def set_position(self, position):
        self._vertices_changed = True
        self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._position

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._position)
        return coordinate_converter.output_coordinates(format=format)

    def set_size(self, size):
        self._vertices_changed = True
        self._size = size

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._size

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._size)
        return coordinate_converter.output_coordinates(format=format)

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_border_radius(self, border_radius):
        self._vertices_changed = True
        self._border_radius = border_radius

    def get_border_radius(self):
        return self._border_radius

    def set_border_top_left_radius(self, border_top_left_radius):
        self._vertices_changed = True
        self._border_top_left_radius = border_top_left_radius

    def get_border_top_left_radius(self):
        return self._border_top_left_radius

    def set_border_top_right_radius(self, border_top_right_radius):
        self._vertices_changed = True
        self._border_top_right_radius = border_top_right_radius

    def get_border_top_right_radius(self):
        return self._border_top_right_radius

    def set_border_bottom_left_radius(self, border_bottom_left_radius):
        self._vertices_changed = True
        self._border_bottom_left_radius = border_bottom_left_radius

    def get_border_bottom_left_radius(self):
        return self._border_bottom_left_radius

    def set_border_bottom_right_radius(self, border_bottom_right_radius):
        self._vertices_changed = True
        self._border_bottom_right_radius = border_bottom_right_radius

    def get_border_bottom_right_radius(self):
        return self._border_bottom_right_radius

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None# returnable

class Circle:
    def __init__(
            self,
            color=None,
            center=None,
            radius=None,
            width=0,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._center = center
        self._radius = radius
        self._width = width
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_center(self, center):
        self._vertices_changed = True
        self._center = center

    def get_center(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._center

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._center)
        return coordinate_converter.output_coordinates(format=format)

    def set_radius(self, radius):
        self._vertices_changed = True
        self._radius = radius

    def get_radius(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._radius
        elif format == Constants.OPENGL_COORDINATES:
            return self._radius / (self._canvas.get_height() / 2)

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        if abs(self._radius) < 1:
            end_time = _time.perf_counter()
            _Registry.total_time_spent_drawing += end_time - start_time
            self._logger.log_development("You have created a circle with radius of less than 1. \
This means that the circle wont be visible onscreen, so we exit without even trying \
for improved performance.")
            return

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None# returnable

class Arc:
    def __init__(
            self,
            color=None,
            position=None,
            size=None,
            start_angle=None,
            stop_angle=None,
            width=1,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._position = position
        self._size = size
        self._start_angle = start_angle
        self._stop_angle = stop_angle
        self._width = width
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_position(self, position):
        self._vertices_changed = True
        self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._position

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._position)
        return coordinate_converter.output_coordinates(format=format)

    def set_size(self, size):
        self._vertices_changed = True
        self._size = size

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._size

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._size)
        return coordinate_converter.output_coordinates(format=format)

    def set_start_angle(self, start_angle):
        self._vertices_changed = True
        self._start_angle = start_angle

    def get_start_angle(self):
        return self._start_angle

    def set_stop_angle(self, stop_angle):
        self._vertices_changed = True
        self._stop_angle = stop_angle

    def get_stop_angle(self):
        return self._stop_angle

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None# returnable

class Polygon:
    def __init__(
            self,
            color=None,
            points=None,
            width=0,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._points = points
        self._width = width
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_points(self, points):
        self._vertices_changed = True
        self._points = points

    def get_points(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._points

        coordinate_converter = _Coordinate()
        points = []
        for point in self._points:
            coordinate_converter.input_coordinates(point)
            points.append(coordinate_converter.output_coordinates(format=format))
        return points

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None# returnable

class Ellipse:
    def __init__(
            self,
            color=None,
            position=None,
            size=None,
            width=0,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._position = position
        self._size = size
        self._width = width
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_position(self, position):
        self._vertices_changed = True
        self._position = position

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._position

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._position)
        return coordinate_converter.output_coordinates(format=format)

    def set_size(self, size):
        self._vertices_changed = True
        self._size = size

    def get_size(self, format=Constants.CONVENTIONAL_COORDINATES): # radius = max(x, y)/2
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._size

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._size)
        return coordinate_converter.output_coordinates(format=format)

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None# returnable

class Pixel:
    def __init__(
            self,
            color=None,
            position=None,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._position = position
        self._canvas = canvas

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_position(self, point):
        self._vertices_changed = True
        self._position = point

    def get_position(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._position

        coordinate_converter = _Coordinate()
        coordinate_converter.input_coordinates(self._position)
        return coordinate_converter.output_coordinates(format=format)

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None #returnable

class CurvedLines:
    def __init__(
            self,
            color=None,
            points=None,
            steps=2,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if _Registry.display_mode_set is False:
            _Registry.display_mode_set = True
            _Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            if _Registry.display_mode == Constants.PYGAME:
                _Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._points = points
        self._steps = steps
        self._canvas = canvas

        self._alternative = Lines()

        self._hardware_accelerated_data = {"vertices": None, "indices": None, "colors": None}

        self._color_changed = True
        self._vertices_changed = True

    def set_vertices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["vertices"] = data

    def set_indices_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["indices"] = data

    def set_colors_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data["colors"] = data

    def get_hardware_accelerated_data(self):
        return self._hardware_accelerated_data

    def set_hardware_accelerated_data(self, data):
        self._hardware_accelerated_data = data

    def set_color_changed(self, value=False):
        self._color_changed = value

    def set_vertices_changed(self, value=False):
        self._vertices_changed = value

    def get_color_changed(self):
        return self._color_changed

    def get_color(self, format=Constants.RGBA):
        return self._color.output_color(format=format)

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_points(self, points):
        self._vertices_changed = True
        self._points = points

    def get_points(self, format=Constants.CONVENTIONAL_COORDINATES):
        if format == Constants.CONVENTIONAL_COORDINATES:
            return self._points

        coordinate_converter = _Coordinate()
        points = []
        for point in self._points:
            coordinate_converter.input_coordinates(point)
            points.append(coordinate_converter.output_coordinates(format=format))
        return points

    def set_steps(self, steps):
        self._vertices_changed = True
        self._steps = steps

    def get_steps(self):
        return self._steps

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in _Registry.pmma_module_spine.keys():
            canvas = _Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def draw(self):
        start_time = _time.perf_counter()
        _Registry.number_of_draw_calls += 1

        end_time = _time.perf_counter()
        _Registry.total_time_spent_drawing += end_time - start_time
        return None #returnable