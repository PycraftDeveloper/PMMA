from gc import collect as _gc__collect
import math as _math

import pygame as _pygame
import numpy as _numpy

from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import ColorConverter as _ColorConverter
from pmma.python_src.events import WindowResized_EVENT as _WindowResized_EVENT

from pmma.python_src.utility.display_utils import DisplayIntermediary as _DisplayIntermediary
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.general_utils import create_cache_id as _create_cache_id
from pmma.python_src.utility.error_utils import ShapeRadiusNotSpecifiedError as _ShapeRadiusNotSpecifiedError

class ShapeTemplate: # add vertex manager and changes to rendering!
    def __init__(self):
        _initialize(self)

        if not _Constants.SHAPE_GEOMETRY_MANAGER_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT)
            from pmma.python_src.utility.shape_geometry_utils import ShapeGeometryManager as _ShapeGeometryManager
            _ShapeGeometryManager()

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            self._logger.log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self._color_changed = True
        self._fill_color_manager = _ColorConverter()
        self._display: "_DisplayIntermediary" = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT]

        self._resized_event = _WindowResized_EVENT()

        self._geometry_created = False

        _Registry.shape_count += 1

        self.old_shape_identifier = None

        self._color_data = None
        self._vertex_data = None

    def set_color(self, color, format=_Constants.RGB):
        """
        🟩 **R** -
        """
        if type(color) == _ColorConverter:
            color = color.get_color(format=_Constants.RGBA)
            format = _Constants.RGBA

        if self._fill_color_manager.get_color_set():
            original_color = self._fill_color_manager.get_color(format=_Constants.RGBA)
            self._fill_color_manager.set_color(color, format=format)
            if self._fill_color_manager.get_color(format=_Constants.RGBA) != original_color:
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
        return self._fill_color_manager.get_color_set()

    def get_color(self, format):
        if self._fill_color_manager.get_color_set():
            return self._fill_color_manager.get_color(format=format)

    def generate_random_color(
            self,
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        self._color_changed = True
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
            color_range=[0, 255],
            red_color_range=None,
            green_color_range=None,
            blue_color_range=None,
            alpha_color_range=None):
        self._color_changed = True
        self._color_data = self._fill_color_manager.generate_color_from_perlin_noise(
            self,
            value=value,
            format=_Constants.SMALL_RGBA,
            color_range=color_range,
            red_color_range=red_color_range,
            green_color_range=green_color_range,
            blue_color_range=blue_color_range,
            alpha_color_range=alpha_color_range)

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            del self
            _Registry.shape_count -= 1
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

class LineUtils:
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
        rotation_in_radians = self._rotation.get_angle(format=_Constants.RADIANS)
        start_coords = self.get_start(format=_Constants.OPENGL_COORDINATES)
        end_coords = self.get_end(format=_Constants.OPENGL_COORDINATES)

        identifier = _create_cache_id(
            rotation_in_radians,
            start_coords,
            end_coords,
            self._width)

        if self.old_shape_identifier is not None:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_line(self.old_shape_identifier)

        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_line_exists(identifier):
            vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_line(identifier)
        else:
            rotated_line_points = self._rotate_line(rotation_in_radians, start_coords, end_coords)

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

            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_line(identifier, vertices)

        self.old_shape_identifier = identifier
        self._vertex_data = vertices

        if not self._vbo.get_created():
            self._vbo.create(vertices)
        else:
            self._vbo.update(vertices)

class RadialPolygonUtils:
    def _create_geometry(self):
        if self._radius.get_point_set() is False:
            raise _ShapeRadiusNotSpecifiedError()

        radius = self._radius.get_point(_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(_Constants.RADIANS)  # Get the current rotation angle

        identifier = _create_cache_id(radius, rotation, self._width)

        if self.old_shape_identifier is not None:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_radial_polygon(self.old_shape_identifier)

        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_radial_polygon_exists(identifier):
            vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_radial_polygon(identifier)
        else:
            if self._point_count is None:
                try:
                    point_count = 1 + int((_Constants.TAU / _math.asin(1 / self._radius.get_point(format=_Constants.CONVENTIONAL_COORDINATES))) * _Registry.shape_quality)
                except:
                    point_count = 3
                if point_count < 3:
                    point_count = 3
            else:
                point_count = self._point_count

            angle_step = 2 * _math.pi / point_count
            angles = _numpy.arange(point_count) * angle_step + rotation

            # Get the outer and inner radii
            outer_radius = radius

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

            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_radial_polygon(identifier, vertices)

        self.old_shape_identifier = identifier
        self._vertex_data = vertices

        if self._initial_point_count == None or self._initial_point_count != point_count: # delete and recreate as size changed.
            self._initial_point_count = point_count
            self._vbo.quit()
            self._vbo.create(vertices)
        else:
            if self._vbo.get_created():
                self._vbo.update(vertices)
            else:
                self._vbo.create(vertices)

        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

class RectangleUtils:
    def _arc(self, cx, cy, start_angle, end_angle, r, segments):
        arc_vertices = []
        for angle in _numpy.linspace(start_angle, end_angle, segments):
            px = cx + r * _math.cos(angle)
            py = cy + r * _math.sin(angle)
            arc_vertices.append((px, py))
        return arc_vertices

    def _generate_corner(self, cx, cy, start_angle, end_angle, outer_radius, inner_radius, segments):
        outer_arc = self._arc(cx, cy, start_angle, end_angle, outer_radius, segments)
        inner_arc = self._arc(cx, cy, start_angle, end_angle, inner_radius, segments)
        return zip(outer_arc, inner_arc)

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
        🟩 **R** - Calculate the vertices of the polygon based on the radius, center, point count, and rotation.
        """
        if self._position.get_coordinate_set() is False or self._x_size.get_point_set() is False or self._y_size.get_point_set() is False:
            return None

        x_size = self._x_size.get_point(_Constants.OPENGL_COORDINATES)
        y_size = self._y_size.get_point(_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)
        width = self._width.get_point(_Constants.OPENGL_COORDINATES)
        corner_radius = self._corner_radius.get_point(_Constants.OPENGL_COORDINATES)
        corner_radius = min(corner_radius, x_size / 2, y_size / 2)
        width = min(width, x_size / 2, y_size / 2)

        identifier = _create_cache_id(x_size, y_size, width, rotation, corner_radius)

        if self.old_shape_identifier is not None:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_rectangle(self.old_shape_identifier)

        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_rectangle_exists(identifier):
            vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_rectangle(identifier)
        else:
            # start

            segments = 16  # Number of segments for each corner
            vertices = []

            # Outer and inner rectangle dimensions
            outer_radius = corner_radius
            inner_radius = corner_radius - width
            outer_width = x_size
            outer_height = y_size

            # Generate vertices for the rounded rectangle (outer and inner arcs)

            # Bottom-left corner
            bl_corners = self._generate_corner(
                -outer_width / 2 + outer_radius,
                -outer_height / 2 + outer_radius,
                _math.pi, 1.5 * _math.pi,
                outer_radius,
                inner_radius,
                segments)
            # Bottom-right corner
            br_corners = self._generate_corner(
                outer_width / 2 - outer_radius,
                -outer_height / 2 + outer_radius,
                1.5 * _math.pi,
                2 * _math.pi,
                outer_radius,
                inner_radius,
                segments)
            # Top-right corner
            tr_corners = self._generate_corner(
                outer_width / 2 - outer_radius,
                outer_height / 2 - outer_radius,
                0,
                0.5 * _math.pi,
                outer_radius,
                inner_radius,
                segments)
            # Top-left corner
            tl_corners = self._generate_corner(
                -outer_width / 2 + outer_radius,
                outer_height / 2 - outer_radius,
                0.5 * _math.pi,
                _math.pi,
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

            combined_vertices = _numpy.array(vertices, dtype='f4')

            # end -> combined_vertices

            # Apply rotation around the center
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            # Rotate each vertex around the center
            vertices = _numpy.array([self._rotate_point(v[0], v[1], 0, 0, cos_theta, sin_theta) for v in combined_vertices], dtype='f4')

            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_rectangle(identifier, vertices)

        self._geometry_created = True  # Reset the flag
        self.old_shape_identifier = identifier
        self._vertex_data = vertices

        if self._vbo.get_created() is False:
            self._vbo.create(vertices)
        else:
            self._vbo.update(vertices)

        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())

class ArcUtils:
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
        🟩 **R** - Calculate the vertices for the arc based on start_angle, stop_angle, center, radius, and width.
        """
        if self._radius is None or self._start_angle is None or self._stop_angle is None:
            return None  # Cannot proceed without these parameters

        start_angle = self._start_angle.get_angle(format=_Constants.RADIANS)
        stop_angle = self._stop_angle.get_angle(format=_Constants.RADIANS)
        outer_radius = self._radius.get_point(format=_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)

        identifier = _create_cache_id(start_angle, stop_angle, outer_radius, rotation, self._width)

        if self.old_shape_identifier is not None:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_arc(self.old_shape_identifier)

        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_arc_exists(identifier):
            rotated_vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_arc(identifier)
        else:
            center_x, center_y = [0, 0]
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
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)
            rotated_vertices = _numpy.array([
                self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta)
                for v in vertices
            ], dtype='f4')

            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_arc(identifier, rotated_vertices)

        self._geometry_created = True  # Reset the flag
        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())
        self.old_shape_identifier = identifier
        self._vertex_data = rotated_vertices

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

class EllipseUtils:
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
        if self._outer_x_size.get_point_set() is False or self._outer_y_size.get_point_set() is False:
            return None  # Cannot proceed without these parameters

        outer_size_x = self._outer_x_size.get_point(format=_Constants.OPENGL_COORDINATES)
        outer_size_y = self._outer_y_size.get_point(format=_Constants.OPENGL_COORDINATES)
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)

        identifier = _create_cache_id(
            outer_size_x,
            outer_size_y,
            self._width,
            rotation)

        if self.old_shape_identifier is not None:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_ellipse(self.old_shape_identifier)

        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_ellipse_exists(identifier):
            rotated_vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_ellipse(identifier)
        else:
            center_x, center_y = [0, 0]

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
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_ellipse(identifier, rotated_vertices)

        self._geometry_created = True  # Reset the flag
        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())
        self.old_shape_identifier = identifier
        self._vertex_data = rotated_vertices

        if self._initial_point_count == None or self._initial_point_count != num_points:
            self._initial_point_count = num_points
            self._vbo.quit()
            self._vbo.create(rotated_vertices)
        else:
            if self._vbo.get_created():
                self._vbo.update(rotated_vertices)
            else:
                self._vbo.create(rotated_vertices)

class PolygonUtils:
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
        if not self._points:
            return None  # No points to form the polygon

        outer_points = _numpy.array([p.get_coordinates(format=_Constants.OPENGL_COORDINATES) for p in self._points], dtype='f4')
        rotation = self._rotation.get_angle(format=_Constants.RADIANS)

        identifier = _create_cache_id(
            outer_points,
            rotation,
            self._width)

        if self.old_shape_identifier is not None:
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_polygon(self.old_shape_identifier)

        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_polygon_exists(identifier):
            rotated_vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_polygon(identifier)
        else:
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
            cos_theta = _numpy.cos(rotation)
            sin_theta = _numpy.sin(rotation)

            rotated_vertices = _numpy.array([self._rotate_point(v[0], v[1], center_x, center_y, cos_theta, sin_theta) for v in vertices], dtype='f4')

            # If closed, append the first vertex to close the loop
            if self._closed and len(rotated_vertices) > 1:
                extra_points = _numpy.array([rotated_vertices[0], rotated_vertices[1]], dtype='f4')
                rotated_vertices = _numpy.concatenate((rotated_vertices, extra_points))

            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_polygon(identifier, rotated_vertices)

        self._geometry_created = True  # Reset the flag
        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())
        self.old_shape_identifier = identifier
        self._vertex_data = rotated_vertices

        if self._vbo.get_created() is False:
            self._vbo.create(rotated_vertices)
        else:
            self._vbo.update(rotated_vertices)

class PixelUtils:
    def _create_geometry(self):
        """
        🟩 **R** -
        """
        if _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].check_if_pixel_exists():
            vertices = _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].get_pixel()
        else:
            vertices = _numpy.array([0, 0], dtype='f4')
            _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].add_pixel(vertices)

        if self._vbo.get_created():
            self._vbo.update(vertices)
        else:
            self._vbo.create(vertices)