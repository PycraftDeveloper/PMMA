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
        cdef int i, num_points
        cdef cnp.ndarray[cnp.float32_t, ndim=1] vertices, colors_array, offset_array
        cdef cnp.ndarray[cnp.float32_t, ndim=1] degenerate_vertex, degenerate_color, degenerate_offset
        cdef cnp.ndarray[cnp.float32_t, ndim=1] first_vertex, first_color, first_offset

        if shapes == self.shapes:
            for shape in shapes:
                if (shape._render_pipeline_color_data_changed or
                    shape._render_pipeline_vertex_data_changed or
                    shape._render_pipeline_offset_data_changed):
                    break
            else:
                return

        self.shapes = shapes

        # Reallocate buffers
        self.vertex_data = np.empty((0,), dtype=np.float32)
        self.color_data = np.empty((0,), dtype=np.float32)
        self.offset_data = np.empty((0,), dtype=np.float32)

        for i, shape in enumerate(shapes):
            vertices = shape._vertex_data.flatten()
            colors = shape._color_data
            offset = shape._offset_data

            num_points = vertices.shape[0] // 2

            if len(colors) == 3:
                colors = np.append(colors, 1.0)  # Ensure RGBA
                colors = colors.astype(np.float32)
            else:
                colors = np.array(colors, dtype=np.float32)

            offset = np.array(offset, dtype=np.float32)

            colors_array = repeat_array_cython(colors, num_points) # -1 ??
            offset_array = repeat_array_cython(offset, num_points)

            if self.vertex_data.size > 0:
                degenerate_vertex = self.vertex_data[-2:]
                degenerate_color = self.color_data[-4:]
                degenerate_offset = self.offset_data[-2:]

                first_vertex = vertices[:2]
                first_color = colors_array[:4]
                first_offset = offset_array[:2]

                self.vertex_data = np.concatenate([self.vertex_data, degenerate_vertex, first_vertex])
                self.color_data = np.concatenate([self.color_data, degenerate_color, first_color])
                self.offset_data = np.concatenate([self.offset_data, degenerate_offset, first_offset])

            self.vertex_data = np.concatenate([self.vertex_data, vertices])
            self.color_data = np.concatenate([self.color_data, colors_array])
            self.offset_data = np.concatenate([self.offset_data, offset_array])

            if i == len(shapes) - 1:
                degenerate_vertex = vertices[-2:]
                degenerate_color = colors_array[-4:]
                degenerate_offset = offset_array[-2:]

                self.vertex_data = np.concatenate([self.vertex_data, degenerate_vertex, degenerate_vertex])
                self.color_data = np.concatenate([self.color_data, degenerate_color, degenerate_color])
                self.offset_data = np.concatenate([self.offset_data, degenerate_offset, degenerate_offset])

            shape._render_pipeline_color_data_changed = False
            shape._render_pipeline_vertex_data_changed = False
            shape._render_pipeline_offset_data_changed = False

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
