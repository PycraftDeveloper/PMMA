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

        self.vertex_data = []
        self.color_data = []
        self.offset_data = []
        self._vbo = _VertexBufferObject()
        self._cbo = _ColorBufferObject()
        self._obo = _GenericBufferObject()
        self._vao = _VertexArrayObject()
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "render_pipeline"))
        self._program.create()
        aspect_ratio = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()
        self._program.set_shader_variable('aspect_ratio', aspect_ratio+1) # deliberate offset

    def __del__(self, do_garbage_collection=False):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._program.quit(do_garbage_collection=False)
            self._vao.quit(do_garbage_collection=False)
            self._vbo.quit(do_garbage_collection=False)
            self._cbo.quit(do_garbage_collection=False)
            self._obo.quit(do_garbage_collection=False)
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        """
        🟩 **R** -
        """
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def add_shape(self, vertices, colors, offset=[0, 0]):
        """
        Adds a shape's vertex and color data to the buffers, with degenerate vertices for Triangle Strip rendering.
        """
        vertices = vertices.flatten()
        if len(colors) == 3:
            colors.append(1)

        old_color = colors
        old_offset = offset
        num_points = vertices.shape[0] // 2
        colors = []
        offset = []
        for _ in range(num_points):
            colors.extend(old_color)
            offset.extend(old_offset)

        if len(self.vertex_data) > 0:
            # Add degenerate vertices to disconnect the previous shape
            self.vertex_data.extend(self.vertex_data[-2:])  # Repeat last vertex
            self.vertex_data.extend(vertices[:2])  # Repeat first vertex of new shape
            self.color_data.extend(self.color_data[-4:])  # Repeat last color
            self.color_data.extend(colors[:4])  # Repeat first color of new shape
            self.offset_data.extend(self.offset_data[-2:])
            self.offset_data.extend(offset[:2])

        # Append the new shape's vertices and colors
        self.vertex_data.extend(vertices.tolist())
        self.color_data.extend(colors)
        self.offset_data.extend(offset)

    def _internal_render(self):
        self._vbo.set_data(self.get_vertex_buffer())
        self._cbo.set_data(self.get_color_buffer())
        self._obo.set_data(self.get_offset_buffer())
        self._program.set_shader_variable('aspect_ratio', _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio())
        self._vao.create(
            self._program,
            self._vbo, ["2f", "in_position"],
            color_buffer_object=self._cbo, color_buffer_shader_attributes=["4f", "in_color"],
            additional_buffers=[self._obo], additional_buffer_attributes=[["2f", "in_offset"]])
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)

    def get_vertex_buffer(self):
        """Returns a NumPy array of vertex data."""
        return _numpy.array(self.vertex_data, dtype=_numpy.float32)

    def get_color_buffer(self):
        """Returns a NumPy array of color data."""
        return _numpy.array(self.color_data, dtype=_numpy.float32)

    def get_offset_buffer(self):
        return _numpy.array(self.offset_data, dtype=_numpy.float32)