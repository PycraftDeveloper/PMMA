import numpy as np
import math
import random

PERMUTATION_SIZE = 512

class PerlinNoise:
    """
    🟩 **R** -
    """
    def __init__(self, seed, octaves, persistence):
        """
        🟩 **R** -
        """
        self.octaves = octaves
        self.persistence = persistence
        self.p = np.empty(512, dtype=np.int32)
        self.init_permutation(seed)

    def init_permutation(self, seed):
        """
        🟩 **R** -
        """
        perm = []
        for i in range(256):
            perm.append(i)

        random.seed(seed)
        for i in range(255, 0, -1):
            j = random.randint(0, i)
            temp = perm[i]
            perm[i] = perm[j]
            perm[j] = temp

        for i in range(256):
            self.p[256 + i] = self.p[i] = perm[i]

    def fade(self, t):
        """
        🟩 **R** -
        """
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, t, a, b):
        """
        🟩 **R** -
        """
        return a + t * (b - a)

    def grad1(self, hash, x):
        """
        🟩 **R** -
        """
        h = hash & 15
        grad = 1.0 + (h & 7)  # Gradient value is one of 1.0, 2.0, ..., 8.0
        if h & 8:
            grad = -grad  # and a random sign for the gradient
        return grad * x  # Multiply the gradient with the distance

    def grad2(self, hash, x, y):
        """
        🟩 **R** -
        """
        h = hash & 7  # Convert low 3 bits of hash code
        u = x if h < 4 else y  # into 8 simple gradient directions,
        v = y if h < 4 else x  # and compute the dot product with (x,y).
        return ((-u if h & 1 else u) + (-2.0 * v if h & 2 else 2.0 * v))

    def grad3(self, hash, x, y, z):
        """
        🟩 **R** -
        """
        h = hash & 15
        u = x if h < 8 else y
        v = y if h < 4 else (x if h == 12 or h == 14 else z)
        return ((u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v))

    def perlin1D(self, x):
        """
        🟩 **R** -
        """
        X = int(math.floor(x)) & 255
        x -= math.floor(x)

        u = self.fade(x)

        A = self.p[X]
        B = self.p[X + 1]

        return self.lerp(u, self.grad1(self.p[A], x), self.grad1(self.p[B], x - 1))

    def perlin2D(self, x, y):
        """
        🟩 **R** -
        """
        X = int(math.floor(x)) & 255
        Y = int(math.floor(y)) & 255
        x -= math.floor(x)
        y -= math.floor(y)

        u = self.fade(x)
        v = self.fade(y)

        A = self.p[X] + Y
        B = self.p[X + 1] + Y

        return self.lerp(v, self.lerp(u, self.grad2(self.p[A], x, y), self.grad2(self.p[B], x - 1, y)),
                            self.lerp(u, self.grad2(self.p[A + 1], x, y - 1), self.grad2(self.p[B + 1], x - 1, y - 1)))

    def perlin3D(self, x, y, z):
        """
        🟩 **R** -
        """
        X = int(math.floor(x)) & 255
        Y = int(math.floor(y)) & 255
        Z = int(math.floor(z)) & 255
        x -= math.floor(x)
        y -= math.floor(y)
        z -= math.floor(z)

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

    def fBM1D(self, x):
        """
        🟩 **R** -
        """
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin1D(x * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue

    def fBM2D(self, x, y):
        """
        🟩 **R** -
        """
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin2D(x * frequency, y * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue

    def fBM3D(self, x, y, z):
        """
        🟩 **R** -
        """
        total = 0.0
        frequency = 1.0
        amplitude = 1.0
        maxValue = 0.0  # Used for normalizing the result

        for i in range(self.octaves):
            total += self.perlin3D(x * frequency, y * frequency, z * frequency) * amplitude
            maxValue += amplitude

            amplitude *= self.persistence
            frequency *= 2.0

        return total / maxValue
