import numpy as np
import numba

@numba.njit(fastmath=True, cache=True)
def fade(t):
    """Fade function as defined by Ken Perlin. This eases coordinate values
    so that they will ease towards integral values. This ends up smoothing
    the final output."""
    return t * t * t * (t * (t * 6 - 15) + 10)

@numba.njit(fastmath=True, cache=True)
def lerp(t, a, b):
        """Linear interpolation function."""
        return a + t * (b - a)

@numba.njit(fastmath=True, cache=True)
def grad(hash, x):
        """Calculate gradient vector and dot product with distance vector."""
        g = hash & 15
        grad = 1 + (g & 7)  # Gradient is one of 1, 2, ..., 8
        if g & 8:
            grad = -grad  # And a random sign for the gradient
        return grad * x

@numba.njit(fastmath=True, cache=True)
def noise(x, permutation):
    """Generate Perlin noise value at a given x coordinate."""
    xi = int(np.floor(x)) & 255  # Calculate the "unit cube" that the point asked will be located in
    xf = x - np.floor(x)         # Relative x coordinate in the unit cube
    u = fade(xf)            # Compute fade curves for each of x

    # Hash coordinates of the 2 cube corners
    aa = permutation[xi]
    ab = permutation[xi + 1]

    # And add blended results from 2 corners of the cube
    x1 = lerp(u, grad(aa, xf), grad(ab, xf - 1))

    return (x1 + 1) / 2  # Normalize to [0, 1] range

class PerlinNoise1D:
    def __init__(self, seed=None):
        self.permutation = np.arange(256, dtype=int)
        if seed is not None:
            np.random.seed(seed)
        np.random.shuffle(self.permutation)
        self.permutation = np.stack([self.permutation, self.permutation]).flatten()

# Example usage
perlin = PerlinNoise1D(seed=42)
noise_values = noise(0, perlin.permutation)
x_values = 0
import time
tt = 0
for i in range(100_000):
    start = time.perf_counter()
    noise_values = noise(x_values, perlin.permutation)
    end = time.perf_counter()
    tt += end - start
print(tt/i)
print(1/(tt/i))
print(noise_values)
