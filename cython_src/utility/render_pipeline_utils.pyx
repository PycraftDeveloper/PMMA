import numpy as np
cimport numpy as cnp
import moderngl as _moderngl

from pmma.python_src.opengl import GenericBufferObject as _GenericBufferObject
from pmma.python_src.opengl import VertexArrayObject as _VertexArrayObject
from pmma.python_src.opengl import Shader as _Shader
from pmma.python_src.file import path_builder as _path_builder
from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry

cdef inline cnp.ndarray[cnp.float32_t, ndim=1] repeat_array_cython(cnp.ndarray[cnp.float32_t, ndim=1] base, int N):
    cdef int base_size = base.shape[0]
    cdef cnp.ndarray[cnp.float32_t, ndim=1] result = np.zeros(N * base_size, dtype=np.float32)
    cdef int i

    # Fill the result array using slicing
    for i in range(N):
        result[i * base_size : (i + 1) * base_size] = base

    return result

cdef class RenderPipeline:
    cdef:
        object _gbo
        object _vao
        object _program
        float aspect_ratio

    def __cinit__(self):
        self.aspect_ratio = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()

        # Buffer objects
        self._gbo = _GenericBufferObject()
        self._gbo.set_dynamic(True)
        self._vao = _VertexArrayObject()

        # Shader
        self._program = _Shader()
        self._program.load_shader_from_folder(_path_builder(_Registry.base_path, "shaders", "render_pipeline"))
        self._program.create()

    def quit(self, bint do_garbage_collection=True):
        self._shut_down = True
        self._program.quit(do_garbage_collection=False)
        self._vao.quit(do_garbage_collection=False)
        self._gbo.quit(do_garbage_collection=False)

    cdef void internal_update(self, cnp.ndarray[cnp.float32_t, ndim=3] shape_data, int total_data_points):
        # Preallocate buffer
        cdef cnp.ndarray[cnp.float32_t, ndim=1] pipeline_data = np.empty(total_data_points, dtype=np.float32)

        index = 0
        for i in range(shape_data.shape[0]):
            vertices = shape_data[i][0]
            colors = repeat_array_cython(shape_data[i][1], vertices.shape[0] // 2)
            offsets = repeat_array_cython(shape_data[i][2], vertices.shape[0] // 2)

            num_points = vertices.shape[0] // 2

            if i > 0:
                # Insert degenerate vertex: repeat last vertex of previous shape
                pipeline_data[index:index+8] = pipeline_data[index-8:index]

                # Insert first vertex of the new shape
                pipeline_data[index+8:index+10] = vertices[:2]  # Position
                pipeline_data[index+10:index+14] = colors[:4]   # Color
                pipeline_data[index+14:index+16] = offsets[:2]  # Offset

                index += 16  # Move index forward correctly

            # Insert actual shape data
            for j in range(num_points):
                pipeline_data[index:index+2] = vertices[j*2:j*2+2]
                pipeline_data[index+2:index+6] = colors[j*4:j*4+4]
                pipeline_data[index+6:index+8] = offsets[j*2:j*2+2]
                index += 8

            if i == shape_data.shape[0] - 1:
                # Insert degenerate vertices (last vertex repeated)
                pipeline_data[index:index+8] = pipeline_data[index-8:index]
                pipeline_data[index+8:index+16] = pipeline_data[index-8:index]
                index += 16

        # Upload data to GPU
        self._gbo.set_data(pipeline_data)

    cpdef void update(self, list shapes):
        cdef int i, num_points, index
        cdef cnp.ndarray[cnp.float32_t, ndim=1] vertices, colors, offsets
        cdef cnp.ndarray[cnp.float32_t, ndim=3] shape_data
        cdef object shape
        cdef cnp.ndarray[cnp.float32_t, ndim=1] single_shape_data

        # Compute total size for buffer (including degenerate vertices)
        cdef int total_data_points = 0
        for shape in shapes:
            num_points = shape._vertex_data.shape[0] // 2
            total_data_points += (num_points + 2) * 8  # 2 extra degenerate vertices, each with 8 attributes (2 pos, 4 col, 2 offset)

            single_shape_data = np.array([shape._vertex_data, shape._color_data, shape._offset_data])
            shape_data = np.append(shape_data, single_shape_data)

        self.internal_update(shape_data, total_data_points)

    def _internal_render(self):
        new_aspect_ratio = _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].get_aspect_ratio()
        if new_aspect_ratio != self.aspect_ratio:
            self._program.set_shader_variable(
                "aspect_ratio", new_aspect_ratio
            )
            self.aspect_ratio = new_aspect_ratio

        self._vao.create(
            self._program,
            self._gbo, ["2f", "in_position", "4f", "in_color", "2f", "in_offset"])
        self._vao.render(mode=_moderngl.TRIANGLE_STRIP)
