import numpy as np
cimport numpy as np
from libc.math cimport sqrt

ctypedef np.float32_t DTYPE_f4
ctypedef np.int32_t DTYPE_i4

cpdef create_batch_shapes(object ctx, object program, list shapes):
    cdef int num_shapes = len(shapes)
    cdef int total_vertices = 0
    cdef int total_indices = 0

    for shape in shapes:
        if shape[0] == 0:  # Rectangle
            total_vertices += 4
            total_indices += 6
        elif shape[0] == 1:  # Circle (using a bounding rectangle)
            total_vertices += 4
            total_indices += 6
        elif shape[0] == 2:  # Triangle
            total_vertices += 3
            total_indices += 3

    cdef np.ndarray[DTYPE_f4, ndim=1] vertices_np = np.empty(total_vertices * 2, dtype=np.float32)
    cdef np.ndarray[DTYPE_f4, ndim=1] colors_np = np.empty(total_vertices * 3, dtype=np.float32)
    cdef np.ndarray[DTYPE_i4, ndim=1] indices_np = np.empty(total_indices, dtype=np.int32)

    cdef DTYPE_f4[::1] vertices = vertices_np
    cdef DTYPE_f4[::1] colors = colors_np
    cdef DTYPE_i4[::1] indices = indices_np

    cdef int vertex_offset = 0
    cdef int color_offset = 0
    cdef int index_offset = 0
    cdef int shape_index = 0

    for shape in shapes:
        if shape[0] == 0:  # Rectangle
            x, y, width, height = shape[1], shape[2], shape[3], shape[4]
            color1, color2, color3, color4 = shape[5], shape[6], shape[7], shape[8]
            vertices[vertex_offset] = x
            vertices[vertex_offset + 1] = y
            vertices[vertex_offset + 2] = x + width
            vertices[vertex_offset + 3] = y
            vertices[vertex_offset + 4] = x + width
            vertices[vertex_offset + 5] = y + height
            vertices[vertex_offset + 6] = x
            vertices[vertex_offset + 7] = y + height

            colors[color_offset] = color1[0]
            colors[color_offset + 1] = color1[1]
            colors[color_offset + 2] = color1[2]
            colors[color_offset + 3] = color2[0]
            colors[color_offset + 4] = color2[1]
            colors[color_offset + 5] = color2[2]
            colors[color_offset + 6] = color3[0]
            colors[color_offset + 7] = color3[1]
            colors[color_offset + 8] = color3[2]
            colors[color_offset + 9] = color4[0]
            colors[color_offset + 10] = color4[1]
            colors[color_offset + 11] = color4[2]

            indices[index_offset] = shape_index
            indices[index_offset + 1] = shape_index + 1
            indices[index_offset + 2] = shape_index + 2
            indices[index_offset + 3] = shape_index + 2
            indices[index_offset + 4] = shape_index + 3
            indices[index_offset + 5] = shape_index

            vertex_offset += 8
            color_offset += 12
            index_offset += 6
            shape_index += 4

        elif shape[0] == 1:  # Circle
            x, y, radius = shape[1], shape[2], shape[3]
            center_color, edge_color = shape[4], shape[5]
            half_size = radius * sqrt(2) / 2
            vertices[vertex_offset] = x - half_size
            vertices[vertex_offset + 1] = y - half_size
            vertices[vertex_offset + 2] = x + half_size
            vertices[vertex_offset + 3] = y - half_size
            vertices[vertex_offset + 4] = x + half_size
            vertices[vertex_offset + 5] = y + half_size
            vertices[vertex_offset + 6] = x - half_size
            vertices[vertex_offset + 7] = y + half_size

            colors[color_offset] = center_color[0]
            colors[color_offset + 1] = center_color[1]
            colors[color_offset + 2] = center_color[2]
            colors[color_offset + 3] = center_color[0]
            colors[color_offset + 4] = center_color[1]
            colors[color_offset + 5] = center_color[2]
            colors[color_offset + 6] = edge_color[0]
            colors[color_offset + 7] = edge_color[1]
            colors[color_offset + 8] = edge_color[2]
            colors[color_offset + 9] = edge_color[0]
            colors[color_offset + 10] = edge_color[1]
            colors[color_offset + 11] = edge_color[2]

            indices[index_offset] = shape_index
            indices[index_offset + 1] = shape_index + 1
            indices[index_offset + 2] = shape_index + 2
            indices[index_offset + 3] = shape_index + 2
            indices[index_offset + 4] = shape_index + 3
            indices[index_offset + 5] = shape_index

            vertex_offset += 8
            color_offset += 12
            index_offset += 6
            shape_index += 4

        elif shape[0] == 2:  # Triangle
            x1, y1, x2, y2, x3, y3 = shape[1], shape[2], shape[3], shape[4], shape[5], shape[6]
            color1, color2, color3 = shape[7], shape[8], shape[9]
            vertices[vertex_offset] = x1
            vertices[vertex_offset + 1] = y1
            vertices[vertex_offset + 2] = x2
            vertices[vertex_offset + 3] = y2
            vertices[vertex_offset + 4] = x3
            vertices[vertex_offset + 5] = y3

            colors[color_offset] = color1[0]
            colors[color_offset + 1] = color1[1]
            colors[color_offset + 2] = color1[2]
            colors[color_offset + 3] = color2[0]
            colors[color_offset + 4] = color2[1]
            colors[color_offset + 5] = color2[2]
            colors[color_offset + 6] = color3[0]
            colors[color_offset + 7] = color3[1]
            colors[color_offset + 8] = color3[2]

            indices[index_offset] = shape_index
            indices[index_offset + 1] = shape_index + 1
            indices[index_offset + 2] = shape_index + 2

            vertex_offset += 6
            color_offset += 9
            index_offset += 3
            shape_index += 3

    vbo = ctx.buffer(vertices)
    cbo = ctx.buffer(colors)
    ibo = ctx.buffer(indices)
    vao = ctx.vertex_array(program, [(vbo, '2f', 'in_vert'), (cbo, '3f', 'in_color')], ibo)

    return vao, vbo, cbo, ibo
