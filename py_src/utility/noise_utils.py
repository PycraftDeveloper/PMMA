import math

from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

from pmma.py_src.utility.math_utils import *

import numpy as np

GRADIENTS2 = Constants.GRADIENTS2
STRETCH_CONSTANT2 = Constants.STRETCH_CONSTANT2
SQUISH_CONSTANT2 = Constants.SQUISH_CONSTANT2
SQUISH_CONSTANT2 = Constants.SQUISH_CONSTANT2
NORM_CONSTANT2 = Constants.NORM_CONSTANT2
GRADIENTS3 = Constants.GRADIENTS3

def raw_generate_1D_perlin_noise(x, permutation, fade_function, grad_function, lerp_function):
    """Generate Perlin noise value at a given x coordinate."""
    xi = int(np.floor(x)) & 255  # Calculate the "unit cube" that the point asked will be located in
    xf = x - np.floor(x)         # Relative x coordinate in the unit cube
    u = fade_function(xf)            # Compute fade curves for each of x

    # Hash coordinates of the 2 cube corners
    aa = permutation[xi]
    ab = permutation[xi + 1]

    # And add blended results from 2 corners of the cube
    x1 = lerp_function(u, grad_function(aa, xf), grad_function(ab, xf - 1))

    return (x1 + 1) / 2  # Normalize to [0, 1] range

def raw_generate_2D_perlin_noise(x, y, permutation, fade_function, grad_function, lerp_function):
    """Generate Perlin noise value at coordinates (x, y)."""
    xi = int(np.floor(x)) & 255
    yi = int(np.floor(y)) & 255
    xf = x - np.floor(x)
    yf = y - np.floor(y)
    u = fade_function(xf)
    v = fade_function(yf)

    aa = permutation[permutation[xi] + yi]
    ab = permutation[permutation[xi] + yi + 1]
    ba = permutation[permutation[xi + 1] + yi]
    bb = permutation[permutation[xi + 1] + yi + 1]

    x1 = lerp_function(u, grad_function(aa, xf, yf), grad_function(ba, xf - 1, yf))
    x2 = lerp_function(u, grad_function(ab, xf, yf - 1), grad_function(bb, xf - 1, yf - 1))

    return (lerp_function(v, x1, x2) + 1) / 2  # Normalize to [0, 1]

def raw_generate_seedless_1D_perlin_noise(x, fade_function, hash_function, grad_function, lerp_function):
    # Determine grid cell coordinates
    x0 = math.floor(x)
    x1 = x0 + 1

    # Relative x coordinate in the cell
    sx = x - x0

    # Fade curves
    u = fade_function(sx)

    # Hash coordinates of the 1D points
    h0 = hash_function(x0)
    h1 = hash_function(x1)

    # Calculate gradient vectors and dot product with distance vectors
    g0 = grad_function(h0, sx)
    g1 = grad_function(h1, sx - 1)

    # Interpolate between the results
    return lerp_function(g0, g1, u)

def raw_generate_seedless_2D_perlin_noise(x, y, fade_function, hash_function, grad_function, lerp_function):
    # Determine grid cell coordinates
    x0 = math.floor(x)
    y0 = math.floor(y)
    x1 = x0 + 1
    y1 = y0 + 1

    # Relative coordinates in the cell
    sx = x - x0
    sy = y - y0

    # Fade curves
    u = fade_function(sx)
    v = fade_function(sy)

    # Hash coordinates of the 2D points
    h00 = hash_function(x0, y0)
    h10 = hash_function(x1, y0)
    h01 = hash_function(x0, y1)
    h11 = hash_function(x1, y1)

    # Calculate gradient vectors and dot product with distance vectors
    g00 = grad_function(h00, sx, sy)
    g10 = grad_function(h10, sx - 1, sy)
    g01 = grad_function(h01, sx, sy - 1)
    g11 = grad_function(h11, sx - 1, sy - 1)

    # Interpolate between the results
    nx0 = lerp_function(g00, g10, u)
    nx1 = lerp_function(g01, g11, u)
    nxy = lerp_function(nx0, nx1, v)

    return nxy