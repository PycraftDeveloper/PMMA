from gc import collect as _gc__collect

import numpy as np
cimport numpy as cnp
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

cdef cnp.ndarray[cnp.float32_t, ndim=1] repeat_array_cython(cnp.ndarray[cnp.float32_t, ndim=1] base, int N):
    cdef int base_size = base.shape[0]
    cdef cnp.ndarray[cnp.float32_t, ndim=1] result = np.zeros(N * base_size, dtype=np.float32)
    cdef int i

    # Fill the result array using slicing
    for i in range(N):
        result[i * base_size : (i + 1) * base_size] = base

    return result

cdef class RenderPipeline:
    cdef:
        list shapes
        object vertex_data
        object color_data
        object offset_data
        object _vbo
        object _cbo
        object _obo
        object _vao
        object _program
        float aspect_ratio

    def __cinit__(self):
        self.shapes = []  # Store references to shapes

        self.aspect_ratio = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()

        # Preallocate memory for vertex, color, and offset data
        self.vertex_data = np.empty((0,), dtype=np.float32)
        self.color_data = np.empty((0,), dtype=np.float32)
        self.offset_data = np.empty((0,), dtype=np.float32)

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

    def quit(self, bint do_garbage_collection=True):
        self._shut_down = True
        self._program.quit(do_garbage_collection=False)
        self._vao.quit(do_garbage_collection=False)
        self._vbo.quit(do_garbage_collection=False)
        self._cbo.quit(do_garbage_collection=False)
        self._obo.quit(do_garbage_collection=False)

    cpdef update(self, shapes):
        cdef int i, num_points, vertex_index, color_index, offset_index
        cdef cnp.ndarray[cnp.float32_t, ndim=1] vertices, colors_array, offset_array, colors, offset

        if shapes == self.shapes:
            for shape in shapes:
                if (shape._render_pipeline_color_data_changed or
                    shape._render_pipeline_vertex_data_changed or
                    shape._render_pipeline_offset_data_changed):
                    break
            else:
                return

        self.shapes = shapes

        # Compute total size for buffers (including degenerate vertices)
        cdef int total_vertices = 0
        cdef int total_colors = 0
        cdef int total_offsets = 0

        for i in range(len(shapes)):
            shape = shapes[i]

            vertices = shape._vertex_data.flatten()
            num_points = vertices.shape[0] // 2
            total_vertices += vertices.shape[0] + 4  # +4 for degenerate vertices (2 per shape)
            total_colors += num_points * 4 + 8       # +8 for degenerate colors (4 per shape)
            total_offsets += num_points * 2 + 4     # +4 for degenerate offsets (2 per shape)

        # Preallocate buffers
        self.vertex_data = np.empty((total_vertices,), dtype=np.float32)
        self.color_data = np.empty((total_colors,), dtype=np.float32)
        self.offset_data = np.empty((total_offsets,), dtype=np.float32)

        # Fill buffers using slicing
        vertex_index = 0
        color_index = 0
        offset_index = 0

        for i in range(len(shapes)):
            shape = shapes[i]

            vertices = shape._vertex_data.flatten()
            colors = shape._color_data
            offset = shape._offset_data

            num_points = vertices.shape[0] // 2
            colors_array = repeat_array_cython(colors, num_points)
            offset_array = repeat_array_cython(offset, num_points)

            if vertex_index > 0:
                # Add degenerate vertices to separate shapes
                # Copy the last vertex of the previous shape
                self.vertex_data[vertex_index:vertex_index + 2] = self.vertex_data[vertex_index - 2:vertex_index]
                self.color_data[color_index:color_index + 4] = self.color_data[color_index - 4:color_index]
                self.offset_data[offset_index:offset_index + 2] = self.offset_data[offset_index - 2:offset_index]

                # Copy the first vertex of the current shape
                self.vertex_data[vertex_index + 2:vertex_index + 4] = vertices[:2]
                self.color_data[color_index + 4:color_index + 8] = colors_array[:4]
                self.offset_data[offset_index + 2:offset_index + 4] = offset_array[:2]

                vertex_index += 4
                color_index += 8
                offset_index += 4

            # Add current shape's data
            self.vertex_data[vertex_index:vertex_index + vertices.shape[0]] = vertices
            self.color_data[color_index:color_index + colors_array.shape[0]] = colors_array
            self.offset_data[offset_index:offset_index + offset_array.shape[0]] = offset_array

            vertex_index += vertices.shape[0]
            color_index += colors_array.shape[0]
            offset_index += offset_array.shape[0]

            if i == len(shapes) - 1:
                # Add degenerate vertices for the end of the last shape
                # Copy the last vertex of the current shape twice to close the shape cleanly
                self.vertex_data[vertex_index:vertex_index + 2] = vertices[-2:]
                self.vertex_data[vertex_index + 2:vertex_index + 4] = vertices[-2:]
                self.color_data[color_index:color_index + 4] = colors_array[-4:]
                self.color_data[color_index + 4:color_index + 8] = colors_array[-4:]
                self.offset_data[offset_index:offset_index + 2] = offset_array[-2:]
                self.offset_data[offset_index + 2:offset_index + 4] = offset_array[-2:]

                vertex_index += 4
                color_index += 8
                offset_index += 4

            # Reset shape change flags
            shape._render_pipeline_color_data_changed = False
            shape._render_pipeline_vertex_data_changed = False
            shape._render_pipeline_offset_data_changed = False

        # Upload data to GPU
        self._vbo.set_data(self.vertex_data)
        self._cbo.set_data(self.color_data)
        self._obo.set_data(self.offset_data)

    def _internal_render(self):
        new_aspect_ratio = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()
        if new_aspect_ratio != self.aspect_ratio:
            self._program.set_shader_variable(
                "aspect_ratio", new_aspect_ratio
            )
            self.aspect_ratio = new_aspect_ratio

        self._vao.create(
            self._program,
            self._vbo, ["2f", "in_position"],
            color_buffer_object=self._cbo, color_buffer_shader_attributes=["4f", "in_color"],
            additional_buffers=[self._obo], additional_buffer_attributes=[["2f", "in_offset"]],
        )
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)
