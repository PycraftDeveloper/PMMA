import numpy as np

# Define the types for numpy arrays

# Cubic smoothstep function for acceleration/deceleration
def raw_smooth_step(t):
    """
    🟩 **R** -
    """
    return t * t * (3 - 2 * t)

# Clamping and mapping function
def raw_ranger(value, old, new):
    """
    🟩 **R** -
    """
    # Ensure value is within bounds of the 'old' range
    if value > old[1]:
        value = old[1]
    elif value < old[0]:
        value = old[0]

    # Check if 'old' and 'new' lists are identical
    if old[0] == new[0] and old[1] == new[1]:
        return value

    old_range = old[1] - old[0]
    new_range = new[1] - new[0]

    if old_range == 0:
        old_range = np.finfo(float).tiny

    new_value = (((value - old[0]) * new_range) / old_range) + new[0]
    return new_value

# Clamping and mapping function for numpy arrays
def raw_nparray_ranger(value, old, new):
    """
    🟩 **R** -
    """
    value[value > old[1]] = old[1]
    value[value < old[0]] = old[0]

    if np.array_equal(old, new):
        return value

    old_range = old[1] - old[0]
    new_range = new[1] - new[0]

    if old_range == 0:
        old_range = np.finfo(float).tiny

    new_value = (((value - old[0]) * new_range) / old_range) + new[0]
    return new_value

# Compute the camera's orientation matrix
def raw_gl_look_at(pos, target, up):
    """
    🟩 **R** -
    """
    x, y, z = raw_compute_position(pos, target, up)

    translate = np.identity(4, dtype=np.double32)
    translate[3][0] = -pos[0]
    translate[3][1] = -pos[1]
    translate[3][2] = -pos[2]

    rotate = np.identity(4, dtype=np.double32)
    rotate[0][0] = x[0]  # -- X
    rotate[1][0] = x[1]
    rotate[2][0] = x[2]
    rotate[0][1] = y[0]  # -- Y
    rotate[1][1] = y[1]
    rotate[2][1] = y[2]
    rotate[0][2] = z[0]  # -- Z
    rotate[1][2] = z[1]
    rotate[2][2] = z[2]

    return rotate @ translate[:, np.newaxis]

# Compute the norm and direction
def raw_pythag(points):
    """
    🟩 **R** -
    """
    sum = 0
    for point in points:
        sum += point ** 2
    return sum ** 0.5

# Function to normalize a vector
def normalize(v):
    """
    🟩 **R** -
    """
    norm = np.dot(v, v) ** 0.5  # Compute the norm manually
    if norm == 0:
        return v
    return v / norm

# Function to compute the camera's basis vectors
def raw_compute_position(pos, target, up):
    """
    🟩 **R** -
    """
    z = normalize(target - pos)
    x = normalize(np.cross(up, z))
    y = np.cross(z, x)
    return (x, y, z)

# Look at function
def raw_look_at(camera_position, camera_target, up_vector):
    """
    🟩 **R** -
    """
    vector = camera_target - camera_position

    x = np.linalg.norm(vector)
    vector = vector / x

    vector2 = np.cross(up_vector, vector)
    vector2 /= np.linalg.norm(vector2)

    vector3 = np.cross(vector, vector2)

    return np.array([
        [vector2[0], vector3[0], vector[0], 0.0],
        [vector2[1], vector3[1], vector[1], 0.0],
        [vector2[2], vector3[2], vector[2], 0.0],
        [-np.dot(vector2, camera_position), -np.dot(vector3, camera_position), np.dot(vector, camera_position), 1.0]
    ], dtype=np.double32)

# Matrix multiplication function
def raw_multiply(light_proj, sun_light_look_at):
    """
    🟩 **R** -
    """
    return light_proj @ sun_light_look_at
