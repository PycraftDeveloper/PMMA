import numpy as np
from libc.math cimport floor
from libc.stdlib cimport rand, srand
from libc.time cimport time

cdef int PERMUTATION_SIZE = 512

cdef class PerlinNoise:
    cdef int p[512]
    cdef int octaves
    cdef double persistence

    def __init__(self, int seed, int octaves, double persistence):
        self.init_permutation(seed)
        self.octaves = octaves
        self.persistence = persistence

    cdef void init_permutation(self, int seed):
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

    cdef double fade(self, double t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    cdef double lerp(self, double t, double a, double b):
        return a + t * (b - a)

    cdef double grad1(self, int hash, double x):
        cdef int h = hash & 15
        cdef double grad = 1.0 + (h & 7)  # Gradient value is one of 1.0, 2.0, ..., 8.0
        if h & 8:
            grad = -grad  # and a random sign for the gradient
        return grad * x  # Multiply the gradient with the distance

    cdef double grad2(self, int hash, double x, double y):
        cdef int h = hash & 7  # Convert low 3 bits of hash code
        cdef double u = x if h < 4 else y  # into 8 simple gradient directions,
        cdef double v = y if h < 4 else x  # and compute the dot product with (x,y).
        return ((-u if h & 1 else u) + (-2.0 * v if h & 2 else 2.0 * v))

    cdef double grad3(self, int hash, double x, double y, double z):
        cdef int h = hash & 15
        cdef double u = x if h < 8 else y
        cdef double v = y if h < 4 else (x if h == 12 or h == 14 else z)
        return ((u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v))

    cdef double perlin1D(self, double x):
        cdef int X
        cdef double u
        cdef int A, B

        X = int(floor(x)) & 255
        x -= floor(x)

        u = self.fade(x)

        A = self.p[X]
        B = self.p[X + 1]

        return self.lerp(u, self.grad1(self.p[A], x), self.grad1(self.p[B], x - 1))

    cdef double perlin2D(self, double x, double y):
        cdef int X, Y
        cdef double u, v
        cdef int A, B

        X = int(floor(x)) & 255
        Y = int(floor(y)) & 255
        x -= floor(x)
        y -= floor(y)

        u = self.fade(x)
        v = self.fade(y)

        A = self.p[X] + Y
        B = self.p[X + 1] + Y

        return self.lerp(v, self.lerp(u, self.grad2(self.p[A], x, y), self.grad2(self.p[B], x - 1, y)),
                            self.lerp(u, self.grad2(self.p[A + 1], x, y - 1), self.grad2(self.p[B + 1], x - 1, y - 1)))

    cdef double perlin3D(self, double x, double y, double z):
        cdef int X, Y, Z
        cdef double u, v, w
        cdef int A, AA, AB, B, BA, BB

        X = int(floor(x)) & 255
        Y = int(floor(y)) & 255
        Z = int(floor(z)) & 255
        x -= floor(x)
        y -= floor(y)
        z -= floor(z)

        u = self.fade(x)
        v = self.fade(y)
        w = self.fade(z)

        A = self.p[X] + Y
        AA = self.p[A] + Z
        AB = self.p[A + 1] + Z
        B = self.p[X + 1] + Y
        BA = self.p[B] + Z
        BB = self.p[B + 1] + Z

        return self.lerp(w, self.lerp(v, self.lerp(u, self.grad3(self.p[AA], x, y, z), self.grad3(self.p[BA], x - 1, y, z)),
                                self.lerp(u, self.grad3(self.p[AB], x, y - 1, z), self.grad3(self.p[BB], x - 1, y - 1, z))),
                            self.lerp(v, self.lerp(u, self.grad3(self.p[AA + 1], x, y, z - 1), self.grad3(self.p[BA + 1], x - 1, y, z - 1)),
                                self.lerp(u, self.grad3(self.p[AB + 1], x, y - 1, z - 1), self.grad3(self.p[BB + 1], x - 1, y - 1, z - 1))))

    cpdef double fBM1D(self, double x):
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

    cpdef double fBM2D(self, double x, double y):
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

    cpdef double fBM3D(self, double x, double y, double z):
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
