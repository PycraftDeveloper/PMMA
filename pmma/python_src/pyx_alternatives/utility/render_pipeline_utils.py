from gc import collect as _gc__collect

import numpy as _numpy
import moderngl as _moderngl

from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import ColorBufferObject as _ColorBufferObject
from pmma.python_src.opengl import GenericBufferObject as _GenericBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize

class RenderPipeline:
    def __init__(self):
        _initialize(self)

        self.shapes = []  # Store references to shapes
        self.vertex_data = _numpy.empty((0,), dtype=_numpy.float32)
        self.color_data = _numpy.empty((0,), dtype=_numpy.float32)
        self.offset_data = _numpy.empty((0,), dtype=_numpy.float32)

        # Buffer objects
        self._vbo = _VertexBufferObject()
        self._vbo.set_dynamic(True)
        self._cbo = _ColorBufferObject()
        self._cbo.set_dynamic(True)
        self._obo = _GenericBufferObject()
        self._obo.set_dynamic(True)
        self._vao = _VertexArrayObject()

        # Shader
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "render_pipeline"))
        self._program.create()

    def __del__(self, do_garbage_collection=False):
        if not self._shut_down:
            self._program.quit(do_garbage_collection=False)
            self._vao.quit(do_garbage_collection=False)
            self._vbo.quit(do_garbage_collection=False)
            self._cbo.quit(do_garbage_collection=False)
            self._obo.quit(do_garbage_collection=False)
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def update(self, shapes):
        """
        Updates the pipeline's vertex, color, and offset data based on the given shapes.
        """
        # If the list of shapes hasn't changed
        if shapes == self.shapes:
            # Check if any of the shapes' data has changed
            for shape in shapes:
                if shape._render_pipeline_color_data_changed:  # Check if `shape._vertex_data` has changed
                    break
                if shape._render_pipeline_vertex_data_changed:  # Check if `shape._color_data` has changed
                    break
                if shape._render_pipeline_offset_data_changed:  # Check if `shape._offset_data` has changed
                    break
            else:
                # If no changes were detected, we don't need to update
                return

        # Update the shapes and recalculate the data
        self.shapes = shapes
        self.vertex_data = _numpy.empty((0,), dtype=_numpy.float32)
        self.color_data = _numpy.empty((0,), dtype=_numpy.float32)
        self.offset_data = _numpy.empty((0,), dtype=_numpy.float32)

        for i, shape in enumerate(shapes):
            vertices = shape._vertex_data.flatten()
            colors = shape._color_data
            offset = shape._offset_data

            num_points = vertices.shape[0] // 2

            if len(colors) == 3:
                colors.append(1)  # Ensure RGBA

            colors_array = _numpy.tile(colors, num_points).astype(_numpy.float32)
            offset_array = _numpy.tile(offset, num_points).astype(_numpy.float32)

            if self.vertex_data.size > 0:
                # Add degenerate vertices to disconnect the previous shape
                degenerate_vertex = self.vertex_data[-2:]  # Last vertex
                degenerate_color = self.color_data[-4:]  # Last color
                degenerate_offset = self.offset_data[-2:]  # Last offset

                first_vertex = vertices[:2]  # First vertex of new shape
                first_color = colors_array[:4]  # First color of new shape
                first_offset = offset_array[:2]  # First offset of new shape

                self.vertex_data = _numpy.concatenate([self.vertex_data, degenerate_vertex, first_vertex])
                self.color_data = _numpy.concatenate([self.color_data, degenerate_color, first_color])
                self.offset_data = _numpy.concatenate([self.offset_data, degenerate_offset, first_offset])

            self.vertex_data = _numpy.concatenate([self.vertex_data, vertices])
            self.color_data = _numpy.concatenate([self.color_data, colors_array])
            self.offset_data = _numpy.concatenate([self.offset_data, offset_array])

            # Add degenerate vertices at the end of the last shape to disconnect it from the first shape
            if i == len(shapes) - 1:  # Last shape in the list
                degenerate_vertex = vertices[-2:]  # Last vertex of the shape
                degenerate_color = colors_array[-4:]  # Last color of the shape
                degenerate_offset = offset_array[-2:]  # Last offset of the shape

                self.vertex_data = _numpy.concatenate([self.vertex_data, degenerate_vertex, degenerate_vertex])
                self.color_data = _numpy.concatenate([self.color_data, degenerate_color, degenerate_color])
                self.offset_data = _numpy.concatenate([self.offset_data, degenerate_offset, degenerate_offset])

            shape._render_pipeline_color_data_changed = False
            shape._render_pipeline_vertex_data_changed = False
            shape._render_pipeline_offset_data_changed = False

        self._vbo.set_data(self.vertex_data)
        self._cbo.set_data(self.color_data)
        self._obo.set_data(self.offset_data)

    def _internal_render(self):
        self._program.set_shader_variable(
            "aspect_ratio", _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()
        )
        self._vao.create(
            self._program,
            self._vbo, ["2f", "in_position"],
            color_buffer_object=self._cbo, color_buffer_shader_attributes=["4f", "in_color"],
            additional_buffers=[self._obo], additional_buffer_attributes=[["2f", "in_offset"]],
        )
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)
