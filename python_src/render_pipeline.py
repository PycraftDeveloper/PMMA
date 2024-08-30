import gc as _gc

import numpy as _numpy
import moderngl as _moderngl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.opengl import OpenGL as _OpenGL
from pmma.python_src.draw import Line as _Line
from pmma.python_src.draw import Lines as _Lines
from pmma.python_src.draw import AdvancedPolygon as _AdvancedPolygon
from pmma.python_src.draw import RotatedRect as _RotatedRect
from pmma.python_src.draw import Rect as _Rect
from pmma.python_src.draw import Circle as _Circle
from pmma.python_src.draw import Arc as _Arc
from pmma.python_src.draw import Polygon as _Polygon
from pmma.python_src.draw import Ellipse as _Ellipse
from pmma.python_src.draw import Pixel as _Pixel
from pmma.python_src.draw import CurvedLines as _CurvedLines

from pmma.python_src.utility.general_utils import initialize as _initialize

class RenderPipeline:
    def __init__(self):
        _initialize(self)

        self._render_points = []

        self._vao = None

        self._opengl = _OpenGL()
        self._display = Registry.pmma_module_spine[Constants.DISPLAY_OBJECT]

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add(self, render_class):
        if Constants.RENDER_PIPELINE_ABLE in render_class._attributes:
            self._render_points.append(render_class)

    def render(self, canvas=None): # not sure on width yet.
        if canvas is None:
            Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_2D_hardware_accelerated_surface()

        if self._render_points == []:
            return

        changed = False
        for render_point in self._render_points:
            if render_point.get_vertices_changed() or render_point.get_color_changed():
                changed = True
                break

        if self._vao is None or changed:
            total_number_of_vertices = 0
            total_number_of_indices = 0

            for render_point in self._render_points:
                if type(render_point) == _Line: # not sure on aspect scaling
                    total_number_of_vertices += 4
                    total_number_of_indices += 6

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        start = _numpy.array(render_point.get_start(), dtype=_numpy.float32)
                        end = _numpy.array(render_point.get_end(), dtype=_numpy.float32)

                        direction = end - start
                        length = _numpy.linalg.norm(direction)

                        # Normalize the direction vector
                        direction = direction.astype(_numpy.float32) / length
                        perpendicular = _numpy.array([-direction[1], direction[0]], dtype=_numpy.float32)

                        width = (render_point.get_width() / self._display.get_width()) * self._display.get_aspect_ratio()
                        offset = perpendicular * width

                        # Define vertices in correct order (counter-clockwise for triangle strip)
                        vertices_list = [
                            start[0] + offset[0], start[1] + offset[1],
                            end[0] + offset[0], end[1] + offset[1],
                            start[0] - offset[0], start[1] - offset[1],
                            end[0] - offset[0], end[1] - offset[1],
                        ]

                        # Create vertex buffer and index buffer
                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array([0, 1, 2, 1, 3, 2], dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        render_point.set_colors_hardware_accelerated_data(_numpy.array([
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                        ], dtype=_numpy.float32))

                elif type(render_point) == _Lines:
                    num_points = len(render_point.get_points())
                    total_number_of_vertices += num_points
                    total_number_of_indices += num_points if not render_point.get_closed() else num_points + 1

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = []
                        for point in render_point.get_points():
                            vertices_list.extend([point[0], point[1]])
                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))

                        indices_list = list(range(num_points))
                        if render_point.get_closed():
                            indices_list.append(0)  # Closing the shape
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in render_point.get_points():
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


                elif type(render_point) == _AdvancedPolygon:
                    total_number_of_vertices += render_point.get_number_of_sides()
                    total_number_of_indices += (render_point.get_number_of_sides() - 2) * 3

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = []
                        indices_list = []

                        angle_step = 2 * _numpy.pi / render_point.get_number_of_sides()
                        for i in range(render_point.get_number_of_sides()):
                            angle = render_point.get_rotation_angle() + i * angle_step
                            x = render_point.get_center()[0] + render_point.get_radius() * _numpy.cos(angle)
                            y = render_point.get_center()[1] + render_point.get_radius() * _numpy.sin(angle)
                            vertices_list.extend([x/self._display.get_aspect_ratio(), y])

                            if i > 1:
                                indices_list.extend([0, i - 1, i])

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in range(render_point.get_number_of_sides()):
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


                elif type(render_point) == _RotatedRect:
                    total_number_of_vertices += 4
                    total_number_of_indices += 6

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        half_width = render_point.get_radius()
                        half_height = render_point.get_height() / 2

                        angle_rad = _numpy.radians(render_point.get_rotation_angle())
                        cos_angle = _numpy.cos(angle_rad)
                        sin_angle = _numpy.sin(angle_rad)

                        vertices_list = [
                            (render_point.get_center_of_rect()[0] + cos_angle * half_width - sin_angle * half_height)/self._display.get_aspect_ratio(),
                            render_point.get_center_of_rect()[1] + sin_angle * half_width + cos_angle * half_height,

                            (render_point.get_center_of_rect()[0] - cos_angle * half_width - sin_angle * half_height)/self._display.get_aspect_ratio(),
                            render_point.get_center_of_rect()[1] - sin_angle * half_width + cos_angle * half_height,

                            (render_point.get_center_of_rect()[0] - cos_angle * half_width + sin_angle * half_height)/self._display.get_aspect_ratio(),
                            render_point.get_center_of_rect()[1] - sin_angle * half_width - cos_angle * half_height,

                            (render_point.get_center_of_rect()[0] + cos_angle * half_width + sin_angle * half_height)/self._display.get_aspect_ratio(),
                            render_point.get_center_of_rect()[1] + sin_angle * half_width - cos_angle * half_height,
                        ]

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array([0, 1, 2, 2, 3, 0], dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        render_point.set_colors_hardware_accelerated_data(_numpy.array([
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2],
                        ], dtype=_numpy.float32))


                elif type(render_point) == _Rect:
                    total_number_of_vertices += 4
                    total_number_of_indices += 6

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        render_point.set_vertices_hardware_accelerated_data(_numpy.array([
                            render_point.get_position()[0],
                            render_point.get_position()[1],
                            render_point.get_position()[0] + render_point.get_size()[0],
                            render_point.get_position()[1],
                            render_point.get_position()[0] + render_point.get_size()[0],
                            render_point.get_position()[1] + render_point.get_size()[1],
                            render_point.get_position()[0],
                            render_point.get_position()[1] + render_point.get_size()[1]]))

                        render_point.set_indices_hardware_accelerated_data(_numpy.array([
                            0,
                            1,
                            2,
                            2,
                            3,
                            0
                        ]))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        render_point.set_colors_hardware_accelerated_data(_numpy.array([
                            render_point.get_color()[0],
                            render_point.get_color()[1],
                            render_point.get_color()[2],
                            render_point.get_color()[0],
                            render_point.get_color()[1],
                            render_point.get_color()[2],
                            render_point.get_color()[0],
                            render_point.get_color()[1],
                            render_point.get_color()[2],
                            render_point.get_color()[0],
                            render_point.get_color()[1],
                            render_point.get_color()[2]
                        ]))

                elif type(render_point) == _Circle:
                    num_segments = 36  # Number of segments used to approximate the circle
                    total_number_of_vertices += num_segments + 1  # Circle center + edge points
                    total_number_of_indices += num_segments * 3  # Triangles to fill the circle

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = [render_point.get_center()[0], render_point.get_center()[1]]  # Circle center

                        for i in range(num_segments):
                            angle = 2 * _numpy.pi * i / num_segments
                            x = render_point.get_center()[0] + render_point.get_radius() * _numpy.cos(angle)
                            y = render_point.get_center()[1] + render_point.get_radius() * _numpy.sin(angle)
                            vertices_list.extend([x/self._display.get_aspect_ratio(), y])

                        indices_list = []
                        for i in range(1, num_segments):
                            indices_list.extend([0, i, i + 1])
                        indices_list.extend([0, num_segments, 1])  # Closing the circle

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in range(num_segments + 1):
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


                elif type(render_point) == _Arc: # problem
                    num_segments = 36
                    arc_length = render_point.get_stop_angle() - render_point.get_start_angle()
                    num_arc_segments = int(num_segments * arc_length / 360)
                    total_number_of_vertices += num_arc_segments + 1
                    total_number_of_indices += num_arc_segments * 3

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = [render_point.get_position()[0], render_point.get_position()[1]]

                        angle_step = arc_length / num_arc_segments
                        for i in range(num_arc_segments + 1):
                            angle = _numpy.radians(render_point.get_start_angle() + i * angle_step)
                            x = render_point.get_position()[0] + render_point.get_size()[0] * _numpy.cos(angle)
                            y = render_point.get_position()[1] + render_point.get_size()[1] * _numpy.sin(angle)
                            vertices_list.extend([x, y])

                        indices_list = []
                        for i in range(1, num_arc_segments):
                            indices_list.extend([0, i, i + 1])

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in range(num_arc_segments + 1):
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


                elif type(render_point) == _Polygon:
                    num_points = len(render_point.get_points())
                    total_number_of_vertices += num_points
                    total_number_of_indices += (num_points - 2) * 3

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = []
                        for point in render_point.get_points():
                            vertices_list.extend([point[0], point[1]])

                        indices_list = []
                        for i in range(1, num_points - 1):
                            indices_list.extend([0, i, i + 1])

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in render_point.get_points():
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


                elif type(render_point) == _Ellipse:
                    num_segments = 36
                    total_number_of_vertices += num_segments + 1
                    total_number_of_indices += num_segments * 3

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = [render_point.get_position()[0], render_point.get_position()[1]]

                        for i in range(num_segments):
                            angle = 2 * _numpy.pi * i / num_segments
                            x = render_point.get_position()[0] + render_point.get_size()[0] * _numpy.cos(angle)
                            y = render_point.get_position()[1] + render_point.get_size()[1] * _numpy.sin(angle)
                            vertices_list.extend([x, y])

                        indices_list = []
                        for i in range(1, num_segments):
                            indices_list.extend([0, i, i + 1])
                        indices_list.extend([0, num_segments, 1])

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in range(num_segments + 1):
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


                elif type(render_point) == _Pixel:
                    total_number_of_vertices += 1
                    total_number_of_indices += 1

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        render_point.set_vertices_hardware_accelerated_data(_numpy.array([
                            render_point.get_position()[0], render_point.get_position()[1]
                        ], dtype=_numpy.float32))

                        render_point.set_indices_hardware_accelerated_data(_numpy.array([0], dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        render_point.set_colors_hardware_accelerated_data(_numpy.array([
                            render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]
                        ], dtype=_numpy.float32))


                elif type(render_point) == _CurvedLines:
                    num_segments = render_point.get_steps()
                    total_number_of_vertices += num_segments
                    total_number_of_indices += num_segments - 1

                    if render_point.get_vertices_changed():
                        render_point.set_vertices_changed(False)
                        vertices_list = []
                        t_values = _numpy.linspace(0, 1, num_segments)
                        for t in t_values:
                            x = 0
                            y = 0
                            n = len(render_point.get_points()) - 1
                            for i, point in enumerate(render_point.get_points()):
                                binom = _numpy.math.comb(n, i)
                                coeff = binom * (1 - t) ** (n - i) * t ** i
                                x += coeff * point[0]
                                y += coeff * point[1]
                            vertices_list.extend([x, y])

                        indices_list = list(range(num_segments))

                        render_point.set_vertices_hardware_accelerated_data(_numpy.array(vertices_list, dtype=_numpy.float32))
                        render_point.set_indices_hardware_accelerated_data(_numpy.array(indices_list, dtype=_numpy.uint32))

                    if render_point.get_color_changed():
                        render_point.set_color_changed(False)
                        colors_list = []
                        for _ in range(num_segments):
                            colors_list.extend([render_point.get_color()[0], render_point.get_color()[1], render_point.get_color()[2]])
                        render_point.set_colors_hardware_accelerated_data(_numpy.array(colors_list, dtype=_numpy.float32))


            vertices_np = _numpy.empty(total_number_of_vertices * 2, dtype=_numpy.float32)
            colors_np = _numpy.empty(total_number_of_vertices * 3, dtype=_numpy.float32)
            indices_np = _numpy.empty(total_number_of_indices, dtype=_numpy.int32)

            vertices = vertices_np
            colors = colors_np
            indices = indices_np

            vertex_offset = 0
            color_offset = 0
            index_offset = 0
            shape_index = 0

            for render_point in self._render_points:
                vertices[vertex_offset:vertex_offset + len(render_point.get_hardware_accelerated_data()["vertices"])] = render_point.get_hardware_accelerated_data()["vertices"]
                indices[index_offset:index_offset + len(render_point.get_hardware_accelerated_data()["indices"])] = shape_index + render_point.get_hardware_accelerated_data()["indices"]
                colors[color_offset:color_offset + len(render_point.get_hardware_accelerated_data()["colors"])] = render_point.get_hardware_accelerated_data()["colors"]

                vertex_offset += len(render_point.get_hardware_accelerated_data()["vertices"])
                color_offset += len(render_point.get_hardware_accelerated_data()["colors"])
                index_offset += len(render_point.get_hardware_accelerated_data()["indices"])

                if type(render_point) == _Line:
                    shape_index += 4

                elif type(render_point) == _Lines: # shape_index right, but shape filled not line!
                    shape_index += len(render_point.get_points())

                elif type(render_point) == _AdvancedPolygon: # aspect all good
                    shape_index += render_point.get_number_of_sides()

                elif type(render_point) == _RotatedRect: # rotation isnt working? / aspect all good
                    shape_index += 4

                elif type(render_point) == _Rect:
                    shape_index += 4

                elif type(render_point) == _Circle: # aspect all good
                    shape_index += 37

                elif type(render_point) == _Arc: # broken
                    shape_index += 37 # might not be right

                elif type(render_point) == _Polygon: # broken
                    shape_index += len(render_point.get_points()) # might not be right

                elif type(render_point) == _Ellipse:
                    shape_index += 37

                elif type(render_point) == _Pixel: # might be broken, cant see
                    shape_index += 1 # might not be right

                elif type(render_point) == _CurvedLines: # broken
                    shape_index += len(render_point.get_hardware_accelerated_data()["indices"]) # might not be right

            vbo = self._opengl.create_vbo(vertices).get()
            cbo = self._opengl.create_cbo(colors).get()
            ibo = self._opengl.create_ibo(indices).get()

            if self._vao is not None:
                self._vao.release()
            #vao = self.opengl.create_vao(program, vbo, ).get() Not yet finished!!!
            self._vao = Registry.context.vertex_array(self._opengl.get_simple_shape_rendering_program().get(), [(vbo, '2f', 'in_vert'), (cbo, '3f', 'in_color')], ibo)
            self._vao.render(_moderngl.TRIANGLES)
        else:
            self._vao.render(_moderngl.TRIANGLES)

