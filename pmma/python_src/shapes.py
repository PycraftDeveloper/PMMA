from gc import collect as _gc__collect

import moderngl as _moderngl

from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.number_converter import DisplayCoordinatesConverter as _DisplayCoordinatesConverter
from pmma.python_src.number_converter import DisplayScalarConverter as _DisplayScalarConverter
from pmma.python_src.number_converter import AngleConverter as _AngleConverter
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.advmath import Math as _Math

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.shape_utils import ShapeTemplate as _ShapeTemplate
from pmma.python_src.utility.shape_utils import LineUtils as _LineUtils
from pmma.python_src.utility.shape_utils import RadialPolygonUtils as _RadialPolygonUtils
from pmma.python_src.utility.shape_utils import RectangleUtils as _RectangleUtils
from pmma.python_src.utility.shape_utils import ArcUtils as _ArcUtils
from pmma.python_src.utility.shape_utils import EllipseUtils as _EllipseUtils
from pmma.python_src.utility.shape_utils import PolygonUtils as _PolygonUtils
from pmma.python_src.utility.shape_utils import PixelUtils as _PixelUtils

class Line(_ShapeTemplate, _LineUtils):
    """
    🟩 **R** -Draws a basic line.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._properties[_Constants.RENDER_PIPELINE_COMPATIBLE] = True

        self._start = _DisplayCoordinatesConverter()
        self._end = _DisplayCoordinatesConverter()
        self._width = 1
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_line"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_line(self.old_shape_identifier)

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._geometry_created = False

        if self._color_changed or self._geometry_created is False:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
            self._color_changed = False  # Reset the flag

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Render the line
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._geometry_created = False
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

        self._geometry_created = False
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

        self._geometry_created = False
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

class RadialPolygon(_ShapeTemplate, _RadialPolygonUtils):
    """
    🟩 **R** - Draws a radial polygon.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._properties[_Constants.RENDER_PIPELINE_COMPATIBLE] = True

        self._point_count = None
        self._radius = _DisplayScalarConverter()
        self._inner_radius = _DisplayScalarConverter()
        self._center = _DisplayCoordinatesConverter()
        self._width = None
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_radial_polygon"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._position_changed = True
        self._initial_point_count = None

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_radial_polygon(self.old_shape_identifier)

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._geometry_created = False

        if self._color_changed or self._geometry_created is False or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors
        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._position_changed:
            offset = self._center.get_coordinates(format=_Constants.OPENGL_COORDINATES)
            self._program.set_shader_variable('offset', offset)
            self._position_changed = False

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
            self._color_changed = False  # Reset the flag

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])
        if self._vbo._reassign_to_vertex_array_object:
            '''self._vao.quit()
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])'''
            self._vao.recreate()
            self._vbo._reassign_to_vertex_array_object = False

        self._vao.render(_moderngl.TRIANGLE_STRIP)

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._geometry_created = False
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
        self._geometry_created = False
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
        self._geometry_created = False
        if point_count < 3:
            point_count = 3
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

class Rectangle(_ShapeTemplate, _RectangleUtils):
    """
    🟩 **R** - Draws a rectangle.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._properties[_Constants.RENDER_PIPELINE_COMPATIBLE] = True

        self._position = _DisplayCoordinatesConverter()
        self._x_size = _DisplayScalarConverter()
        self._y_size = _DisplayScalarConverter()
        self._width = _DisplayScalarConverter()
        self._width.set_point(1)
        self._rotation = _AngleConverter()
        self._rotation.set_angle(0)
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_rectangle"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._position_changed = True
        self._corner_radius = _DisplayScalarConverter()
        self._corner_radius.set_point(1)

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_rectangle(self.old_shape_identifier)

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._geometry_created = False

        if self._color_changed or self._geometry_created is False or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
            self._color_changed = False

        if self._position_changed:
            self._program.set_shader_variable('offset', self._position.get_coordinates(_Constants.OPENGL_COORDINATES))
            self._position_changed = False

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(_moderngl.TRIANGLE_STRIP)

    def set_width(self, width=1, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._geometry_created = False
        if type(width) != _DisplayScalarConverter:
            self._width.set_point(width, format=format)
        else:
            self._width = width

    def get_width(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._width.get_point(format=format)

    def set_corner_radius(self, corner_radius=1, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        self._geometry_created = False
        if type(corner_radius) != _DisplayScalarConverter:
            if corner_radius < 1:
                corner_radius = 1
            self._corner_radius.set_point(corner_radius, format=format)
        else:
            self._corner_radius = corner_radius

    def get_corner_width(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        return self._corner_radius.get_point(format=format)

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._geometry_created = False
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
        self._geometry_created = False
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

class Arc(_ShapeTemplate, _ArcUtils):
    """
    🟩 **R** - Draws an arc.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._properties[_Constants.RENDER_PIPELINE_COMPATIBLE] = True

        self._radius = _DisplayScalarConverter()
        self._inner_radius = _DisplayScalarConverter()
        self._center = _DisplayCoordinatesConverter()
        self._start_angle = _AngleConverter()
        self._stop_angle = _AngleConverter()
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

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_arc(self.old_shape_identifier)

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._geometry_created = False

        if self._color_changed or self._geometry_created is False or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
            self._color_changed = False  # Reset the flag

        if self._position_changed:
            self._program.set_shader_variable('offset', self._center.get_coordinates(format=_Constants.OPENGL_COORDINATES))
            self._position_changed = False

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Render the arc using GL_TRIANGLE_STRIP
        self._vao.render(_moderngl.TRIANGLE_STRIP)

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
        self._geometry_created = False
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
        self._geometry_created = False
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
        self._geometry_created = False
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
        self._geometry_created = False
        if type(value) != _DisplayScalarConverter():
            self._radius.set_point(value, format=format)

    def get_radius(self, format=_Constants.CONVENTIONAL_COORDINATES):
        """
        🟩 **R** -
        """
        if self._radius is not None:
            return self._radius.get_point(format=format)

class Ellipse(_ShapeTemplate, _EllipseUtils):
    """
    🟩 **R** - Draws an ellipse.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._properties[_Constants.RENDER_PIPELINE_COMPATIBLE] = True

        self._position = _DisplayCoordinatesConverter()
        self._outer_x_size = _DisplayScalarConverter()
        self._outer_y_size = _DisplayScalarConverter()
        self._rotation = _AngleConverter()
        self._inner_x_size = _DisplayScalarConverter()
        self._inner_y_size = _DisplayScalarConverter()
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

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_ellipse(self.old_shape_identifier)

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._geometry_created = False

        if self._color_changed or self._geometry_created is False or self._position_changed:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()
        # Update VBO with any changes to vertices or colors

        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
            self._color_changed = False  # Reset the flag

        if self._position_changed:
            self._program.set_shader_variable('offset', self._position.get_coordinates(format=_Constants.OPENGL_COORDINATES))
            self._position_changed = False

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        self._vao.render(_moderngl.TRIANGLE_STRIP)

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
        self._geometry_created = False
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
        self._geometry_created = False
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

class Polygon(_ShapeTemplate, _PolygonUtils):
    """
    🟩 **R** - Draws a polygon.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._properties[_Constants.RENDER_PIPELINE_COMPATIBLE] = True

        self._points = []
        self._closed = True
        self._curved = False
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

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_polygon(self.old_shape_identifier)

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self):
        """
        🟩 **R** -
        """
        self._display.update_attempted_render_calls(1)

        if self._resized_event.get_value():
            self._geometry_created = False

        if self._color_changed or self._geometry_created is False:
            self._display.set_refresh_optimization_override(True)

        if self._display.get_clear_called_but_skipped():
            return None

        self._display.get_2D_hardware_accelerated_surface()

        # Update VBO with any changes to vertices or colors
        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
            self._color_changed = False  # Reset the flag

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._vbo, ['2f', 'in_position'])

        # Draw the polygon using triangle fan (good for convex shapes)
        if self._closed is False and self._width is None:
            self._width = 1 # idk about this bit yet

        self._vao.render(_moderngl.TRIANGLE_STRIP)

    def set_rotation(self, rotation, format=_Constants.RADIANS):
        """
        🟩 **R** -
        """
        self._geometry_created = False
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
        self._geometry_created = False
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

class Pixel(_ShapeTemplate, _PixelUtils):
    """
    🟩 **R** - Draws a Pixel.
    """
    def __init__(self):
        """
        🟩 **R** -
        """
        super().__init__()

        _initialize(self)

        self._position = _DisplayCoordinatesConverter()
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "draw_pixel"))
        self._program.create()
        self._vbo = _VertexBufferObject()
        self._vao = _VertexArrayObject()
        self._position_changed = True

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit()
            self._vbo.quit()
            self._vao.quit()

            if self.old_shape_identifier is not None:
                _Registry.pmma_module_spine[_Constants.SHAPE_GEOMETRY_MANAGER_OBJECT].remove_pixel()

            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def render(self, point_size=None, dynamic_rendering=True):
        """
        🟩 **R** -
        """
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

        if self._geometry_created is False:
            self._create_geometry()
            self._geometry_created = True

        if self._position_changed:
            offset = self._position.get_coordinates(format=_Constants.OPENGL_COORDINATES)
            self._program.set_shader_variable('offset', offset)
            self._position_changed = False

        if self._color_changed:
            self._program.set_shader_variable('color', self._color_data)
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