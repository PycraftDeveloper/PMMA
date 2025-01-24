import numpy as np
cimport numpy as cnp

# Define types for clarity
ctypedef cnp.float32_t float32
ctypedef cnp.int32_t int32

cdef class RenderPipeline:
    cdef:
        list shapes            # List of dictionaries to store shape data
        object vertex_data     # Vertex array (2D float32 array)
        object index_data      # Index array (1D int32 array)
        bint rebuild

    def __cinit__(self):
        """
        Initialize the ShapeManager with a ModernGL context and shader program.
        """
        self.shapes = []
        self.vertex_data = np.empty((0, 5), dtype=np.float32)  # (x, y, r, g, b)
        self.index_data = np.empty(0, dtype=np.int32)
        #self.rebuild = False

    cpdef add_shape(self, float32[:, :] points, int32[:] indices, float32[::1] color):
        """
        Add a new shape.
        - points: A 2D array of vertex positions (x, y).
        - indices: A 1D array of indices defining triangles.
        - color: A 1D array representing the solid color (r, g, b).
        """
        cdef int index_offset = len(self.vertex_data)

        # Append shape data to the shape list
        self.shapes.append({
            "points": points.copy(),
            "indices": indices.copy(),
            "color": color.copy(),
            "start_index": len(self.index_data),  # Track start index for this shape
            "end_index": len(self.index_data) + len(indices),  # Track end index
        })

        # Add vertices with color
        cdef int num_points = points.shape[0]
        cdef cnp.ndarray[float32, ndim=2] new_vertex_data = np.empty((num_points, 5), dtype=np.float32)

        for i in range(num_points):
            new_vertex_data[i, 0] = points[i, 0]
            new_vertex_data[i, 1] = points[i, 1]
            new_vertex_data[i, 2] = color[0]
            new_vertex_data[i, 3] = color[1]
            new_vertex_data[i, 4] = color[2]

        self.vertex_data = np.vstack([self.vertex_data, new_vertex_data])

        # Adjust indices and append
        adjusted_indices = np.add(indices, index_offset)
        self.index_data = np.hstack([self.index_data, adjusted_indices])

    cpdef update_shape(self, int shape_index, float32[:, :] points=None, int32[:] indices=None, float32[::1] color=None):
        """
        Update an existing shape.
        - shape_index: Index of the shape to modify.
        - points: New vertex positions, if provided.
        - indices: New indices, if provided.
        - color: New color, if provided.
        """
        cdef dict shape = self.shapes[shape_index]

        # Update points and color
        if points is not None:
            shape["points"] = points.copy()

        if color is not None:
            shape["color"] = color.copy()

        # Update indices
        if indices is not None:
            shape["indices"] = indices.copy()

        if points is not None or color is not None or indices is not None:
            self.rebuild = True

    cdef void _build_data(self):
        """
        Rebuild the vertex and index buffers only for dirty shapes.
        """
        # Declare variables at the top
        cdef int index_offset = 0
        cdef int num_points
        cdef cnp.ndarray[float32, ndim=2] points
        cdef cnp.ndarray[int32, ndim=1] indices
        cdef cnp.ndarray[float32, ndim=1] color
        cdef cnp.ndarray[float32, ndim=2] new_vertex_data

        # Initialize empty vertex and index data arrays
        self.vertex_data = np.empty((0, 5), dtype=np.float32)
        self.index_data = np.empty(0, dtype=np.int32)

        for shape in self.shapes:
            points = np.array(shape["points"], dtype=np.float32)  # Convert to NumPy array
            indices = np.array(shape["indices"], dtype=np.int32)  # Convert to NumPy array
            color = np.array(shape["color"], dtype=np.float32)  # Convert to NumPy array

            num_points = points.shape[0]
            new_vertex_data = np.empty((num_points, 5), dtype=np.float32)

            # Populate the new vertex data array
            new_vertex_data[:, 0:2] = points  # Copy x, y coordinates
            new_vertex_data[:, 2:5] = color

            # Append to the vertex data array
            self.vertex_data = np.vstack([self.vertex_data, new_vertex_data])

            # Adjust indices and append
            adjusted_indices = np.add(indices, index_offset)
            self.index_data = np.hstack([self.index_data, adjusted_indices])

            index_offset += num_points

        self.rebuild = False

    def get_vertex_data(self):
        if self.rebuild:
            self._build_data()
        return self.vertex_data.tobytes()

    def get_index_data(self):
        if self.rebuild:
            self._build_data()
        return self.index_data.tobytes()