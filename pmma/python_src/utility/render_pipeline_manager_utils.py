from gc import collect as _gc__collect
import importlib as _importlib

import numpy as _numpy
import moderngl as _moderngl

from pmma.python_src.opengl import VertexBufferObject as _VertexBufferObject
from pmma.python_src.opengl import ColorBufferObject as _ColorBufferObject
from pmma.python_src.opengl import GenericBufferObject as _GenericBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.registry_utils import Registry as _Registry

class RenderPipelineManager:
    def __init__(self):
        _initialize(self, unique_instance=_Constants.RENDER_PIPELINE_MANAGER_OBJECT, add_to_pmma_module_spine=True)

        _Registry.render_pipeline_acceleration_available = True

        self._render_queue = []
        self._groupings = []
        self._raw_data = []

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            _Registry.render_pipeline_acceleration_available = False
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add_to_render_pipeline(self, object):
        self._raw_data.append(object)

    def arrange(self): # acceleration % = (1 / num of groupings) * 100
        # Quit all existing render pipelines
        for element in self._render_queue:
            if isinstance(element, RenderPipeline):
                element.quit(do_garbage_collection=False)

        # Clear the render queue for new groupings
        self._render_queue.clear()

        new_groupings = []
        current_group = None

        for content in self._raw_data:
            is_compatible = content._properties[_Constants.RENDER_PIPELINE_COMPATIBLE]

            if is_compatible:
                # Start a new group if none exists or the last group isn't compatible
                if not current_group:
                    current_group = []
                    new_groupings.append(current_group)
                current_group.append(content)
            else:
                # End the current group if it exists
                if current_group:
                    current_group = None
                new_groupings.append(content)

        # Build the render queue
        for group in new_groupings:
            if isinstance(group, list):
                render_pipeline = RenderPipeline()  # Replace with self.render_pipeline_module.RenderPipeline if needed
                for element in group:
                    render_pipeline.add_shape(element._vertex_data, element._color_data, element._offset_data)
                self._render_queue.append(render_pipeline)
            else:
                self._render_queue.append(group)

        # Clear raw data
        self._raw_data.clear()

    def render(self):
        """
        🟩 **R** -
        """
        self.arrange()
        for renderable in self._render_queue:
            renderable._internal_render(*renderable._properties[_Constants.ADDITIONAL_INTERNAL_RENDER_DATA])

class RenderPipeline:
    def __init__(self):
        _initialize(self)

        # Initialize numpy arrays for vertex, color, and offset data
        self.vertex_data = _numpy.empty((0,), dtype=_numpy.float32)
        self.color_data = _numpy.empty((0,), dtype=_numpy.float32)
        self.offset_data = _numpy.empty((0,), dtype=_numpy.float32)

        # Other initialization
        self._vbo = _VertexBufferObject()
        self._cbo = _ColorBufferObject()
        self._obo = _GenericBufferObject()
        self._vao = _VertexArrayObject()
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "render_pipeline"))
        self._program.create()

        aspect_ratio = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()
        self._program.set_shader_variable("aspect_ratio", aspect_ratio + 1)  # deliberate offset

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

    def add_shape(self, vertices, colors, offset=[0, 0]):
        """
        Adds a shape's vertex and color data to the buffers, with degenerate vertices for Triangle Strip rendering.
        """
        vertices = vertices.flatten()
        num_points = vertices.shape[0] // 2

        # Ensure colors is a list of four components (RGBA)
        if len(colors) == 3:
            colors.append(1)

        # Create colors and offsets arrays
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

        # Append the new shape's vertices, colors, and offsets
        self.vertex_data = _numpy.concatenate([self.vertex_data, vertices])
        self.color_data = _numpy.concatenate([self.color_data, colors_array])
        self.offset_data = _numpy.concatenate([self.offset_data, offset_array])

    def _internal_render(self):
        self._vbo.set_data(self.vertex_data)
        self._cbo.set_data(self.color_data)
        self._obo.set_data(self.offset_data)
        self._program.set_shader_variable(
            "aspect_ratio", _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()
        )
        self._vao.create(
            self._program,
            self._vbo, ["2f", "in_position"],
            color_buffer_object=self._cbo, color_buffer_shader_attributes=["4f", "in_color"],
            additional_buffers=[self._obo], additional_buffer_attributes=[["2f", "in_offset"]]
        )
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)