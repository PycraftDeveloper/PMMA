# cython: language_level=3

from libc.math cimport floor
from libc.stdlib cimport rand, srand
from libc.time cimport time

import cython

cdef int PERMUTATION_SIZE = 512

cdef extern from "math.h":
    double floor(double) noexcept nogil

cdef inline double fade(double t) noexcept nogil:
    """
    🟩 **R** -
    """
    return t * t * t * (t * (t * 6 - 15) + 10)

cdef inline double lerp(double t, double a, double b) noexcept nogil:
    """
    🟩 **R** -
    """
    return a + t * (b - a)

cdef inline double grad1(int hash, double x) noexcept nogil:
    """
    🟩 **R** -
    """
    cdef int h = hash & 15
    cdef double grad = 1.0 + (h & 7)
    if h & 8:
        grad = -grad
    return grad * x

cdef inline double grad2(int hash, double x, double y) noexcept nogil:
    """
    🟩 **R** -
    """
    cdef int h = hash & 7
    cdef double u = x if h < 4 else y
    cdef double v = y if h < 4 else x
    return ((-u if h & 1 else u) + (-2.0 * v if h & 2 else 2.0 * v))

cdef inline double grad3(int hash, double x, double y, double z) noexcept nogil:
    """
    🟩 **R** -
    """
    cdef int h = hash & 15
    cdef double u = x if h < 8 else y
    cdef double v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return ((u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v))

cdef class PerlinNoise:
    """
    🟩 **R** -
    """
    cdef int p[512]
    cdef int octaves
    cdef double persistence

    def __init__(self, int seed, int octaves, double persistence):
        """
        🟩 **R** -
        """
        self.init_permutation(seed)
        self.octaves = octaves
        self.persistence = persistence

    cdef void init_permutation(self, int seed) noexcept:
        """
        🟩 **R** -
        """
        cdef int perm[256]
        cdef int i, j, temp

        for i in range(256):
            perm[i] = i

        srand(seed)
        for i in range(255, 0, -1):
            j = rand() % (i + 1)
            temp = perm[i]
            perm[i] = perm[j]
            perm[j] = temp

        for i in range(256):
            self.p[256 + i] = self.p[i] = perm[i]

    @cython.boundscheck(False)
    @cython.wraparound(False)
    cdef inline double perlin1D(self, double x) noexcept:
        """
        🟩 **R** -
        """
        cdef int X
        cdef double u
        cdef int A, B

        X = int(floor(x)) & 255
        x -= floor(x)

        u = fade(x)

        A = self.p[X]
        B = self.p[X + 1]

        return lerp(u, grad1(self.p[A], x), grad1(self.p[B], x - 1))

    @cython.boundscheck(False)
    @cython.wraparound(False)
    cdef inline double perlin2D(self, double x, double y) noexcept:
        """
        🟩 **R** -
        """
        cdef int X, Y
        cdef double u, v
        cdef int A, B

        X = int(floor(x)) & 255
        Y = int(floor(y)) & 255
        x -= floor(x)
        y -= floor(y)

        u = fade(x)
        v = fade(y)

        A = self.p[X] + Y
        B = self.p[X + 1] + Y

        return lerp(v, lerp(u, grad2(self.p[A], x, y), grad2(self.p[B], x - 1, y)),
                            lerp(u, grad2(self.p[A + 1], x, y - 1), grad2(self.p[B + 1], x - 1, y - 1)))

    @cython.boundscheck(False)
    @cython.wraparound(False)
    cdef inline double perlin3D(self, double x, double y, double z) noexcept:
        """
        🟩 **R** -
        """
        cdef int X, Y, Z
        cdef double u, v, w
        cdef int A, AA, AB, B, BA, BB

        X = int(floor(x)) & 255
        Y = int(floor(y)) & 255
        Z = int(floor(z)) & 255
        x -= floor(x)
        y -= floor(y)
        z -= floor(z)

        u = fade(x)
        v = fade(y)
        w = fade(z)

        A = self.p[X] + Y
        AA = self.p[A] + Z
        AB = self.p[A + 1] + Z
        B = self.p[X + 1] + Y
        BA = self.p[B] + Z
        BB = self.p[B + 1] + Z

        return lerp(w, lerp(v, lerp(u, grad3(self.p[AA], x, y, z), grad3(self.p[BA], x - 1, y, z)),
                                lerp(u, grad3(self.p[AB], x, y - 1, z), grad3(self.p[BB], x - 1, y - 1, z))),
                            lerp(v, lerp(u, grad3(self.p[AA + 1], x, y, z - 1), grad3(self.p[BA + 1], x - 1, y, z - 1)),
                                lerp(u, grad3(self.p[AB + 1], x, y - 1, z - 1), grad3(self.p[BB + 1], x - 1, y - 1, z - 1))))

    cpdef double fBM1D(self, double x) noexcept:
        """
        🟩 **R** -
        """
        cdef double total = 0.0
        cdef double frequency = 1.0
        cdef double amplitude = 1.0
        cdef double maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin1D(x * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue

    cpdef double fBM2D(self, double x, double y) noexcept:
        """
        🟩 **R** -
        """
        cdef double total = 0.0
        cdef double frequency = 1.0
        cdef double amplitude = 1.0
        cdef double maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin2D(x * frequency, y * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue

    cpdef double fBM3D(self, double x, double y, double z) noexcept:
        """
        🟩 **R** -
        """
        cdef double total = 0.0
        cdef double frequency = 1.0
        cdef double amplitude = 1.0
        cdef double maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin3D(x * frequency, y * frequency, z * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue
