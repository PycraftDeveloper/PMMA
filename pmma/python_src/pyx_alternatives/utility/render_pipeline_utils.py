import numpy as np

class RenderPipeline:
    def __init__(self):
        """
        Initialize the ShapeManager with a ModernGL context and shader program.
        """
        self.shapes = []
        self.vertex_data = np.empty((0, 5), dtype=np.float32)  # (x, y, r, g, b)
        self.index_data = np.empty(0, dtype=np.int32)
        #rebuild = False

    def add_shape(self, points, indices, color):
        """
        Add a new shape.
        - points: A 2D array of vertex positions (x, y).
        - indices: A 1D array of indices defining triangles.
        - color: A 1D array representing the solid color (r, g, b).
        """
        index_offset = len(self.vertex_data)

        # Append shape data to the shape list
        self.shapes.append({
            "points": points.copy(),
            "indices": indices.copy(),
            "color": color.copy(),
            "start_index": len(self.index_data),  # Track start index for this shape
            "end_index": len(self.index_data) + len(indices),  # Track end index
        })

        # Add vertices with color
        num_points = points.shape[0]
        new_vertex_data = np.empty((num_points, 5), dtype=np.float32)

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

    def update_shape(self, shape_index, points=None, indices=None, color=None):
        """
        Update an existing shape.
        - shape_index: Index of the shape to modify.
        - points: New vertex positions, if provided.
        - indices: New indices, if provided.
        - color: New color, if provided.
        """
        shape = self.shapes[shape_index]

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

    def _build_data(self):
        """
        Rebuild the vertex and index buffers only for dirty shapes.
        """
        # Declare variables at the top
        index_offset = 0

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