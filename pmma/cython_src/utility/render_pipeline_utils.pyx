# cython: language_level=3

import cython

from libc.string cimport memcpy
cimport numpy as cnp

import numpy as np
import moderngl as _moderngl

from pmma.python_src.opengl import GenericBufferObject as _GenericBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.file import path_builder as _path_builder

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline cnp.ndarray[cnp.float32_t, ndim=1] repeat_array_cython(cnp.ndarray[cnp.float32_t, ndim=1] base, int N):
    cdef int base_size = base.shape[0]
    cdef cnp.ndarray[cnp.float32_t, ndim=1] result = np.empty(N * base_size, dtype=np.float32)
    cdef int i
    for i in range(N):
        memcpy(&result[i * base_size], &base[0], base_size * sizeof(cnp.float32_t))
    return result

cdef class RenderPipeline:
    cdef:
        object _gbo
        object _vao
        object _program
        float aspect_ratio
        int _total_vertexes

    def __cinit__(self):
        self.aspect_ratio = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio()
        self._gbo = _GenericBufferObject()
        self._gbo.set_dynamic(True)
        self._vao = _VertexArrayObject()
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "render_pipeline"))
        self._program.create()
        self._program.set_shader_variable("aspect_ratio", self.aspect_ratio)
        self._total_vertexes = 0

    def quit(self):
        self._program.quit()
        self._vao.quit()
        self._gbo.quit()

    @cython.boundscheck(False) # compiler directive
    @cython.wraparound(False) # compiler directive
    cdef void internal_update(self, list shape_data, int total_data_points) noexcept:
        cdef cnp.float32_t[::1] pipeline_data = np.empty(total_data_points, dtype=np.float32)
        cdef cnp.float32_t[::1] colors, vertices, offsets
        cdef int index = 0
        cdef int i, num_points

        for i in range(len(shape_data)):
            vertices = shape_data[i][0]
            num_points = vertices.shape[0] // 2
            colors = repeat_array_cython(shape_data[i][1], num_points)
            offsets = repeat_array_cython(shape_data[i][2], num_points)

            if i > 0:
                pipeline_data[index:index+8] = pipeline_data[index-8:index]
                pipeline_data[index+8:index+10] = vertices[:2]
                pipeline_data[index+10:index+14] = colors[:4]
                pipeline_data[index+14:index+16] = offsets[:2]
                index += 16

            pipeline_data[index:index + 8 * num_points:8] = vertices[::2]
            pipeline_data[index + 1:index + 8 * num_points:8] = vertices[1::2]
            pipeline_data[index + 2:index + 8 * num_points:8] = colors[::4]
            pipeline_data[index + 3:index + 8 * num_points:8] = colors[1::4]
            pipeline_data[index + 4:index + 8 * num_points:8] = colors[2::4]
            pipeline_data[index + 5:index + 8 * num_points:8] = colors[3::4]
            pipeline_data[index + 6:index + 8 * num_points:8] = offsets[::2]
            pipeline_data[index + 7:index + 8 * num_points:8] = offsets[1::2]

            index += 8 * num_points

            if i == len(shape_data) - 1:
                pipeline_data[index:index+8] = pipeline_data[index-8:index]
                pipeline_data[index+8:index+16] = pipeline_data[index-8:index]
                index += 16

        self._gbo.set_data(pipeline_data)

    @cython.boundscheck(False) # compiler directive
    @cython.wraparound(False) # compiler directive
    cpdef void update(self, list shapes):
        cdef int i, num_points, total_data_points = 0
        cdef int num_shapes = len(shapes)
        cdef list shape_data_list = [None] * num_shapes  # Preallocate list
        cdef object shape

        for i in range(num_shapes):
            shape = shapes[i]
            num_points = shape._vertex_data.shape[0] // 2
            total_data_points += (num_points + 2) * 8
            shape_data_list[i] = [shape._vertex_data, shape._color_data, shape._offset_data]

        self.internal_update(shape_data_list, total_data_points)

    cpdef _internal_render(self):
        new_aspect_ratio = _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].get_aspect_ratio()
        if new_aspect_ratio != self.aspect_ratio:
            self._program.set_shader_variable("aspect_ratio", new_aspect_ratio)
            self.aspect_ratio = new_aspect_ratio

        if self._vao.get_created() is False:
            self._vao.create(self._program, self._gbo, ["2f", "in_position", "4f", "in_color", "2f", "in_offset"])

        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)
