import math as _math
import time as _time
import gc as _gc

import pygame as _pygame
import pygame.gfxdraw as _gfxdraw
import pyglet as _pyglet

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.color import Color as _Color
from pmma.python_src.general import *

from pmma.python_src.utility.general_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger

class Line:
    """
    Draws a line.
    """
    def __init__(
            self,
            color=None,
            start=None,
            end=None,
            width=1,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                self._logger.log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._start = start
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

    def get_color(self) -> "_Color":
        return self._color

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

    def set_start(self, start):
        self._vertices_changed = True
        self._start = start

    def get_start(self):
        return self._start

    def set_end(self, end):
        self._vertices_changed = True
        self._end = end

    def get_end(self):
        return self._end

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1
        if Registry.display_mode == Constants.PYGAME:
            if Registry.do_anti_aliasing:
                returnable = _pygame.draw.aaline(
                    self._canvas.get_pygame_surface().get_pygame_surface(),
                    self._color.output_color(Constants.RGBA),
                    self._start,
                    self._end,
                    self._width)

            else:
                returnable = _pygame.draw.line(
                    self._canvas.get_pygame_surface().get_pygame_surface(),
                    self._color.output_color(Constants.RGBA),
                    self._start,
                    self._end,
                    self._width)
        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_points(self):
        return self._points

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
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            if len(self._points) < 2:
                end_time = _time.perf_counter()
                Registry.total_time_spent_drawing += end_time - start_time
                return
            if Registry.do_anti_aliasing:
                returnable = _pygame.draw.aalines(
                    self._canvas.get_pygame_surface().get_pygame_surface(),
                    self._color.output_color(Constants.RGBA),
                    self._closed,
                    self._points,
                    self._width)

            else:
                returnable = _pygame.draw.lines(
                    self._canvas.get_pygame_surface().get_pygame_surface(),
                    self._color.output_color(Constants.RGBA),
                    self._closed,
                    self._points,
                    self._width)
        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color)
        else:
            self._color = color

        self._centre = centre
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

    def get_color(self):
        return self._color

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def set_centre(self, centre):
        self._vertices_changed = True
        self._centre = centre

    def get_center(self):
        return self._centre

    def set_radius(self, radius):
        self._vertices_changed = True
        self._radius = radius

    def get_radius(self):
        return self._radius

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
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1
        if self._wire_frame:
            for i in range(0, self._number_of_sides):
                if Registry.display_mode == Constants.PYGAME:
                    _pygame.draw.line(
                        self._canvas.get_pygame_surface().get_pygame_surface(),
                        self._color.output_color(Constants.RGBA),
                        self._centre, (
                            _math.cos(i / self._number_of_sides * Constants.TAU) * self._radius + self._centre[0],
                            _math.sin(i / self._number_of_sides * Constants.TAU) * self._radius + self._centre[1]))

        points = [
            (_math.cos(i / self._number_of_sides * Constants.TAU + self._rotation_angle) * self._radius + self._centre[0],
                _math.sin(i / self._number_of_sides * Constants.TAU + self._rotation_angle) * self._radius + self._centre[1]) for i in range(0, self._number_of_sides)]

        if self._wire_frame:
            width = 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.polygon(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                points,
                width=width), points
        else:
            return None, self._cache
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_center_of_rect(self):
        return self._center_of_rect

    def set_radius(self, radius):
        self._vertices_changed = True
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_height(self, height):
        self._vertices_changed = True
        self._height = height

    def get_height(self):
        return self._height

    def set_rotation_angle(self, rotation_angle):
        self._rotation_angle = rotation_angle

    def get_rotation_angle(self):
        return self._rotation_angle

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1
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

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.polygon(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                points,
                width=self._width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

    def get_vertices_changed(self):
        return self._vertices_changed

    def set_color(self, color, format=Constants.AUTODETECT):
        self._color_changed = True
        if type(color) != _Color:
            self._color = _Color()
            self._color.input_color(color, format=format)
        else:
            self._color = color

    def get_color(self):
        return self._color

    def set_position(self, position):
        self._vertices_changed = True
        self._position = position

    def get_position(self):
        return self._position

    def set_size(self, size):
        self._vertices_changed = True
        self._size = size

    def get_size(self):
        return self._size

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
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            rect = _pygame.Rect(*self._position, *self._size)

            returnable = _pygame.draw.rect(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                rect,
                self._width,
                self._border_radius,
                self._border_top_left_radius,
                self._border_top_right_radius,
                self._border_bottom_left_radius,
                self._border_bottom_right_radius)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_center(self):
        return self._center

    def set_radius(self, radius):
        self._vertices_changed = True
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if abs(self._radius) < 1:
            end_time = _time.perf_counter()
            Registry.total_time_spent_drawing += end_time - start_time
            self._logger.log_development("You have created a circle with radius of less than 1. \
This means that the circle wont be visible onscreen, so we exit without even trying \
for improved performance.")
            return

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.circle(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                self._center,
                abs(self._radius),
                self._width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_position(self):
        return self._position

    def set_size(self, size):
        self._vertices_changed = True
        self._size = size

    def get_size(self):
        return self._size

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
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            rect = _pygame.Rect(*self._position, *self._size)
            returnable = _pygame.draw.arc(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                rect,
                self._start_angle,
                self._stop_angle,
                self._width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

class Polygon:
    def __init__(
            self,
            color=None,
            points=None,
            width=0,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_points(self):
        return self._points

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.polygon(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                self._points,
                self._width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

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

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_position(self):
        return self._position

    def set_size(self, size):
        self._vertices_changed = True
        self._size = size

    def get_size(self):
        return self._size

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            rect = _pygame.Rect(*self._position, *self._size)
            returnable = _pygame.draw.ellipse(
                self._canvas.get_pygame_surface().get_pygame_surface(),
                self._color.output_color(Constants.RGBA),
                rect,
                self._width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

class Pixel:
    def __init__(
            self,
            color=None,
            position=None,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_position(self):
        return self._position

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            try:
                returnable = _gfxdraw.pixel(
                    self._canvas.get_pygame_surface().get_pygame_surface(),
                    self._color.output_color(Constants.RGBA),
                    self._position), True

            except:
                temp_rect = _pygame.rect.Rect(
                    *self._position,
                    1,
                    1)

                returnable = _pygame.draw.rect(
                    self._canvas.get_pygame_surface().get_pygame_surface(),
                    self._color.output_color(Constants.RGBA),
                    temp_rect,
                    1), False

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

class CurvedLines:
    def __init__(
            self,
            color=None,
            points=None,
            steps=2,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        self._attributes.append(Constants.RENDER_PIPELINE_ABLE)

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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

    def get_color(self):
        return self._color

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

    def get_points(self):
        return self._points

    def set_steps(self, steps):
        self._vertices_changed = True
        self._steps = steps

    def get_steps(self):
        return self._steps

    def set_canvas(self, canvas):
        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

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
        Registry.number_of_draw_calls += 1

        if Registry.display_mode == Constants.PYGAME:
            if len(self._points) > 2:
                try:
                    returnable = _gfxdraw.bezier(
                        self._canvas.get_pygame_surface().get_pygame_surface(),
                        self._points,
                        self._steps,
                        self._color.output_color(Constants.RGBA)), True

                    end_time = _time.perf_counter()
                    Registry.total_time_spent_drawing += end_time - start_time
                    return returnable
                except:
                    pass

            self._alternative.set_canvas(self._canvas)
            self._alternative.set_color(self._color)
            self._alternative.set_points(self._points)
            self._alternative.set_width(1)
            self._alternative.set_closed(False)

            returnable = self._alternative.draw(), False

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

class Draw:
    def __init__(
            self,
            canvas=None):

        _initialize(self)

        self._logger = _InternalLogger()

        if Registry.display_mode_set is False:
            Registry.display_mode_set = True
            Registry.display_mode = Constants.PYGAME
            self._logger.log_development("You haven't yet set a display mode, \
therefore it has been decided for you! To manually pick a display mode, call \
'pmma.set_display_mode()' with your preferred display mode. The default display \
mode is Pygame.")

        if Registry.displayed_pygame_start_message is False:
            Registry.displayed_pygame_start_message = True
            if Registry.display_mode == Constants.PYGAME:
                Registry.pmma_module_spine[Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(Registry.pygame_launch_message)
                _pygame.init()

        if canvas is None and Constants.DISPLAY_OBJECT in Registry.pmma_module_spine.keys():
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

        self._canvas = canvas

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def line(
            self,
            color,
            start,
            end,
            width,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            if Registry.do_anti_aliasing:
                returnable = _pygame.draw.aaline(
                    canvas.get_pygame_surface(),
                    color,
                    start,
                    end,
                    width)

            else:
                returnable = _pygame.draw.line(
                    canvas.get_pygame_surface(),
                    color,
                    start,
                    end,
                    width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def lines(
            self,
            color,
            points,
            width=1,
            closed=False,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            if len(points) < 2:
                end_time = _time.perf_counter()
                Registry.total_time_spent_drawing += end_time - start_time
                return
            if Registry.do_anti_aliasing:
                returnable = _pygame.draw.aalines(
                    canvas.get_pygame_surface(),
                    color,
                    closed,
                    points,
                    width)

            else:
                returnable = _pygame.draw.lines(
                    canvas.get_pygame_surface(),
                    color,
                    closed,
                    points,
                    width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def advanced_polygon(
            self,
            color,
            centre,
            radius,
            number_of_sides,
            rotation_angle=0,
            width=0,
            cache=None,
            wire_frame=False,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = _pygame.draw.polygon(
                    canvas.get_pygame_surface(),
                    color,
                    points,
                    width=width), cache

                end_time = _time.perf_counter()
                Registry.total_time_spent_drawing += end_time - start_time
                return returnable
            else:
                end_time = _time.perf_counter()
                Registry.total_time_spent_drawing += end_time - start_time
                return None, cache

        if wire_frame:
            for i in range(0, number_of_sides):
                Registry.number_of_draw_calls += 1
                if Registry.display_mode == Constants.PYGAME:
                    _pygame.draw.line(
                        canvas.get_pygame_surface(),
                        color,
                        centre, (
                            _math.cos(i / number_of_sides * Constants.TAU) * radius + centre[0],
                            _math.sin(i / number_of_sides * Constants.TAU) * radius + centre[1]))

        points = [
            (_math.cos(i / number_of_sides * Constants.TAU + rotation_angle) * radius + centre[0],
                _math.sin(i / number_of_sides * Constants.TAU + rotation_angle) * radius + centre[1]) for i in range(0, number_of_sides)]

        if wire_frame:
            width = 1

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.polygon(
                canvas.get_pygame_surface(),
                color,
                points,
                width=width), points
        else:
            end_time = _time.perf_counter()
            Registry.total_time_spent_drawing += end_time - start_time
            return None, cache
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def rotated_rect(
            self,
            color,
            center_of_rect,
            radius,
            height,
            rotation_angle=0,
            cache=None,
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
        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if cache is not None:
            if Registry.display_mode == Constants.PYGAME:
                returnable = _pygame.draw.polygon(
                    canvas.get_pygame_surface(),
                    color,
                    points,
                    width=width), cache

                end_time = _time.perf_counter()
                Registry.total_time_spent_drawing += end_time - start_time
                return returnable
            else:
                end_time = _time.perf_counter()
                Registry.total_time_spent_drawing += end_time - start_time
                return None, cache

        x, y = center_of_rect
        points = []

        # The distance from the center of the rectangle to
        # one of the corners is the same for each corner.
        radius = _math.sqrt((height / 2)**2 + (radius / 2)**2)

        # Get the angle to one of the corners with respect
        # to the x-axis.
        angle = _math.atan2(height / 2, radius / 2)

        # Transform that angle to reach each corner of the rectangle.
        angles = [angle, -angle + _math.pi, angle + _math.pi, -angle]

        # Convert rotation from degrees to radians.
        rot_radians = (_math.pi / 180) * rotation_angle

        # Calculate the coordinates of each point.
        for angle in angles:
            y_offset = -1 * radius * _math.sin(angle + rot_radians)
            x_offset = radius * _math.cos(angle + rot_radians)
            points.append((x + x_offset, y + y_offset))

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.polygon(
                canvas.get_pygame_surface(),
                color,
                points,
                width=width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def rect(
            self,
            color,
            position,
            size,
            width=0,
            border_radius=-1,
            border_top_left_radius=-1,
            border_top_right_radius=-1,
            border_bottom_left_radius=-1,
            border_bottom_right_radius=-1,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            rect = _pygame.Rect(*position, *size)
            returnable = _pygame.draw.rect(
                canvas.get_pygame_surface(),
                color,
                rect,
                width,
                border_radius,
                border_top_left_radius,
                border_top_right_radius,
                border_bottom_left_radius,
                border_bottom_right_radius)
        else:
            raise NotImplementedError

        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def circle(
            self,
            color,
            center,
            radius,
            width=0,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas
        if abs(radius) < 1:
            end_time = _time.perf_counter()
            Registry.total_time_spent_drawing += end_time - start_time
            return

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.circle(
                canvas.get_pygame_surface(),
                color,
                center,
                abs(radius),
                width)

        else:
            raise NotImplementedError

        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def arc(
            self,
            color,
            rect,
            start_angle,
            stop_angle,
            width=1,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.arc(
                canvas.get_pygame_surface(),
                color,
                rect,
                start_angle,
                stop_angle,
                width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def polygon(
            self,
            color,
            points,
            width=0,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.polygon(
            canvas.get_pygame_surface(),
            color,
            points,
            width)

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def ellipse(
            self,
            color,
            rect,
            width=0,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            returnable = _pygame.draw.ellipse(
                canvas.get_pygame_surface(),
                color,
                rect,
                width)
        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def pixel(
            self,
            color,
            position,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            try:
                returnable = _gfxdraw.pixel(
                    canvas.get_pygame_surface(),
                    color,
                    position), True

            except:
                temp_rect = _pygame.rect.Rect(
                    *position,
                    1,
                    1)

                returnable = _pygame.draw.rect(
                    canvas.get_pygame_surface(),
                    color,
                    temp_rect,
                    1), False

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable

    def curved_lines(
            self,
            color,
            points,
            steps=2,
            canvas=None):

        start_time = _time.perf_counter()
        Registry.number_of_draw_calls += 1
        if self._canvas is None and canvas is None:
            canvas = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]
        if canvas is None:
            canvas = self._canvas

        if type(color) != _Color:
            color = _Color()
            color.input_color(color)

        if Registry.display_mode == Constants.PYGAME:
            if len(points) > 2:
                try:
                    returnable = _gfxdraw.bezier(
                        canvas.get_pygame_surface(),
                        points,
                        steps,
                        color), True

                    end_time = _time.perf_counter()
                    Registry.total_time_spent_drawing += end_time - start_time
                    return returnable
                except:
                    pass
            returnable = self.lines(
                canvas,
                color,
                points,
                width=1,
                closed=False), False

        else:
            raise NotImplementedError
        end_time = _time.perf_counter()
        Registry.total_time_spent_drawing += end_time - start_time
        return returnable