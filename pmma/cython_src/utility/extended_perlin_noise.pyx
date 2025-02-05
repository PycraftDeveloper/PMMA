# cython: language_level=3

# Correct import for numpy and accessing its random module
from numpy import random as _numpy__random
from numpy import empty as _numpy__empty
from numpy import float64 as _numpy__float64
from numpy import asarray as _numpy__asarray
from libc.math cimport floor, pow

cdef inline double fade(double t) noexcept:
    """
    🟩 **R** -
    """
    return t * t * t * (t * (t * 6 - 15) + 10)

cdef inline double lerp(double t, double a, double b) noexcept:
    """
    🟩 **R** -
    """
    return a + t * (b - a)

cdef inline double grad(int hash, double x, double y=0, double z=0) noexcept:
    """
    🟩 **R** -
    """
    cdef int h = hash & 15
    cdef double u = x if h < 8 else y
    cdef double v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return ((u if h & 1 == 0 else -u) + (v if h & 2 == 0 else -v))

cdef class ExtendedPerlinNoise:
    """
    🟩 **R** -
    """
    cdef int[512] permutation
    cdef int octaves
    cdef double persistence

    def __init__(self, int seed, int octaves, double persistence):
        """
        🟩 **R** -
        """
        self.init_permutation(seed)
        self.octaves = octaves
        self.persistence = persistence

    def init_permutation(self, int seed):
        """
        🟩 **R** -
        """
        cdef int i
        rng = _numpy__random.RandomState(seed)
        perm = rng.permutation(256)
        for i in range(256):
            self.permutation[i] = self.permutation[i + 256] = perm[i]

    cdef inline double perlin(self, double x, double y=0, double z=0) noexcept:
        """
        🟩 **R** -
        """
        cdef int X = int(floor(x)) & 255
        cdef int Y = int(floor(y)) & 255
        cdef int Z = int(floor(z)) & 255

        x -= floor(x)
        y -= floor(y)
        z -= floor(z)

        u = fade(x)
        v = fade(y)
        w = fade(z)

        cdef int A = self.permutation[X  ]+Y
        cdef int AA = self.permutation[A]+Z
        cdef int AB = self.permutation[A+1]+Z
        cdef int B = self.permutation[X+1]+Y
        cdef int BA = self.permutation[B]+Z
        cdef int BB = self.permutation[B+1]+Z

        return lerp(w, lerp(v, lerp(u, grad(self.permutation[AA  ], x  , y  , z  ),
                                       grad(self.permutation[BA  ], x-1, y  , z  )),
                               lerp(u, grad(self.permutation[AB  ], x  , y-1, z  ),
                                       grad(self.permutation[BB  ], x-1, y-1, z  ))),
                       lerp(v, lerp(u, grad(self.permutation[AA+1], x  , y  , z-1),
                                       grad(self.permutation[BA+1], x-1, y  , z-1)),
                               lerp(u, grad(self.permutation[AB+1], x  , y-1, z-1),
                                       grad(self.permutation[BB+1], x-1, y-1, z-1))))

    def generate_fbm_1d(self, double[:] input_array):
        """
        🟩 **R** -
        """
        cdef int length = input_array.shape[0]
        cdef double[:] output_array = _numpy__empty(length, dtype=_numpy__float64)
        cdef int i, j
        cdef double amplitude, frequency, total, max_amplitude
        for i in range(length):
            amplitude = 1.0
            frequency = 1.0
            total = 0.0
            max_amplitude = 0.0
            for j in range(self.octaves):
                total += self.perlin(input_array[i] * frequency) * amplitude
                max_amplitude += amplitude
                amplitude *= self.persistence
                frequency *= 2
            output_array[i] = total / max_amplitude
        return _numpy__asarray(output_array)

    def generate_fbm_2d(self, double[:, :, :] input_array):
        """
        🟩 **R** -
        """
        cdef int height = input_array.shape[0]
        cdef int width = input_array.shape[1]
        cdef double[:, :] output_array = _numpy__empty((height, width), dtype=_numpy__float64)
        cdef int i, j, k
        cdef double amplitude, frequency, total, max_amplitude, x, y
        for i in range(height):
            for j in range(width):
                x = input_array[i, j, 0]
                y = input_array[i, j, 1]
                amplitude = 1.0
                frequency = 1.0
                total = 0.0
                max_amplitude = 0.0
                for k in range(self.octaves):
                    total += self.perlin(x * frequency, y * frequency) * amplitude
                    max_amplitude += amplitude
                    amplitude *= self.persistence
                    frequency *= 2
                output_array[i, j] = total / max_amplitude
        return _numpy__asarray(output_array)

    def generate_fbm_3d(self, double[:, :, :, :] input_array):
        """
        🟩 **R** -
        """
        cdef int depth = input_array.shape[0]
        cdef int height = input_array.shape[1]
        cdef int width = input_array.shape[2]
        cdef double[:, :, :] output_array = _numpy__empty((depth, height, width), dtype=_numpy__float64)
        cdef int i, j, k, l
        cdef double amplitude, frequency, total, max_amplitude, x, y, z
        for i in range(depth):
            for j in range(height):
                for k in range(width):
                    x = input_array[i, j, k, 0]
                    y = input_array[i, j, k, 1]
                    z = input_array[i, j, k, 2]
                    amplitude = 1.0
                    frequency = 1.0
                    total = 0.0
                    max_amplitude = 0.0
                    for l in range(self.octaves):
                        total += self.perlin(x * frequency, y * frequency, z * frequency) * amplitude
                        max_amplitude += amplitude
                        amplitude *= self.persistence
                        frequency *= 2
                    output_array[i, j, k] = total / max_amplitude
        return _numpy__asarray(output_array)
