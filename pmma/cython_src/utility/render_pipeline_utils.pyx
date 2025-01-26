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

cdef cnp.ndarray[cnp.float32_t, ndim=1] repeat_array_cython(
    cnp.ndarray[cnp.float32_t, ndim=1] base, int N
):
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
        cdef int i, num_points, total_vertices, total_colors, total_offsets
        cdef cnp.ndarray[cnp.float32_t, ndim=1] vertices
        cdef list colors, offset
        cdef cnp.ndarray[cnp.float32_t, ndim=1] degenerate_vertex, degenerate_color, degenerate_offset
        cdef cnp.ndarray[cnp.float32_t, ndim=1] first_vertex, first_color, first_offset

        # Check if update is needed
        if shapes == self.shapes:
            for shape in shapes:
                if (shape._render_pipeline_color_data_changed or
                    shape._render_pipeline_vertex_data_changed or
                    shape._render_pipeline_offset_data_changed):
                    break
            else:
                return

        self.shapes = shapes

        # Calculate total sizes for preallocation
        total_vertices = 0
        total_colors = 0
        total_offsets = 0
        for shape in shapes:
            vertices = shape._vertex_data.flatten()
            total_vertices += vertices.shape[0]
            total_colors += (vertices.shape[0] // 2) * 4  # RGBA per vertex
            total_offsets += vertices.shape[0]  # 2D offset per vertex

        # Preallocate buffers
        self.vertex_data = np.empty((total_vertices + 2 * len(shapes),), dtype=np.float32)  # Degenerate vertices
        self.color_data = np.empty((total_colors + 8 * len(shapes),), dtype=np.float32)  # Degenerate colors
        self.offset_data = np.empty((total_offsets + 2 * len(shapes),), dtype=np.float32)  # Degenerate offsets

        cdef int vertex_index = 0
        cdef int color_index = 0
        cdef int offset_index = 0

        for i, shape in enumerate(shapes):
            vertices = shape._vertex_data.flatten()
            colors = shape._color_data
            offset = shape._offset_data

            num_points = (vertices.shape[0] // 2)

            if len(colors) == 3:
                colors.append(1.0)

            colors_array = np.array(colors*num_points, dtype=np.float32)
            offset_array = np.array(offset*num_points, dtype=np.float32)

            if vertex_index > 0:
                # Add degenerate triangle to join previous and current shape
                degenerate_vertex = self.vertex_data[vertex_index - 2:vertex_index]
                degenerate_color = self.color_data[color_index - 4:color_index]
                degenerate_offset = self.offset_data[offset_index - 2:offset_index]

                first_vertex = vertices[:2]
                first_color = colors_array[:4]
                first_offset = offset_array[:2]

                self.vertex_data[vertex_index:vertex_index + 2] = degenerate_vertex
                self.color_data[color_index:color_index + 4] = degenerate_color
                self.offset_data[offset_index:offset_index + 2] = degenerate_offset

                vertex_index += 2
                color_index += 4
                offset_index += 2

            # Add shape data
            self.vertex_data[vertex_index:vertex_index + vertices.shape[0]] = vertices
            self.color_data[color_index:color_index + colors_array.shape[0]] = colors_array
            self.offset_data[offset_index:offset_index + offset_array.shape[0]] = offset_array

            vertex_index += vertices.shape[0]
            color_index += colors_array.shape[0]
            offset_index += offset_array.shape[0]

            if i == len(shapes) - 1:
                # Add degenerate triangle at the end
                degenerate_vertex = vertices[-2:]
                degenerate_color = colors_array[-4:]
                degenerate_offset = offset_array[-2:]

                self.vertex_data[vertex_index:vertex_index + 2] = degenerate_vertex
                self.color_data[color_index:color_index + 4] = degenerate_color
                self.offset_data[offset_index:offset_index + 2] = degenerate_offset

                vertex_index += 2
                color_index += 4
                offset_index += 2

            shape._render_pipeline_color_data_changed = False
            shape._render_pipeline_vertex_data_changed = False
            shape._render_pipeline_offset_data_changed = False

        # Trim excess memory
        self.vertex_data = self.vertex_data[:vertex_index]
        self.color_data = self.color_data[:color_index]
        self.offset_data = self.offset_data[:offset_index]

        # Update VBOs
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
