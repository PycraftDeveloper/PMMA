# shapes.pyx
import numpy as np
cimport numpy as np

# Declare the numpy types
ctypedef np.float32_t DTYPE_f4
ctypedef np.int32_t DTYPE_i4

# Function to create a filled rectangle
def create_rect(object ctx, object program, tuple top_left, float width, float height, tuple color) -> object:
    cdef float x = top_left[0]
    cdef float y = top_left[1]

    cdef np.ndarray[DTYPE_f4, ndim=1] vertices = np.array([
        x, y,
        x + width, y,
        x + width, y + height,
        x, y + height
    ], dtype=np.float32)

    cdef np.ndarray[DTYPE_i4, ndim=1] indices = np.array([0, 1, 2, 2, 3, 0], dtype=np.int32)

    program['color'].value = color
    vbo = ctx.buffer(vertices)
    ibo = ctx.buffer(indices)
    vao = ctx.vertex_array(program, [(vbo, '2f', 'in_vert')], ibo)

    return vao

# Function to render the VAO with optional optimizations
def render_vao(object vao, int mode):
    vao.render(mode)
