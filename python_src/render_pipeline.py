import gc as _gc

import numpy as _numpy
import moderngl as _moderngl

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.general import create_cache_id as _create_cache_id
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

class RenderPipeline:
    def __init__(self):
        initialize(self)

        self.render_points = []

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add(self, render_class):
        if Constants.RENDER_PIPELINE_ABLE in render_class.attributes:
            self.render_points.append(render_class)

    def render(self, canvas=None): # not sure on width yet. RECTANGLES AND CIRCLES TO START WITH!!! FOR INDICES ARRAY + shape_index = vao indices
        if canvas is None:
            Registry.pmma_module_spine[Constants.DISPLAY_OBJECT].get_2D_hardware_accelerated_surface()

        total_number_of_vertices = 0
        total_number_of_indices = 0

        for render_point in self.render_points:
            if type(render_point) == _Line:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _Lines:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _AdvancedPolygon:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _RotatedRect:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _Rect:
                total_number_of_vertices += 4
                total_number_of_indices += 6

                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = _numpy.array([
                        render_point.position[0],
                        render_point.position[1],
                        render_point.position[0] + render_point.size[0],
                        render_point.position[1],
                        render_point.position[0] + render_point.size[0],
                        render_point.position[1] + render_point.size[1],
                        render_point.position[0],
                        render_point.position[1] + render_point.size[1]])

                    render_point.hardware_accelerated_data["indices"] = _numpy.array([
                        0,
                        1,
                        2,
                        2,
                        3,
                        0
                    ])

                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = _numpy.array([
                        render_point.color[0],
                        render_point.color[1], # worry about unique index coloring later for gradients.
                        render_point.color[2],
                        render_point.color[0],
                        render_point.color[1],
                        render_point.color[2],
                        render_point.color[0],
                        render_point.color[1],
                        render_point.color[2],
                        render_point.color[0],
                        render_point.color[1],
                        render_point.color[2]
                    ])

            elif type(render_point) == _Circle:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _Arc:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _Polygon:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _Ellipse:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _Pixel:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

            elif type(render_point) == _CurvedLines:
                if render_point.vertices_changed:
                    render_point.vertices_changed = False
                    render_point.hardware_accelerated_data["vertices"] = None
                    render_point.hardware_accelerated_data["indices"] = None
                if render_point.color_changed:
                    render_point.color_changed = False
                    render_point.hardware_accelerated_data["colors"] = None

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

        for render_point in self.render_points:
            '''vertices[vertex_offset:vertex_offset + len(render_point.hardware_accelerated_data["vertices"])] = render_point.hardware_accelerated_data["vertices"]
            indices[index_offset:index_offset + len(render_point.hardware_accelerated_data["indices"])] = shape_index + render_point.hardware_accelerated_data["indices"]
            colors[color_offset:color_offset + len(render_point.hardware_accelerated_data["colors"])] = render_point.hardware_accelerated_data["colors"]'''
            if type(render_point) == _Line:
                pass

            elif type(render_point) == _Lines:
                pass

            elif type(render_point) == _AdvancedPolygon:
                pass

            elif type(render_point) == _RotatedRect:
                pass

            elif type(render_point) == _Rect:
                vertices[vertex_offset:vertex_offset + len(render_point.hardware_accelerated_data["vertices"])] = render_point.hardware_accelerated_data["vertices"] # for testing purposes
                indices[index_offset:index_offset + len(render_point.hardware_accelerated_data["indices"])] = shape_index + render_point.hardware_accelerated_data["indices"] # for testing purposes
                colors[color_offset:color_offset + len(render_point.hardware_accelerated_data["colors"])] = render_point.hardware_accelerated_data["colors"] # for testing purposes

                vertex_offset += len(render_point.hardware_accelerated_data["vertices"])
                color_offset += len(render_point.hardware_accelerated_data["colors"])
                index_offset += len(render_point.hardware_accelerated_data["indices"])
                shape_index += 4

            elif type(render_point) == _Circle:
                vertices[vertex_offset:vertex_offset + len(render_point.hardware_accelerated_data["vertices"])] = render_point.hardware_accelerated_data["vertices"] # for testing purposes
                indices[index_offset:index_offset + len(render_point.hardware_accelerated_data["indices"])] = shape_index + render_point.hardware_accelerated_data["indices"] # for testing purposes
                colors[color_offset:color_offset + len(render_point.hardware_accelerated_data["colors"])] = render_point.hardware_accelerated_data["colors"] # for testing purposes

                vertex_offset += len(render_point.hardware_accelerated_data["vertices"])
                color_offset += len(render_point.hardware_accelerated_data["colors"])
                index_offset += len(render_point.hardware_accelerated_data["indices"])
                shape_index += 4

            elif type(render_point) == _Arc:
                pass

            elif type(render_point) == _Polygon:
                pass

            elif type(render_point) == _Ellipse:
                pass

            elif type(render_point) == _Pixel:
                pass

            elif type(render_point) == _CurvedLines:
                pass

        vbo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vbo(vertices).get()
        cbo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_cbo(colors).get()
        ibo = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_ibo(indices).get()
        #vao = Registry.pmma_module_spine[Constants.OPENGL_OBJECT].create_vao(program, vbo, ).get() Not yet finished!!!
        vao = Registry.context.vertex_array(Registry.pmma_module_spine[Constants.OPENGL_OBJECT].simple_shape_rendering_program.get(), [(vbo, '2f', 'in_vert'), (cbo, '3f', 'in_color')], ibo)
        vao.render(_moderngl.TRIANGLES)

